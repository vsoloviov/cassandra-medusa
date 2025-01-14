# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: medusa.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='medusa.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmedusa.proto\"d\n\rBackupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x04mode\x18\x02 \x01(\x0e\x32\x13.BackupRequest.Mode\"\"\n\x04Mode\x12\x10\n\x0c\x44IFFERENTIAL\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\"A\n\x0e\x42\x61\x63kupResponse\x12\x12\n\nbackupName\x18\x01 \x01(\t\x12\x1b\n\x06status\x18\x02 \x01(\x0e\x32\x0b.StatusType\")\n\x13\x42\x61\x63kupStatusRequest\x12\x12\n\nbackupName\x18\x01 \x01(\t\"\xa0\x01\n\x14\x42\x61\x63kupStatusResponse\x12\x15\n\rfinishedNodes\x18\x01 \x03(\t\x12\x17\n\x0funfinishedNodes\x18\x02 \x03(\t\x12\x14\n\x0cmissingNodes\x18\x03 \x03(\t\x12\x11\n\tstartTime\x18\x04 \x01(\t\x12\x12\n\nfinishTime\x18\x05 \x01(\t\x12\x1b\n\x06status\x18\x06 \x01(\x0e\x32\x0b.StatusType\"#\n\x13\x44\x65leteBackupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"A\n\x14\x44\x65leteBackupResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x06status\x18\x02 \x01(\x0e\x32\x0b.StatusType\"\x13\n\x11GetBackupsRequest\"Y\n\x12GetBackupsResponse\x12\x1f\n\x07\x62\x61\x63kups\x18\x01 \x03(\x0b\x32\x0e.BackupSummary\x12\"\n\roverallStatus\x18\x02 \x01(\x0e\x32\x0b.StatusType\"\xc2\x01\n\rBackupSummary\x12\x12\n\nbackupName\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\x03\x12\x12\n\nfinishTime\x18\x03 \x01(\x03\x12\x12\n\ntotalNodes\x18\x04 \x01(\x05\x12\x15\n\rfinishedNodes\x18\x05 \x01(\x05\x12\x1a\n\x05nodes\x18\x06 \x03(\x0b\x32\x0b.BackupNode\x12\x1b\n\x06status\x18\x07 \x01(\x0e\x32\x0b.StatusType\x12\x12\n\nbackupType\x18\x08 \x01(\t\"L\n\nBackupNode\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0e\n\x06tokens\x18\x02 \x03(\x03\x12\x12\n\ndatacenter\x18\x03 \x01(\t\x12\x0c\n\x04rack\x18\x04 \x01(\t\"\x15\n\x13PurgeBackupsRequest\"\x84\x01\n\x14PurgeBackupsResponse\x12\x17\n\x0fnbBackupsPurged\x18\x01 \x01(\x05\x12\x17\n\x0fnbObjectsPurged\x18\x02 \x01(\x05\x12\x17\n\x0ftotalPurgedSize\x18\x03 \x01(\x03\x12!\n\x19totalObjectsWithinGcGrace\x18\x04 \x01(\x05\"S\n\x15PrepareRestoreRequest\x12\x12\n\nbackupName\x18\x01 \x01(\t\x12\x12\n\ndatacenter\x18\x02 \x01(\t\x12\x12\n\nrestoreKey\x18\x03 \x01(\t\"\x18\n\x16PrepareRestoreResponse*C\n\nStatusType\x12\x0f\n\x0bIN_PROGRESS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03\x32\x94\x03\n\x06Medusa\x12)\n\x06\x42\x61\x63kup\x12\x0e.BackupRequest\x1a\x0f.BackupResponse\x12.\n\x0b\x41syncBackup\x12\x0e.BackupRequest\x1a\x0f.BackupResponse\x12;\n\x0c\x42\x61\x63kupStatus\x12\x14.BackupStatusRequest\x1a\x15.BackupStatusResponse\x12;\n\x0c\x44\x65leteBackup\x12\x14.DeleteBackupRequest\x1a\x15.DeleteBackupResponse\x12\x35\n\nGetBackups\x12\x12.GetBackupsRequest\x1a\x13.GetBackupsResponse\x12;\n\x0cPurgeBackups\x12\x14.PurgeBackupsRequest\x1a\x15.PurgeBackupsResponse\x12\x41\n\x0ePrepareRestore\x12\x16.PrepareRestoreRequest\x1a\x17.PrepareRestoreResponseb\x06proto3'
)

