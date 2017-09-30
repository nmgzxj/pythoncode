#coding:utf8
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

session = requests.Session()
url="http://www.cb.com.cn/xinqiche/"
#s=session.get(url)
#print(s.text)

import urllib2
import sys
import chardet
import time

req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
html = content.decode(infoencode,'ignore').encode(typeEncode)
#print html

web_name = '未设置'
title = '未设置'
anthor = '未设置'
url = '未设置'
source = '未设置'
content = '未设置'
pub_time = '1970-1-1 0:0:0'
crawl_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
keywords = '未设置'
description = '未设置'
root_url = 'http://www.cb.com.cn'


def crawl_content(url1):
    url1 = root_url + url1
    print '================== '+url1+' ==============================='
    req1 = urllib2.Request(url1)
    content1 = urllib2.urlopen(req1).read()
    html1 = content1.decode(infoencode, 'ignore').encode(typeEncode)
    text = BeautifulSoup(html1)
    web_name = '中国经营报'
    title = text.title
    anthor = text.findAll('div',{"class":"contentmes auto"})
    url = url1
    source = text.findAll('div',{"class":"contentmes auto"})
    content = text.findAll('div',{"class":"contenttext auto"})

    print 'web_name='+web_name
    print 'title='
    print text.title
    print 'anthor='
    print anthor.decode(infoencode, 'ignore').encode(typeEncode)
    print 'url='+url
    print 'source='+source
    print 'content='+content
    print 'pub_time='+pub_time
    print 'crawl_time='+crawl_time
    print 'keywords='+keywords
    print 'description='+description
    return text.title

soup = BeautifulSoup(html)
print soup.title
#print soup.dl.dt.a
for link in soup.findAll('dl',{"class":"listdlr"}):
#     print(link.get('href'))
#     print(link.dt.a.get('href'))
#     print(link.dt.a.string)
    print(crawl_content(link.dt.a.get('href')))


#print soup.get_text()