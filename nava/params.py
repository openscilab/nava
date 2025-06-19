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


class PythonEnvironment(Enum):
    """Python environment class."""

    COLAB = "Google Colab"
    LOCAL_JUPYTER = "Local Jupyter Notebook or JupyterLab"
    VSCODE = "VS Code Notebook"
    IPYTHON_TERMINAL = "IPython Terminal"
    PLAIN_PYTHON = "Plain Python (.py script)"
    UNKNOWN = "Unknown Environment"


# Environment variables typically set by VS Code
VSCODE_ENV_VARS = [
    "VSCODE_PID", # this is often set when running in VS Code
    "VSCODE_CWD", # this is often set when running in VS Code
    "VSCODE_IPC_HOOK_CLI",
    "TERM_PROGRAM",  # often set to "vscode"
]

# Shell type identifiers
SHELL_TYPE_ZMQ = "zmqinteractiveshell"           # Jupyter Notebook/Lab
SHELL_TYPE_TERMINAL = "terminalinteractiveshell" # IPython Terminal

SOUND_FILE_PLAY_ERROR = "Sound can not play due to some issues."
SOUND_FILE_EXIST_ERROR = "Given sound file doesn't exist."
SOUND_FILE_PATH_TYPE_ERROR = "Sound file's path should be a string."
SOUND_ID_EXIST_ERROR = "Given sound id doesn't exist."
LOOP_ASYNC_ERROR = "`loop` can not be set True when `async_mode` is False."
ENGINE_TYPE_ERROR = "`engine` type must be `Engine` enum."

_play_threads_map = dict()
_play_threads_counter = 0
