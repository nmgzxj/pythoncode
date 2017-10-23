#!/usr/bin/env python
# coding:utf-8
import urllib2
import http.client
import re
import Tkinter
from ScrolledText import ScrolledText
import lxml.html


root = Tkinter.Tk()
root.title('大众论坛--临沂')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 布局
varl = Tkinter.StringVar()
printTxt = ''

url='http://bbs.dzwww.com/forum.php?mod=forumdisplay&fid=138'
html = urllib2.urlopen(url).read().decode('utf-8', 'ignore')

doc = lxml.html.fromstring(html)

#print html
contents =  doc.xpath('//tr/th/a[3]')  #re.findall(reg, html)

print type(contents)


def start():
    for link in contents:
        print link.text
        print link.attrib['href']
        # for i in link:
        #     print i
        if link.text == u'预览':
            continue
        text.insert(Tkinter.END,  link.text+' http://bbs.dzwww.com/'+link.attrib['href']+'\n\n')



button = Tkinter.Button(root, text='开始爬取', font=('微软雅黑', 10), command = start)
button.grid()


label = Tkinter.Label(root, font=('微软雅黑', 10), fg='blue', textvariable = varl)
label.grid()
varl.set('爬虫已准备...')
root.mainloop()  # 进入主事件循环