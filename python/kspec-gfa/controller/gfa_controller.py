#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-01-03
# @Filename: gfa_controller.ipynb

import os
import time

import matplotlib.pyplot as plt
import pypylon.pylon as py

from .gfa_config import gfa_config
from .gfa_logger import gfa_logger
from .gfa_exceptions import GFACamNumError, GFAConfigError, GFAError, GFAPingError

__all__ = ["gfa_controller"]

# logger = gfa_logger(__file__)
config_path = "./etc/camera.yml"


class gfa_controller:
    """Talk to an KSPEC GFA Camera over TCP/IP.

    Parameters
    ----------
    name
        A name identifying this controller.
    config
        The configuration defined on the .yaml file under /etc/cameras.yml
    log
        The logger for logging
    """

    def __init__(self, name: str, config: str, logger: gfa_logger):
        self.name = name
        self.logger = logger

        now1 = time.time()
        self.logger.info("Class start")

        try:
            config = gfa_config(self.name, config, logger).from_config()
        except:
            self.logger.error("No config")
            raise GFAConfigError("Wrong config")

        self.cameras_info = config["GfaController"]["Elements"]["Cameras"]["Elements"]
        self.camera_list = list(self.cameras_info.keys())

        self.tlf = py.TlFactory.GetInstance()
        self.tl = self.tlf.CreateTl("BaslerGigE")

        now2 = time.time()
        self.logger.info("Class init done")
        self.logger.info(f"process time: {now2-now1}")

    def ping(self, CamNum=0):
        
        now1 = time.time()
        self.logger.info("Func ping start")
        
        if not CamNum == 0:
            try:
                Cam_name = self.cameras_info[f"Cam{CamNum}"]["Name"]
                Cam_IpAddress = self.cameras_info[f"Cam{CamNum}"]["IpAddress"]
                ping_test = os.system("ping -c 3 -w 1 " + Cam_IpAddress)

            except:
                self.logger.error(f"No ping for Camera {CamNum}")
                raise GFAPingError(f"No ping for Camera {CamNum}")

        else:
            try:
                for cam in self.camera_list:
                    Cam_name = self.cameras_info[cam]["Name"]
                    Cam_IpAddress = self.cameras_info[cam]["IpAddress"]
                    ping_test = os.system("ping -c 3 -w 1 " + Cam_IpAddress)

            except:
                self.logger.error("No ping")
                raise GFAPingError("No ping")

        now2 = time.time()
        self.logger.info("Func ping done")
        self.logger.info(f"process time: {now2-now1}")

        return ping_test

    def status(self, CamNum):
        """Return connection status of the camera

        Parameters
        ----------
        CamNum
            Camera number
        """

        now1 = time.time()
        self.logger.info("Func status start")

        status_result = {}
        if not CamNum == 0:
            try:
                Cam_name = self.cameras_info[f"Cam{CamNum}"]["Name"]
                Cam_IpAddress = self.cameras_info[f"Cam{CamNum}"]["IpAddress"]
                cam_status = py.InstantCamera(self.tlf.CreateDevice(Cam_IpAddress))
                if cam_status:
                    status_result[Cam_name] = True
            except:
                self.logger.error(f"No Camera {CamNum}")
                self.logger.error(f"Camera: {self.cameras_info.keys()}")
                raise GFACamNumError(f"No Camera {CamNum}")

        else:
            for cam in self.camera_list:
                Cam_name = self.cameras_info[cam]["Name"]
                Cam_IpAddress = self.cameras_info[cam]["IpAddress"]
                try:
                    cam_status = py.InstantCamera(self.tlf.CreateDevice(Cam_IpAddress))
                    if cam_status:
                        status_result[Cam_name] = True
                except:
                    raise GFAError("No Camera")

        now2 = time.time()
        self.logger.info("Func status done")
        self.logger.info(f"process time: {now2-now1}")

        return status_result


    def ready(self, CamNum: int):
        """ready to open and close

        Parameters
        ----------
        CamNum
            Camera number
        """

        now1 = time.time()
        self.logger.info("Func ready start")
        cam_ready_dict = {}

        try:
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

        except:
            self.logger.error(f"No Camera {CamNum}")
            self.logger.error(f"Camera: {self.cameras_info.keys()}")
            raise GFACamNumError(f"No Camera {CamNum}")

        now2 = time.time()
        self.logger.info("Func ready done")
        self.logger.info(f"process time: {now2-now1}")

        return cam_ready

    def open(self, ready):
        """Open the camera connection

        Parameters
        ----------
        ready
            Connected camera instance
        """

        now1 = time.time()
        self.logger.info("Func open start")

        if ready:
            ready.Open()
        else:
            self.logger.error("No Camera for Open")
            raise GFAError("No Camera for Open")

        now2 = time.time()
        self.logger.info("Func open done")
        self.logger.info(f"process time: {now2-now1}")

    def close(self, ready):
        """Close the camera connection

        Parameters
        ----------
        ready
            Connected camera instance
        """

        now1 = time.time()
        self.logger.info("Func close start")

        if ready:
            ready.Close()
        else:
            self.logger.error("No Camera for Close")
            raise GFAError("No Camera for Close")

        now2 = time.time()
        self.logger.info("Func close done")
        self.logger.info(f"process time: {now2-now1}")

    def grab(self, ready, CamNum, ExpTime):
        """Grab the image

        Parameters
        ----------
        ready
            Connected camera instance
        CamNum
            Camera number
        ExpTime
            Exposure time (sec)
        """
        
        now1 = time.time()
        self.logger.info("Func grab start")
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)

        if ready:
            cam = ready
            ExpTime_microsec = ExpTime * 1000000
            cam.ExposureTime.SetValue(ExpTime_microsec)
            res = cam.GrabOne(100000)
            img = res.GetArray()
            plt.imshow(img)
            plt.savefig(f"./img_saved/{formatted}_cam{CamNum}_img.png")
        else:
            self.logger.error("No Camera for grab")
            raise GFAError("No Camera for grab")

        now2 = time.time()
        self.logger.info("Func grab done")
        self.logger.info(f"Exposure time: {ExpTime}")
        self.logger.info(f"process time: {now2-now1}")
