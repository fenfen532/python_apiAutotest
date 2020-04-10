#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: MeiFen
# 基础包: 日志服务


import logging
import logging.handlers
import time,os

def logfile(log_path,time):

    # logging对象,设置从那个等级开始提示
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    #日志文件
    logfile = os.path.join(log_path,"log%s.log") %time

    #print (logfile)
    #日志文件
    #logtime=time.strftime("%H%M%S")
    #logfile="apilog%s.log"%logtime

    #创建handler
    time_handler=logging.handlers.TimedRotatingFileHandler(logfile,'D')
    #handler设置日志格式
    fmt=logging.Formatter("%(asctime)s - %(name)s -%(module)s- %(levelname)s - %(message)s","%Y-%m-%d %H:%M:%S")
    time_handler.setFormatter(fmt)
    #添加刚设置的handler
    logger.addHandler(time_handler)


"""
#调用
import common
com = common.commonUtils()
time = time.strftime("%H%M%S")
log_path=com.getPath("logs")   #生成的日志文件在当前Folder下
logfile(log_path,time)
logging.info("-----test---我再测试哈-")
"""
