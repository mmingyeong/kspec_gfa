#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: gfa_controller.ipynb

import pypylon.pylon as py
import logging
import time
import matplotlib.pyplot as plt
import os
import yaml

from .gfa_log import gfa_logger
from .gfa_config import gfa_config

__all__ = ["gfa_controller"]

# logger = gfa_logger(__file__)
config_path = "/home/kspec/mingyeong/gfa_controller/gfa_controller/etc/cameras.yml" # absolute path

class gfa_controller():
    """Talk to an KSPEC GFA Camera over TCP/IP.

    Parameters
    ----------
    name
        A name identifying this controller.
    config
        The configuration defined on the .yaml file under /etc/lvmecp.yml
    log
        The logger for logging
    """
    
    def __init__(self, name: str):
        self.name = name
        # self.log = logger

        config = gfa_config(self.name, config_path).from_config()
        self.cameras_info = config["GfaController"]["Elements"]["Cameras"]["Elements"]
        self.camera_list = self.cameras_info.keys()
        
        self.tlf = py.TlFactory.GetInstance()
        self.tl = self.tlf.CreateTl('BaslerGigE')
        
    def status(self, CamNum=0):
        """status"""
        
        status_result = {}
        if not CamNum==0:
            Cam_name = self.cameras_info[f"Cam{CamNum}"]["Name"]
            Cam_IpAddress = self.cameras_info[f"Cam{CamNum}"]["IpAddress"]
            
            cam_status = py.InstantCamera(self.tlf.CreateDevice(Cam_IpAddress))
            if cam_status:
                status_result[Cam_name]=True
            
        else:
            for cam in self.camera_list:
                Cam_name = self.cameras_info[cam]["Name"]
                Cam_IpAddress = self.cameras_info[cam]["IpAddress"]
                
                cam_status = py.InstantCamera(self.tlf.CreateDevice(Cam_IpAddress))
                if cam_status:
                    status_result[Cam_name]=True
                else:
                    status_result[Cam_name]=False
        
        return status_result
    
    def open(self, CamNum: int):
        pass
    
    def close(self, CamNum: int):
        pass
    
    def grab(self, CamNum: int, ExpTime: int):
        pass

