# helics server web interface

## Developing

First you'll need to install dependencies.

In the root of the repository, run the following:

```bash
pip install -e ".[cli,server]"
```

In the `./client` folder, run the following:

```bash
npm install
```

Open two terminals:

In one terminal run:

```bash
helics server --no-open
```

In another run:

```bash
npm run dev
```

The client uses same-origin `/api/v1` endpoints.  During development the
FastAPI server permits the default Vite origins (`localhost:5173` and
`127.0.0.1:5173`); set `HELICS_WEB_CORS_ORIGINS` to override them.
