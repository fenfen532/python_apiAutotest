#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:MeiFen
#主程序

from HTMLTestRunner import HTMLTestRunner
import time
import unittest
import os
import common.common as common
import common.log as log

#创建日志目录
def log_track():
    try:
        com = common.commonUtils()
        logtime = time.strftime("%H%M%S")
        # 生成的日志目录在当前Folder下
        log_path=com.getPath("logs")
        #生成日志文件
        log.logfile(log_path,logtime)
    except Exception as e:
        print("生成日志文件error:",e)


#创建report目录
com = common.commonUtils()
report_path=com.getReportPath("report")


path = os.getcwd()
print (path)
# 获取测试文件下的测试用例
def suite():
    dir_case = unittest.defaultTestLoader.discover(
        path,
        pattern='test*.py',
        top_level_dir=None
    )
    return dir_case

# 获取当前时间
def getNowTime():
    return time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))


def runAutomation():
    log_track()
    filename = path + r'\report\Report_' + getNowTime() + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'接口自动化测试报告',
        description=u'接口自动化测试报告详细的信息'
    )
    runner.run(suite())


if __name__ == '__main__':
    runAutomation()
