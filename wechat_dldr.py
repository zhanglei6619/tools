# -*- coding:utf-8 -*-
import re
import pandas as pd
import requests
#from time import time
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
# 读取动态页面链接；该方法未完续待，问题在于读不到element
# def getHTMLText(url):
#     try:
#         driver = webdriver.Chrome(r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe')
#         r = driver.get('http://www.baidu.com')
#         r.raise_for_status()
#         return r.text
#     except:
#         return ""

#事先采用读取八爪鱼下载好的文章链接。字符集要统一成utf8才行
def getArticles(type_select, fpath):
    i = 0
    ulist = pd.read_excel('E:\\data\\articles\\' + type_select + '.xlsx', header=0, index_col=None, encoding='utf8')
    while i < ulist.iloc[:,0].size:
        try:
            url = ulist[u'链接'][i]
            html = requests.get(url)
            content = html.text
            with open(fpath + ulist[u'标题'][i] +'.html', 'wb') as f:
                f.write(content.encode('utf8'))
                f.close()
                print("文件保存成功！")
            i = i + 1
        except:
            i = i + 1
            continue

if __name__ == '__main__':
    article_type = ['Finance','IT','thoughts','tech','teaching']
    for i in article_type:
        print(i)
        output_file = 'E://data//articles//' + i + '//'
        getArticles(i, output_file)




