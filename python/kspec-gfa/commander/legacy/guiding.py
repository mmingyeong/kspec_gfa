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

import click
from gfa_controller.gfa_controller.controller.legacy.gfa_controller import \
    gfa_controller


@click.group()
@click.pass_context
def guiding(ctx):
    controller = gfa_controller("controller")
    ready = controller.ready()
    ctx.obj = {"controller": controller}
    ctx.obj = {"ready": ready}


@guiding.command()
@click.pass_context
def start(ctx):
    # controller = ctx.obj.get('controller')
    controller = gfa_controller("controller")
    ready = ctx.obj.get("ready")
    controller.open(ready)


@guiding.command()
@click.pass_context
def stop(ctx):
    # controller = ctx.obj.get('controller')
    controller = gfa_controller("controller")
    ready = ctx.obj.get("ready")
    controller.close(ready)


@guiding.command()
@click.pass_context
@click.option(
    "-n", "--num", type=click.INT, required=True, default=0, show_default=True
)
@click.option(
    "-e", "--exp", required=False, default=1000000, show_default=True
)  # default = 1 sec
def grab(ctx, num: int, exp):
    # controller = ctx.obj.get('controller')
    controller = gfa_controller("controller")
    ready = ctx.obj.get("ready")
    controller.grab(ready, num, exp)


if __name__ == "__main__":
    guiding()
