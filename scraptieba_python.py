import urllib.request
import http.client
import bs4
import re

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
        for div in soup.find_all('a',{"class":"j_th_tit"}):
                file.write(div.get_text()+'\r\n')
                print(div.get_text()+'\r\n')

url='http://tieba.baidu.com/f?ie=utf-8&kw=python&pn='
file_tieba=open('pythonba.txt','w+',encoding='utf-8')
for i in range(1,17):
    url_everypage=url+str((i-1)*50)
    print('Processing page:'+url+str(i)+str('/16......'))
    GetEveryPage(url_everypage,file_tieba)
print('Finished!')
file_tieba.close()
   
