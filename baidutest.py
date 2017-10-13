# coding:utf-8
import urllib
import urllib.request
import re

data = {}
data['word'] = '张显金'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')

reg = re.compile("")
print(data)