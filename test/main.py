import time
import nava.functions as nv

if __name__ == "__main__":
    sound_thread = nv.play("test/test.wav", is_async=True)

    for _ in range(10):
        print("Hello World!")
        time.sleep(0.25)

    """
    How to run? Make sure you're in the project root
    directory. Then, pass the script to Python interpreter 
    like below:
    > python -m test.main

    Expected behaviours:
        * Async mode: If you don't wait for the thread, you
            can only hear about 2.5 seconds of the voice. In the 
            meantime you will see "Hello World!" messages printing
            on the screen
        * Sync mode: You will hear the sound completely and then,
            for about 2.5 seconds you will see 10 "Hello World!" 
            messages printing on the screen.
    """
