#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:MeiFen
# 基础类:接口测试的封装(requests api请求)


import requests
import json
import logging


class testApi():

    def requestsApi(self, method,url,data,cookies=None):
        """
        自定义一个接口测试的方法
        :param method: 请求类型
        :param url: 地址
        :param data: 数据
        :param headers: 请求头
        """
        global result
        #判断发起的是get请求还是post请求
        if (method == "get" or "GET"):
            try:
                result = requests.get(url, params=data,cookies=cookies)
            except Exception as e:
                logging.error("发起get请求报错，错误是：", e)
                print("发起get请求报错，错误是：", e)
        elif (method == "post" or "POST"):
            try:
                result = requests.post(url, params=data,cookies=cookies)
            except Exception as e:
                logging.error("发起post请求报错，错误是：", e)
                print("发起post请求报错，错误是：", e)
        # elif (method == "put"):
            # results = requests.put(url, params=data, headers=headers)
        # elif (method == "delete"):
            # results = requests.delete(url, headers=headers)
        # elif (method == "patch"):
            # results == requests.patch(url, params=data, headers=headers)
        # elif (method == "options"):
            # results == requests.options(url, headers=headers)
        # json_data = results.json()   # 获取返回信息的json数据
        return result

    def requestsApid(self,method,url,data):
        """
        自定义一个接口测试的方法
        :param method: 请求类型
        :param url: 地址
        :param data: 数据
        :param headers: 请求头
        """
        global result
        #判断发起的是get请求还是post请求
        if (method == "get" or "GET"):
            try:
                result = requests.get(url, params=data)
            except Exception as e:
                logging.error("发起get请求报错，错误是：", e)
                print("发起get请求报错，错误是：", e)
        elif (method == "post" or "POST"):
            try:
                result = requests.post(url, params=data)
            except Exception as e:
                logging.error("发起post请求报错，错误是：", e)
                print("发起post请求报错，错误是：", e)
        # elif (method == "put"):
            # results = requests.put(url, params=data, headers=headers)
        # elif (method == "delete"):
            # results = requests.delete(url, headers=headers)
        # elif (method == "patch"):
            # results == requests.patch(url, params=data, headers=headers)
        # elif (method == "options"):
            # results == requests.options(url, headers=headers)
        # json_data = results.json()   # 获取返回信息的json数据
        return result

"""
from   read_excel import readData
import  log
import time
import common
#创建日志目录
com = common.commonUtils()
logtime = time.strftime("%H%M%S")
log_path=com.getPath("logs")  #生成的日志目录在当前Folder下
#生成日志文件
log.logfile(log_path,logtime)

#获取excel数据
excel = readData(r'D:\python_apitest\src\data\data.xlsx')
url = excel.getUrl()[0]
method = excel.getMethod()[0]
data = excel.getData()[0]
requestdata_dict =eval(data)
#设置类对象
api=testApi()
#调用类方法
result=api.requestsApid(method,url,requestdata_dict)
print (result.url)
print (result.json())

#调用日志
logging.info(result.json())
"""

"""
requestdata = {'username': 'humeifen', 'password': '123456aa'}
print (type(requestdata))
print (requestdata)
#设置类对象
api=testApi()
#调用类方法
result=api.requestsApid("post","http://10.10.42.240:9980/login/submitLogin",requestdata)
print (result.url)
print (result.json())

loginCookies=result.cookies
print (loginCookies)


#新增立项
requestdata2 = {'id': '', 'busiType': '[{"id":"1","busiTypeId":"1812b53ddb4f458d93937a56d37214c2","visiblePersonId":"900a8fef-3663-11e9-9e8c-2c44fd254fe9","status":"2","proBusiType":"传播-广告购买","proNumber":"-CBGGGM","visiblePreson":"胡梅芬"}]', 'annex': '[]', 'customerName': '', 'customerId': '00abbae0a6894e20a826a15b5ca46f1c', 'proYear': '2019', 'proMonth': '4', 'proName': 'hutest001', 'proNumber': 'ABCD'}
print (type(requestdata2))
print (requestdata2)
#api=testApi()
#调用类方法
r=api.requestsApi("post","http://10.10.42.240:9980/project/addAndUpdateProjectSave",requestdata2,loginCookies)
print (r.url)

print (r.json())
"""




