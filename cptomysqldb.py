#coding:utf8
import requests
import time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

session = requests.Session()
url="http://www.cb.com.cn/fangdichan/"
#s=session.get(url)
#print(s.text)

import mysql.connector

# 创建连接
config = {
          'user':'root',
          'password':'editedit',
          'host':'127.0.0.1',
          'port':3306,
          'database':'crawldb'}
conn = mysql.connector.connect(**config)

# 创建游标
cur = conn.cursor()

import urllib2
import sys
import chardet

def crawl_content():

    return content

req = urllib2.Request(url)
content = urllib2.urlopen(req).read()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(content).get('encoding','utf-8')
html = content.decode(infoencode,'ignore').encode(typeEncode)
#print html

soup = BeautifulSoup(html)
print soup.title
for link in soup.findAll('dl',{"class":"listdlr"}):
    web_name = '中国经营报'
    title = link.dt.a.string
    anthor = ''
    url = link.dt.a.get('href')
    source = ''
    content = ''
    pub_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    crawl_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    keywords = ''
    description = ''

    sql = "insert into cbcomcn (web_name,title,anthor,url,source,content,pub_time,crawl_time,keywords,description) " \
          "values ('"+web_name+"','"+title+"','"+anthor+"','"+url+"','"+source+"','"+content+"','"+pub_time+"','"\
          + crawl_time + "','" + keywords + "','" + description + "');"
    cur.execute(sql)

    print sql
  #  except:
   #     print "出错了。"
conn.commit()

# 执行查询SQL
sql = "SELECT * FROM cbcomcn"
cur.execute(sql)

# 获取查询结果
result_set = cur.fetchall()
if result_set:
    for row in result_set:
        print "%s, %s, %s" % (row[1],row[2],row[3])

# 关闭游标和连接
cur.close()
conn.close()