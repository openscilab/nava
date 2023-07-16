# -*- coding: utf-8 -*-
"""Nava modules."""
from .params import NAVA_VERSION
from .errors import NavaBaseError
from .functions import play

import atexit
# Async play processes clean up 
atexit.register(functions.__cleanup_processes)

__version__ = NAVA_VERSION
