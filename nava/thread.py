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
        self.sys_platform = sys.platform
        self.play_process = None
        self.loop = False

    def run(self):
        """
        Run target function.

        :return: None
        """
        if self._target is not None:
            if self.sys_platform == "win32":
                self.play_process = self._target(*self._args, **self._kwargs)
            else:
                while True:
                    self.play_process = self._target(*self._args, **self._kwargs)
                    self.play_process.wait()
                    if not self.loop:
                        break


    def stop(self):
        """
        Stop sound.

        :return: None
        """
        if self.sys_platform == "win32":
            import winsound
            winsound.PlaySound(None, winsound.SND_PURGE)
        else:
            if self.play_process is not None:
                try:
                    self.play_process.stdout.close()
                    self.play_process.stdin.close()
                    self.play_process.stderr.close()
                    self.play_process.kill()
                    self.play_process.terminate()
                except Exception:
                    pass
                finally:
                    self.play_process.wait()

