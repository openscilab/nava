# -*- coding: utf-8 -*-
"""
>>> import os
>>> import sys
>>> from nava import play, stop, Engine
>>> from nava import NavaBaseError, NavaValidationError, NavaPlayError
>>> issubclass(NavaBaseError, Exception)
True
>>> issubclass(NavaValidationError, NavaBaseError)
True
>>> issubclass(NavaValidationError, ValueError)
True
>>> issubclass(NavaPlayError, NavaBaseError)
True
>>> issubclass(NavaPlayError, RuntimeError)
True
>>> test_sound_path = os.path.join("others", "test.wav")
>>> play("test.wav")
Traceback (most recent call last):
    ...
nava.errors.NavaValidationError: Given sound file doesn't exist.
>>> play(1)
Traceback (most recent call last):
    ...
nava.errors.NavaValidationError: Sound file's path should be a string.
>>> stop(222222)
Traceback (most recent call last):
    ...
nava.errors.NavaValidationError: Given sound id doesn't exist.
>>> play(test_sound_path, async_mode=False, loop=True)
Traceback (most recent call last):
    ...
nava.errors.NavaValidationError: `loop` can not be set True when `async_mode` is False.
>>> play(test_sound_path, async_mode=True, loop=True, engine=2)
Traceback (most recent call last):
    ...
nava.errors.NavaValidationError: `engine` type must be `Engine` enum.
>>> sys_platform = sys.platform
>>> if sys_platform == "win32":
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.AFPLAY)
... elif sys_platform == "darwin":
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.WINSOUND)
... else:
...     sound_id = play(test_sound_path, async_mode=False, engine=Engine.WINSOUND)
Traceback (most recent call last):
    ...
nava.errors.NavaPlayError: Sound can not play due to some issues.
"""
