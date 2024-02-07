# -*- coding: utf-8 -*-
"""
>>> import os
>>> import time
>>> from nava import play, stop, stop_all
>>> play(os.path.join("others", "test.wav"))
>>> sound_id_1 = play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_1 == 1001
True
>>> sound_id_2 = play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_2 == 1002
True
>>> sound_id_3 = play(os.path.join("others", "test.wav"), async_mode=True)
>>> sound_id_3 == 1003
True
>>> stop(1001)
>>> for i in range(50):
...     sound_id = play(os.path.join("others", "test.wav"), async_mode=True)
>>> from nava.functions import nava_help
>>> nava_help()
<BLANKLINE>
A Python library for playing sound everywhere natively and securely.
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/openscilab/nava
Webpage : https://openscilab.com/
"""
