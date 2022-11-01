---
name: Bug report
about: Create a bug report
title: ""
labels: bug
assignees: ""
---

<!--

Thank you for taking the time to fill out a bug report.

-->

**Describe the bug**

<!-- A clear and concise description of what the bug is with screenshots if available. -->

**To Reproduce**

- [ ] Reproducible using test suite located here: <https://github.com/GMLC-TDC/pyhelics/blob/main/tests/test_python_api.py>

Steps to reproduce the behavior:

<!--
Please provide a minimal working example of the bug with screenshots if possible.

-->

**Environment (please complete the following information):**

- Operating System: <!-- Windows | Mac | Linux -->
- Installation: <!-- github releases | homebrew | arch | zinit -->
- helics and pyhelics version:

```
helics --version
```

Share the output of the following:

```
$ python -c "import helics as h; import json; print(json.dumps(h.helicsGetSystemInfo(), indent=4, sort_keys=True))"
```

**Additional context and information**

<!--

Please provide detailed stacktraces, screenshots, log files, example files etc here.
-->
