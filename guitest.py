# -*- coding:utf8 -*-
# from tkinter import *  第一步
# 下载百思不得姐的前10个视频
import os, getpass, time
import Tkinter
from ScrolledText import ScrolledText
import urllib, requests, re, threading, time

root = Tkinter.Tk()
root.title('The first Python GUI')
text = ScrolledText(root, font=('微软雅黑', 10))
text.grid()  # 布局
varl = Tkinter.StringVar()



url_name = []
a = 1 #页数
def get():
    global a
    hd = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0','Referer':'http://www.budejie.com/'}
    url = 'http://www.budejie.com/video/'+str(a)
    varl.set('已经获取到第%s页的视频。'%(a))
    html = requests.get(url,headers = hd).text
    #print html
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)', re.S)
    url_contents = re.findall(url_content,html)
    # print url_contents
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'
        url_items = re.findall(url_reg,i)
        #print url_items
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}?.html">(.*?)</a>', re.S)
            name_items = re.findall(name_reg, i)
            #print name_items[0]
            for i,k in zip(name_items, url_items):
                url_name.append([i,k])
                print i,k
    return url_name

id = 1 #视频个数

def write():
    global id
    while id < 10:
        url_name = get()
        for i in url_name:
            urllib.urlretrieve(i[1],'/users/zhangxianjin/Downloads/video/%s.mp4'% (i[0])) #下载.decode('utf-8').encode('gbk')
            text.insert(Tkinter.END, str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            url_name.pop(0)
            id += 1
    varl.set('蘑菇头：视频下载完毕。')

def start():
    th = threading.Thread(target=write)
    th.start()

b = get()

button = Tkinter.Button(root, text='开始爬取', font=('微软雅黑', 10), command = start)
button.grid()


label = Tkinter.Label(root, font=('微软雅黑', 10), fg='blue', textvariable = varl)
label.grid()
varl.set('爬虫已准备...')
root.mainloop()  # 进入主事件循环

