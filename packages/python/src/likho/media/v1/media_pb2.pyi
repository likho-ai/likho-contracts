import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_STATUS_UNSPECIFIED: _ClassVar[MediaStatus]
    MEDIA_STATUS_UPLOADED: _ClassVar[MediaStatus]
    MEDIA_STATUS_READY: _ClassVar[MediaStatus]
    MEDIA_STATUS_FAILED: _ClassVar[MediaStatus]

class MediaKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEDIA_KIND_UNSPECIFIED: _ClassVar[MediaKind]
    MEDIA_KIND_ORIGINAL: _ClassVar[MediaKind]
    MEDIA_KIND_NORMALIZED: _ClassVar[MediaKind]
    MEDIA_KIND_PEAKS: _ClassVar[MediaKind]
MEDIA_STATUS_UNSPECIFIED: MediaStatus
MEDIA_STATUS_UPLOADED: MediaStatus
MEDIA_STATUS_READY: MediaStatus
MEDIA_STATUS_FAILED: MediaStatus
MEDIA_KIND_UNSPECIFIED: MediaKind
MEDIA_KIND_ORIGINAL: MediaKind
MEDIA_KIND_NORMALIZED: MediaKind
MEDIA_KIND_PEAKS: MediaKind

class Media(_message.Message):
    __slots__ = ("id", "original_name", "sha256", "content_type", "size_bytes", "duration_seconds", "channels", "sample_rate", "status", "failure_reason", "created_at", "workspace_id", "recording_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    original_name: str
    sha256: str
    content_type: str
    size_bytes: int
    duration_seconds: float
    channels: int
    sample_rate: int
    status: MediaStatus
    failure_reason: str
    created_at: _timestamp_pb2.Timestamp
    workspace_id: str
    recording_id: str
    def __init__(self, id: _Optional[str] = ..., original_name: _Optional[str] = ..., sha256: _Optional[str] = ..., content_type: _Optional[str] = ..., size_bytes: _Optional[int] = ..., duration_seconds: _Optional[float] = ..., channels: _Optional[int] = ..., sample_rate: _Optional[int] = ..., status: _Optional[_Union[MediaStatus, str]] = ..., failure_reason: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., workspace_id: _Optional[str] = ..., recording_id: _Optional[str] = ...) -> None: ...

class GetMediaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetMediaResponse(_message.Message):
    __slots__ = ("media",)
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    media: Media
    def __init__(self, media: _Optional[_Union[Media, _Mapping]] = ...) -> None: ...

class CreateUploadRequest(_message.Message):
    __slots__ = ("original_name", "size_bytes", "content_type", "sha256", "workspace_id", "recording_id")
    ORIGINAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHA256_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    original_name: str
    size_bytes: int
    content_type: str
    sha256: str
    workspace_id: str
    recording_id: str
    def __init__(self, original_name: _Optional[str] = ..., size_bytes: _Optional[int] = ..., content_type: _Optional[str] = ..., sha256: _Optional[str] = ..., workspace_id: _Optional[str] = ..., recording_id: _Optional[str] = ...) -> None: ...

class CreateUploadResponse(_message.Message):
    __slots__ = ("media_id", "upload_url", "expires_at", "existing_media")
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_MEDIA_FIELD_NUMBER: _ClassVar[int]
    media_id: str
    upload_url: str
    expires_at: _timestamp_pb2.Timestamp
    existing_media: Media
    def __init__(self, media_id: _Optional[str] = ..., upload_url: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., existing_media: _Optional[_Union[Media, _Mapping]] = ...) -> None: ...

class GetDownloadUrlRequest(_message.Message):
    __slots__ = ("id", "kind")
    ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    id: str
    kind: MediaKind
    def __init__(self, id: _Optional[str] = ..., kind: _Optional[_Union[MediaKind, str]] = ...) -> None: ...

class GetDownloadUrlResponse(_message.Message):
    __slots__ = ("url", "expires_at")
    URL_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    url: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, url: _Optional[str] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeleteMediaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteMediaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
