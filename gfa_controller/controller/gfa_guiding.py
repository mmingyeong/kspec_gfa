#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: gfa_guiding.ipynb

import pypylon.pylon as py
import logging
import time
import matplotlib.pyplot as plt
import os
import yaml

from .gfa_log import gfa_logger
from .gfa_config import gfa_config

__all__ = ["gfa_guiding"]

class gfa_guiding():
    """Calculation the offset value

    Parameters
    ----------
    """
    
    def __init__(self, name: str):
        self.name = name
        # self.log = logger
        
    def offset(self):
        pass