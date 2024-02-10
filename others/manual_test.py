# -*- coding: utf-8 -*-
"""Manual test script."""
import sys
import os
import time
import art
import nava

TEST_FILE_PATH = os.path.join("others", "test.wav")
SYS_PLATFORM = sys.platform


def print_line(length=80, char="#"):
    """
    Print line.

    :param length: length of line
    :type length: int
    :param char: character
    :type char: str
    :return: None
    """
    print(char * length)


def wait(seconds=10):
    """
    Wait for seconds.

    :param seconds: seconds
    :type seconds: int
    :return: None
    """
    print("Please wait for {0} seconds".format(seconds))
    time.sleep(seconds)


art.tprint("Nava Manual Test", font="bulbhead")
print("System Platform: {0}\n".format(SYS_PLATFORM))
print("Nava Version: {0}\n".format(nava.__version__))
print_line()

# Test1
print("1. 'async_mode = False'")
nava.play(TEST_FILE_PATH, async_mode=False)
print("You should only see this text after the completion of the first test.")
wait()

# Test2
print_line()
print("2. 'async_mode = True'")
sid1 = nava.play(TEST_FILE_PATH, async_mode=True)
print("If you see this text immediately after 'test2' begins, it means that the async mode is working properly.")
wait()

# Test3
print_line()
print("3. Stop")
nava.stop(sid1)
wait()

# Test4
print_line()
print("4. Play two sounds simultaneously (macOS/Linux)")
sid2 = nava.play(TEST_FILE_PATH, async_mode=True)
sid3 = nava.play(TEST_FILE_PATH, async_mode=True)
wait()

# Test5
print_line()
print("5. Stop all sounds")
nava.stop_all()
print("End!")
