import asyncio
import nava.functions as nv


async def test_print():
    """
    Simple function printing hello world async

    :return: None
    """
    while True:
        print("Hello, World!")
        await asyncio.sleep(0.1)

async def test_play():
    """
    Simple function playing sound async (must provide path to file)

    :return: None
    """
    play_task = asyncio.create_task(nv.play("test/clear.wav", is_async=True))
    print_task = asyncio.create_task(test_print())

    await play_task

if __name__ == "__main__":
    asyncio.run(test_play())
    """
    How to run? Make sure you're in the project root
    directory. Then, pass the script to Python interpreter 
    like below:
    > python -m test.main
    The result in async mode with 0.1 second delay is as follows:
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!
    Hello, World!

    In the meantime you should be able to hear the sound. The actual
    number of hello worlds depend on the voice length and the delay value.
    """
