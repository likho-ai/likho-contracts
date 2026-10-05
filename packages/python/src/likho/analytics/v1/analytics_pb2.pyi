import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METRIC_UNSPECIFIED: _ClassVar[Metric]
    METRIC_CALLS: _ClassVar[Metric]
    METRIC_TRANSCRIBED: _ClassVar[Metric]
    METRIC_MINUTES: _ClassVar[Metric]
    METRIC_REALTIME_FACTOR: _ClassVar[Metric]
    METRIC_ANALYSED: _ClassVar[Metric]
    METRIC_SCORE: _ClassVar[Metric]
    METRIC_NEGATIVE: _ClassVar[Metric]

class Bucket(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUCKET_UNSPECIFIED: _ClassVar[Bucket]
    BUCKET_DAY: _ClassVar[Bucket]
    BUCKET_HOUR: _ClassVar[Bucket]

class Dimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIMENSION_UNSPECIFIED: _ClassVar[Dimension]
    DIMENSION_AGENT: _ClassVar[Dimension]
    DIMENSION_CAMPAIGN: _ClassVar[Dimension]
    DIMENSION_DISPOSITION: _ClassVar[Dimension]
    DIMENSION_LANGUAGE: _ClassVar[Dimension]
    DIMENSION_SENTIMENT: _ClassVar[Dimension]
    DIMENSION_SOURCE: _ClassVar[Dimension]
METRIC_UNSPECIFIED: Metric
METRIC_CALLS: Metric
METRIC_TRANSCRIBED: Metric
METRIC_MINUTES: Metric
METRIC_REALTIME_FACTOR: Metric
METRIC_ANALYSED: Metric
METRIC_SCORE: Metric
METRIC_NEGATIVE: Metric
BUCKET_UNSPECIFIED: Bucket
BUCKET_DAY: Bucket
BUCKET_HOUR: Bucket
DIMENSION_UNSPECIFIED: Dimension
DIMENSION_AGENT: Dimension
DIMENSION_CAMPAIGN: Dimension
DIMENSION_DISPOSITION: Dimension
DIMENSION_LANGUAGE: Dimension
DIMENSION_SENTIMENT: Dimension
DIMENSION_SOURCE: Dimension

class Window(_message.Message):
    __slots__ = ("since", "until")
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Facts(_message.Message):
    __slots__ = ("campaign", "agent", "disposition", "source", "language")
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    campaign: str
    agent: str
    disposition: str
    source: str
    language: str
    def __init__(self, campaign: _Optional[str] = ..., agent: _Optional[str] = ..., disposition: _Optional[str] = ..., source: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class GetOverviewRequest(_message.Message):
    __slots__ = ("workspace_id", "window", "facts")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    window: Window
    facts: Facts
    def __init__(self, workspace_id: _Optional[str] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., facts: _Optional[_Union[Facts, _Mapping]] = ...) -> None: ...

class Overview(_message.Message):
    __slots__ = ("calls", "transcribed", "failed", "minutes", "realtime_factor", "analysed", "score", "sentiments", "languages")
    CALLS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIBED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    REALTIME_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ANALYSED_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SENTIMENTS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    calls: int
    transcribed: int
    failed: int
    minutes: float
    realtime_factor: float
    analysed: int
    score: float
    sentiments: _containers.RepeatedCompositeFieldContainer[Count]
    languages: _containers.RepeatedCompositeFieldContainer[Count]
    def __init__(self, calls: _Optional[int] = ..., transcribed: _Optional[int] = ..., failed: _Optional[int] = ..., minutes: _Optional[float] = ..., realtime_factor: _Optional[float] = ..., analysed: _Optional[int] = ..., score: _Optional[float] = ..., sentiments: _Optional[_Iterable[_Union[Count, _Mapping]]] = ..., languages: _Optional[_Iterable[_Union[Count, _Mapping]]] = ...) -> None: ...

class Count(_message.Message):
    __slots__ = ("key", "count")
    KEY_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    key: str
    count: int
    def __init__(self, key: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetOverviewResponse(_message.Message):
    __slots__ = ("overview",)
    OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    overview: Overview
    def __init__(self, overview: _Optional[_Union[Overview, _Mapping]] = ...) -> None: ...

class GetTimeseriesRequest(_message.Message):
    __slots__ = ("workspace_id", "window", "facts", "metric", "bucket")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    window: Window
    facts: Facts
    metric: Metric
    bucket: Bucket
    def __init__(self, workspace_id: _Optional[str] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., facts: _Optional[_Union[Facts, _Mapping]] = ..., metric: _Optional[_Union[Metric, str]] = ..., bucket: _Optional[_Union[Bucket, str]] = ...) -> None: ...

class Point(_message.Message):
    __slots__ = ("at", "value")
    AT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    at: _timestamp_pb2.Timestamp
    value: float
    def __init__(self, at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ...) -> None: ...

class GetTimeseriesResponse(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[Point]
    def __init__(self, points: _Optional[_Iterable[_Union[Point, _Mapping]]] = ...) -> None: ...

class GetBreakdownRequest(_message.Message):
    __slots__ = ("workspace_id", "window", "facts", "by", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    FACTS_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    window: Window
    facts: Facts
    by: Dimension
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., window: _Optional[_Union[Window, _Mapping]] = ..., facts: _Optional[_Union[Facts, _Mapping]] = ..., by: _Optional[_Union[Dimension, str]] = ..., limit: _Optional[int] = ...) -> None: ...

class Row(_message.Message):
    __slots__ = ("key", "calls", "transcribed", "minutes", "analysed", "score", "negative")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIBED_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    ANALYSED_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    key: str
    calls: int
    transcribed: int
    minutes: float
    analysed: int
    score: float
    negative: int
    def __init__(self, key: _Optional[str] = ..., calls: _Optional[int] = ..., transcribed: _Optional[int] = ..., minutes: _Optional[float] = ..., analysed: _Optional[int] = ..., score: _Optional[float] = ..., negative: _Optional[int] = ...) -> None: ...

class GetBreakdownResponse(_message.Message):
    __slots__ = ("rows",)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[Row]
    def __init__(self, rows: _Optional[_Iterable[_Union[Row, _Mapping]]] = ...) -> None: ...
