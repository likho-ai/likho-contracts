# likho-contracts for TypeScript

Generated from the protos in this repository (`npm run generate`). Do not edit `gen/`.

From the tarball attached to the release of the same version:

```json
{
  "dependencies": {
    "@likho-ai/contracts": "https://github.com/likho-ai/likho-contracts/releases/download/v0.5.0/likho-ai-contracts-0.5.0.tgz",
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
