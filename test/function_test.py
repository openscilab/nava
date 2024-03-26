# -*- coding: utf-8 -*-
"""
>>> import os
>>> import time
>>> import nava
>>> nava.play(os.path.join("others", "test.wav"))
>>> sound_id_1 = nava.play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_1 == 1001
True
>>> sound_id_2 = nava.play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_2 == 1002
True
>>> sound_id_3 = nava.play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_3 == 1003
True
>>> sound_id_4 = nava.play(os.path.join("others", "test.wav"), async_mode=True, loop=True)
>>> sound_id_4 == 1004
True
>>> nava.stop(sound_id_1)
>>> nava.stop(sound_id_4)
>>> for i in range(40):
...     sound_id = nava.play(os.path.join("others", "test.wav"), async_mode=True)
...     time.sleep(0.2)
>>> time.sleep(1)
>>> nava.stop_all()
>>> len(nava.params._play_threads_map) == 43
True
>>> nava.params._play_threads_counter == 43
True
>>> nava.functions.nava_help()
<BLANKLINE>
A Python library for playing sound everywhere natively and securely.
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/openscilab/nava
Webpage : https://openscilab.com/
"""
