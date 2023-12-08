#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mmingyeong@kasi.re.kr)
# @Date: 2023-12-07
# @Filename: gfa_log.ipynb

import os
import logging

# Logger 정의
class GFA_Logger:
    def __init__(self, file):
        self.logger = logging.getLogger("GFA_Logger")
        self.file_name = os.path.basename(file)

        if len(self.logger.handlers) == 0:
            # StreamHandler
            formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            self.logger.addHandler(stream_handler)
            stream_handler.setLevel(logging.ERROR)
            
            # FileHandler
            log_name = self.file_name.rstrip('.py')
            file_handler = logging.FileHandler(f'./{log_name}.log')
            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            file_handler.setLevel(logging.INFO)

    def info(self, value):
        self.logger.info("%s (at %s)" % (str(value), self.file_name))

    def error(self, value):
        self.logger.error("%s (at %s)" % (str(value), self.file_name))
       
# Logger
#Log = GFA_Logger(__file__)
#Log.info("Info Test")
#Log.info("Error Test")
