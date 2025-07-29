# -*- coding: utf-8 -*-
"""
>>> import os
>>> import sys
>>> import time
>>> import nava
>>> test_sound_path = os.path.join("others", "test.wav")
>>> nava.play(test_sound_path)
>>> sound_id_1 = nava.play(test_sound_path, async_mode=True)
>>> sound_id_1 == 1001
True
>>> sound_id_2 = nava.play(test_sound_path, async_mode=True)
>>> sound_id_2 == 1002
True
>>> sound_id_3 = nava.play(test_sound_path, async_mode=True)
>>> sound_id_3 == 1003
True
>>> sound_id_4 = nava.play(test_sound_path, async_mode=True, loop=True)
>>> sound_id_4 == 1004
True
>>> nava.stop(sound_id_1)
>>> nava.stop(sound_id_4)
>>> for i in range(40):
...     sound_id = nava.play(test_sound_path, async_mode=True)
...     time.sleep(0.2)
>>> time.sleep(1)
>>> nava.stop_all()
>>> len(nava.params._play_threads_map) == 44
True
>>> nava.params._play_threads_counter == 44
True
>>> sys_platform = sys.platform
>>> if sys_platform == "win32":
...     sound_id = nava.play(test_sound_path, async_mode=True, engine=nava.Engine.WINSOUND)
...     sound_id = nava.play(test_sound_path, engine=nava.Engine.WINMM)
...     sound_id = nava.play(test_sound_path, async_mode=True, engine=nava.Engine.WINMM)
...     time.sleep(1)
...     nava.stop(sound_id)
...     sound_id = nava.play(test_sound_path, async_mode=True, engine=nava.Engine.WINMM, loop=True)
...     time.sleep(30)
...     nava.stop(sound_id)
... elif sys_platform == "darwin":
...     sound_id = nava.play(test_sound_path, async_mode=True, engine=nava.Engine.AFPLAY)
... else:
...     sound_id = nava.play(test_sound_path, async_mode=True, engine=nava.Engine.ALSA)
>>> nava.functions.play_cli(test_sound_path)
>>> nava.functions.nava_help()
<BLANKLINE>
A Python library for playing sound everywhere natively and securely.
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/openscilab/nava
Webpage : https://openscilab.com/
"""
