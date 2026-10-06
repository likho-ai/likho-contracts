# likho-contracts

The single place where Likho's interfaces are defined. Services never describe an interface
themselves; they generate code from here.

| What | Where | Checked by |
| --- | --- | --- |
| gRPC services between services | `proto/likho/<area>/v1/*.proto` | `buf lint`, `buf build`, `buf breaking` |
| Events on the bus | `events/<type>.schema.json` (JSON Schema for the event's `data`) with one example each in `events/examples/` | `npm run validate` |
| The event envelope (CloudEvents 1.0) | `events/cloudevent.schema.json` | `npm run validate` |
| NATS streams, subjects, producers and consumers | `streams.yaml` | `npm run validate` |

## Use

```bash
npm install
npm run check        # lint + build the protos, validate the events
npm run generate     # writes packages/python/src, packages/go/gen and packages/ts/gen (all committed)
```

## Use from a Python service

```toml
dependencies = ["likho-contracts"]

[tool.uv.sources]
likho-contracts = { git = "https://github.com/likho-ai/likho-contracts", tag = "v0.11.0", subdirectory = "packages/python" }
```

```python
from likho.language.v1 import language_pb2, language_pb2_grpc
```

## Use from a Go service

```bash
go get github.com/likho-ai/likho-contracts/packages/go@v0.11.0
```

```go
import (
	mediav1 "github.com/likho-ai/likho-contracts/packages/go/gen/likho/media/v1"
	"github.com/likho-ai/likho-contracts/packages/go/gen/likho/media/v1/mediav1connect"
)
```

The Go code is for [Connect](https://connectrpc.com): a Connect server also answers plain gRPC,
so the Python services call it with their normal gRPC clients.

## Use from a TypeScript service or web app

Every version tag has a GitHub release with the package attached; npm and pnpm install a
tarball by URL, no registry account needed:

```json
"@likho-ai/contracts": "https://github.com/likho-ai/likho-contracts/releases/download/v0.11.0/likho-ai-contracts-0.11.0.tgz"
```

```ts
import { MediaService } from "@likho-ai/contracts/media/v1/media_pb";
```

The generated Python, Go and TypeScript code is committed, and CI fails if it does not match
the protos. A release has two tags: `vX.Y.Z` (Python, and the TypeScript tarball attached to the GitHub
release by CI) and `packages/go/vX.Y.Z` (the Go module).

## gRPC services (version 1)

| Service | Owner | Calls |
| --- | --- | --- |
| `likho.media.v1.MediaService` | likho-media | `GetMedia`, `CreateUpload`, `GetDownloadUrl`, `DeleteMedia` |
| `likho.transcription.v1.TranscriptionService` | likho-transcription | `GetTranscript`, `ListTranscripts`, `Transcribe` (streams lines), `Retransliterate`, `CorrectSegment` (a new version, the correction kept), `ListCorrections`, `ListEngines`, `CancelJob` |
| `likho.language.v1.LanguageService` | likho-language | `Transliterate`, `TransliterateBatch`, `GetHotwords`, `ResolveDecodePolicy`, glossary and spelling calls |
| `likho.search.v1.SearchService` | likho-search | `Search` (lines matching a query, with the matches marked), `Reindex`, `DeleteRecording` |
| `likho.insights.v1.InsightsService` | likho-insights | `GetInsights`, `Analyse`, `GetStatus` (what a model says about a call: summary, products, sentiment, the auditor's checks) |
| `likho.analytics.v1.AnalyticsService` | likho-analytics | `GetOverview`, `GetTimeseries`, `GetBreakdown` (the numbers behind the calls in a window: calls, minutes, speed, languages, by agent and campaign, what the model made of them) |
| `likho.dialer.v1.DialerService` | likho-connector-ameyo | `ListCampaigns`, `ListAgents`, `ListCalls`, `GetCall` (what the dialer knows about its calls, from its reporting database), `GetStatus` (the connector's schedule and budget) |

Shared messages are in `likho.common.v1`: `Segment` (one transcript line with both text
layers), `LanguageDetection`, `DialerCall`, `Script`.

## Events (version 1)

| Event type | NATS subject | Stream | Published by | Listened to by |
| --- | --- | --- | --- | --- |
| `likho.media.uploaded.v1` | `likho.media.uploaded` | LIKHO | likho-media | likho-analytics |
| `likho.media.ready.v1` | `likho.media.ready` | LIKHO | likho-media | likho-api, likho-analytics |
| `likho.media.failed.v1` | `likho.media.failed` | LIKHO | likho-media | likho-api, likho-analytics |
| `likho.transcription.requested.v1` | `likho.transcription.requested` | LIKHO | likho-api | likho-transcription (the job queue), likho-analytics |
| `likho.transcription.segment.v1` | `likho.live.segment` | LIKHO_LIVE | likho-transcription | likho-api, likho-analytics |
| `likho.transcription.completed.v1` | `likho.transcription.completed` | LIKHO | likho-transcription | likho-api, likho-search, likho-analytics |
| `likho.transcription.failed.v1` | `likho.transcription.failed` | LIKHO | likho-transcription | likho-api, likho-analytics |
| `likho.vocabulary.updated.v1` | `likho.vocabulary.updated` | LIKHO | likho-language | likho-transcription, likho-analytics |
| `likho.transcript.corrected.v1` | `likho.transcript.corrected` | LIKHO_KEEP | likho-api | likho-search, likho-analytics |
| `likho.import.requested.v1` | `likho.import.requested` | LIKHO | likho-api | likho-connector-ameyo (fetch this call from the dialer), likho-analytics |
| `likho.import.completed.v1` | `likho.import.completed` | LIKHO | likho-connector-ameyo | likho-api, likho-analytics |
| `likho.import.failed.v1` | `likho.import.failed` | LIKHO | likho-connector-ameyo | likho-api, likho-analytics |
| `likho.recording.deleted.v1` | `likho.recording.deleted` | LIKHO | likho-api | likho-search, likho-connector-ameyo, likho-analytics |
| `likho.recording.updated.v1` | `likho.recording.updated` | LIKHO | likho-api | likho-search, likho-analytics |
| `likho.insights.completed.v1` | `likho.insights.completed` | LIKHO | likho-insights | likho-api, likho-analytics |
| `likho.insights.failed.v1` | `likho.insights.failed` | LIKHO | likho-insights | likho-api, likho-analytics |
| `likho.settings.changed.v1` | `likho.settings.changed` | LIKHO | likho-api | likho-connector-ameyo, likho-insights, likho-analytics (the keys only; the values are read from likho-api) |

## Rules

* A released field is never removed or renumbered. A breaking change is a new package version
  (`v2`) or a new event type (`….v2`); `buf breaking` enforces this for the protos.
* Events only gain optional fields.
* Ids are prefixed ULIDs: `rec_`, `med_`, `job_`, `trn_`, `wsp_`, `usr_`.
* Dialer times are carried as India time text exactly as the dialer stores them; they are never
  converted through UTC.
* Publishers send the CloudEvent `id` as the `Nats-Msg-Id` header; consumers acknowledge
  explicitly and must be safe to run twice for the same id.

## Adding an event

1. Add `events/<type>.schema.json` and `events/examples/<type>.json`.
2. Add the type to `streams.yaml` with its subject, stream, producer and consumers.
3. `npm run validate`. It fails if the example does not match, if the subject is captured by
   no stream or by two, or if a schema is not listed.
