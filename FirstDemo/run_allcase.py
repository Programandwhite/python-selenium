#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import unittest,os,time
from common import HTMLTestRunner

# 当前脚本所在文件绝对路径,其实就是项目目录
absolute_path = os.path.dirname(os.path.realpath(__file__))

def all_case(caseName="case", rule="*_case.py"):
    '''加载所有的测试用例'''
    case_path = os.path.join(absolute_path, caseName)  # case文件夹，拼接路径

    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("测试用例路径:%s"%case_path)
    testcase = unittest.TestSuite()
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    # return discover
    for test_suite in discover:
        for test_case in test_suite:
            # 添加用例到 testcase
            testcase.addTests(test_case)
    print(testcase)
    return testcase

def run_case(all_case, reportName="report"):
    '''执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = os.path.join(absolute_path, reportName)  # HTMLreport文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, "result%s.html"%now)
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

if __name__ == "__main__":
    all_case = all_case()
    run_case(all_case)

