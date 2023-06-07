# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os 
import shlex

from .params import OVERVIEW, SOUND_ERROR_MESSAGE, SOUND_FILE_DOES_NOT_EXIST, INVALID_INPUT_FOR_SOUND_FILE_PATH
from .errors import NavaBaseError


def nava_help():
    """
    Print nava details.

    :return: None
    """
    print(OVERVIEW)
    print("Repo : https://github.com/openscilab/nava")
    print("Webpage : https://openscilab.com/")


def __play_win(sound_path):
    """
    Play sound in Windows.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    import winsound
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)


def __play_linux(sound_path):
    """
    Play sound in Linux.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    _ = subprocess.check_call(["aplay",
                               sound_path],
                              shell=False,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE)


def __play_mac(sound_path):
    """
    Play sound in macOS.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    _ = subprocess.check_call(["afplay",
                               sound_path],
                              shell=False,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE)


def play(sound_path):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    if not(isinstance(sound_path, str)):
        raise NavaBaseError(INVALID_INPUT_FOR_SOUND_FILE_PATH)
    
    # check sound file existance 
    if not(os.path.isfile(sound_path)):
        raise NavaBaseError(SOUND_FILE_DOES_NOT_EXIST)

    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            __play_win(sound_path)
        else:
            # quote the file path argument that you're passing to the command line in a decorator pattern manner 
            quoted_sound_path = QuoterDecorator(sound_path).quote()
            if(sys_platform == "darwin"):
                __play_mac(quoted_sound_path)
            else:
                __play_linux(quoted_sound_path)
    except Exception:
        raise NavaBaseError(SOUND_ERROR_MESSAGE)


class QuoterDecorator:
    """decorate the input to get quoted."""

    def __init__(self, shell_string):
        """
        Initialize the QuoterDecorator instance.

        :param shell_string: given shell_string
        :type shell_string: str
        :return: an instance of the QuoterDecorator class
        """
        self._shell_string = shell_string

    def quote(self):
        """
        Quote the given shell_string.

        :return: str
        """
        return shlex.quote(self._shell_string)