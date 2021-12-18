# -*- coding: utf-8 -*-
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

import zipfile
import os
import io

current_directory = os.path.dirname(os.path.abspath(__file__))

url = "https://learning-python.com/ziptools/ziptools.zip"
r = urlopen(url)
if r.getcode() == 200:
    content = io.BytesIO(r.read())
    content.seek(0)
    with zipfile.ZipFile(content) as f:
        f.extractall(os.path.join(current_directory, ".."))
