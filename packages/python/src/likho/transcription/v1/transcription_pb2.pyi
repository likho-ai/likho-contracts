import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from likho.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Layer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAYER_UNSPECIFIED: _ClassVar[Layer]
    LAYER_SCRIPT: _ClassVar[Layer]
    LAYER_ROMAN: _ClassVar[Layer]
LAYER_UNSPECIFIED: Layer
LAYER_SCRIPT: Layer
LAYER_ROMAN: Layer

class ModelRef(_message.Message):
    __slots__ = ("registry_id", "engine", "compute")
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_FIELD_NUMBER: _ClassVar[int]
    registry_id: str
    engine: str
    compute: str
    def __init__(self, registry_id: _Optional[str] = ..., engine: _Optional[str] = ..., compute: _Optional[str] = ...) -> None: ...

class TranscriptStats(_message.Message):
    __slots__ = ("audio_seconds", "elapsed_seconds", "realtime_factor", "chunks", "silence_skipped_seconds")
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REALTIME_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    SILENCE_SKIPPED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    audio_seconds: float
    elapsed_seconds: float
    realtime_factor: float
    chunks: int
    silence_skipped_seconds: float
    def __init__(self, audio_seconds: _Optional[float] = ..., elapsed_seconds: _Optional[float] = ..., realtime_factor: _Optional[float] = ..., chunks: _Optional[int] = ..., silence_skipped_seconds: _Optional[float] = ...) -> None: ...

