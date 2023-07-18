# -*- coding: utf-8 -*-
# Copyright 2019 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import concurrent.futures
import logging
import multiprocessing
import os
import pathlib
import threading
import time

from libcloud.storage.types import ObjectDoesNotExistError
from retrying import retry

import medusa
import base64
import io

MAX_UPLOAD_RETRIES = 5


class StorageJob:
    """
    Manages concurrency and storage connection pools for tasks like uploading or downloading files. The libcloud
    drivers are not thread safe, so each thread will a separate connection. If the function executed by StorageJob
    uses any shared state, then it is the responsibility of that function to manage concurrent access to that state.
    """
    def __init__(self, storage, func, max_workers=None):
        self.storage = storage
        self.lock = threading.Lock()
        self.func = func
        self.connection_pool = []
        self.timer = time.time()
        self.connection_ttl = 1200
        if max_workers is None:
            self.max_workers = int(multiprocessing.cpu_count())
        else:
            self.max_workers = int(max_workers)

    def execute(self, iterables):
        with concurrent.futures.ThreadPoolExecutor(self.max_workers) as executor:
            return list(executor.map(self.with_storage, iterables))

    def with_storage(self, iterable):
        with self.lock:
            current_timer = time.time()
            if current_timer - self.timer > self.connection_ttl:
                self.connection_pool = []
                self.timer = time.time()
            if not self.connection_pool:
                connection = self.storage.connect_storage()
            else:
                connection = self.connection_pool.pop()
        try:
            return self.func(connection, iterable)
        finally:
            with self.lock:
                self.connection_pool.append(connection)


def upload_blobs(storage, src, dest, bucket, max_workers=None):
    """
    Uploads a list of files from local storage concurrently to the remote storage.

    :param storage: An AbstractStorage instance, needed to create a connection pool
    :param src: A list of files to upload
    :param dest: The location where to upload the files in the target bucket (doesn't contain the filename)
    :param bucket: The remote bucket in which files will be stored
    :param max_workers: The max number of worker threads to use. Defaults to the number of CPUs.
    :return: A list of ManifestObject describing all the uploaded files
    """
    job = StorageJob(storage,
                     lambda connection, src_file: __upload_file(storage, connection, src_file, dest, bucket),
                     max_workers)
    return job.execute(list(src))


def __upload_file(storage, connection, src, dest, bucket):
    """
    This function is called by StorageJob. It may be called concurrently by multiple threads.

    :param connection: A storage connection which is created and managed by StorageJob
    :param src: The file to upload
    :param dest: The location where to upload the file
    :param bucket: The remote bucket where the file will be stored
    :return: A ManifestObject describing the uploaded file
    """
    if not isinstance(src, pathlib.Path):
        src = pathlib.Path(src)

    file_size = os.stat(str(src)).st_size
    logging.info("Uploading {} ({})".format(src, human_readable_size(file_size)))
    # check if objects resides in a sub-folder (e.g. secondary index). if it does, use the sub-folder in object path
    obj_name = '{}/{}'.format(src.parent.name, src.name) if src.parent.name.startswith('.') else src.name
    full_object_name = str("{}/{}".format(dest, obj_name))
    obj = _upload_single_part(storage, connection, src, bucket, full_object_name)

    return medusa.storage.ManifestObject(obj.name, obj.size, obj.hash.replace('"', ''))


@retry(stop_max_attempt_number=MAX_UPLOAD_RETRIES, wait_fixed=5000)
def _upload_single_part(storage, connection, src, bucket, object_name):
    headers = storage.additional_upload_headers()
    with open(str(src), 'rb') as iterator:
        # Read the file content
        file_content = iterator.read()

        # Encrypt the file content using base64 encoding
        encrypted_content = base64.b64encode(file_content)

        # Create a file-like object from the encrypted content
        encrypted_iterator = io.BytesIO(encrypted_content)

        # Upload the encrypted file via stream
        obj = connection.upload_object_via_stream(
            encrypted_iterator,
            container=bucket,
            object_name=object_name,
            headers=headers
        )

    return obj

def download_blobs(storage, src, dest, bucket_name, max_workers=None):
    """
    Download files concurrently to local storage

    :param storage: An AbstractStorage instance, needed to create a connection pool
    :param src: A list of files to download from the remote storage system
    :param dest: The path to where objects should be downloaded locally
    :param bucket_name: The name of the storage bucket from which files will be downloaded
    :param max_workers: The max number of threads to use. Defaults to the number of CPUS.
    :return:
    """
    job = StorageJob(storage,
                     lambda connection, src_file: __download_blob(connection, src_file, str(dest), bucket_name),
                     max_workers)
    job.execute(list(src))


def __download_blob(connection, src, dest, bucket_name):
    """
    This function is called by StorageJob. It may be called concurrently by multiple threads.

    :param connection: A storage connection which is created and managed by StorageJob
    :param src: The file to download
    :param dest: The path to where the file should be downloaded
    :param bucket_name: The name of the bucket from which the file will be downloaded
    :return:
    """
    try:
        logging.debug("[Storage] Getting object {}".format(src))
        blob = connection.get_object(bucket_name, str(src))
        # we must make sure the blob gets stored under sub-folder (if there is any)
        # the dest variable only points to the table folder, so we need to add the sub-folder
        src_path = pathlib.Path(src)
        blob_dest = '{}/{}'.format(dest, src_path.parent.name) if src_path.parent.name.startswith('.') else dest
        index = blob.name.rfind("/")
        if index > 0:
            file_name = blob.name[blob.name.rfind("/") + 1:]
        else:
            file_name = blob.name

        with open("{}/{}".format(blob_dest, file_name), "wb") as file_handle:
            for chunk in blob.as_stream():
                file_handle.write(chunk)

        # Decrypt the downloaded file if it is base64 encoded
        decrypted_file_path = "{}/{}".format(blob_dest, file_name)
        with open(decrypted_file_path, "rb") as encrypted_file:
            encrypted_content = encrypted_file.read()

            # Check if the file is base64 encoded
            try:
                decrypted_content = base64.b64decode(encrypted_content)
            except base64.binascii.Error:
                # If the file is not base64 encoded, skip decryption
                decrypted_content = encrypted_content

        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_content)
    except ObjectDoesNotExistError:
        return None

def human_readable_size(size, decimal_places=3):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return '{:.{}f}{}'.format(size, decimal_places, unit)