_STATUSTYPE = _descriptor.EnumDescriptor(
  name='StatusType',
  full_name='StatusType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1151,
  serialized_end=1218,
)
_sym_db.RegisterEnumDescriptor(_STATUSTYPE)

StatusType = enum_type_wrapper.EnumTypeWrapper(_STATUSTYPE)
IN_PROGRESS = 0
SUCCESS = 1
FAILED = 2
UNKNOWN = 3


_BACKUPREQUEST_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='BackupRequest.Mode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIFFERENTIAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=82,
  serialized_end=116,
)
_sym_db.RegisterEnumDescriptor(_BACKUPREQUEST_MODE)


_BACKUPREQUEST = _descriptor.Descriptor(
  name='BackupRequest',
  full_name='BackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BackupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='BackupRequest.mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BACKUPREQUEST_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=116,
)


_BACKUPRESPONSE = _descriptor.Descriptor(
  name='BackupResponse',
  full_name='BackupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='BackupResponse.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='BackupResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=183,
)


_BACKUPSTATUSREQUEST = _descriptor.Descriptor(
  name='BackupStatusRequest',
  full_name='BackupStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='BackupStatusRequest.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=226,
)


_BACKUPSTATUSRESPONSE = _descriptor.Descriptor(
  name='BackupStatusResponse',
  full_name='BackupStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='finishedNodes', full_name='BackupStatusResponse.finishedNodes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unfinishedNodes', full_name='BackupStatusResponse.unfinishedNodes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missingNodes', full_name='BackupStatusResponse.missingNodes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='BackupStatusResponse.startTime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishTime', full_name='BackupStatusResponse.finishTime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='BackupStatusResponse.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=229,
  serialized_end=389,
)


_DELETEBACKUPREQUEST = _descriptor.Descriptor(
  name='DeleteBackupRequest',
  full_name='DeleteBackupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DeleteBackupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=391,
  serialized_end=426,
)


_DELETEBACKUPRESPONSE = _descriptor.Descriptor(
  name='DeleteBackupResponse',
  full_name='DeleteBackupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DeleteBackupResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='DeleteBackupResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=493,
)


_GETBACKUPSREQUEST = _descriptor.Descriptor(
  name='GetBackupsRequest',
  full_name='GetBackupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=514,
)


_GETBACKUPSRESPONSE = _descriptor.Descriptor(
  name='GetBackupsResponse',
  full_name='GetBackupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backups', full_name='GetBackupsResponse.backups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overallStatus', full_name='GetBackupsResponse.overallStatus', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=605,
)


_BACKUPSUMMARY = _descriptor.Descriptor(
  name='BackupSummary',
  full_name='BackupSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='BackupSummary.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='BackupSummary.startTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishTime', full_name='BackupSummary.finishTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalNodes', full_name='BackupSummary.totalNodes', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finishedNodes', full_name='BackupSummary.finishedNodes', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='BackupSummary.nodes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='BackupSummary.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backupType', full_name='BackupSummary.backupType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=802,
)


_BACKUPNODE = _descriptor.Descriptor(
  name='BackupNode',
  full_name='BackupNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='BackupNode.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='BackupNode.tokens', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datacenter', full_name='BackupNode.datacenter', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rack', full_name='BackupNode.rack', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=880,
)


_PURGEBACKUPSREQUEST = _descriptor.Descriptor(
  name='PurgeBackupsRequest',
  full_name='PurgeBackupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=882,
  serialized_end=903,
)


