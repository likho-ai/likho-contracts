# likho-contracts for TypeScript

Generated from the protos in this repository (`npm run generate`). Do not edit `gen/`.

With pnpm, straight from the repository at a tag:

```json
{
  "dependencies": {
    "@likho-ai/contracts": "github:likho-ai/likho-contracts#v0.5.0&path:/packages/ts",
    "@bufbuild/protobuf": "^2.2.0",
    "@connectrpc/connect": "^2.0.0"
  }
}
```

```ts
import { createClient } from "@connectrpc/connect";
import { createGrpcTransport } from "@connectrpc/connect-node";
import { MediaService } from "@likho-ai/contracts/media/v1/media_pb";

const media = createClient(MediaService, createGrpcTransport({ baseUrl: "http://localhost:5010" }));
const { media: file } = await media.getMedia({ id: "med_..." });
```

The files are JavaScript with type declarations ([Protobuf-ES](https://github.com/bufbuild/protobuf-es)
v2), so nothing has to be built. The same descriptors work with Connect, gRPC and gRPC-web.
