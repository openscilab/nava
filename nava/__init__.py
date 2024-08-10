# -*- coding: utf-8 -*-
"""Nava modules."""
from .params import NAVA_VERSION, Engine
from .errors import NavaBaseError
from .functions import play, stop, stop_all
import atexit

atexit.register(stop_all)

__version__ = NAVA_VERSION