_PURGEBACKUPSRESPONSE = _descriptor.Descriptor(
  name='PurgeBackupsResponse',
  full_name='PurgeBackupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nbBackupsPurged', full_name='PurgeBackupsResponse.nbBackupsPurged', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nbObjectsPurged', full_name='PurgeBackupsResponse.nbObjectsPurged', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalPurgedSize', full_name='PurgeBackupsResponse.totalPurgedSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalObjectsWithinGcGrace', full_name='PurgeBackupsResponse.totalObjectsWithinGcGrace', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=906,
  serialized_end=1038,
)


_PREPARERESTOREREQUEST = _descriptor.Descriptor(
  name='PrepareRestoreRequest',
  full_name='PrepareRestoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='backupName', full_name='PrepareRestoreRequest.backupName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datacenter', full_name='PrepareRestoreRequest.datacenter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restoreKey', full_name='PrepareRestoreRequest.restoreKey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1040,
  serialized_end=1123,
)


_PREPARERESTORERESPONSE = _descriptor.Descriptor(
  name='PrepareRestoreResponse',
  full_name='PrepareRestoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1125,
  serialized_end=1149,
)

_BACKUPREQUEST.fields_by_name['mode'].enum_type = _BACKUPREQUEST_MODE
_BACKUPREQUEST_MODE.containing_type = _BACKUPREQUEST
_BACKUPRESPONSE.fields_by_name['status'].enum_type = _STATUSTYPE
_BACKUPSTATUSRESPONSE.fields_by_name['status'].enum_type = _STATUSTYPE
_DELETEBACKUPRESPONSE.fields_by_name['status'].enum_type = _STATUSTYPE
_GETBACKUPSRESPONSE.fields_by_name['backups'].message_type = _BACKUPSUMMARY
_GETBACKUPSRESPONSE.fields_by_name['overallStatus'].enum_type = _STATUSTYPE
_BACKUPSUMMARY.fields_by_name['nodes'].message_type = _BACKUPNODE
_BACKUPSUMMARY.fields_by_name['status'].enum_type = _STATUSTYPE
DESCRIPTOR.message_types_by_name['BackupRequest'] = _BACKUPREQUEST
DESCRIPTOR.message_types_by_name['BackupResponse'] = _BACKUPRESPONSE
DESCRIPTOR.message_types_by_name['BackupStatusRequest'] = _BACKUPSTATUSREQUEST
DESCRIPTOR.message_types_by_name['BackupStatusResponse'] = _BACKUPSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteBackupRequest'] = _DELETEBACKUPREQUEST
DESCRIPTOR.message_types_by_name['DeleteBackupResponse'] = _DELETEBACKUPRESPONSE
DESCRIPTOR.message_types_by_name['GetBackupsRequest'] = _GETBACKUPSREQUEST
DESCRIPTOR.message_types_by_name['GetBackupsResponse'] = _GETBACKUPSRESPONSE
DESCRIPTOR.message_types_by_name['BackupSummary'] = _BACKUPSUMMARY
DESCRIPTOR.message_types_by_name['BackupNode'] = _BACKUPNODE
DESCRIPTOR.message_types_by_name['PurgeBackupsRequest'] = _PURGEBACKUPSREQUEST
DESCRIPTOR.message_types_by_name['PurgeBackupsResponse'] = _PURGEBACKUPSRESPONSE
DESCRIPTOR.message_types_by_name['PrepareRestoreRequest'] = _PREPARERESTOREREQUEST
DESCRIPTOR.message_types_by_name['PrepareRestoreResponse'] = _PREPARERESTORERESPONSE
DESCRIPTOR.enum_types_by_name['StatusType'] = _STATUSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BackupRequest = _reflection.GeneratedProtocolMessageType('BackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupRequest)
  })
_sym_db.RegisterMessage(BackupRequest)

BackupResponse = _reflection.GeneratedProtocolMessageType('BackupResponse', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupResponse)
  })
_sym_db.RegisterMessage(BackupResponse)

BackupStatusRequest = _reflection.GeneratedProtocolMessageType('BackupStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSTATUSREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupStatusRequest)
  })
_sym_db.RegisterMessage(BackupStatusRequest)

BackupStatusResponse = _reflection.GeneratedProtocolMessageType('BackupStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSTATUSRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupStatusResponse)
  })
