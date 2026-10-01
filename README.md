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
npm run generate     # writes gen/ts, gen/python, gen/go (not committed)
```

## gRPC services (version 1)

| Service | Owner | Calls |
| --- | --- | --- |
| `likho.media.v1.MediaService` | likho-media | `GetMedia`, `CreateUpload`, `GetDownloadUrl`, `DeleteMedia` |
| `likho.transcription.v1.TranscriptionService` | likho-transcription | `GetTranscript`, `ListTranscripts`, `Transcribe` (streams lines), `Retransliterate`, `ListEngines`, `CancelJob` |
| `likho.language.v1.LanguageService` | likho-language | `Transliterate`, `TransliterateBatch`, `GetHotwords`, `ResolveDecodePolicy`, glossary and spelling calls |

Shared messages are in `likho.common.v1`: `Segment` (one transcript line with both text
layers), `LanguageDetection`, `DialerCall`, `Script`.

## Events (version 1)

| Event type | NATS subject | Stream | Published by | Listened to by |
| --- | --- | --- | --- | --- |
| `likho.media.uploaded.v1` | `likho.media.uploaded` | LIKHO | likho-media | — |
| `likho.media.ready.v1` | `likho.media.ready` | LIKHO | likho-media | likho-api |
| `likho.transcription.requested.v1` | `likho.transcription.requested` | LIKHO | likho-api | likho-transcription (the job queue) |
| `likho.transcription.segment.v1` | `likho.live.segment` | LIKHO_LIVE | likho-transcription | likho-api |
| `likho.transcription.completed.v1` | `likho.transcription.completed` | LIKHO | likho-transcription | likho-api, likho-search |
| `likho.transcription.failed.v1` | `likho.transcription.failed` | LIKHO | likho-transcription | likho-api |
| `likho.vocabulary.updated.v1` | `likho.vocabulary.updated` | LIKHO | likho-language | likho-transcription |
| `likho.transcript.corrected.v1` | `likho.transcript.corrected` | LIKHO_KEEP | likho-api | likho-search |

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
