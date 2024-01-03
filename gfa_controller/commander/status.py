#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: status.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from controller.gfa_controller import gfa_controller

import click

@click.command()
@click.option('-n', '--num', type=click.INT, required=False, default=0, show_default=True)
def status(num:int):
    """Returns the camera status."""
    
    controller = gfa_controller("controller")
    status = controller.status(num)
    click.echo(status)
    
if __name__ == '__main__':
    status()