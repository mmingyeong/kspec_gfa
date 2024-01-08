#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: guiding.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time

import click
from controller.gfa_controller import gfa_controller


@click.command()
@click.option(
    "-n", "--num", type=click.INT, required=True, default=1, show_default=True
)
@click.option(
    "-e", "--exp", type=click.FLOAT, required=False, default=1, show_default=True
)  # default = 1 sec
def grab(num: int, exp):
    now1 = time.time()
    lt = time.localtime(now1)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)

    controller = gfa_controller("controller")
    ready = controller.ready(num)
    controller.open(ready)
    controller.grab(ready, num, exp)
    controller.close(ready)

    now2 = time.time()
    lt = time.localtime(now2)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    print("process time:", now2 - now1)


if __name__ == "__main__":
    grab()
