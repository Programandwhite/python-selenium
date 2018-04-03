#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from business.baidu_search_page_business import baidu_search_page_business
from case.baseCase import baseCase
import ddt
from common.read_excel import read_Excel

filePath = r"E:\pyworkpase\FirstDemo\testdata.xlsx"
sheetName = "Sheet1"
data = read_Excel(filePath, sheetName)
testData = data.dict_data()
print(testData)

@ddt.ddt
class baidu_search_page_case(baseCase):

    # def test_search_baidu01(self):
    #     self.searchDriver = baidu_search_page_business(self.driver)
    #     self.searchDriver.baiduSearch("python selenium")

    def search_baidu02(self,vaule):
        self.searchDriver=baidu_search_page_business(self.driver)
        self.searchDriver.baiduSearch(vaule)

    @ddt.data(*testData)
    def test_search_baidu02(self, data):
        '''百度搜索案例'''
        print("当前测试数据%s" % data)

        # 调用登录方法
        self.search_baidu02(data["value"])
        self.logger.info("调试成功")




