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
from controller.gfa_controller import gfa_controller

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
config_path = "../etc/cameras.yml"


@click.command()
@click.option(
    "-e", "--exp", type=click.FLOAT, required=False, default=1, show_default=True
)  # default = 1 sec
def graball(exp):
    """Grab images for all camera.

    Parameters
    ----------
    e, exp
        Exposure Time to grab
    """
    now1 = time.time()

    controller = gfa_controller("controller", config_path)
    for i in range(len(controller.camera_list)):
        num = i + 1
        ready = controller.ready(num)
        controller.open(ready)
        controller.grab(ready, num, exp)
        controller.close(ready)

    now2 = time.time()
    print("process time:", now2 - now1)


if __name__ == "__main__":
    graball()
