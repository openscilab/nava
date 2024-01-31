# -*- coding: utf-8 -*-
"""Nava parameters."""

NAVA_VERSION = "0.3"

OVERVIEW = """
A Python library for playing sound everywhere natively and securely.

"""

SOUND_FILE_PLAY_ERROR = "Sound can not play due to some issues."
SOUND_FILE_EXIST_ERROR = "Given sound file doesn't exist."
SOUND_FILE_PATH_TYPE_ERROR = "Sound file's path should be a string."
SOUND_ID_EXIST_ERROR = "Given sound id doesn't exist."

_play_threads_map = dict()
_play_threads_counter = 0
