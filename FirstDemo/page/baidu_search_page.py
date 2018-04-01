#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang

from common.baseMethod import Base

class baidu_search_page(Base):
    search_box=("id","kw")
    button=("id","su")

    def searchBox(self,vaule):
        '''向搜索框内发送文本'''
        self.sendkeys(self.search_box,vaule)

    def buttonSearch(self):
        '''点击百度一下按钮'''
        self.click(self.button)


# if __name__ == "__main__":
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#
#     driver.get("http://www.baidu.com")
#     search = baidu_search_page(driver)
#     search.login()







