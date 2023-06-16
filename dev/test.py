import asyncio
import subprocess


async def count():
    """
    Example function to test async play

    """
    while True:
        print("Hi!")
        await asyncio.sleep(1)

async def play_sound_async(file_name, loop = True):
    """
    Play sound asynchronously

    :param file_name: input sound file name
    :type file_name: str
    :param loop: play sound on loop
    :type: bool
    :return: None
    """
    task = asyncio.create_task(count())
    cmd = f"aplay {file_name}"
    while True:
        proc = await asyncio.subprocess.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await proc.communicate()

        if not loop:
            task.cancel()
            break

def play_sound_sync(file_name, loop = True):
    """
    Play sound synchronously

    :param file_name: input sound file name
    :type file_name: str
    :param loop: play sound on loop
    :type: bool
    :return: None
    """
    while True:
        _ = subprocess.check_call(["aplay",
                                file_name],
                                shell=False,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        if not loop:
            break


def start_sound(file_name: str, is_async: bool = True, loop: bool = True) -> None:
    """
    Start playing given sound

    :file_name: sound file name to play
    :type: str
    :is_async: play sound synchronously or asynchronously
    :type: bool
    :loop: play sound on loop
    :type: bool
    :return: None
    """
    if is_async:
        asyncio.run(play_sound_async(file_name, loop))
    else:
        play_sound_sync(file_name, loop)

def test_sound_playing():
    """
    Example function testing sound player
    """
    start_sound("clear.wav", True, True)

if __name__ == "__main__":
    test_sound_playing()
