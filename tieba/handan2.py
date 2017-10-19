#!/usr/bin/env python
# coding:utf-8
import urllib2
import http.client
import re
import Tkinter
from ScrolledText import ScrolledText

root = Tkinter.Tk()
root.title('百度贴吧--邯郸')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 布局
varl = Tkinter.StringVar()
printTxt = ''

page_num=5
url='http://tieba.baidu.com/f?ie=utf-8&kw=%E9%82%AF%E9%83%B8'
reg = re.compile('<a href="(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">')
req = urllib2.Request(url)

page_num=page_num+1
pattern=re.compile('post_content_[0-9]{1,}')


def IsRightId(id):
    group=pattern.findall(id)
    if group:
        return group
    else:
        return None


def GetEveryPage(url):
    try:
        rep=urllib2.urlopen(url)
    except http.client.HTTPException as e:
        print 'exception' #(repr(e))
    else:
        rep_utf=rep.read().decode('utf-8')
        # print rep_utf
        for a in reg.findall(rep_utf):
            printTxt = a[1]+',http://tieba.baidu.com'+a[0]+'\n'
            text.insert(Tkinter.END, printTxt)

def start():
    for i in range(1,page_num):
        url_everypage=url+'&pn='+str((i-1)*50)
        printTxt = ('正在抓取第'+str(i)+'页......\n')
        text.insert(Tkinter.END, printTxt)
        GetEveryPage(url_everypage)
        text.insert(Tkinter.END, '\n\n')
    text.insert(Tkinter.END, 'finished!')
        # break


button = Tkinter.Button(root, text='开始爬取', font=('微软雅黑', 10), command = start)
button.grid()


label = Tkinter.Label(root, font=('微软雅黑', 10), fg='blue', textvariable = varl)
label.grid()
varl.set('爬虫已准备...')
root.mainloop()  # 进入主事件循环
