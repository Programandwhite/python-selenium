#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from selenium import webdriver

#def browsersManager(browser="Chrome"):
def browsersManager(browser):
    '''打开浏览器函数，Firefox、Chrome、IE'''
    try:
        if browser == "Firefox":
            driver = webdriver.Firefox()
            return driver
        elif browser == "Chrome":
                driver = webdriver.Chrome()
                return driver
        elif browser == "IE":
                driver = webdriver.Ie()
                return driver
        else:
            print("没有此类型浏览器")
    except Exception as msg:
        print("%s" % msg)