class Transcript(_message.Message):
    __slots__ = ("id", "recording_id", "job_id", "version", "model", "language", "script", "segments", "stats", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    recording_id: str
    job_id: str
    version: int
    model: ModelRef
    language: _common_pb2.LanguageDetection
    script: _common_pb2.Script
    segments: _containers.RepeatedCompositeFieldContainer[_common_pb2.Segment]
    stats: TranscriptStats
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., recording_id: _Optional[str] = ..., job_id: _Optional[str] = ..., version: _Optional[int] = ..., model: _Optional[_Union[ModelRef, _Mapping]] = ..., language: _Optional[_Union[_common_pb2.LanguageDetection, _Mapping]] = ..., script: _Optional[_Union[_common_pb2.Script, str]] = ..., segments: _Optional[_Iterable[_Union[_common_pb2.Segment, _Mapping]]] = ..., stats: _Optional[_Union[TranscriptStats, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetTranscriptRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTranscriptResponse(_message.Message):
    __slots__ = ("transcript",)
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    transcript: Transcript
    def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class ListTranscriptsRequest(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class ListTranscriptsResponse(_message.Message):
    __slots__ = ("transcripts",)
    TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    transcripts: _containers.RepeatedCompositeFieldContainer[Transcript]
    def __init__(self, transcripts: _Optional[_Iterable[_Union[Transcript, _Mapping]]] = ...) -> None: ...

class TranscribeRequest(_message.Message):
    __slots__ = ("recording_id", "model_registry_id", "language_policy", "media_id", "workspace_id", "evaluation")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_POLICY_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    model_registry_id: str
    language_policy: str
    media_id: str
    workspace_id: str
    evaluation: bool
    def __init__(self, recording_id: _Optional[str] = ..., model_registry_id: _Optional[str] = ..., language_policy: _Optional[str] = ..., media_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., evaluation: _Optional[bool] = ...) -> None: ...

class TranscribeStarted(_message.Message):
    __slots__ = ("audio_seconds", "language")
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    audio_seconds: float
    language: _common_pb2.LanguageDetection
    def __init__(self, audio_seconds: _Optional[float] = ..., language: _Optional[_Union[_common_pb2.LanguageDetection, _Mapping]] = ...) -> None: ...

class TranscribeResponse(_message.Message):
    __slots__ = ("started", "segment", "completed")
    STARTED_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    started: TranscribeStarted
    segment: _common_pb2.Segment
    completed: Transcript
    def __init__(self, started: _Optional[_Union[TranscribeStarted, _Mapping]] = ..., segment: _Optional[_Union[_common_pb2.Segment, _Mapping]] = ..., completed: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class Correction(_message.Message):
    __slots__ = ("id", "recording_id", "transcript_id", "corrected_transcript_id", "segment_index", "layer", "before", "after", "user_id", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    CORRECTED_TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    recording_id: str
    transcript_id: str
    corrected_transcript_id: str
    segment_index: int
    layer: Layer
    before: str
    after: str
    user_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., recording_id: _Optional[str] = ..., transcript_id: _Optional[str] = ..., corrected_transcript_id: _Optional[str] = ..., segment_index: _Optional[int] = ..., layer: _Optional[_Union[Layer, str]] = ..., before: _Optional[str] = ..., after: _Optional[str] = ..., user_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CorrectSegmentRequest(_message.Message):
    __slots__ = ("transcript_id", "segment_index", "layer", "text", "user_id", "workspace_id")
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    LAYER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    transcript_id: str
    segment_index: int
    layer: Layer
    text: str
    user_id: str
    workspace_id: str
    def __init__(self, transcript_id: _Optional[str] = ..., segment_index: _Optional[int] = ..., layer: _Optional[_Union[Layer, str]] = ..., text: _Optional[str] = ..., user_id: _Optional[str] = ..., workspace_id: _Optional[str] = ...) -> None: ...

class CorrectSegmentResponse(_message.Message):
    __slots__ = ("transcript", "correction")
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    CORRECTION_FIELD_NUMBER: _ClassVar[int]
    transcript: Transcript
    correction: Correction
    def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ..., correction: _Optional[_Union[Correction, _Mapping]] = ...) -> None: ...

class ListCorrectionsRequest(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    def __init__(self, recording_id: _Optional[str] = ...) -> None: ...

class ListCorrectionsResponse(_message.Message):
    __slots__ = ("corrections",)
    CORRECTIONS_FIELD_NUMBER: _ClassVar[int]
    corrections: _containers.RepeatedCompositeFieldContainer[Correction]
    def __init__(self, corrections: _Optional[_Iterable[_Union[Correction, _Mapping]]] = ...) -> None: ...

class RetransliterateRequest(_message.Message):
    __slots__ = ("transcript_id",)
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    transcript_id: str
    def __init__(self, transcript_id: _Optional[str] = ...) -> None: ...

class RetransliterateResponse(_message.Message):
    __slots__ = ("transcript",)
    TRANSCRIPT_FIELD_NUMBER: _ClassVar[int]
    transcript: Transcript
    def __init__(self, transcript: _Optional[_Union[Transcript, _Mapping]] = ...) -> None: ...

class Engine(_message.Message):
    __slots__ = ("registry_id", "engine", "output_script", "available", "is_default")
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    registry_id: str
    engine: str
    output_script: _common_pb2.Script
    available: bool
    is_default: bool
    def __init__(self, registry_id: _Optional[str] = ..., engine: _Optional[str] = ..., output_script: _Optional[_Union[_common_pb2.Script, str]] = ..., available: _Optional[bool] = ..., is_default: _Optional[bool] = ...) -> None: ...

class ListEnginesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListEnginesResponse(_message.Message):
    __slots__ = ("engines",)
    ENGINES_FIELD_NUMBER: _ClassVar[int]
    engines: _containers.RepeatedCompositeFieldContainer[Engine]
    def __init__(self, engines: _Optional[_Iterable[_Union[Engine, _Mapping]]] = ...) -> None: ...

class CancelJobRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class CancelJobResponse(_message.Message):
    __slots__ = ("cancelled",)
    CANCELLED_FIELD_NUMBER: _ClassVar[int]
    cancelled: bool
    def __init__(self, cancelled: _Optional[bool] = ...) -> None: ...
