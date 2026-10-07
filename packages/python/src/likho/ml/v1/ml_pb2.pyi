import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModelStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODEL_STATUS_UNSPECIFIED: _ClassVar[ModelStatus]
    MODEL_STATUS_AVAILABLE: _ClassVar[ModelStatus]
    MODEL_STATUS_RETIRED: _ClassVar[ModelStatus]

class EvaluationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVALUATION_STATUS_UNSPECIFIED: _ClassVar[EvaluationStatus]
    EVALUATION_STATUS_QUEUED: _ClassVar[EvaluationStatus]
    EVALUATION_STATUS_RUNNING: _ClassVar[EvaluationStatus]
    EVALUATION_STATUS_COMPLETED: _ClassVar[EvaluationStatus]
    EVALUATION_STATUS_FAILED: _ClassVar[EvaluationStatus]

class TrainingRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAINING_RUN_STATUS_UNSPECIFIED: _ClassVar[TrainingRunStatus]
    TRAINING_RUN_STATUS_PENDING: _ClassVar[TrainingRunStatus]
    TRAINING_RUN_STATUS_RUNNING: _ClassVar[TrainingRunStatus]
    TRAINING_RUN_STATUS_COMPLETED: _ClassVar[TrainingRunStatus]
    TRAINING_RUN_STATUS_FAILED: _ClassVar[TrainingRunStatus]
MODEL_STATUS_UNSPECIFIED: ModelStatus
MODEL_STATUS_AVAILABLE: ModelStatus
MODEL_STATUS_RETIRED: ModelStatus
EVALUATION_STATUS_UNSPECIFIED: EvaluationStatus
EVALUATION_STATUS_QUEUED: EvaluationStatus
EVALUATION_STATUS_RUNNING: EvaluationStatus
EVALUATION_STATUS_COMPLETED: EvaluationStatus
EVALUATION_STATUS_FAILED: EvaluationStatus
TRAINING_RUN_STATUS_UNSPECIFIED: TrainingRunStatus
TRAINING_RUN_STATUS_PENDING: TrainingRunStatus
TRAINING_RUN_STATUS_RUNNING: TrainingRunStatus
TRAINING_RUN_STATUS_COMPLETED: TrainingRunStatus
TRAINING_RUN_STATUS_FAILED: TrainingRunStatus

class Scores(_message.Message):
    __slots__ = ("wer_script", "cer_script", "wer_roman", "cer_roman")
    WER_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    CER_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    WER_ROMAN_FIELD_NUMBER: _ClassVar[int]
    CER_ROMAN_FIELD_NUMBER: _ClassVar[int]
    wer_script: float
    cer_script: float
    wer_roman: float
    cer_roman: float
    def __init__(self, wer_script: _Optional[float] = ..., cer_script: _Optional[float] = ..., wer_roman: _Optional[float] = ..., cer_roman: _Optional[float] = ...) -> None: ...

