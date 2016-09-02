#!/usr/bin/env python3 
import urllib.request
import http.client
import bs4
import re
import sys
import importlib
importlib.reload(sys)

page_num=10
url='http://tieba.baidu.com/f?ie=utf-8&kw=%E6%B2%A7%E5%B7%9E'


page_num=page_num+1
pattern=re.compile('post_content_[0-9]{1,}')
def IsRightId(id):
    group=pattern.findall(id)
    if group:
        return group
    else:
        return None
def GetEveryPage(url,file):
    try:
        rep=urllib.request.urlopen(url)
    except http.client.HTTPException as e:
        print(repr(e))
    else:
        rep_utf=rep.read().decode('utf-8')
        soup=bs4.BeautifulSoup(rep_utf)
        for a in soup.find_all('a',{"class":"j_th_tit"}):
                file.write('"'+a.get_text()+'",http://tieba.baidu.com'+a.attrs['href']+'\r\n')
                print(a.get_text()+',http://tieba.baidu.com'+a.attrs['href']+'\n')

file_tieba=open('cangzhouba.csv','w+',encoding='utf-8')
for i in range(1,page_num):
    url_everypage=url+'&pn='+str((i-1)*50)
    print('Processing page:'+url+'&pn='+str(i)+'/'+str(page_num)+'......')
    GetEveryPage(url_everypage,file_tieba)
print('Finished!')
file_tieba.close()
   
