# -*- coding: utf-8 -*-
"""Nava thread."""

import sys
import threading


class NavaThread(threading.Thread):
    """Nava custom thread."""

    def __init__(self, *args, **kwargs):
        """
        Init method.

        :param args: arguments
        :type args: list
        :param kwargs: keyword arguments
        :type kwargs: dict
        """
        super(NavaThread, self).__init__(*args, **kwargs)
        self.play_process = None

    def run(self):
        """
        Run target function.

        :return: None
        """
        if self._target is not None:
            self.play_process = self._target(*self._args, **self._kwargs)

    def stop(self):
        """
        Stop sound.

        :return: None
        """
        sys_platform = sys.platform
        if sys_platform == "win32":
            import winsound
            winsound.PlaySound(None, winsound.SND_PURGE)
        else:
            if self.play_process is not None:
                self.play_process.kill()
                self.play_process.terminate()
