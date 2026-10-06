import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Window(_message.Message):
    __slots__ = ("since", "until")
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListCampaignsRequest(_message.Message):
    __slots__ = ("window",)
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    window: Window
    def __init__(self, window: _Optional[_Union[Window, _Mapping]] = ...) -> None: ...

class Campaign(_message.Message):
    __slots__ = ("name", "calls", "connected", "interactions", "talk_seconds")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    TALK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    calls: int
    connected: int
    interactions: int
    talk_seconds: int
    def __init__(self, name: _Optional[str] = ..., calls: _Optional[int] = ..., connected: _Optional[int] = ..., interactions: _Optional[int] = ..., talk_seconds: _Optional[int] = ...) -> None: ...

class ListCampaignsResponse(_message.Message):
    __slots__ = ("campaigns",)
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    campaigns: _containers.RepeatedCompositeFieldContainer[Campaign]
    def __init__(self, campaigns: _Optional[_Iterable[_Union[Campaign, _Mapping]]] = ...) -> None: ...

class ListAgentsRequest(_message.Message):
    __slots__ = ("window", "campaign")
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    window: Window
    campaign: str
    def __init__(self, window: _Optional[_Union[Window, _Mapping]] = ..., campaign: _Optional[str] = ...) -> None: ...

class Agent(_message.Message):
    __slots__ = ("id", "name", "calls", "connected", "talk_seconds")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CALLS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TALK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    calls: int
    connected: int
    talk_seconds: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., calls: _Optional[int] = ..., connected: _Optional[int] = ..., talk_seconds: _Optional[int] = ...) -> None: ...

class ListAgentsResponse(_message.Message):
    __slots__ = ("agents",)
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    agents: _containers.RepeatedCompositeFieldContainer[Agent]
    def __init__(self, agents: _Optional[_Iterable[_Union[Agent, _Mapping]]] = ...) -> None: ...

class ListCallsRequest(_message.Message):
    __slots__ = ("window", "campaign", "agent", "connected_only", "min_talk_seconds", "after", "limit")
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_ONLY_FIELD_NUMBER: _ClassVar[int]
    MIN_TALK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    window: Window
    campaign: str
    agent: str
    connected_only: bool
    min_talk_seconds: int
    after: str
    limit: int
    def __init__(self, window: _Optional[_Union[Window, _Mapping]] = ..., campaign: _Optional[str] = ..., agent: _Optional[str] = ..., connected_only: _Optional[bool] = ..., min_talk_seconds: _Optional[int] = ..., after: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class Call(_message.Message):
    __slots__ = ("crt_object_id", "call_id", "call_time", "campaign", "transferred_campaign", "agent", "agent_id", "disposition", "call_type", "connected", "talk_seconds", "phone", "hangup_by", "queue")
    CRT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TIME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    TRANSFERRED_CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    TALK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    HANGUP_BY_FIELD_NUMBER: _ClassVar[int]
    QUEUE_FIELD_NUMBER: _ClassVar[int]
    crt_object_id: str
    call_id: str
    call_time: str
    campaign: str
    transferred_campaign: str
    agent: str
    agent_id: str
    disposition: str
    call_type: str
    connected: bool
    talk_seconds: int
    phone: str
    hangup_by: str
    queue: str
    def __init__(self, crt_object_id: _Optional[str] = ..., call_id: _Optional[str] = ..., call_time: _Optional[str] = ..., campaign: _Optional[str] = ..., transferred_campaign: _Optional[str] = ..., agent: _Optional[str] = ..., agent_id: _Optional[str] = ..., disposition: _Optional[str] = ..., call_type: _Optional[str] = ..., connected: _Optional[bool] = ..., talk_seconds: _Optional[int] = ..., phone: _Optional[str] = ..., hangup_by: _Optional[str] = ..., queue: _Optional[str] = ...) -> None: ...

class ListCallsResponse(_message.Message):
    __slots__ = ("calls", "next_cursor")
    CALLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    calls: _containers.RepeatedCompositeFieldContainer[Call]
    next_cursor: str
    def __init__(self, calls: _Optional[_Iterable[_Union[Call, _Mapping]]] = ..., next_cursor: _Optional[str] = ...) -> None: ...

class GetCallRequest(_message.Message):
    __slots__ = ("crt_object_id",)
    CRT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    crt_object_id: str
    def __init__(self, crt_object_id: _Optional[str] = ...) -> None: ...

class GetCallResponse(_message.Message):
    __slots__ = ("call",)
    CALL_FIELD_NUMBER: _ClassVar[int]
    call: Call
    def __init__(self, call: _Optional[_Union[Call, _Mapping]] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStatusResponse(_message.Message):
    __slots__ = ("database_configured", "schedule_enabled", "cursor", "imported_today", "daily_limit", "campaigns", "min_talk_seconds", "writeback_enabled", "archive_enabled", "version", "last_run_at", "last_run_summary")
    DATABASE_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_TODAY_FIELD_NUMBER: _ClassVar[int]
    DAILY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    MIN_TALK_SECONDS_FIELD_NUMBER: _ClassVar[int]
    WRITEBACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    database_configured: bool
    schedule_enabled: bool
    cursor: str
    imported_today: int
    daily_limit: int
    campaigns: _containers.RepeatedScalarFieldContainer[str]
    min_talk_seconds: int
    writeback_enabled: bool
    archive_enabled: bool
    version: str
    last_run_at: _timestamp_pb2.Timestamp
    last_run_summary: str
    def __init__(self, database_configured: _Optional[bool] = ..., schedule_enabled: _Optional[bool] = ..., cursor: _Optional[str] = ..., imported_today: _Optional[int] = ..., daily_limit: _Optional[int] = ..., campaigns: _Optional[_Iterable[str]] = ..., min_talk_seconds: _Optional[int] = ..., writeback_enabled: _Optional[bool] = ..., archive_enabled: _Optional[bool] = ..., version: _Optional[str] = ..., last_run_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_run_summary: _Optional[str] = ...) -> None: ...
