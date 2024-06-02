import sys

sys.path.append("src")

import importlib

pkg = importlib.import_module("example-package-scott-baldwin")

pkg.main.hello()