_sym_db.RegisterMessage(BackupStatusResponse)

DeleteBackupRequest = _reflection.GeneratedProtocolMessageType('DeleteBackupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:DeleteBackupRequest)
  })
_sym_db.RegisterMessage(DeleteBackupRequest)

DeleteBackupResponse = _reflection.GeneratedProtocolMessageType('DeleteBackupResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBACKUPRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:DeleteBackupResponse)
  })
_sym_db.RegisterMessage(DeleteBackupResponse)

GetBackupsRequest = _reflection.GeneratedProtocolMessageType('GetBackupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPSREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:GetBackupsRequest)
  })
_sym_db.RegisterMessage(GetBackupsRequest)

GetBackupsResponse = _reflection.GeneratedProtocolMessageType('GetBackupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBACKUPSRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:GetBackupsResponse)
  })
_sym_db.RegisterMessage(GetBackupsResponse)

BackupSummary = _reflection.GeneratedProtocolMessageType('BackupSummary', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPSUMMARY,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupSummary)
  })
_sym_db.RegisterMessage(BackupSummary)

BackupNode = _reflection.GeneratedProtocolMessageType('BackupNode', (_message.Message,), {
  'DESCRIPTOR' : _BACKUPNODE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:BackupNode)
  })
_sym_db.RegisterMessage(BackupNode)

PurgeBackupsRequest = _reflection.GeneratedProtocolMessageType('PurgeBackupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _PURGEBACKUPSREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:PurgeBackupsRequest)
  })
_sym_db.RegisterMessage(PurgeBackupsRequest)

PurgeBackupsResponse = _reflection.GeneratedProtocolMessageType('PurgeBackupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PURGEBACKUPSRESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:PurgeBackupsResponse)
  })
_sym_db.RegisterMessage(PurgeBackupsResponse)

PrepareRestoreRequest = _reflection.GeneratedProtocolMessageType('PrepareRestoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _PREPARERESTOREREQUEST,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:PrepareRestoreRequest)
  })
_sym_db.RegisterMessage(PrepareRestoreRequest)

PrepareRestoreResponse = _reflection.GeneratedProtocolMessageType('PrepareRestoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _PREPARERESTORERESPONSE,
  '__module__' : 'medusa_pb2'
  # @@protoc_insertion_point(class_scope:PrepareRestoreResponse)
  })
_sym_db.RegisterMessage(PrepareRestoreResponse)



_MEDUSA = _descriptor.ServiceDescriptor(
  name='Medusa',
  full_name='Medusa',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1221,
  serialized_end=1625,
  methods=[
  _descriptor.MethodDescriptor(
    name='Backup',
    full_name='Medusa.Backup',
    index=0,
    containing_service=None,
    input_type=_BACKUPREQUEST,
    output_type=_BACKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AsyncBackup',
    full_name='Medusa.AsyncBackup',
    index=1,
    containing_service=None,
    input_type=_BACKUPREQUEST,
    output_type=_BACKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BackupStatus',
    full_name='Medusa.BackupStatus',
    index=2,
    containing_service=None,
    input_type=_BACKUPSTATUSREQUEST,
    output_type=_BACKUPSTATUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBackup',
    full_name='Medusa.DeleteBackup',
    index=3,
    containing_service=None,
    input_type=_DELETEBACKUPREQUEST,
    output_type=_DELETEBACKUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBackups',
    full_name='Medusa.GetBackups',
    index=4,
    containing_service=None,
    input_type=_GETBACKUPSREQUEST,
    output_type=_GETBACKUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PurgeBackups',
    full_name='Medusa.PurgeBackups',
    index=5,
    containing_service=None,
    input_type=_PURGEBACKUPSREQUEST,
    output_type=_PURGEBACKUPSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PrepareRestore',
    full_name='Medusa.PrepareRestore',
    index=6,
    containing_service=None,
    input_type=_PREPARERESTOREREQUEST,
    output_type=_PREPARERESTORERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MEDUSA)

DESCRIPTOR.services_by_name['Medusa'] = _MEDUSA

# @@protoc_insertion_point(module_scope)
