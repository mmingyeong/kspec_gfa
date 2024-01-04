#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-12-06
# @Filename: gfa_init.ipynb

import pypylon.pylon as py
import logging
import time
import matplotlib.pyplot as plt
import os

from .gfa_log import gfa_logger
from .exceptions import GFAInitError, GFAInitConnectCameraError, GFAInitOpenCameraError, GFAInitGrabError, GFAInitGrabImageError

__all__ = ["gfa_init"]

logger = gfa_logger(__file__)

class gfa_init():
    """initialization to start the GFA sequence normally"""
    
    def __init__(self, *args, **kwargs):
        logger.info('Start the GFA sequence')
        pass
        
    def gfa_init_connect_camera(self):
        
        try:
            logger.info('Connect the KSPEC GFA cameras')
            
            cam1_ip = '192.168.9.3' # 3834
            cam2_ip = '192.168.8.3' # 3833
            cam3_ip = '192.168.10.3' # 3831
            self.cams_ready = []
            
            logger.info('Cam1 Ready?')
            # Get the transport layer factory.
            tlf = py.TlFactory.GetInstance()
            tl = tlf.CreateTl('BaslerGigE')
            cam1_info_ip = tl.CreateDeviceInfo()
            cam1_info_ip.SetIpAddress(cam1_ip)
            cam1 = py.InstantCamera(tlf.CreateDevice(cam1_info_ip))
            
            # Get fullname
            fullname = cam1.GetDeviceInfo().GetFullName()
            
            # Create cam using fullname
            cam1_info_fullname = tl.CreateDeviceInfo()
            cam1_info_fullname.SetFullName(fullname)
            cam1_ready = py.InstantCamera(tlf.CreateDevice(cam1_info_fullname))
            self.cams_ready.append(cam1_ready)
            logger.info('Cam1 Ready.')

            logger.info('Cam2 Ready?')
            # Get the transport layer factory.
            cam2_info_ip = tl.CreateDeviceInfo()
            cam2_info_ip.SetIpAddress(cam2_ip)
            cam2 = py.InstantCamera(tlf.CreateDevice(cam2_info_ip))
            
            # Get fullname
            fullname = cam2.GetDeviceInfo().GetFullName()
            
            # Create cam using fullname
            cam2_info_fullname = tl.CreateDeviceInfo()
            cam2_info_fullname.SetFullName(fullname)
            cam2_ready = py.InstantCamera(tlf.CreateDevice(cam2_info_fullname))
            self.cams_ready.append(cam2_ready)
            logger.info('Cam2 Ready.')
            
            logger.info('Cam3 Ready?')
            # Get the transport layer factory.
            cam3_info_ip = tl.CreateDeviceInfo()
            cam3_info_ip.SetIpAddress(cam3_ip)
            cam3 = py.InstantCamera(tlf.CreateDevice(cam3_info_ip))
            
            # Get fullname
            fullname = cam3.GetDeviceInfo().GetFullName()
            
            # Create cam using fullname
            cam3_info_fullname = tl.CreateDeviceInfo()
            cam3_info_fullname.SetFullName(fullname)
            cam3_ready = py.InstantCamera(tlf.CreateDevice(cam3_info_fullname))
            self.cams_ready.append(cam3_ready)
            logger.info('Cam3 Ready.')
        
        except GFAInitConnectCameraError as err:
            logger.error(err)
        
        logger.info('Connected the KSPEC GFA cameras')
        logger.info('Done')
        
        return self.cams_ready

    def gfa_init_exposure(self, ExposureTime):
        
        cam1 = self.cams_ready[0]
        cam2 = self.cams_ready[1]
        cam3 = self.cams_ready[2]
        
        try:
            logger.info('Start Exposure Check')
            logger.info('Open Cam')
            for cam in self.cams_ready:
                cam.Open()
            logger.info('check')        

        except GFAInitOpenCameraError as err:
            logger.error(err)
    
        try:
            img_list = []
        
            logger.info('Cam1 Grab One Image')
            cam1.ExposureTime.SetValue(ExposureTime)
            logger.info(f"Exposure Time, {cam1.ExposureTime.Value} micro sec")
            res1 = cam1.GrabOne(100000)
            img1 = res1.GetArray()
            img_list.append(img1)

        except GFAInitGrabError as err:
            logger.error(err)

        # ? 이미지 array를 저장하는게 아니라 fit file로 return 해야 하는지?
        
        now = time
        now_time = now.strftime('%Y-%m-%d_%H:%M:%S')
        
        for i in range(len(img_list)):
            plt.imshow(img_list[i])
            index = i + 1
            plt.savefig(f'/home/kspec/mingyeong/gfa_controller/controller/img_saved/{now_time}_cam{index}_img.png')
            
        logger.info('Done')

        return img_list

    def gfa_init_set_ready(self):
        pass
