# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os
import shlex
from functools import wraps
from .thread import NavaThread
from .params import OVERVIEW
from .params import SOUND_FILE_PLAY_ERROR, SOUND_FILE_EXIST_ERROR
from .params import SOUND_FILE_PATH_TYPE_ERROR, SOUND_ID_EXIST_ERROR, LOOP_ASYNC_ERROR
from .errors import NavaBaseError
from . import params


def stop(sound_id):
    """
    Stop sound.

    :param sound_id: sound id
    :type sound_id: int
    :return: None
    """
    if sound_id not in params._play_threads_map:
        raise NavaBaseError(SOUND_ID_EXIST_ERROR)
    params._play_threads_map[sound_id].stop()


def stop_all():
    """
    Stop all sounds.

    :return: None
    """
    for thread in params._play_threads_map.values():
        thread.stop()


def sound_id_gen():
    """
    Sound id generator.

    :return: sound id as int
    """
    params._play_threads_counter += 1
    sound_id = params._play_threads_counter + 1000
    return sound_id


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


def __play_win(sound_path, async_mode=False, loop=False):
    """
    Play sound in Windows.

    :param sound_path: sound path
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :return: None or sound id
    """
    import winsound
    play_flags = \
        winsound.SND_FILENAME | \
        (async_mode & winsound.SND_ASYNC)
    if loop:
        play_flags = play_flags | winsound.SND_LOOP

    if async_mode:
        sound_thread = NavaThread(loop,
                                  target=__play_win_flags,
                                  args=(sound_path, play_flags),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        __play_win_flags(sound_path, play_flags)


def __play_win_flags(sound_path, flags):
    """
    Play sound in Windows using different flags.

    :param sound_path: sound path
    :type sound_path: str
    :param flags: different mode flags
    :type flags: winsound flags
    :return: None
    """
    import winsound
    winsound.PlaySound(sound_path, flags)


@quote
def __play_linux(sound_path, async_mode=False, loop=False):
    """
    Play sound in Linux.

    :param sound_path: sound path to be played
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :return: None or sound id
    """
    if async_mode:
        sound_thread = NavaThread(loop,
                                  target=__play_proc_linux,
                                  args=(sound_path,),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        while True:
            proc = __play_proc_linux(sound_path)
            proc.wait()
            if not loop:
                break


def __play_proc_linux(sound_path):
    """
    Create sound playing process in Linux.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: process
    """
    proc = subprocess.Popen(["aplay",
                             sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return proc


@quote
def __play_mac(sound_path, async_mode=False, loop=False):
    """
    Play sound in macOS.

    :param sound_path: sound path
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :return: None or sound id
    """
    if async_mode:
        sound_thread = NavaThread(loop,
                                  target=__play_proc_mac,
                                  args=(sound_path,),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        while True:
            proc = __play_proc_mac(sound_path)
            proc.wait()
            if not loop:
                break


def __play_proc_mac(sound_path):
    """
    Create sound playing process in macOS.

    :param sound_path: sound path to be played
    :type sound_path: str
    :return: process
    """
    proc = subprocess.Popen(["afplay",
                             sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return proc


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
def play(sound_path, async_mode=False, loop=False):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :return: None or sound id
    """
    if loop and not async_mode:
        raise NavaBaseError(LOOP_ASYNC_ERROR)
    try:
        sys_platform = sys.platform
        if sys_platform == "win32":
            return __play_win(sound_path, async_mode, loop)
        elif sys_platform == "darwin":
            return __play_mac(sound_path, async_mode, loop)
        else:
            return __play_linux(sound_path, async_mode, loop)
    except Exception:  # pragma: no cover
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR)
