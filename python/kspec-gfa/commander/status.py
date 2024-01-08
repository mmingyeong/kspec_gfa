#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: status.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time

import click
from controller.gfa_controller import gfa_controller


@click.command()
@click.option(
    "-n", "--num", type=click.INT, required=False, default=0, show_default=True
)
def status(num: int):
    """Returns the camera status."""

    now1 = time.time()
    lt = time.localtime(now1)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)

    controller = gfa_controller("controller")
    status = controller.status(num)
    click.echo(status)

    now2 = time.time()
    lt = time.localtime(now2)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    print("process time:", now2 - now1)


if __name__ == "__main__":
    status()
