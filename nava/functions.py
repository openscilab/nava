# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os
import shlex
from functools import wraps
import threading

from .params import OVERVIEW
from .params import SOUND_FILE_PLAY_ERROR, SOUND_FILE_EXIST_ERROR
from .params import SOUND_FILE_PATH_TYPE_ERROR
from .errors import NavaBaseError

"""
List of all aplay processes
"""
play_processes = []


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


def cleanup_processes():
    """
    Cleanup undead play processes after module exit.

    :return: None
    """
    for proc in play_processes:
        proc.kill()
        proc.terminate()


def __play_win(sound_path, is_async=True):
    """
    Play sound in Windows.

    :param sound_path: sound path
    :type sound_path: str
    :param is_async: play async or not
    :type is_async: bool
    :return: None
    """
    import winsound
    # If is_async is ture, play async
    play_flags = winsound.SND_FILENAME | (is_async & winsound.SND_ASYNC)
    winsound.PlaySound(sound_path, play_flags)


@quote
def __play_linux(sound_path, is_async=True):
    """
    Play sound in Linux.

    :param sound_path: sound path to be played
    :type sound_path: str
    :param is_async: play async or not
    :type is_async: bool
    :return: None or sound thread (depending on async flag)
    """
    if is_async:
        sound_thread = threading.Thread(target=__play_async_linux,
                                        args=(sound_path,),
                                        daemon=True)
        sound_thread.start()
        return sound_thread
    else:
        __play_sync_linux(sound_path)


def __play_sync_linux(sound_path):
    """
    Play sound synchronously in Linux.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: None
    """
    _ = subprocess.check_call(["aplay",
                            sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    

def __play_async_linux(sound_path):
    """
    Play sound asynchronously in Linux.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: None
    """
    proc = subprocess.Popen(["aplay",
                            sound_path],
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    play_processes.append(proc)


@quote
def __play_mac(sound_path, is_async=True):
    """
    Play sound in macOS.

    :param sound_path: sound path
    :type sound_path: str
    :param is_async: play sound in async mode
    :type is_async: bool
    :return: None or sound thread, depending on the flag
    """
    if is_async:
        sound_thread = threading.Thread(target=__play_async_mac,
                                        args=(sound_path,),
                                        daemon=True)
        sound_thread.start()
        return sound_thread
    else:
        __play_sync_mac(sound_path)


def __play_sync_mac(sound_path):
    """
    Play sound synchronously in macOS.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: None
    """
    _ = subprocess.check_call(["afplay",
                               sound_path],
                              shell=False,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE)


def __play_async_mac(sound_path):
    """
    Play sound asynchronously in macOS.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: None
    """
    proc = subprocess.Popen(["afplay",
                            sound_path],
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    play_processes.append(proc)


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
def play(sound_path, is_async=True):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :param is_async: play synchronously or asynchronously (async by default)
    :type is_async: bool
    :return: None or sound thread for futher handlings
    """
    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            __play_win(sound_path, is_async)
        elif sys_platform == "darwin":
            return __play_mac(sound_path, is_async)
        else:
            return __play_linux(sound_path, is_async)
    except Exception: # pragma: no cover
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR)
