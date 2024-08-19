# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import subprocess
import os
import shlex
from functools import wraps
from .thread import NavaThread
from .params import OVERVIEW, Engine
from .params import SOUND_FILE_PLAY_ERROR, SOUND_FILE_EXIST_ERROR, ENGINE_TYPE_ERROR
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
    print("Webpage : https://openscilab.com/\n")


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


def __play_winsound(sound_path, async_mode=False, loop=False):
    """
    Play sound using the winsound library.

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
                                  engine=Engine.WINSOUND,
                                  target=__play_winsound_flags,
                                  args=(sound_path, play_flags),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        __play_winsound_flags(sound_path, play_flags)


def __play_winsound_flags(sound_path, flags):
    """
    Play sound in winsound using different flags.

    :param sound_path: sound path
    :type sound_path: str
    :param flags: different mode flags
    :type flags: winsound flags
    :return: None
    """
    import winsound
    winsound.PlaySound(sound_path, flags)


@quote
def __play_alsa(sound_path, async_mode=False, loop=False):
    """
    Play sound using ALSA.

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
                                  engine=Engine.ALSA,
                                  target=__play_proc_alsa,
                                  args=(sound_path,),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        while True:
            proc = __play_proc_alsa(sound_path)
            proc.wait()
            if not loop:
                break


def __play_proc_alsa(sound_path):
    """
    Create sound playing process using ALSA.

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
def __play_afplay(sound_path, async_mode=False, loop=False):
    """
    Play sound using afplay.

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
                                  engine=Engine.AFPLAY,
                                  target=__play_proc_afplay,
                                  args=(sound_path,),
                                  daemon=True)
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        while True:
            proc = __play_proc_afplay(sound_path)
            proc.wait()
            if not loop:
                break


def __play_proc_afplay(sound_path):
    """
    Create sound playing process using afplay.

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


def __play_auto(sound_path, async_mode=False, loop=False):
    """
    Play sound in automatic mode.

    :param sound_path: sound path
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :return: None or sound id
    """
    sys_platform = sys.platform
    if sys_platform == "win32":
        return __play_winsound(sound_path, async_mode, loop)
    elif sys_platform == "darwin":
        return __play_afplay(sound_path, async_mode, loop)
    else:
        return __play_alsa(sound_path, async_mode, loop)


@path_check
def play(sound_path, async_mode=False, loop=False, engine=Engine.AUTO):
    """
    Play sound.

    :param sound_path: sound path
    :type sound_path: str
    :param async_mode: async mode flag
    :type async_mode: bool
    :param loop: sound loop flag
    :type loop: bool
    :param engine: play engine
    :type engine: Engine enum
    :return: None or sound id
    """
    if not isinstance(engine, Engine):
        raise NavaBaseError(ENGINE_TYPE_ERROR)
    if loop and not async_mode:
        raise NavaBaseError(LOOP_ASYNC_ERROR)
    try:
        if engine == Engine.AUTO:
            return __play_auto(sound_path=sound_path, async_mode=async_mode, loop=loop)
        elif engine == Engine.WINSOUND:
            return __play_winsound(sound_path=sound_path, async_mode=async_mode, loop=loop)
        elif engine == Engine.AFPLAY:
            return __play_afplay(sound_path=sound_path, async_mode=async_mode, loop=loop)
        elif engine == Engine.ALSA:
            return __play_alsa(sound_path=sound_path, async_mode=async_mode, loop=loop)
    except Exception:
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR)


def play_cli(sound_path, loop=False):
    """
    Play sound from CLI.

    :param sound_path: sound path
    :type sound_path: str
    :param loop: sound loop flag
    :type loop: bool
    :return: None
    """
    try:
        while True:
            play(sound_path)
            if not loop:
                break
    except NavaBaseError as e:
        print("Error: {0}".format(e))
    finally:
        stop_all()
