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
        self.camera_list = list(self.cameras_info.keys())
        # print(self.camera_list) dict_keys(['Cam1', 'Cam2', 'Cam3', 'Cam4'])
        
        self.tlf = py.TlFactory.GetInstance()
        self.tl = self.tlf.CreateTl('BaslerGigE')
        
    def status(self, CamNum=0):
        """status"""
        
        now1 = time.time()
        lt = time.localtime(now1)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func start", formatted)
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
                    
        now2 = time.time()
        lt = time.localtime(now2)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func done", formatted)
        #print("process time:", now2-now1)
        
        return status_result
    
    def ready(self, CamNum:int):
        """ready to open and close"""
        #print("start to ready")
        now1 = time.time()
        lt = time.localtime(now1)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func start", formatted)
        cam_ready_dict = {}
        
        # Cam Info check
        Cam_name = self.cameras_info[f"Cam{CamNum}"]["Name"]
        Cam_IpAddress = self.cameras_info[f"Cam{CamNum}"]["IpAddress"]
        
        # Get the transport layer factory.
        cam_info_ip = self.tl.CreateDeviceInfo()
        cam_info_ip.SetIpAddress(Cam_IpAddress)
        cam = py.InstantCamera(self.tlf.CreateDevice(cam_info_ip))

        # Get fullname
        fullname = cam.GetDeviceInfo().GetFullName()
        
        # Create cam using fullname
        cam_info_fullname = self.tl.CreateDeviceInfo()
        cam_info_fullname.SetFullName(fullname)
        cam_ready = py.InstantCamera(self.tlf.CreateDevice(cam_info_fullname))
        cam_ready_dict[Cam_name] = cam_ready

        now2 = time.time()
        lt = time.localtime(now2)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func done", formatted)
        #print("process time:", now2-now1)
        
        return cam_ready
        
    def open(self, ready):
        """Open the camera connection"""
        #print("start to open")
        now1 = time.time()
        lt = time.localtime(now1)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func start", formatted)

        ready.Open()
            
        now2 = time.time()
        lt = time.localtime(now2)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func done", formatted)
        #print("process time:", now2-now1)
    
    def close(self, ready):
        """Close the camera connection"""
        #print("start to close")
        now1 = time.time()
        lt = time.localtime(now1)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func start", formatted)
        
        ready.Close()

        now2 = time.time()
        lt = time.localtime(now2)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func done", formatted)
        #print("process time:", now2-now1)
    
    def grab(self, ready, CamNum, ExpTime):
        """ExpTime: Microsecond"""
        now1 = time.time()
        lt = time.localtime(now1)
        formatted = time.strftime("%Y-%m-%d_%H:%M:%S", lt)
        
        cam = ready
        ExpTime_microsec = ExpTime * 1000000
        cam.ExposureTime.SetValue(ExpTime_microsec)
        res = cam.GrabOne(100000)
        img = res.GetArray()
        plt.imshow(img)
        plt.savefig(f'/home/kspec/mingyeong/gfa_controller/gfa_controller/controller/img_saved/{formatted}_cam{CamNum}_img.png')

        now2 = time.time()
        lt = time.localtime(now2)
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
        #print("Func done", formatted)
        #print("Exposure Time time:", ExpTime)
        #print("grab process time:", now2-now1)
