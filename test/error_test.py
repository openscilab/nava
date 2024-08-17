# -*- coding: utf-8 -*-
"""
>>> import os
>>> import sys
>>> from nava import play, stop, Engine
>>> test_sound_path = os.path.join("others", "test.wav")
>>> play("test.wav")
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: Given sound file doesn't exist.
>>> play(1)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: Sound file's path should be a string.
>>> stop(222222)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: Given sound id doesn't exist.
>>> play(test_sound_path, async_mode=False, loop=True)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: `loop` can not be set True when `async_mode` is False.
>>> play(test_sound_path, async_mode=True, loop=True, engine=2)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: `engine` type must be `Engine` enum.
>>> sys_platform = sys.platform
>>> if sys_platform == "win32":
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.AFPLAY)
... elif sys_platform == "darwin":
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.WINSOUND)
... else:
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.WINSOUND)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: Sound can not play due to some issues.
>>> import nava
>>> nava.functions.play_cli("test2.wav")
Error: Given sound file doesn't exist.
"""
