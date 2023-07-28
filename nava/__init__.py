# -*- coding: utf-8 -*-
"""Nava modules."""
from .params import NAVA_VERSION
from .errors import NavaBaseError
from .functions import play, cleanup_processes

import atexit
# Async play processes clean up 
atexit.register(cleanup_processes)

__version__ = NAVA_VERSION
