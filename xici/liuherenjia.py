#!/usr/bin/env python
# coding:utf-8
import urllib2
import http.client
import re
import Tkinter
from ScrolledText import ScrolledText

root = Tkinter.Tk()
root.title('西祠胡同--六合人家')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 布局
varl = Tkinter.StringVar()
printTxt = ''

page_num=5
url='http://www.xici.net/b583561/board.asp'
reg = re.compile('{"aDocs_i_0":(.*?),"aDocs_i_1":"(.*?)","aDocs_i_10":(.*?),"aDocs_i_12":(.*?),"aDocs_i_13":(.*?),'
                 '"aDocs_i_14":(.*?),"aDocs_i_16":(.*?),"aDocs_i_18":"(.*?)","aDocs_i_19":(.*?),"aDocs_i_2":(.*?),'
                 '"aDocs_i_3":"(.*?)","aDocs_i_5":(.*?),"aDocs_i_8":(.*?),"Docs_i_15":(.*?),"lDocPageSize":(.*?),'
                 '"lTotalPage":(.*?),"m":(.*?),"response_20_i":"(.*?)","ShortDate":"(.*?)","visited":(.*?)}')
html = urllib2.urlopen(url).read().decode('gb2312', 'ignore')

#print html
contents =  re.findall(reg, html)


def start():
    for link in contents:
        # for i in link:
        #     print i
        text.insert(Tkinter.END,  link[1]+' '+link[7]+' '+link[18]+'\n\n')


button = Tkinter.Button(root, text='开始爬取', font=('微软雅黑', 10), command = start)
button.grid()


label = Tkinter.Label(root, font=('微软雅黑', 10), fg='blue', textvariable = varl)
label.grid()
varl.set('爬虫已准备...')
root.mainloop()  # 进入主事件循环