#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: status.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys
import time

import click
from controller.gfa_controller import gfa_controller
from controller.gfa_logger import gfa_logger

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
logger = gfa_logger(__file__)
config_path = "../etc/cameras.yml"


@click.command()
@click.option(
    "-n", "--num", type=click.INT, required=False, default=0, show_default=True
)
def status(num: int):
    """Returns the camera status.

    Parameters
    ----------
    n, num
        KSPEC GFA Camera Number to use
    """

    now1 = time.time()

    controller = gfa_controller("controller", config_path, logger)
    status = controller.status(num)
    for k, v in status.items():
        click.echo("{} : {}".format(k, v))

    now2 = time.time()
    print("process time:", now2 - now1)


if __name__ == "__main__":
    status()
