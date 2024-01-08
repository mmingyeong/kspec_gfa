#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-04
# @Filename: guiding.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from controller.gfa_controller import gfa_controller

import click
import time

@click.command()
@click.option('-e', '--exp', type=click.FLOAT, required=False, default=1, show_default=True) # default = 1 sec
def graball(exp):
    now1 = time.time()
    lt = time.localtime(now1)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    
    controller = gfa_controller("controller")
    for i in range(len(controller.camera_list)):
        num = i + 1
        ready = controller.ready(num)
        controller.open(ready)
        controller.grab(ready, num, exp)
        controller.close(ready)
    
    now2 = time.time()
    lt = time.localtime(now2)
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
    print("process time:", now2-now1)

if __name__ == '__main__':
    graball()