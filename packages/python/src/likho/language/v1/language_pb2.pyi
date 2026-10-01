from likho.common.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransliterateRequest(_message.Message):
    __slots__ = ("workspace_id", "text", "source_script")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    text: str
    source_script: _common_pb2.Script
    def __init__(self, workspace_id: _Optional[str] = ..., text: _Optional[str] = ..., source_script: _Optional[_Union[_common_pb2.Script, str]] = ...) -> None: ...

class TransliterateResponse(_message.Message):
    __slots__ = ("text_roman", "vocabulary_version")
    TEXT_ROMAN_FIELD_NUMBER: _ClassVar[int]
    VOCABULARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    text_roman: str
    vocabulary_version: int
    def __init__(self, text_roman: _Optional[str] = ..., vocabulary_version: _Optional[int] = ...) -> None: ...

class TransliterateBatchRequest(_message.Message):
    __slots__ = ("workspace_id", "texts", "source_script")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    texts: _containers.RepeatedScalarFieldContainer[str]
    source_script: _common_pb2.Script
    def __init__(self, workspace_id: _Optional[str] = ..., texts: _Optional[_Iterable[str]] = ..., source_script: _Optional[_Union[_common_pb2.Script, str]] = ...) -> None: ...

class TransliterateBatchResponse(_message.Message):
    __slots__ = ("texts_roman", "vocabulary_version")
    TEXTS_ROMAN_FIELD_NUMBER: _ClassVar[int]
    VOCABULARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    texts_roman: _containers.RepeatedScalarFieldContainer[str]
    vocabulary_version: int
    def __init__(self, texts_roman: _Optional[_Iterable[str]] = ..., vocabulary_version: _Optional[int] = ...) -> None: ...

class GetHotwordsRequest(_message.Message):
    __slots__ = ("workspace_id", "language")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    language: str
    def __init__(self, workspace_id: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class GetHotwordsResponse(_message.Message):
    __slots__ = ("terms", "vocabulary_version")
    TERMS_FIELD_NUMBER: _ClassVar[int]
    VOCABULARY_VERSION_FIELD_NUMBER: _ClassVar[int]
    terms: _containers.RepeatedScalarFieldContainer[str]
    vocabulary_version: int
    def __init__(self, terms: _Optional[_Iterable[str]] = ..., vocabulary_version: _Optional[int] = ...) -> None: ...

class ResolveDecodePolicyRequest(_message.Message):
    __slots__ = ("workspace_id", "detected", "probability", "candidates")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    detected: str
    probability: float
    candidates: _containers.RepeatedCompositeFieldContainer[_common_pb2.LanguageCandidate]
    def __init__(self, workspace_id: _Optional[str] = ..., detected: _Optional[str] = ..., probability: _Optional[float] = ..., candidates: _Optional[_Iterable[_Union[_common_pb2.LanguageCandidate, _Mapping]]] = ...) -> None: ...

class ResolveDecodePolicyResponse(_message.Message):
    __slots__ = ("decode_as", "transliterate")
    DECODE_AS_FIELD_NUMBER: _ClassVar[int]
    TRANSLITERATE_FIELD_NUMBER: _ClassVar[int]
    decode_as: str
    transliterate: bool
    def __init__(self, decode_as: _Optional[str] = ..., transliterate: _Optional[bool] = ...) -> None: ...

class GlossaryTerm(_message.Message):
    __slots__ = ("id", "term", "language", "enabled", "note")
    ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    term: str
    language: str
    enabled: bool
    note: str
    def __init__(self, id: _Optional[str] = ..., term: _Optional[str] = ..., language: _Optional[str] = ..., enabled: _Optional[bool] = ..., note: _Optional[str] = ...) -> None: ...

class ListGlossaryTermsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListGlossaryTermsResponse(_message.Message):
    __slots__ = ("terms",)
    TERMS_FIELD_NUMBER: _ClassVar[int]
    terms: _containers.RepeatedCompositeFieldContainer[GlossaryTerm]
    def __init__(self, terms: _Optional[_Iterable[_Union[GlossaryTerm, _Mapping]]] = ...) -> None: ...

class UpsertGlossaryTermRequest(_message.Message):
    __slots__ = ("workspace_id", "term")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    term: GlossaryTerm
    def __init__(self, workspace_id: _Optional[str] = ..., term: _Optional[_Union[GlossaryTerm, _Mapping]] = ...) -> None: ...

class UpsertGlossaryTermResponse(_message.Message):
    __slots__ = ("term",)
    TERM_FIELD_NUMBER: _ClassVar[int]
    term: GlossaryTerm
    def __init__(self, term: _Optional[_Union[GlossaryTerm, _Mapping]] = ...) -> None: ...

class DeleteGlossaryTermRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteGlossaryTermResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Spelling(_message.Message):
    __slots__ = ("id", "source", "target", "is_phrase", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    IS_PHRASE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    source: str
    target: str
    is_phrase: bool
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[str] = ..., is_phrase: _Optional[bool] = ..., enabled: _Optional[bool] = ...) -> None: ...

class ListSpellingsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListSpellingsResponse(_message.Message):
    __slots__ = ("spellings",)
    SPELLINGS_FIELD_NUMBER: _ClassVar[int]
    spellings: _containers.RepeatedCompositeFieldContainer[Spelling]
    def __init__(self, spellings: _Optional[_Iterable[_Union[Spelling, _Mapping]]] = ...) -> None: ...

class UpsertSpellingRequest(_message.Message):
    __slots__ = ("workspace_id", "spelling")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPELLING_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    spelling: Spelling
    def __init__(self, workspace_id: _Optional[str] = ..., spelling: _Optional[_Union[Spelling, _Mapping]] = ...) -> None: ...

class UpsertSpellingResponse(_message.Message):
    __slots__ = ("spelling",)
    SPELLING_FIELD_NUMBER: _ClassVar[int]
    spelling: Spelling
    def __init__(self, spelling: _Optional[_Union[Spelling, _Mapping]] = ...) -> None: ...

class DeleteSpellingRequest(_message.Message):
    __slots__ = ("workspace_id", "id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    id: str
    def __init__(self, workspace_id: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteSpellingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
