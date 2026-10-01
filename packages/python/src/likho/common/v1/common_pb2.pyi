from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Script(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCRIPT_UNSPECIFIED: _ClassVar[Script]
    SCRIPT_DEVANAGARI: _ClassVar[Script]
    SCRIPT_LATIN: _ClassVar[Script]
    SCRIPT_ARABIC: _ClassVar[Script]
SCRIPT_UNSPECIFIED: Script
SCRIPT_DEVANAGARI: Script
SCRIPT_LATIN: Script
SCRIPT_ARABIC: Script

class LanguageCandidate(_message.Message):
    __slots__ = ("language", "probability")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    language: str
    probability: float
    def __init__(self, language: _Optional[str] = ..., probability: _Optional[float] = ...) -> None: ...

class LanguageDetection(_message.Message):
    __slots__ = ("detected", "probability", "candidates", "decoded_as", "policy")
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    DECODED_AS_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    detected: str
    probability: float
    candidates: _containers.RepeatedCompositeFieldContainer[LanguageCandidate]
    decoded_as: str
    policy: str
    def __init__(self, detected: _Optional[str] = ..., probability: _Optional[float] = ..., candidates: _Optional[_Iterable[_Union[LanguageCandidate, _Mapping]]] = ..., decoded_as: _Optional[str] = ..., policy: _Optional[str] = ...) -> None: ...

class Segment(_message.Message):
    __slots__ = ("index", "start_seconds", "end_seconds", "text_script", "text_roman", "speaker", "leg_call_id", "avg_logprob", "no_speech_prob")
    INDEX_FIELD_NUMBER: _ClassVar[int]
    START_SECONDS_FIELD_NUMBER: _ClassVar[int]
    END_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TEXT_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    TEXT_ROMAN_FIELD_NUMBER: _ClassVar[int]
    SPEAKER_FIELD_NUMBER: _ClassVar[int]
    LEG_CALL_ID_FIELD_NUMBER: _ClassVar[int]
    AVG_LOGPROB_FIELD_NUMBER: _ClassVar[int]
    NO_SPEECH_PROB_FIELD_NUMBER: _ClassVar[int]
    index: int
    start_seconds: float
    end_seconds: float
    text_script: str
    text_roman: str
    speaker: str
    leg_call_id: str
    avg_logprob: float
    no_speech_prob: float
    def __init__(self, index: _Optional[int] = ..., start_seconds: _Optional[float] = ..., end_seconds: _Optional[float] = ..., text_script: _Optional[str] = ..., text_roman: _Optional[str] = ..., speaker: _Optional[str] = ..., leg_call_id: _Optional[str] = ..., avg_logprob: _Optional[float] = ..., no_speech_prob: _Optional[float] = ...) -> None: ...

class DialerCall(_message.Message):
    __slots__ = ("crt_object_id", "leg_call_ids", "campaign", "agent_user_id", "call_time_ist")
    CRT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LEG_CALL_IDS_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AGENT_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CALL_TIME_IST_FIELD_NUMBER: _ClassVar[int]
    crt_object_id: str
    leg_call_ids: _containers.RepeatedScalarFieldContainer[str]
    campaign: str
    agent_user_id: str
    call_time_ist: str
    def __init__(self, crt_object_id: _Optional[str] = ..., leg_call_ids: _Optional[_Iterable[str]] = ..., campaign: _Optional[str] = ..., agent_user_id: _Optional[str] = ..., call_time_ist: _Optional[str] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ("limit", "cursor")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    limit: int
    cursor: str
    def __init__(self, limit: _Optional[int] = ..., cursor: _Optional[str] = ...) -> None: ...

class PageInfo(_message.Message):
    __slots__ = ("next_cursor",)
    NEXT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    next_cursor: str
    def __init__(self, next_cursor: _Optional[str] = ...) -> None: ...
