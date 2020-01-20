from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import xlsxwriter
html = urlopen('https://www.sec-un.org/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BF%A1%E6%81%AF%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8%E4%B8%93%E7%94%A8%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E8%AE%B8%E5%8F%AF%E8%AF%81%E5%AE%8C%E5%85%A8%E7%9B%AE%E5%BD%95/https://www.sec-un.org/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BF%A1%E6%81%AF%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8%E4%B8%93%E7%94%A8%E4%BA%A7%E5%93%81%E9%94%80%E5%94%AE%E8%AE%B8%E5%8F%AF%E8%AF%81%E5%AE%8C%E5%85%A8%E7%9B%AE%E5%BD%95/')
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

workbook = xlsxwriter.Workbook('test.xls')
sheet = workbook.add_worksheet()
i = 0
for u in ulist:
    for j in range(len(u)):
        sheet.write(i,j,u[j])
    i = i + 1
workbook.close()






