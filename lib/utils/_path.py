#coding: utf-8
import os
from pathlib import Path
from .coloring_utils  import toBLUE

__all__ = [
    "UTILS_DIR", "MODULE_DIR", "TEMPLATES_DIR", "REPO_DIR", "<LIB>_DIR",
]

UTILS_DIR     = os.path.dirname(os.path.abspath(__file__))      # path/to/<lib>/utils
MODULE_DIR    = os.path.dirname(UTILS_DIR)                      # path/to/<lib>
REPO_DIR      = os.path.dirname(MODULE_DIR)                     # path/to/python-package-template
