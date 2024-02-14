#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: gfa_guiding.ipynb

import logging
import os
import time

import matplotlib.pyplot as plt
import pypylon.pylon as py
import yaml

from .gfa_config import gfa_config
from .gfa_logger import gfa_logger

__all__ = ["gfa_guiding"]


class gfa_guiding:
    """Calculation the offset value

    Parameters
    ----------
    """

    def __init__(self, name: str):
        self.name = name
        # self.log = logger

    def offset(self):
        pass
