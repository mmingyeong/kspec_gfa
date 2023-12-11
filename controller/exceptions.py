#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-12-06
# @Filename: exceptions.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import annotations


class GFAError(Exception):
    """A general ``GFA`` error."""

    pass


class GFAInitError(GFAError):
    """A GFA Initialization-related error."""

    pass


class GFAInitConnectCameraError(GFAError):
    """A Camera connection-related error."""

    pass

class GFAInitOpenCameraError(GFAError):
    """A Camera Open-related error."""

    pass


class GFAInitGrabError(GFAError):
    """A Camera Open-related error."""

    pass

class GFAInitGrabImageError(GFAError):
    """A Camera Open-related error."""

    pass

class GFAWarning(UserWarning):
    """General warnings for ``GFA.``"""

    pass