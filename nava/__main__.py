# -*- coding: utf-8 -*-
"""nava main."""

import sys
from art import tprint

from .params import NAVA_VERSION
from .functions import nava_help

if __name__ == "__main__":
    args = sys.argv
    tprint("nava")
    tprint("V:" + NAVA_VERSION)
    nava_help()
