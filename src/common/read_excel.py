#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Meifen
# 基础包:excel读取数据的封装

import xlrd


class readData():
    def __init__(self, path):
        self.path = path

    def getSheet(self):
        # 获取sheet索引(0代表第1个sheet)
        data = xlrd.open_workbook(self.path)
        sheet = data.sheet_by_index(0)
        # sheet=data.sheets()[0]
        return sheet

    def getRows(self):
        # 获取行数
        row = self.getSheet().nrows
        return row

    def getCols(self):
        # 获取列数
        col = self.getSheet().ncols
        return col

    # 以下是分别获取每1列的数值
    def getName(self):
        TestName = []
        for i in range(1, self.getRows()):
            TestName.append(self.getSheet().cell_value(i, 0))
        return TestName

    def getUrl(self):
        TestUrl = []
        for i in range(1, self.getRows()):
            TestUrl.append(self.getSheet().cell_value(i, 1))
        return TestUrl

    def getData(self):
        RequestData = []
        for i in range(1, self.getRows()):
            RequestData.append(self.getSheet().cell_value(i, 2))
        return RequestData

    def getMethod(self):
        TestMethod = []
        for i in range(1, self.getRows()):
            TestMethod.append(self.getSheet().cell_value(i, 3))
        return TestMethod

    def getHeaders(self):
        TestHeaders = []
        for i in range(1, self.getRows()):
            TestHeaders.append(self.getSheet().cell_value(i, 4))
        return TestHeaders

    def getCode(self):
        TestCode = []
        for i in range(1, self.getRows()):
            TestCode.append(self.getSheet().cell_value(i, 5))
        return TestCode

    """
    def get_content(self):
       sheet=self.getSheet()
       row=self.getRows()
       col=self.getCols()
       :获取表格中内容
       :param sheet: sheet
       :param row: 行
       :param col: 列
       :return:    
       return sheet.cell_value(row, col)
    """


"""
#获取类readData的对象
re=readData(r"../config/data.xlsx")
#对象调用方法
print (re.getSheet())
print (re.getRows())
print (re.getCols())
print (re.getName())
print (re.getData())
print (re.getMethod())
print (re.getHeaders())
print (re.getCode())
"""

