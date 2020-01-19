from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import xlsxwriter
html = urlopen('http://www.isccc.gov.cn/zxyw/fwzzrz/fwzzrzzscx/09/870940.shtml')
bs = BeautifulSoup(html,'lxml')
trs = bs.find_all('tr')
ulist = []
for tr in trs:
    ui = []
    for td in tr:
        ui.append(td.string)
    ulist.append(ui)

for u in ulist:
    for n in u:
        if n == '\n':
            u.remove(n)

workbook = xlsxwriter.Workbook('信息系统灾难备份与恢复服务资质认证获证组织名单.xls')
sheet = workbook.add_worksheet()
i = 0
for u in ulist:
    for j in range(len(u)):
        sheet.write(i,j,u[j])
    i = i + 1
workbook.close()






