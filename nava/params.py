# -*- coding: utf-8 -*-
"""Nava parameters."""
from enum import Enum

NAVA_VERSION = "0.7"

OVERVIEW = """
A Python library for playing sound everywhere natively and securely.

"""


class Engine(Enum):
    """
    Nava engine class.

    >>> import nava
    >>> engine = nava.Engine.ALSA
    """

    AUTO = "auto"
    WINSOUND = "winsound"
    ALSA = "alsa"
    AFPLAY = "afplay"


SOUND_FILE_PLAY_ERROR = "Sound can not play due to some issues."
SOUND_FILE_EXIST_ERROR = "Given sound file doesn't exist."
SOUND_FILE_PATH_TYPE_ERROR = "Sound file's path should be a string."
SOUND_ID_EXIST_ERROR = "Given sound id doesn't exist."
LOOP_ASYNC_ERROR = "`loop` can not be set True when `async_mode` is False."
ENGINE_TYPE_ERROR = "`engine` type must be `Engine` enum."

_play_threads_map = dict()
_play_threads_counter = 0
