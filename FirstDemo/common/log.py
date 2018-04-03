#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author:YangShuang
import logging

class logger():
    def __init__(self,path,consoleLevel,logFile,fileLevel):
        #创建logger对象
        self.logger=logging.getLogger(path)
        #设置默认log级别
        self.logger.setLevel(logging.DEBUG)
        #定义输出handler的格式
        fmt=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s -%(message)s")


        #设置控制台日志
        cg=logging.StreamHandler()
        #配置logger
        cg.setFormatter(fmt)
        cg.setLevel(consoleLevel)


        #设置文件日志
        fg=logging.FileHandler(logFile,"a",encoding="utf-8")
        fg.setFormatter(fmt)
        fg.setLevel(fileLevel)

        #给logger添加handler
        self.logger.addHandler(cg)
        self.logger.addHandler(fg)

    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)
    def warning(self,message):
        self.logger.warning(message)
    def error(self,message):
        self.logger.error(message)
    def critical(self,message):
        self.logger.critical(message)
if __name__=="__main__":
    logger=logger("path",consoleLevel=logging.INFO,logFile="logger.txt",fileLevel=logging.DEBUG)
    #应用日志
    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')


