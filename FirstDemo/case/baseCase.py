#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import unittest,time
from selenium import webdriver
from common.browsersManager import browsersManager



class baseCase(unittest.TestCase):

    def setUp(self):
        self.driver=browsersManager("Chrome")
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()