class Model(_message.Message):
    __slots__ = ("id", "registry_id", "engine", "name", "description", "languages", "artifact_uri", "base_model_id", "status", "is_default", "latest_evaluation_id", "latest_scores", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LATEST_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    LATEST_SCORES_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    registry_id: str
    engine: str
    name: str
    description: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    artifact_uri: str
    base_model_id: str
    status: ModelStatus
    is_default: bool
    latest_evaluation_id: str
    latest_scores: Scores
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., registry_id: _Optional[str] = ..., engine: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., artifact_uri: _Optional[str] = ..., base_model_id: _Optional[str] = ..., status: _Optional[_Union[ModelStatus, str]] = ..., is_default: _Optional[bool] = ..., latest_evaluation_id: _Optional[str] = ..., latest_scores: _Optional[_Union[Scores, _Mapping]] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ListModelsRequest(_message.Message):
    __slots__ = ("include_retired",)
    INCLUDE_RETIRED_FIELD_NUMBER: _ClassVar[int]
    include_retired: bool
    def __init__(self, include_retired: _Optional[bool] = ...) -> None: ...

class ListModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[Model]
    def __init__(self, models: _Optional[_Iterable[_Union[Model, _Mapping]]] = ...) -> None: ...

class GetModelRequest(_message.Message):
    __slots__ = ("model_id", "registry_id")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    registry_id: str
    def __init__(self, model_id: _Optional[str] = ..., registry_id: _Optional[str] = ...) -> None: ...

class GetModelResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class GetDefaultRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefaultResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class RegisterModelRequest(_message.Message):
    __slots__ = ("registry_id", "description", "languages", "artifact_uri", "base_model_id", "user_id")
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    registry_id: str
    description: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    artifact_uri: str
    base_model_id: str
    user_id: str
    def __init__(self, registry_id: _Optional[str] = ..., description: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., artifact_uri: _Optional[str] = ..., base_model_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RegisterModelResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class SetDefaultRequest(_message.Message):
    __slots__ = ("model_id", "user_id")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    user_id: str
    def __init__(self, model_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class SetDefaultResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class RetireModelRequest(_message.Message):
    __slots__ = ("model_id", "user_id")
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    model_id: str
    user_id: str
    def __init__(self, model_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RetireModelResponse(_message.Message):
    __slots__ = ("model",)
    MODEL_FIELD_NUMBER: _ClassVar[int]
    model: Model
    def __init__(self, model: _Optional[_Union[Model, _Mapping]] = ...) -> None: ...

class GoldItem(_message.Message):
    __slots__ = ("id", "workspace_id", "recording_id", "transcript_id", "transcript_version", "language", "audio_seconds", "lines", "added_by", "added_at", "media_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_VERSION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    ADDED_BY_FIELD_NUMBER: _ClassVar[int]
    ADDED_AT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    recording_id: str
    transcript_id: str
    transcript_version: int
    language: str
    audio_seconds: float
    lines: int
    added_by: str
    added_at: _timestamp_pb2.Timestamp
    media_id: str
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., recording_id: _Optional[str] = ..., transcript_id: _Optional[str] = ..., transcript_version: _Optional[int] = ..., language: _Optional[str] = ..., audio_seconds: _Optional[float] = ..., lines: _Optional[int] = ..., added_by: _Optional[str] = ..., added_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., media_id: _Optional[str] = ...) -> None: ...

class AddToGoldSetRequest(_message.Message):
    __slots__ = ("workspace_id", "recording_id", "transcript_id", "user_id", "media_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    recording_id: str
    transcript_id: str
    user_id: str
    media_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., recording_id: _Optional[str] = ..., transcript_id: _Optional[str] = ..., user_id: _Optional[str] = ..., media_id: _Optional[str] = ...) -> None: ...

class AddToGoldSetResponse(_message.Message):
    __slots__ = ("item",)
    ITEM_FIELD_NUMBER: _ClassVar[int]
    item: GoldItem
    def __init__(self, item: _Optional[_Union[GoldItem, _Mapping]] = ...) -> None: ...

class RemoveFromGoldSetRequest(_message.Message):
    __slots__ = ("workspace_id", "recording_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    recording_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., recording_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RemoveFromGoldSetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListGoldSetRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListGoldSetResponse(_message.Message):
    __slots__ = ("items", "audio_seconds")
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GoldItem]
    audio_seconds: float
    def __init__(self, items: _Optional[_Iterable[_Union[GoldItem, _Mapping]]] = ..., audio_seconds: _Optional[float] = ...) -> None: ...

class EvaluationItem(_message.Message):
    __slots__ = ("recording_id", "reference_transcript_id", "scores", "words", "audio_seconds", "elapsed_seconds", "error")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRANSCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    WORDS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    reference_transcript_id: str
    scores: Scores
    words: int
    audio_seconds: float
    elapsed_seconds: float
    error: str
    def __init__(self, recording_id: _Optional[str] = ..., reference_transcript_id: _Optional[str] = ..., scores: _Optional[_Union[Scores, _Mapping]] = ..., words: _Optional[int] = ..., audio_seconds: _Optional[float] = ..., elapsed_seconds: _Optional[float] = ..., error: _Optional[str] = ...) -> None: ...

class Evaluation(_message.Message):
    __slots__ = ("id", "workspace_id", "model_id", "registry_id", "status", "scores", "items_total", "items_done", "audio_seconds", "realtime_factor", "items", "error", "started_by", "created_at", "finished_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCORES_FIELD_NUMBER: _ClassVar[int]
    ITEMS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_DONE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    REALTIME_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STARTED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    model_id: str
    registry_id: str
    status: EvaluationStatus
    scores: Scores
    items_total: int
    items_done: int
    audio_seconds: float
    realtime_factor: float
    items: _containers.RepeatedCompositeFieldContainer[EvaluationItem]
    error: str
    started_by: str
    created_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., model_id: _Optional[str] = ..., registry_id: _Optional[str] = ..., status: _Optional[_Union[EvaluationStatus, str]] = ..., scores: _Optional[_Union[Scores, _Mapping]] = ..., items_total: _Optional[int] = ..., items_done: _Optional[int] = ..., audio_seconds: _Optional[float] = ..., realtime_factor: _Optional[float] = ..., items: _Optional[_Iterable[_Union[EvaluationItem, _Mapping]]] = ..., error: _Optional[str] = ..., started_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartEvaluationRequest(_message.Message):
    __slots__ = ("workspace_id", "model_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    model_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., model_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class StartEvaluationResponse(_message.Message):
    __slots__ = ("evaluation",)
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: Evaluation
    def __init__(self, evaluation: _Optional[_Union[Evaluation, _Mapping]] = ...) -> None: ...

class GetEvaluationRequest(_message.Message):
    __slots__ = ("evaluation_id",)
    EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    evaluation_id: str
    def __init__(self, evaluation_id: _Optional[str] = ...) -> None: ...

class GetEvaluationResponse(_message.Message):
    __slots__ = ("evaluation",)
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: Evaluation
    def __init__(self, evaluation: _Optional[_Union[Evaluation, _Mapping]] = ...) -> None: ...

class ListEvaluationsRequest(_message.Message):
    __slots__ = ("workspace_id", "model_id", "limit")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    model_id: str
    limit: int
    def __init__(self, workspace_id: _Optional[str] = ..., model_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class ListEvaluationsResponse(_message.Message):
    __slots__ = ("evaluations",)
    EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    evaluations: _containers.RepeatedCompositeFieldContainer[Evaluation]
    def __init__(self, evaluations: _Optional[_Iterable[_Union[Evaluation, _Mapping]]] = ...) -> None: ...

class GetTrainingStatsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class GetTrainingStatsResponse(_message.Message):
    __slots__ = ("examples", "script_examples", "roman_examples", "recordings", "audio_seconds", "last_example_at")
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    ROMAN_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXAMPLE_AT_FIELD_NUMBER: _ClassVar[int]
    examples: int
    script_examples: int
    roman_examples: int
    recordings: int
    audio_seconds: float
    last_example_at: _timestamp_pb2.Timestamp
    def __init__(self, examples: _Optional[int] = ..., script_examples: _Optional[int] = ..., roman_examples: _Optional[int] = ..., recordings: _Optional[int] = ..., audio_seconds: _Optional[float] = ..., last_example_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ("id", "workspace_id", "uri", "examples", "audio_seconds", "held_out_recordings", "created_by", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HELD_OUT_RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    uri: str
    examples: int
    audio_seconds: float
    held_out_recordings: int
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., uri: _Optional[str] = ..., examples: _Optional[int] = ..., audio_seconds: _Optional[float] = ..., held_out_recordings: _Optional[int] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ExportDatasetRequest(_message.Message):
    __slots__ = ("workspace_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ExportDatasetResponse(_message.Message):
    __slots__ = ("dataset",)
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: Dataset
    def __init__(self, dataset: _Optional[_Union[Dataset, _Mapping]] = ...) -> None: ...

class TrainingRun(_message.Message):
    __slots__ = ("id", "workspace_id", "dataset_id", "base_model_id", "status", "launcher", "external_id", "model_id", "error", "started_by", "created_at", "finished_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STARTED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FINISHED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    workspace_id: str
    dataset_id: str
    base_model_id: str
    status: TrainingRunStatus
    launcher: str
    external_id: str
    model_id: str
    error: str
    started_by: str
    created_at: _timestamp_pb2.Timestamp
    finished_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., workspace_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., base_model_id: _Optional[str] = ..., status: _Optional[_Union[TrainingRunStatus, str]] = ..., launcher: _Optional[str] = ..., external_id: _Optional[str] = ..., model_id: _Optional[str] = ..., error: _Optional[str] = ..., started_by: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., finished_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StartTrainingRunRequest(_message.Message):
    __slots__ = ("workspace_id", "dataset_id", "base_model_id", "user_id")
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    dataset_id: str
    base_model_id: str
    user_id: str
    def __init__(self, workspace_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., base_model_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class StartTrainingRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: TrainingRun
    def __init__(self, run: _Optional[_Union[TrainingRun, _Mapping]] = ...) -> None: ...

class ListTrainingRunsRequest(_message.Message):
    __slots__ = ("workspace_id",)
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class ListTrainingRunsResponse(_message.Message):
    __slots__ = ("runs",)
    RUNS_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[TrainingRun]
    def __init__(self, runs: _Optional[_Iterable[_Union[TrainingRun, _Mapping]]] = ...) -> None: ...

class ReportTrainingRunRequest(_message.Message):
    __slots__ = ("run_id", "status", "external_id", "registry_id", "artifact_uri", "error")
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_URI_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    status: TrainingRunStatus
    external_id: str
    registry_id: str
    artifact_uri: str
    error: str
    def __init__(self, run_id: _Optional[str] = ..., status: _Optional[_Union[TrainingRunStatus, str]] = ..., external_id: _Optional[str] = ..., registry_id: _Optional[str] = ..., artifact_uri: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...

class ReportTrainingRunResponse(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: TrainingRun
    def __init__(self, run: _Optional[_Union[TrainingRun, _Mapping]] = ...) -> None: ...
