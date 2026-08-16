# Web server API

The experimental HELICS web server is a FastAPI application that manages
brokers in the current Python process.  It is the replacement path for the
former Flask application and does not start `helics_broker_server --http`.

Install the optional server dependencies and start the application:

```bash
pip install "helics[server]"
helics server
```

By default the server binds to `127.0.0.1:8000` and opens its interactive
OpenAPI documentation at `http://127.0.0.1:8000/docs`.  Use `--host`, `--port`,
and `--no-open` to configure the listener.

## Broker API

All endpoints are under `/api/v1`.  The initial API exposes broker lifecycle
and control operations:

| Operation | Endpoint |
| --- | --- |
| Service health | `GET /api/v1/health` |
| List local brokers | `GET /api/v1/brokers` |
| Create a broker | `POST /api/v1/brokers` |
| Inspect/delete a broker | `GET`/`DELETE /api/v1/brokers/{name}` |
| Inspect current broker state | `GET /api/v1/brokers/{name}/state` |
| Inspect connection status | `GET /api/v1/brokers/{name}/connection` |
| Execute a HELICS query | `POST /api/v1/brokers/{name}/query` |
| Send a command | `POST /api/v1/brokers/{name}/commands` |
| Set/clear a time barrier | `PUT`/`DELETE /api/v1/brokers/{name}/time-barrier` |

For example, create a local ZMQ broker that expects two federates:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/brokers \
  -H "Content-Type: application/json" \
  -d '{"name":"example", "core_type":"zmq", "num_federates":2}'
```

The server owns only brokers it creates.  It does not discover or control
brokers started by another process.

## Typed HELICS queries

Standard HELICS queries progressively receive Pydantic response models in
`helics.query_models`.  The first is `isconnected`, available as both the
generic query request and the convenient `GET /brokers/{name}/connection`
endpoint.  Its response is always:

```json
{"target": "root", "query": "isconnected", "value": true}
```

Queries without a registered model remain available through `POST .../query`
with the common `{target, query, value}` envelope.  This lets the API expose
custom and newer HELICS queries immediately while their stable Pydantic models
are added independently.
