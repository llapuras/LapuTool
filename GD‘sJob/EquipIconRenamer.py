import os
import xlwt
from xlwt import *

# ö��dirPathĿ¼�µ������ļ�
fd = "G:\emmmm\����װ������"

site = ["ͷ","��","Ь","��"]
suitnum = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15"]
quality = ["��","��","��","��","��"]

def Initialize():
    doc_site = {}
    for x in site:
        for y in suitnum:
            doc_site.update({x:y})
            print(doc_site.items())

Initialize()


def findFileName(fileDir):
     # ����F:\aaa Ŀ¼��
    filelist = os.listdir(fd)
    total_num = len(filelist)
    print(total_num)

    for item in filelist:
        print(item)
        if item.find('��'):
            print("��")

#findFileName(fd)



