import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchRequest(_message.Message):
    __slots__ = ("workspace_id", "query", "language", "recording_id", "since", "until", "page", "page_size", "campaign", "agent", "disposition", "source", "call_since", "call_until")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CALL_SINCE_FIELD_NUMBER: _ClassVar[int]
    CALL_UNTIL_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    query: str
    language: str
    recording_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    page: int
    page_size: int
    campaign: str
    agent: str
    disposition: str
    source: str
    call_since: _timestamp_pb2.Timestamp
    call_until: _timestamp_pb2.Timestamp
    def __init__(self, workspace_id: _Optional[str] = ..., query: _Optional[str] = ..., language: _Optional[str] = ..., recording_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., campaign: _Optional[str] = ..., agent: _Optional[str] = ..., disposition: _Optional[str] = ..., source: _Optional[str] = ..., call_since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., call_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Hit(_message.Message):
    __slots__ = ("recording_id", "recording_name", "transcript_id", "segment_index", "start_seconds", "end_seconds", "text_roman", "text_script", "highlight_roman", "highlight_script", "language", "created_at", "campaign", "agent", "disposition", "source", "call_time")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_SECONDS_FIELD_NUMBER: _ClassVar[int]
    END_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TEXT_ROMAN_FIELD_NUMBER: _ClassVar[int]
    TEXT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_ROMAN_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CALL_TIME_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    recording_name: str
    transcript_id: str
    segment_index: int
    start_seconds: float
    end_seconds: float
    text_roman: str
    text_script: str
    highlight_roman: str
    highlight_script: str
    language: str
    created_at: _timestamp_pb2.Timestamp
    campaign: str
    agent: str
    disposition: str
    source: str
    call_time: _timestamp_pb2.Timestamp
    def __init__(self, recording_id: _Optional[str] = ..., recording_name: _Optional[str] = ..., transcript_id: _Optional[str] = ..., segment_index: _Optional[int] = ..., start_seconds: _Optional[float] = ..., end_seconds: _Optional[float] = ..., text_roman: _Optional[str] = ..., text_script: _Optional[str] = ..., highlight_roman: _Optional[str] = ..., highlight_script: _Optional[str] = ..., language: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., campaign: _Optional[str] = ..., agent: _Optional[str] = ..., disposition: _Optional[str] = ..., source: _Optional[str] = ..., call_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("hits", "page", "page_size", "total", "processing_ms")
    HITS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_MS_FIELD_NUMBER: _ClassVar[int]
    hits: _containers.RepeatedCompositeFieldContainer[Hit]
    page: int
    page_size: int
    total: int
    processing_ms: int
    def __init__(self, hits: _Optional[_Iterable[_Union[Hit, _Mapping]]] = ..., page: _Optional[int] = ..., page_size: _Optional[int] = ..., total: _Optional[int] = ..., processing_ms: _Optional[int] = ...) -> None: ...

class ReindexRequest(_message.Message):
    __slots__ = ("transcript_id", "workspace_id")
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    transcript_id: str
    workspace_id: str
    def __init__(self, transcript_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class ReindexResponse(_message.Message):
    __slots__ = ("lines",)
    LINES_FIELD_NUMBER: _ClassVar[int]
    lines: int
    def __init__(self, lines: _Optional[int] = ...) -> None: ...

class DeleteRecordingRequest(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class DeleteRecordingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
