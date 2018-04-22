# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_validator/protobuf/client_list_control.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_validator/protobuf/client_list_control.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n5sawtooth_validator/protobuf/client_list_control.proto\"4\n\x14\x43lientPagingControls\x12\r\n\x05start\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\"B\n\x14\x43lientPagingResponse\x12\x0c\n\x04next\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x05\"3\n\x12\x43lientSortControls\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\x0f\n\x07reverse\x18\x02 \x01(\x08\x42\x32\n\x15sawtooth.sdk.protobufP\x01Z\x17\x63lient_list_control_pb2b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLIENTPAGINGCONTROLS = _descriptor.Descriptor(
  name='ClientPagingControls',
  full_name='ClientPagingControls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ClientPagingControls.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ClientPagingControls.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=109,
)


_CLIENTPAGINGRESPONSE = _descriptor.Descriptor(
  name='ClientPagingResponse',
  full_name='ClientPagingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next', full_name='ClientPagingResponse.next', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ClientPagingResponse.start', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ClientPagingResponse.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=177,
)


_CLIENTSORTCONTROLS = _descriptor.Descriptor(
  name='ClientSortControls',
  full_name='ClientSortControls',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='ClientSortControls.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='ClientSortControls.reverse', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=230,
)

DESCRIPTOR.message_types_by_name['ClientPagingControls'] = _CLIENTPAGINGCONTROLS
DESCRIPTOR.message_types_by_name['ClientPagingResponse'] = _CLIENTPAGINGRESPONSE
DESCRIPTOR.message_types_by_name['ClientSortControls'] = _CLIENTSORTCONTROLS

ClientPagingControls = _reflection.GeneratedProtocolMessageType('ClientPagingControls', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTPAGINGCONTROLS,
  __module__ = 'sawtooth_validator.protobuf.client_list_control_pb2'
  # @@protoc_insertion_point(class_scope:ClientPagingControls)
  ))
_sym_db.RegisterMessage(ClientPagingControls)

ClientPagingResponse = _reflection.GeneratedProtocolMessageType('ClientPagingResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTPAGINGRESPONSE,
  __module__ = 'sawtooth_validator.protobuf.client_list_control_pb2'
  # @@protoc_insertion_point(class_scope:ClientPagingResponse)
  ))
_sym_db.RegisterMessage(ClientPagingResponse)

ClientSortControls = _reflection.GeneratedProtocolMessageType('ClientSortControls', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSORTCONTROLS,
  __module__ = 'sawtooth_validator.protobuf.client_list_control_pb2'
  # @@protoc_insertion_point(class_scope:ClientSortControls)
  ))
_sym_db.RegisterMessage(ClientSortControls)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025sawtooth.sdk.protobufP\001Z\027client_list_control_pb2'))
# @@protoc_insertion_point(module_scope)
