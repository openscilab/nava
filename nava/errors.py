# -*- coding: utf-8 -*-
"""Nava errors."""


class NavaBaseError(Exception):
    """Nava base error class."""

    pass


class NavaValidationError(NavaBaseError, ValueError):
    """Nava validation error class."""

    pass
