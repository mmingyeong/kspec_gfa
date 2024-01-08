#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: offset.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import time

import click
from controller.gfa_guiding import gfa_guiding


@click.command()
def offset():
    """Returns the offset value."""

    now1 = time.time()
    lt = time.localtime(now1)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)

    click.echo("Guiding process")

    now2 = time.time()
    lt = time.localtime(now2)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    print("process time:", now2 - now1)


if __name__ == "__main__":
    offset()
