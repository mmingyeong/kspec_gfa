#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: offset.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys
import time

import click

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from controller.gfa_logger import gfa_logger

config_path = "../etc/cameras.yml"


@click.command()
def offset():
    """Returns the offset value."""

    now1 = time.time()

    click.echo("Guiding process")

    now2 = time.time()
    print("process time:", now2 - now1)


if __name__ == "__main__":
    offset()
