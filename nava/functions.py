# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os
import shlex
from functools import wraps
import asyncio

from .params import OVERVIEW
from .params import SOUND_FILE_PLAY_ERROR, SOUND_FILE_EXIST_ERROR
from .params import SOUND_FILE_PATH_TYPE_ERROR
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
    Quote the given shell string.

    :return: inner function
    """
    @wraps(func)
    def quoter(sound_path, *args, **kwargs):
        """
        Inner function.

        :param sound_path: sound path
        :type sound_path: str
        :param args: non-keyword arguments
        :type args: list
        :param kwargs: keyword arguments
        :type kwargs: dict
        :return: modified function result
        """
        sound_path = shlex.quote(sound_path)
        return func(sound_path, *args, **kwargs)
    return quoter


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
def __play_linux(sound_path, loop=False, is_async=True):
    """
    Play sound in Linux.

    :param sound_path: sound path
    :type sound_path: str
    :return: None
    """
    if is_async:
        if loop:
            while True:
                asyncio.run(__play_async_linx(sound_path))
        else:
            asyncio.run(__play_async_linx(sound_path))
    else:
        if loop:
            while True:
                __play_sync_linux(sound_path)
        else:
            __play_sync_linux(sound_path)

def __play_sync_linux(sound_path):
    """
    Play sound synch in Linux
    """
    _ = subprocess.check_call(["aplay",
                            sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)

async def __play_async_linx(sound_path):
    """
    Play sound async in Linux
    """
    play_cmd = f"aplay {sound_path}"
    proc = await asyncio.subprocess.create_subprocess_shell(
        play_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()


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
    Check the given path to be a string and a valid file directory.

    :return: inner function
    """
    @wraps(func)
    def path_checker(sound_path, *args, **kwargs):
        """
        Inner function.

        :param sound_path: sound path
        :type sound_path: str
        :param args: non-keyword arguments
        :type args: list
        :param kwargs: keyword arguments
        :type kwargs: dict
        :return: modified function result
        """
        if not isinstance(sound_path, str):
            raise NavaBaseError(SOUND_FILE_PATH_TYPE_ERROR)
        # check sound file existance
        if not os.path.isfile(sound_path):
            raise NavaBaseError(SOUND_FILE_EXIST_ERROR)
        return func(sound_path, *args, **kwargs)
    return path_checker


@path_check
def play(sound_path, loop=False, is_async=True):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :param loop: play sound on loop (False by default)
    :type loop: bool
    :param is_async: play synchronously or asynchronously (True by default)
    :type is_async: bool
    :return: None
    """
    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            __play_win(sound_path)
        elif sys_platform == "darwin":
            __play_mac(sound_path)
        else:
            __play_linux(sound_path, loop, is_async)
    except Exception:
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR)
