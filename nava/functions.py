# -*- coding: utf-8 -*-
"""Nava functions."""
import sys
import threading
import subprocess
import os
import shlex
from hashlib import sha256
from functools import wraps
import importlib.util
from typing import Callable, List, Dict, Any, Optional
from .thread import NavaThread
from .params import OVERVIEW, Engine
from .params import SOUND_FILE_PLAY_ERROR, SOUND_FILE_EXIST_ERROR, ENGINE_TYPE_ERROR
from .params import SOUND_FILE_PATH_TYPE_ERROR, SOUND_ID_EXIST_ERROR, LOOP_ASYNC_ERROR
from .params import PythonEnvironment, SHELL_TYPE_ZMQ, SHELL_TYPE_TERMINAL, VSCODE_ENV_VARS
from .errors import NavaBaseError
from . import params


def stop(sound_id: int) -> None:
    """
    Stop sound.

    :param sound_id: sound id
    """
    if sound_id not in params._play_threads_map:
        raise NavaBaseError(SOUND_ID_EXIST_ERROR)
    params._play_threads_map[sound_id].stop()


def stop_all() -> None:
    """Stop all sounds."""
    for thread in params._play_threads_map.values():
        thread.stop()


def sound_id_gen() -> int:
    """Sound id generator."""
    params._play_threads_counter += 1
    sound_id = params._play_threads_counter + 1000
    return sound_id


def nava_help() -> None:
    """Print nava details."""
    print(OVERVIEW)
    print("Repo : https://github.com/openscilab/nava")
    print("Webpage : https://openscilab.com/\n")


def quote(func: Callable) -> Callable:
    """
    Quote the given shell string.
    
    :param func: function to wrap
    """
    @wraps(func)
    def quoter(sound_path: str, *args: List[Any], **kwargs: Dict[str, Any]) -> Callable:
        """
        Inner function.

        :param sound_path: sound path
        :param args: non-keyword arguments
        :param kwargs: keyword arguments
        """
        sound_path = shlex.quote(sound_path)
        return func(sound_path, *args, **kwargs)
    return quoter


def __play_winmm(sound_path: str, async_mode: bool = False, loop: bool = False) -> Optional[int]:
    """
    Play sound using the winmm MCI interface.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
    """
    if async_mode:
        sound_thread = NavaThread(
            loop,
            engine=Engine.WINMM,
            target=__play_winmm_flags,
            args=(sound_path, async_mode, loop),
            daemon=True
        )
        sound_thread.start()
        sound_id = sound_id_gen()
        params._play_threads_map[sound_id] = sound_thread
        return sound_id
    else:
        __play_winmm_flags(sound_path, async_mode, loop)


def __play_winmm_flags(sound_path: str, async_mode: bool = False, loop: bool = False) -> None:
    """
    Play a sound using winmm with optional looping.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
    """
    def play_sound(alias: str) -> None:
        """
        Open and play a sound using the specified alias.

        :param alias: MCI alias to assign to the sound
        """
        windll.winmm.mciSendStringW(f'open "{sound_path}" type mpegvideo alias {alias}', None, 0, None)
        do_block = " wait" if not async_mode else ""
        windll.winmm.mciSendStringW(f"play {alias}" + do_block, None, 0, None)

    def stop_sound(alias: str) -> None:
        """
        Stop and close the sound associated with the specified alias.

        :param alias: MCI alias of the sound to stop
        """
        windll.winmm.mciSendStringW(f"stop {alias}", None, 0, None)
        windll.winmm.mciSendStringW(f"close {alias}", None, 0, None)

    def get_sound_status(alias: str) -> str:
        """
        Get the current playback status of the specified alias.

        :param alias: MCI alias to query
        """
        status_buf = create_unicode_buffer(128)
        windll.winmm.mciSendStringW(f"status {alias} mode", status_buf, 128, None)
        return status_buf.value.lower()

    import time
    from ctypes import windll, create_unicode_buffer
    sound_hash = sha256(sound_path.encode()).hexdigest()[-7:]
    alias = f"nava_sound_{sound_hash}"
    play_sound(alias)
    try:
        while True:
            current_thread = threading.current_thread()
            # Immediate stop (forced from stop method of the associated thread)
            # The alias is scoped to the MCI context of the thread that created it.
            # So the main thread can’t “see” the alias created in the worker thread.
            if getattr(current_thread, "_force_stop", False):
                break
            status = get_sound_status (alias)
            if status != "playing":
                if getattr(current_thread, "_loop", loop):
                    stop_sound(alias)
                    play_sound(alias)
                else:
                    break
            time.sleep(0.1)
    finally:
        stop_sound(alias)


