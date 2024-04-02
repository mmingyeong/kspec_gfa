#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: guiding.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys
import time

import click

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from controller.gfa_controller import gfa_controller
from controller.gfa_logger import gfa_logger

logger = gfa_logger(__file__)
config_path = "../etc/cameras.yml"


@click.command()
@click.option(
    "-n",
    "--num",
    type=click.INT,
    required=True,
    show_default=True,
)
@click.option(
    "-e",
    "--exp",
    type=click.FLOAT,
    required=False,
    default=1,
    show_default=True,
)  # default = 1 sec should be changed after field test
def grab(num: int, exp):
    """Grab one image for each camera.

    Parameters
    ----------
    n, num
        KSPEC GFA Camera Number to use
    e, exp
        Exposure Time to grab
    """
    now1 = time.time()

    controller = gfa_controller("controller", config_path, logger)
    ready = controller.ready(num)
    controller.open(ready)
    controller.grab(ready, num, exp)
    controller.close(ready)

    now2 = time.time()
    print("process time:", now2 - now1)


if __name__ == "__main__":
    grab()
