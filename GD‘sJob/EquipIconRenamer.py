import os
import xlwt
from xlwt import *

# 枚举dirPath目录下的所有文件
fd = "G:\emmmm\主角装备新增"

site = ["头","衣","鞋","项"]
suitnum = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15"]
quality = ["白","蓝","紫","橙","红"]

def Initialize():
    doc_site = {}
    for x in site:
        for y in suitnum:
            doc_site.update({x:y})
            print(doc_site.items())

Initialize()


def findFileName(fileDir):
     # 查找F:\aaa 目录下
    filelist = os.listdir(fd)
    total_num = len(filelist)
    print(total_num)

    for item in filelist:
        print(item)
        if item.find('红'):
            print("红")

#findFileName(fd)



