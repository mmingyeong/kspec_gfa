#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: gfa_config.py

import pypylon.pylon as py
import logging
import time
import matplotlib.pyplot as plt
import os
import yaml

__all__ = ["gfa_config"]

config_path = "/home/kspec/mingyeong/gfa_controller/gfa_controller/etc/cameras.yml"  # absolute path

class gfa_config():
    """Defines Cameras connected with an KSPEC Controller.

    Parameters
    ----------
    controller
        A controller name connected with the Cameras.
    config
        The configuration defined on the .yaml file under /etc/cameras.yml
    """

    def __init__(
        self,
        controller: str,
        config: str,
        *args,
        **kwargs,
    ):

        self.controller = controller
        self.config = config

    def from_config(self):
        """Creates an dictionary of the GFA camera info from a configuration file."""
        
        with open(self.config) as f:
            self.film = yaml.load(f, Loader=yaml.FullLoader)
            
        return self.film