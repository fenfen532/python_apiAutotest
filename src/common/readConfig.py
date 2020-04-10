import os
import configparser

class readConfig():
    def __init__(self,configPath):
        self.configPath=configPath    

    def get_http(self, name):
        try:
            self.cf=configparser.ConfigParser()
            self.cf.read(self.configPath)
            value = self.cf.get("HTTP", name)
            return value
        except Exception as e:
            print ("未找到配置文件，无法读取%s值"%name,e)
        


"""
#读取配置文件
readconfig=readConfig("../config/config.ini")
#print (readconfig)
baseurl=readconfig.get_http("baseurl")
port=readconfig.get_http("port")
#print (baseurl,port)
"""
