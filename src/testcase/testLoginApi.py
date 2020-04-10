#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:MeiFen
# 业务接口测试


import sys, os

   
sys.path.append('../')
from common.read_excel import readData
from common.testApi import testApi
from common.readConfig import readConfig

import unittest
import json
import logging


# 生成日志文件(本程序单独执行时可使用)
# import common.log as log
# log.logfile(),/


class testLoginApi(unittest.TestCase):
    def setUp(self):
        print('\n')

    def test_LoginApi(self):
        # 测试login的接口
        logging.info('------testLoginApi------.')

        # 获取当前执行(调用)程序的当前目录,本程序执行，当前目录为D:\python_apitest\src\testcase；runtest.py执行时当前目录为：D:\python_apitest\src
        root_dir = os.path.abspath('.')
        if "testcase" in root_dir:
            data_path = "../data/data.xlsx"
            configpath="../config/config.conf"
        else:
            data_path = "data/data.xlsx"
            configpath="config/config.conf"

        # 获取参数化数据
        excel = readData(r'%s' % data_path)
        # excel = readData(r'D:\python_test\mdp_test3\config\data.xlsx')
        row = excel.getRows()
        url = excel.getUrl()
        method = excel.getMethod()
        headers = excel.getHeaders()
        data = excel.getData()
        exceptcode = excel.getCode()  # 参数data里的预期结果

        #读取配置文件
        #readconfig=readConfig("../config/config.conf")  #在当前程序调用时，使用这个
        readconfig=readConfig(configpath)
        #print (readconfig)
        baseurl=readconfig.get_http("baseurl")
        port=readconfig.get_http("port")
        #print (baseurl,port)


        # 一行一行参数化数据执行
        for i in range(0, row - 1):

            if port=="":
                requesturl=baseurl+url[i]
            else:
                requesturl=baseurl+":"+port+url[i]
            print (requesturl)
            try:
                api = testApi()
                result = api.requestsApid(method[i],requesturl,eval(data[i]))  # 调用requestApid的接口
                print("请求url：%s" % result.url)  # 打印请求的url
                logging.info("请求url：%s" % result.url)
                apijson = result.json()  # 获取请求返回实际结果的json串值
                # print (apijson)
                # print (type(apijson))
                logging.info("请求返回值的json串值:%s" % apijson)

                # 获取返回实际结果json串值的state值
                actualstate = apijson["state"]
                actualmessage = apijson["message"]
            except Exception as e:
                print(e)
                logging.error(e)
            # print (actualcode)
            # print (eval(exceptcode[i]))
            # print (type(eval(exceptcode[i])))
            exceptstate = eval(exceptcode[i])["state"]
            exceptmessage = eval(exceptcode[i])["message"]
            # print (actualstate,type(actualstate))
            # print (exceptstate,type(exceptstate))

            if (actualstate == exceptstate):
                logging.info('检查结果：testLoginApi True,-实际state:%s，预期state:%s.' % (actualstate, exceptstate))
                print('检查结果：testLoginApi True,-实际state:%s，预期state:%s.' % (actualstate, exceptstate))
            else:
                logging.error('检查结果：testLoginApi False,-[实际state:%s,实际message：%s] ,[预期state:%s,预期message:%s].' % (
                actualstate, actualmessage, exceptstate, exceptmessage))
                print('检查结果：testLoginApi False,-[实际state:%s,实际message：%s] ,[预期state:%s,预期message:%s].' % (
                actualstate, actualmessage, exceptstate, exceptmessage))
            self.assertEqual(actualstate, exceptstate, "两者的值不相等")

    def tearDown(self):
        pass

# 可单独用执行
if __name__ == '__main__':
    unittest.main()
