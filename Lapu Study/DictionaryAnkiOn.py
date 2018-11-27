import urllib.request
from bs4 import BeautifulSoup
import xlrd
import xlwt



p = r'E:\出国啊烧酒\GRE\李斯特01.xlsx'
root_url = 'https://www.vocabulary.com/dictionary/'

def GetWords(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(u'Sheet1')
    cww = table.col_values(0)
    return cww


def writein(list, worksheet, col):
    i = 0
    for content in list:
        worksheet.write(i, col, content)
        i += 1


def lookup(path, filename):

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    short = []
    long = []

    wl = GetWords(path)
    for word in wl:
        url = root_url + word  # 拼接URL
        response = urllib.request.urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html, 'lxml')

        s0 = soup.find(class_='short')
        l0 = soup.find(class_='long')

        if s0 is None:
            s = "-"
            l = "-"
        else:
            s = ""
            l = ""
            for i in s0.contents:
                s += str(i).replace("<i>", "").replace("</i>", "")
            for j in l0.contents:
                l += str(j).replace("<i>", "").replace("</i>", "")
        print(word)
        print(s)
        print(l)
        short.append(s)
        long.append(l)

    writein(wl, worksheet, 0)
    writein(short, worksheet, 1)
    writein(long, worksheet, 2)
    workbook.save(filename)

lookup(p, "List001.xlsx")
