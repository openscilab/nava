# -*- coding: utf-8 -*-
"""
>>> import os
>>> from nava import play, stop
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
>>> play(os.path.join("others", "test.wav"), async_mode=False, loop=True)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: `loop` can not be set True when `async_mode` is False.
>>> play(os.path.join("others", "test.wav"), async_mode=True, loop=True, engine=2)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: `engine` type must be `Engine` enum.
>>> import nava
>>> nava.functions.play_cli("test2.wav")
Error: Given sound file doesn't exist.
"""
