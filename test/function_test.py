# -*- coding: utf-8 -*-
"""
>>> import os
>>> import asyncio
>>> from time import time
>>> from nava import play, play_async
>>> PATH2TEST_WAV = os.path.join("others", "test.wav")
>>> play(PATH2TEST_WAV)
>>> async def test_print():
...    start_time = time()
...    while True:
...        print("Test voice is in {:.1f}s".format(time() - start_time))
...        await asyncio.sleep(0.1)
>>> async def play_async_test():
...    asyncio.create_task(test_print())
...    await asyncio.create_task(play_async(PATH2TEST_WAV))
>>> asyncio.run(play_async_test())
Test voice is in 0.0s
Test voice is in 0.1s
Test voice is in 0.2s
Test voice is in 0.3s
>>> from nava.functions import nava_help
>>> nava_help()
<BLANKLINE>
A Python library for playing sound everywhere natively and securely.
<BLANKLINE>
<BLANKLINE>
Repo : https://github.com/openscilab/nava
Webpage : https://openscilab.com/
"""
