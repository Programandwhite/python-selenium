#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import unittest,time,logging
from selenium import webdriver
from common.browsersManager import browsersManager
from common.log import logger



class baseCase(unittest.TestCase,logger):

    def setUp(self):
        self.driver=browsersManager("Chrome")
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(10)
        self.logger = logger("path", consoleLevel=logging.INFO, logFile="logger.txt", fileLevel=logging.DEBUG)
        self.logger.info("浏览器启动ing")


    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