def __play_winsound(sound_path: str, async_mode: bool = False, loop: bool = False) -> Optional[int]:
    """
    Play sound using the winsound library.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
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


def __play_winsound_flags(sound_path: str, flags: int) -> None:
    """
    Play sound in winsound using different flags.

    :param sound_path: sound path
    :param flags: different mode flags
    """
    import winsound
    winsound.PlaySound(sound_path, flags)


def __play_google_colab(sound_path: str) -> None:
    """
    Play sound in Google Colab Notebook.

    :param sound_path: sound path
    """
    from IPython.display import Audio, display
    audio = Audio(sound_path, autoplay=True)
    display(audio)


@quote
def __play_alsa(sound_path: str, async_mode: bool = False, loop: bool = False) -> Optional[int]:
    """
    Play sound using ALSA.

    :param sound_path: sound path to be played
    :param async_mode: async mode flag
    :param loop: sound loop flag
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


def __play_proc_alsa(sound_path: str) -> subprocess.Popen:
    """
    Create sound playing process using ALSA.

    :param sound_path: sound path to be played
    """
    proc = subprocess.Popen(["aplay",
                             sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return proc


@quote
def __play_afplay(sound_path: str, async_mode: bool = False, loop: bool = False) -> Optional[int]:
    """
    Play sound using afplay.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
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


def __play_proc_afplay(sound_path: str) -> subprocess.Popen:
    """
    Create sound playing process using afplay.

    :param sound_path: sound path to be played
    """
    proc = subprocess.Popen(["afplay",
                             sound_path],
                            shell=False,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    return proc


def path_check(func: Callable) -> Callable:
    """
    Check the given path to be a string and a valid file directory.
    
    :param func: function to wrap
    """
    @wraps(func)
    def path_checker(sound_path: str, *args: List[Any], **kwargs: Dict[str, Any]) -> Callable:
        """
        Inner function.

        :param sound_path: sound path
        :param args: non-keyword arguments
        :param kwargs: keyword arguments
        """
        if not isinstance(sound_path, str):
            raise NavaBaseError(SOUND_FILE_PATH_TYPE_ERROR)
        # check sound file existance
        if not os.path.isfile(sound_path):
            raise NavaBaseError(SOUND_FILE_EXIST_ERROR)
        return func(sound_path, *args, **kwargs)
    return path_checker


def __play_auto(sound_path: str, async_mode: bool = False, loop: bool = False) -> Optional[int]:
    """
    Play sound in automatic mode.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
    """
    env = detect_environment()
    if env == PythonEnvironment.COLAB:
        return __play_google_colab(sound_path)
    # we will add other notebook environment handlers in the future

    sys_platform = sys.platform
    if sys_platform == "win32":
        return __play_winsound(sound_path, async_mode, loop)
    elif sys_platform == "darwin":
        return __play_afplay(sound_path, async_mode, loop)
    else:
        return __play_alsa(sound_path, async_mode, loop)


@path_check
def play(sound_path: str, async_mode: bool = False, loop: bool = False, engine: Engine = Engine.AUTO) -> Optional[int]:
    """
    Play sound.

    :param sound_path: sound path
    :param async_mode: async mode flag
    :param loop: sound loop flag
    :param engine: play engine
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
        elif engine == Engine.WINMM:
            return __play_winmm(sound_path=sound_path, async_mode=async_mode, loop=loop)
        elif engine == Engine.AFPLAY:
            return __play_afplay(sound_path=sound_path, async_mode=async_mode, loop=loop)
        elif engine == Engine.ALSA:
            return __play_alsa(sound_path=sound_path, async_mode=async_mode, loop=loop)
    except Exception:
        raise NavaBaseError(SOUND_FILE_PLAY_ERROR)


def play_cli(sound_path: str, loop: bool = False) -> None:
    """
    Play sound from CLI.

    :param sound_path: sound path
    :param loop: sound loop flag
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


def detect_environment():
    """
    Detect the current Python execution environment.

    Supported environments:
    - Google Colab
    - Local Jupyter Notebook/Lab
    - VS Code Notebook
    - IPython Terminal
    - Plain Python script
    
    :return: PythonEnvironment Enum value indicating the environment.
    """
    ip = None
    try:
        from IPython import get_ipython
        ip = get_ipython()
    except ImportError:
        return PythonEnvironment.PLAIN_PYTHON
    if ip is None:
        return PythonEnvironment.PLAIN_PYTHON

    shell_name = ip.__class__.__name__.lower()

    # Explicit Google Colab check (most reliable)
    if importlib.util.find_spec("google.colab") is not None:
        return PythonEnvironment.COLAB

    # VS Code check via known env vars
    if any(var in os.environ for var in VSCODE_ENV_VARS):
        return PythonEnvironment.VSCODE

    if shell_name == SHELL_TYPE_ZMQ:
        return PythonEnvironment.LOCAL_JUPYTER

    if shell_name == SHELL_TYPE_TERMINAL:
        return PythonEnvironment.IPYTHON_TERMINAL

    return PythonEnvironment.UNKNOWN
