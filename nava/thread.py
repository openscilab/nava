# -*- coding: utf-8 -*-
"""Nava thread."""

from typing import List, Dict, Any
import threading
from .params import Engine, SOUND_FILE_PLAY_ERROR
from .errors import NavaBaseError


class NavaThread(threading.Thread):
    """Nava custom thread."""

    def __init__(self, loop: bool, engine: Engine, *args: List[Any], **kwargs: Dict[str, Any]) -> None:
        """
        Init method.

        :param loop: sound thread loop flag
        :param engine: play engine
        :param args: arguments
        :param kwargs: keyword arguments
        """
        super(NavaThread, self).__init__(*args, **kwargs)
        self._play_process = None
        self._loop = loop
        self._force_stop = False
        self._engine = engine
        self._nava_exception = None

    def run(self) -> None:
        """Run target function."""
        try:
            if self._target is not None:
                if self._engine == Engine.WINSOUND or self._engine == Engine.WINMM:
                    self._target(*self._args, **self._kwargs)
                else:
                    while True:
                        self._play_process = self._target(*self._args, **self._kwargs)
                        self._play_process.wait()
                        if not self._loop:
                            break
        except Exception:  # pragma: no cover
            self._nava_exception = SOUND_FILE_PLAY_ERROR
            raise NavaBaseError(SOUND_FILE_PLAY_ERROR)

    def stop(self) -> None:
        """Stop sound."""
        self._loop = False
        if self._engine == Engine.WINSOUND:
            import winsound
            winsound.PlaySound(None, winsound.SND_PURGE)
        elif self._engine == Engine.WINMM:
            self._force_stop = True
            # The alias is scoped to the MCI (Media Control Interface) context of the thread that created it.
            # So the main thread can't "see" the alias created in the worker thread.
        else:
            if self._play_process:
                # Best-effort: close all standard streams
                try:
                    self._play_process.stdout.close()
                    self._play_process.stdin.close()
                    self._play_process.stderr.close()
                except Exception:  # nosec B110 - Best effort cleanup, ignore all errors
                    # Streams may be None, already closed, or OS-specific issues
                    pass

                # Try graceful termination
                try:
                    self._play_process.terminate()
                    self._play_process.wait(timeout=1)
                except Exception:
                    # Fallback to force kill - catch any process-related errors
                    try:
                        self._play_process.kill()
                        self._play_process.wait()
                    except Exception:  # nosec B110 - Best effort cleanup, ignore all errors
                        # Process already terminated or any other issues
                        pass
                finally:
                    self._play_process = None
