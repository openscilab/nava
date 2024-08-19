# -*- coding: utf-8 -*-
"""Nava thread."""

import threading
from .params import Engine, SOUND_FILE_PLAY_ERROR
from .errors import NavaBaseError


class NavaThread(threading.Thread):
    """Nava custom thread."""

    def __init__(self, loop, engine, *args, **kwargs):
        """
        Init method.

        :param loop: sound thread loop flag
        :type loop: bool
        :param engine: play engine
        :type engine: Engine enum
        :param args: arguments
        :type args: list
        :param kwargs: keyword arguments
        :type kwargs: dict
        """
        super(NavaThread, self).__init__(*args, **kwargs)
        self._play_process = None
        self._loop = loop
        self._engine = engine
        self._nava_exception = None

    def run(self):
        """
        Run target function.

        :return: None
        """
        try:
            if self._target is not None:
                if self._engine == Engine.WINSOUND:
                    self._play_process = self._target(*self._args, **self._kwargs)
                else:
                    while True:
                        self._play_process = self._target(*self._args, **self._kwargs)
                        self._play_process.wait()
                        if not self._loop:
                            break
        except Exception:  # pragma: no cover
            self._nava_exception = SOUND_FILE_PLAY_ERROR
            raise NavaBaseError(SOUND_FILE_PLAY_ERROR)

    def stop(self):
        """
        Stop sound.

        :return: None
        """
        self._loop = False
        if self._engine == Engine.WINSOUND:
            import winsound
            winsound.PlaySound(None, winsound.SND_PURGE)
        else:
            if self._play_process is not None:
                try:
                    self._play_process.stdout.close()
                    self._play_process.stdin.close()
                    self._play_process.stderr.close()
                    self._play_process.kill()
                    self._play_process.terminate()
                except ProcessLookupError:
                    pass
                finally:
                    self._play_process.wait()
