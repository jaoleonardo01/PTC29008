# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tmsg.proto\x12\x05tftp2\"/\n\x03RRQ\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x19\n\x04mode\x18\x02 \x02(\x0e\x32\x0b.tftp2.Mode\"/\n\x03WRQ\x12\r\n\x05\x66name\x18\x01 \x02(\t\x12\x19\n\x04mode\x18\x02 \x02(\x0e\x32\x0b.tftp2.Mode\"(\n\x04\x44\x41TA\x12\x0f\n\x07message\x18\x01 \x02(\x0c\x12\x0f\n\x07\x62lock_n\x18\x02 \x02(\r\"\x16\n\x03\x41\x43K\x12\x0f\n\x07\x62lock_n\x18\x01 \x02(\r\",\n\x05\x45rror\x12#\n\terrorcode\x18\x01 \x02(\x0e\x32\x10.tftp2.ErrorCode\"\x14\n\x04LIST\x12\x0c\n\x04path\x18\x01 \x02(\t\".\n\x0cListResponse\x12\x1e\n\x05items\x18\x01 \x03(\x0b\x32\x0f.tftp2.ListItem\"L\n\x08ListItem\x12\x1b\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x0b.tftp2.FILEH\x00\x12\x19\n\x03\x64ir\x18\x02 \x01(\x0b\x32\n.tftp2.DIRH\x00\x42\x08\n\x06\x61nswer\"%\n\x04\x46ILE\x12\x0c\n\x04nome\x18\x01 \x02(\t\x12\x0f\n\x07tamanho\x18\x02 \x02(\x05\"\x13\n\x03\x44IR\x12\x0c\n\x04nome\x18\x01 \x02(\t\"\x15\n\x05MKDIR\x12\x0c\n\x04path\x18\x01 \x02(\t\",\n\x04MOVE\x12\x11\n\tnome_orig\x18\x01 \x02(\t\x12\x11\n\tnome_novo\x18\x02 \x01(\t\"\xa1\x02\n\x08Mensagem\x12\x19\n\x03rrq\x18\x01 \x01(\x0b\x32\n.tftp2.RRQH\x00\x12\x19\n\x03wrq\x18\x02 \x01(\x0b\x32\n.tftp2.WRQH\x00\x12\x1b\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0b.tftp2.DATAH\x00\x12\x19\n\x03\x61\x63k\x18\x04 \x01(\x0b\x32\n.tftp2.ACKH\x00\x12\x1d\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x0c.tftp2.ErrorH\x00\x12\x1b\n\x04list\x18\x06 \x01(\x0b\x32\x0b.tftp2.LISTH\x00\x12(\n\tlist_resp\x18\x07 \x01(\x0b\x32\x13.tftp2.ListResponseH\x00\x12\x1d\n\x05mkdir\x18\x08 \x01(\x0b\x32\x0c.tftp2.MKDIRH\x00\x12\x1b\n\x04move\x18\t \x01(\x0b\x32\x0b.tftp2.MOVEH\x00\x42\x05\n\x03msg*)\n\x04Mode\x12\x0c\n\x08netascii\x10\x01\x12\t\n\x05octet\x10\x02\x12\x08\n\x04mail\x10\x03*\x99\x01\n\tErrorCode\x12\x10\n\x0c\x46ileNotFound\x10\x01\x12\x13\n\x0f\x41\x63\x63\x65ssViolation\x10\x02\x12\x0c\n\x08\x44iskFull\x10\x03\x12\x14\n\x10IllegalOperation\x10\x04\x12\x0e\n\nUnknownTid\x10\x05\x12\x0e\n\nFileExists\x10\x06\x12\x12\n\x0eUnknownSession\x10\x07\x12\r\n\tUnedfined\x10\x08')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODE._serialized_start=799
  _MODE._serialized_end=840
  _ERRORCODE._serialized_start=843
  _ERRORCODE._serialized_end=996
  _RRQ._serialized_start=20
  _RRQ._serialized_end=67
  _WRQ._serialized_start=69
  _WRQ._serialized_end=116
  _DATA._serialized_start=118
  _DATA._serialized_end=158
  _ACK._serialized_start=160
  _ACK._serialized_end=182
  _ERROR._serialized_start=184
  _ERROR._serialized_end=228
  _LIST._serialized_start=230
  _LIST._serialized_end=250
  _LISTRESPONSE._serialized_start=252
  _LISTRESPONSE._serialized_end=298
  _LISTITEM._serialized_start=300
  _LISTITEM._serialized_end=376
  _FILE._serialized_start=378
  _FILE._serialized_end=415
  _DIR._serialized_start=417
  _DIR._serialized_end=436
  _MKDIR._serialized_start=438
  _MKDIR._serialized_end=459
  _MOVE._serialized_start=461
  _MOVE._serialized_end=505
  _MENSAGEM._serialized_start=508
  _MENSAGEM._serialized_end=797
# @@protoc_insertion_point(module_scope)
