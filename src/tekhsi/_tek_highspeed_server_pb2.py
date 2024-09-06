# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TekHighspeedServer.proto
"""Generated protocol buffer code."""

from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18TekHighspeedServer.proto\x12\x08Tekscope"\x1e\n\x0e\x43onnectRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"7\n\x0c\x43onnectReply\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.Tekscope.ConnectStatus"S\n\x13\x41vailableNamesReply\x12\'\n\x06status\x18\x01 \x01(\x0e\x32\x17.Tekscope.ConnectStatus\x12\x13\n\x0bsymbolnames\x18\x02 \x03(\t"8\n\x0fWaveformRequest\x12\x12\n\nsourcename\x18\x01 \x01(\t\x12\x11\n\tchunksize\x18\x02 \x01(\r"\x9b\x04\n\x0eWaveformHeader\x12\x12\n\nsourcename\x18\x01 \x01(\t\x12\x13\n\x0bsourcewidth\x18\x02 \x01(\r\x12\x0e\n\x06\x64\x61taid\x18\x03 \x01(\x04\x12\x0f\n\x07transid\x18\x04 \x01(\x04\x12\x17\n\x0fhorizontalUnits\x18\x05 \x01(\t\x12\x19\n\x11horizontalspacing\x18\x06 \x01(\x01\x12\x1b\n\x13horizontalzeroindex\x18\x07 \x01(\x01\x12%\n\x1dhorizontalfractionalzeroindex\x18\x08 \x01(\x01\x12\x13\n\x0bnoofsamples\x18\t \x01(\x04\x12\x11\n\tchunksize\x18\n \x01(\r\x12"\n\x07wfmtype\x18\x0b \x01(\x0e\x32\x11.Tekscope.WfmType\x12\x0f\n\x07\x62itmask\x18\x0c \x01(\r\x12\'\n\x08pairtype\x18\r \x01(\x0e\x32\x15.Tekscope.WfmPairType\x12\x15\n\rverticalunits\x18\x0e \x01(\t\x12\x17\n\x0fverticalspacing\x18\x0f \x01(\x01\x12\x16\n\x0everticaloffset\x18\x10 \x01(\x01\x12\x1a\n\x12iq_centerFrequency\x18\x11 \x01(\x01\x12\x14\n\x0ciq_fftLength\x18\x12 \x01(\x01\x12\x0e\n\x06iq_rbw\x18\x13 \x01(\x01\x12\x0f\n\x07iq_span\x18\x14 \x01(\x01\x12\x15\n\riq_windowType\x18\x15 \x01(\t\x12\x0f\n\x07hasdata\x18\x16 \x01(\x08"\xb4\x02\n\x0fNormalizedReply\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.Tekscope.WfmReplyStatus\x12\x42\n\x0cheaderordata\x18\x02 \x01(\x0b\x32,.Tekscope.NormalizedReply.DataOrHeaderAccess\x1a\'\n\x13WaveformSampleChunk\x12\x10\n\x04\x64\x61ta\x18\x01 \x03(\x02\x42\x02\x10\x01\x1a\x89\x01\n\x12\x44\x61taOrHeaderAccess\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x18.Tekscope.WaveformHeaderH\x00\x12>\n\x05\x63hunk\x18\x02 \x01(\x0b\x32-.Tekscope.NormalizedReply.WaveformSampleChunkH\x00\x42\x07\n\x05value"\xa3\x02\n\x08RawReply\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.Tekscope.WfmReplyStatus\x12;\n\x0cheaderordata\x18\x02 \x01(\x0b\x32%.Tekscope.RawReply.DataOrHeaderAccess\x1a\'\n\x17WaveformSampleByteChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x1a\x86\x01\n\x12\x44\x61taOrHeaderAccess\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x18.Tekscope.WaveformHeaderH\x00\x12;\n\x05\x63hunk\x18\x02 \x01(\x0b\x32*.Tekscope.RawReply.WaveformSampleByteChunkH\x00\x42\x07\n\x05value*\x85\x02\n\rConnectStatus\x12\x1d\n\x19\x43ONNECTSTATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43ONNECTSTATUS_SUCCESS\x10\x01\x12\'\n#CONNECTSTATUS_NOT_CONNECTED_FAILURE\x10\x02\x12*\n&CONNECTSTATUS_OUTSIDE_SEQUENCE_FAILURE\x10\x03\x12!\n\x1d\x43ONNECTSTATUS_TIMEOUT_FAILURE\x10\x04\x12\x1f\n\x1b\x43ONNECTSTATUS_INUSE_FAILURE\x10\x05\x12!\n\x1d\x43ONNECTSTATUS_UNKNOWN_FAILURE\x10\x06*\xfc\x01\n\x0eWfmReplyStatus\x12\x1e\n\x1aWFMREPLYSTATUS_UNSPECIFIED\x10\x00\x12\x1a\n\x16WFMREPLYSTATUS_SUCCESS\x10\x01\x12-\n)WFMREPLYSTATUS_SOURCENAME_MISSING_FAILURE\x10\x02\x12+\n\'WFMREPLYSTATUS_OUTSIDE_SEQUENCE_FAILURE\x10\x03\x12(\n$WFMREPLYSTATUS_NO_CONNECTION_FAILURE\x10\x04\x12(\n$WFMREPLYSTATUS_TYPE_MISMATCH_FAILURE\x10\x05*V\n\x0bWfmPairType\x12\x1b\n\x17WFMPAIRTYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10WFMPAIRTYPE_NONE\x10\x01\x12\x14\n\x10WFMPAIRTYPE_PAIR\x10\x02*\xcc\x01\n\x07WfmType\x12\x17\n\x13WFMTYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10WFMTYPE_ANALOG_8\x10\x01\x12\x15\n\x11WFMTYPE_ANALOG_16\x10\x02\x12\x18\n\x14WFMTYPE_ANALOG_FLOAT\x10\x03\x12\x15\n\x11WFMTYPE_DIGITAL_8\x10\x04\x12\x16\n\x12WFMTYPE_DIGITAL_16\x10\x05\x12\x18\n\x14WFMTYPE_ANALOG_16_IQ\x10\x06\x12\x18\n\x14WFMTYPE_ANALOG_32_IQ\x10\x07\x32\xbf\x03\n\x07\x43onnect\x12=\n\x07\x43onnect\x12\x18.Tekscope.ConnectRequest\x1a\x16.Tekscope.ConnectReply"\x00\x12@\n\nDisconnect\x12\x18.Tekscope.ConnectRequest\x1a\x16.Tekscope.ConnectReply"\x00\x12H\n\x12RequestNewSequence\x12\x18.Tekscope.ConnectRequest\x1a\x16.Tekscope.ConnectReply"\x00\x12R\n\x15RequestAvailableNames\x12\x18.Tekscope.ConnectRequest\x1a\x1d.Tekscope.AvailableNamesReply"\x00\x12G\n\x11WaitForDataAccess\x12\x18.Tekscope.ConnectRequest\x1a\x16.Tekscope.ConnectReply"\x00\x12L\n\x16\x46inishedWithDataAccess\x12\x18.Tekscope.ConnectRequest\x1a\x16.Tekscope.ConnectReply"\x00\x32\x9e\x01\n\x0eNormalizedData\x12G\n\x0bGetWaveform\x12\x19.Tekscope.WaveformRequest\x1a\x19.Tekscope.NormalizedReply"\x00\x30\x01\x12\x43\n\tGetHeader\x12\x19.Tekscope.WaveformRequest\x1a\x19.Tekscope.NormalizedReply"\x00\x32\x8c\x01\n\nNativeData\x12@\n\x0bGetWaveform\x12\x19.Tekscope.WaveformRequest\x1a\x12.Tekscope.RawReply"\x00\x30\x01\x12<\n\tGetHeader\x12\x19.Tekscope.WaveformRequest\x1a\x12.Tekscope.RawReply"\x00\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "TekHighspeedServer_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _NORMALIZEDREPLY_WAVEFORMSAMPLECHUNK.fields_by_name["data"]._options = None
    _NORMALIZEDREPLY_WAVEFORMSAMPLECHUNK.fields_by_name["data"]._serialized_options = b"\020\001"
    _CONNECTSTATUS._serialized_start = 1418
    _CONNECTSTATUS._serialized_end = 1679
    _WFMREPLYSTATUS._serialized_start = 1682
    _WFMREPLYSTATUS._serialized_end = 1934
    _WFMPAIRTYPE._serialized_start = 1936
    _WFMPAIRTYPE._serialized_end = 2022
    _WFMTYPE._serialized_start = 2025
    _WFMTYPE._serialized_end = 2229
    _CONNECTREQUEST._serialized_start = 38
    _CONNECTREQUEST._serialized_end = 68
    _CONNECTREPLY._serialized_start = 70
    _CONNECTREPLY._serialized_end = 125
    _AVAILABLENAMESREPLY._serialized_start = 127
    _AVAILABLENAMESREPLY._serialized_end = 210
    _WAVEFORMREQUEST._serialized_start = 212
    _WAVEFORMREQUEST._serialized_end = 268
    _WAVEFORMHEADER._serialized_start = 271
    _WAVEFORMHEADER._serialized_end = 810
    _NORMALIZEDREPLY._serialized_start = 813
    _NORMALIZEDREPLY._serialized_end = 1121
    _NORMALIZEDREPLY_WAVEFORMSAMPLECHUNK._serialized_start = 942
    _NORMALIZEDREPLY_WAVEFORMSAMPLECHUNK._serialized_end = 981
    _NORMALIZEDREPLY_DATAORHEADERACCESS._serialized_start = 984
    _NORMALIZEDREPLY_DATAORHEADERACCESS._serialized_end = 1121
    _RAWREPLY._serialized_start = 1124
    _RAWREPLY._serialized_end = 1415
    _RAWREPLY_WAVEFORMSAMPLEBYTECHUNK._serialized_start = 1239
    _RAWREPLY_WAVEFORMSAMPLEBYTECHUNK._serialized_end = 1278
    _RAWREPLY_DATAORHEADERACCESS._serialized_start = 1281
    _RAWREPLY_DATAORHEADERACCESS._serialized_end = 1415
    _CONNECT._serialized_start = 2232
    _CONNECT._serialized_end = 2679
    _NORMALIZEDDATA._serialized_start = 2682
    _NORMALIZEDDATA._serialized_end = 2840
    _NATIVEDATA._serialized_start = 2843
    _NATIVEDATA._serialized_end = 2983
# @@protoc_insertion_point(module_scope)
