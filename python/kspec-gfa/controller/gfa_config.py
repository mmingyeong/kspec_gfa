#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: gfa_config.py


import yaml

from .gfa_exceptions import GFAConfigError

__all__ = ["gfa_config"]
config_path = "./etc/camera.yml"


class gfa_config:
    """Defines Cameras Information connected with an KSPEC Controller.

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
        logger,
        *args,
        **kwargs,
    ):
        self.controller = controller
        self.logger = logger
        if config:
            self.config = config
        else:
            self.logger.error("No config")
            raise GFAConfigError("Wrong config")

    def from_config(self):
        """Creates an dictionary of the GFA camera information
        from a configuration file.
        """

        self.logger.info(f"read {self.config}")

        with open(self.config) as f:
            film = yaml.load(f, Loader=yaml.FullLoader)

        self.logger.info(f"{film}")
        self.logger.info(f"return {self.config}")

        return film
