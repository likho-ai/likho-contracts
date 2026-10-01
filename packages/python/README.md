# likho-contracts (Python)

Generated code. Do not edit `src/`; change the `.proto` files and run `npm run generate`.

Install in a service:

```toml
dependencies = ["likho-contracts"]

[tool.uv.sources]
likho-contracts = { git = "https://github.com/likho-ai/likho-contracts", tag = "v0.1.0", subdirectory = "packages/python" }
```

```python
from likho.language.v1 import language_pb2, language_pb2_grpc
```
