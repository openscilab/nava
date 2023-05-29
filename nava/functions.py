# -*- coding: utf-8 -*-
"""Functions module."""
import sys
import subprocess

from .params import OVERVIEW, SOUND_ERROR_MESSAGE
from .errors import NavaBaseError


def nava_help():
    """
    Print nava details.

    :return: None
    """
    print(OVERVIEW)
    print("Repo : https://github.com/openscilab/nava")
    print("Webpage : https://openscilab.com/")


def play(sound_path):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            import winsound
            winsound.PlaySound(sound_path, winsound.SND_FILENAME)
        elif sys_platform == "darwin":
            _ = subprocess.check_call(["afplay",
                                       sound_path],
                                      shell=False,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
        else:
            _ = subprocess.check_call(["aplay",
                                       sound_path],
                                      shell=False,
                                      stderr=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE)
    except Exception:
        raise NavaBaseError(SOUND_ERROR_MESSAGE)
