# helics server web interface

## Developing

Use Node.js 24 for the web build, matching CI.

In the root of the repository, run the following:

```bash
pip install -e ".[cli,server]"
```

In the repository's `client` folder, run the following:

```bash
npm ci
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

The client uses same-origin `/api/v1` endpoints. Vite proxies API requests
to the local FastAPI service during development.

`npm run build` writes the production UI to `client/build`. The packaged copy
is `helics/webserver/static`; copy the build contents there when updating the
UI, and include the changed static assets in the pyhelics release. The UI is
not a separate Python package.

`npm test` starts the installed `helics server` and exercises its bundled
assets in Chromium. Install the browser first with `npx playwright install chromium`.
