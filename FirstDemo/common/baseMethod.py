#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os

class Base(object):

    def __init__(self,driver):
        '''启动浏览器参数化'''
        self.driver=driver

#常用操作
    def open(self,url):
        '''打开地址，并将浏览器最大化'''
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self,*locator):
        '''定位元素，参数locator是元组类型'''
        try:
            element=WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(*locator))
            return element
        except:
            print("没有找到此%s元素"%locator)

    def find_elements(self, locator):
        '''定位一组元素'''
        elements = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click(self,locator):
        '''点击操作'''
        element=self.find_element(locator)
        element.click()

    def sendkeys(self,locator,vaule,is_clear=True):
        '''发送文本'''
        try:
            element = self.find_element(locator)
            if is_clear:
                element.clear()
                element.send_keys(vaule)
        except:
            print("发送文本失败")

    def get_screenshot(self,image_path):
        '''获取屏幕截图'''
        nowtime=time.strftime("%Y-%m-%d %H_%M_%S")
        try:
            fpath=os.path.join(image_path,nowtime+".jpg")
            self.driver.get_screenshot_as_file(fpath)
            print("screenshot ：%s" % fpath)
        except Exception as a:
            print("Error! screenshot：%s" % a)
#一般操作
    def get_screenasbase64(self):
        '''以base64格式返回屏幕截图，常用在html中'''
        return self.driver.get_screenshot_as_base64()










# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     first_driver=Base(driver)
#     first_driver.open("http://www.baidu.com")
#     serach_locator=("id","kw")
#     first_driver.sendkeys(serach_locator,"FirstDemo")





