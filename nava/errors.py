# -*- coding: utf-8 -*-
"""Nava errors."""


class NavaBaseError(Exception):
    """Nava base error class."""

    pass


class NavaValidationError(NavaBaseError, ValueError):
    """Nava validation error class."""

    pass


class NavaPlayError(NavaBaseError, RuntimeError):
    """Nava play error class."""

    pass
