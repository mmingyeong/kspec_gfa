#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-12-06
# @Filename: gfa_init.ipynb

import pypylon.pylon as py
import logging

from gfa_log import GFA_Logger
from exceptions import GFAInitError, GFAInitConnectCameraError, GFAInitOpenCameraError, GFAInitGrabError, GFAInitGrabImageError

__all__ = ["gfa_init"]

logger = GFA_Logger(__file__)

class gfa_init():
    """initialization to start the GFA sequence normally"""
    
    def __init__(self, *args, **kwargs):
        logger.info('Start the GFA sequence')
        pass
        
    def gfa_init_connect_camera(self):
        
        try:
            logger.info('Connect the KSPEC GFA cameras')
            
            tlf = py.TlFactory.GetInstance()
            devices = tlf.EnumerateDevices()
            self.cameras = {}       # list or dict?
            
            cam1 = py.InstantCamera(tlf.CreateDevice(devices[0]))
            logger.info(f'Cam1 check {cam1}')
            cam2 = py.InstantCamera(tlf.CreateDevice(devices[1]))
            logger.info(f'Cam2 check {cam2}')
            cam3 = py.InstantCamera(tlf.CreateDevice(devices[2]))
            logger.info(f'Cam3 check {cam3}')
            #cam4 = cameras[3]
            #cam5 = cameras[4]
            #cam6 = cameras[5]
            #cam7 = cameras[6]
            
            self.cameras["cam1"] = cam1
            self.cameras["cam2"] = cam2
            self.cameras["cam3"] = cam3
            
        
        except GFAInitConnectCameraError as err:
            logger.error(err)
        
        logger.info('Connected the KSPEC GFA cameras')
        logger.info('Done')
        
        return self.cameras

    def gfa_init_exposure(self, ExposureTime):
        
        try:
            logger.info('Start Exposure Initializaton')
            
            cam1 = self.cameras["cam1"]
            cam2 = self.cameras["cam2"]
            cam3 = self.cameras["cam3"]
            
            logger.info('Open Cams')
            cam1.Open()
            cam2.Open()
            cam3.Open()
            
            logger.info('check')

        except GFAInitOpenCameraError as err:
            logger.error(err)
            
        try:
            logger.info('Grab ready?')
            cam1.TriggerSelector = 'ExposureStart'
            cam1.TriggerSource = "Line1"
            cam2.TriggerSelector = 'ExposureStart'
            cam2.TriggerSource = "Line1"
            cam3.TriggerSelector = 'ExposureStart'
            cam3.TriggerSource = "Line1"
            
            cam1.PixelFormat.SetValue("Mono8")
            cam3.PixelFormat.SetValue("Mono8")
            cam3.PixelFormat.SetValue("Mono8")
            logger.info('Grab ready.')
            
            logger.info('Cam1 Grab')
            cam1_res = cam1.GrabOne(ExposureTime)  # 1 sec
            logger.info('check')
            
            logger.info('Cam2 Grab')
            cam2_res = cam2.GrabOne(ExposureTime)  # 1 sec
            logger.info('check')
            
            logger.info('Cam3 Grab')
            cam3_res = cam3.GrabOne(ExposureTime)  # 1 sec
            logger.info('check')

        except GFAInitGrabError as err:
            logger.error(err)
            
        try:
            logger.info('Save image array')
            cam1_img = cam1_res.GetArray()
            cam2_img = cam2_res.GetArray()
            cam3_img = cam3_res.GetArray()

            img_list = []
            img_list.append(cam1_img)
            img_list.append(cam2_img)
            img_list.append(cam3_img)
            logger.info('Saved image array')
            # ? 이미지 array를 저장하는게 아니라 fit file로 return 해야 하는지?
            
        except GFAInitGrabImageError as err:
            logger.error(err)
            
        logger.info('Done')
        
        return img_list
        
    def gfa_init_set_ready(self):
        pass
