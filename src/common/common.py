#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MeiFen
# 基础包：共用方法


import re, logging
import logging.handlers
import time, os, datetime


class commonUtils():
    def pathExist(self, filepath):
        if os.path.exists(filepath) is False:
            os.mkdir(filepath)

    # get report path.
    def getPath(self, path):
        preset = commonUtils()
        filepath = "%s" % path  # path是看调用的程序目录在哪
        preset.pathExist(filepath)
        filepath = os.path.join(filepath, time.strftime("%Y%m%d"))
        preset.pathExist(filepath)
        return filepath

    def getReportPath(self, path):
        preset = commonUtils()
        filepath = "%s" % path
        preset.pathExist(filepath)
        return filepath

    # get the date for report.
    def getTime(self):
        return time.strftime("%H%M%S")

    def createLogFile(self, path, logName, logtime):
        # 日志文件
        logfile = os.path.join(path, logName + "%s.log") % logtime
        # 日志对象
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        # logger.setLevel(logging.DEBUG)
        time_handler = logging.handlers.TimedRotatingFileHandler(logfile, 'D')
        # handler设置日志格式
        fmt = logging.Formatter("%(asctime)s - %(name)s -%(module)s- %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        time_handler.setFormatter(fmt)
        # 添加刚设置的handler
        logger.addHandler(time_handler)
        # return logger

    def createTestReport(self, path, reportName, date):
        report = os.path.join(path, reportName + "%s.html") % date
        return report


"""
com = commonUtils()
date = com.getReportDate()
report_path  = com.getReportPath()
#html_report = com.createTestReport(report_path, 'testReport', date)
com.createLogFile(report_path, 'log', date)
"""

"""
com = commonUtils()
logtime = com.getReportTime()
log_path  = com.getPath("logs")
com.createLogFile(log_path, 'log', logtime)
logging.info('------testLoginApi------.')
"""
