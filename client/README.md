# helics server web interface

## Developing

First you'll need to install dependencies.

In the root of the repository, run the following:

```bash
pip install -e ".[cli]"
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
