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

from .gfa_log import GFA_Logger
from .exceptions import GFAInitError, GFAInitConnectCameraError, GFAInitOpenCameraError, GFAInitGrabError, GFAInitGrabImageError

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
            
            NUM_CAMERAS = 7
            TEST_NUM_CAMERAS = 3
            
            tlf = py.TlFactory.GetInstance()
            devices = tlf.EnumerateDevices()
            if len(devices) == 0:
                raise py.RuntimeException("No camera present.")
            
            self.cam_array = py.InstantCameraArray(NUM_CAMERAS)
            logger.info(f"{self.cam_array}")
            logger.info(f'Cam array check')
        
        except GFAInitConnectCameraError as err:
            logger.error(err)
        
        logger.info('Connected the KSPEC GFA cameras')
        logger.info('Done')
        
        return self.cam_array

    def gfa_init_exposure(self, ExposureTime):
        
        try:
            logger.info('Start Exposure Initializaton')
            
            logger.info('Open Cams')
            for i, cam in enumerate(self.cam_array):
                cam.Open()
                logger.info("Using device ", cam.GetDeviceInfo().GetModelName())
                
            #self.cam_array.Open()
            l = self.cam_array.GetSize()

            # Create and attach all Pylon Devices.
            for i, cam in enumerate(self.cam_array):
                logger.info("Using device ", cam.GetDeviceInfo().GetModelName())
            logger.info('check')

        except GFAInitOpenCameraError as err:
            logger.error(err)
            
        try:
            logger.info('Cam1 Grab')
            cam1_res = self.cam_array[0].GrabOne(ExposureTime)  # 1 sec
            logger.info('check')
            
            logger.info('Cam2 Grab')
            cam2_res = self.cam_array[1].GrabOne(ExposureTime)  # 1 sec
            logger.info('check')
            
            logger.info('Cam3 Grab')
            cam3_res = self.cam_array[2].GrabOne(ExposureTime)  # 1 sec
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
        
        now = time
        now_time = now.strftime('%Y-%m-%d_%H:%M:%S')

        for i in range(len(img_list)):
            plt.imshow(img_list[i])
            plt.savefig(f'./img_saved/{now_time}_cam{i}_img.png')
        
        return img_list
        
    def gfa_init_set_ready(self):
        pass
