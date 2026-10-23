# helics server web interface

## Developing

First you'll need to install dependencies.

In the root of the repository, run the following:

```bash
pip install -e ".[cli,server]"
```

In the repository's `client` folder, run the following:

```bash
npm ci --legacy-peer-deps
```

Keep `package-lock.json` in Git: the UI CI job uses `npm ci` to install its
locked dependency tree. Generated `node_modules/`, `.svelte-kit/`, and `build/`
directories are ignored.

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

`npm run build` writes the production UI to `client/build`. The packaged copy
is `helics/webserver/static`; copy the build contents there when updating the
UI, and include the changed static assets in the pyhelics release. The UI is
not a separate Python package.
