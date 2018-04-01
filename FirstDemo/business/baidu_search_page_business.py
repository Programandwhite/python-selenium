#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
from page.baidu_search_page import baidu_search_page

class baidu_search_page_business(baidu_search_page):
    def baiduSearch(self,vaule):
        self.searchBox(vaule)
        self.buttonSearch()