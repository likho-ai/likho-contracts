import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetInsightsRequest(_message.Message):
    __slots__ = ("recording_id", "transcript_id")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    transcript_id: str
    def __init__(self, recording_id: _Optional[str] = ..., transcript_id: _Optional[str] = ...) -> None: ...

class GetInsightsResponse(_message.Message):
    __slots__ = ("insights",)
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: Insights
    def __init__(self, insights: _Optional[_Union[Insights, _Mapping]] = ...) -> None: ...

class AnalyseRequest(_message.Message):
    __slots__ = ("transcript_id", "workspace_id", "force")
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    transcript_id: str
    workspace_id: str
    force: bool
    def __init__(self, transcript_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., force: _Optional[bool] = ...) -> None: ...

class AnalyseResponse(_message.Message):
    __slots__ = ("insights",)
    INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    insights: Insights
    def __init__(self, insights: _Optional[_Union[Insights, _Mapping]] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStatusResponse(_message.Message):
    __slots__ = ("enabled", "model", "form_version")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    FORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    model: str
    form_version: str
    def __init__(self, enabled: _Optional[bool] = ..., model: _Optional[str] = ..., form_version: _Optional[str] = ...) -> None: ...

class Check(_message.Message):
    __slots__ = ("key", "label", "answer", "evidence")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    answer: str
    evidence: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., answer: _Optional[str] = ..., evidence: _Optional[str] = ...) -> None: ...

class Score(_message.Message):
    __slots__ = ("key", "label", "score", "max", "reason")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    score: float
    max: float
    reason: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., score: _Optional[float] = ..., max: _Optional[float] = ..., reason: _Optional[str] = ...) -> None: ...

class Insights(_message.Message):
    __slots__ = ("id", "transcript_id", "recording_id", "workspace_id", "transcript_version", "summary", "products", "sentiment", "intent", "checks", "scores", "score_total", "score_max", "model", "input_tokens", "output_tokens", "form_version", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    SENTIMENT_FIELD_NUMBER: _ClassVar[int]
    INTENT_FIELD_NUMBER: _ClassVar[int]
    CHECKS_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    SCORE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    SCORE_MAX_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    FORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    transcript_id: str
    recording_id: str
    workspace_id: str
    transcript_version: int
    summary: str
    products: _containers.RepeatedScalarFieldContainer[str]
    sentiment: str
    intent: str
    checks: _containers.RepeatedCompositeFieldContainer[Check]
    scores: _containers.RepeatedCompositeFieldContainer[Score]
    score_total: float
    score_max: float
    model: str
    input_tokens: int
    output_tokens: int
    form_version: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., transcript_id: _Optional[str] = ..., recording_id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., transcript_version: _Optional[int] = ..., summary: _Optional[str] = ..., products: _Optional[_Iterable[str]] = ..., sentiment: _Optional[str] = ..., intent: _Optional[str] = ..., checks: _Optional[_Iterable[_Union[Check, _Mapping]]] = ..., scores: _Optional[_Iterable[_Union[Score, _Mapping]]] = ..., score_total: _Optional[float] = ..., score_max: _Optional[float] = ..., model: _Optional[str] = ..., input_tokens: _Optional[int] = ..., output_tokens: _Optional[int] = ..., form_version: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
