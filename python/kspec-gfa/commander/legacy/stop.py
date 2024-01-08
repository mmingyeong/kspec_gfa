#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: stop.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import click
from gfa_controller.gfa_controller.controller.legacy.gfa_controller import \
    gfa_controller


@click.command()
def start():
    """Returns the camera status."""

    controller = gfa_controller("controller")
    status = controller.close()
    click.echo(status)


if __name__ == "__main__":
    start()
