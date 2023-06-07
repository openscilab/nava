# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os 
import shlex

from .params import OVERVIEW, SOUND_FILE_PLAY_ERROR , SOUND_FILE_EXIST_ERROR , SOUND_FILE_PATH_TYPE_ERROR
from .errors import NavaBaseError


def nava_help():
    """
    Print nava details.

    :return: None
    """
    print(OVERVIEW)
    print("Repo : https://github.com/openscilab/nava")
    print("Webpage : https://openscilab.com/")


def quote(func):
    """
    Quote the given shell_string.

    :return: str
    """
    def wrapper(*args, **kwargs):
        sound_path = args[0]
        sound_path = shlex.quote(sound_path)
        args = [sound_path]
        return func(*args, **kwargs)
    return wrapper


def __play_win(sound_path):
    """
    Play sound in Windows.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    import winsound
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

@quote
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

@quote
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


def path_check(func):
    """
    Check the given path to be both String and Valid file directory.

    :return: str
    """
    def wrapper(*args, **kwargs):
        sound_path = args[0]
        if not(isinstance(sound_path, str)):
            raise NavaBaseError(SOUND_FILE_PATH_TYPE_ERROR)
        # check sound file existance 
        if not(os.path.isfile(sound_path)):
            raise NavaBaseError(SOUND_FILE_EXIST_ERROR )
        return func(*args, **kwargs)
    return wrapper


@path_check
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
            __play_win(sound_path)
        elif(sys_platform == "darwin"):
            __play_mac(sound_path)
        else:
            __play_linux(sound_path)
    except Exception:
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR )

