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
>>> nava.play(os.path.join("others", "test.wav"), async_mode=False, loop=True)
Traceback (most recent call last):
    ...
nava.errors.NavaBaseError: The loop option can only be used in async mode.
"""
