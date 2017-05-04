# -*- coding:utf-8 -*-

from urllib import urlencode
import cookielib, urllib2
import requests
from lxml import html

session_requests=requests.session()

# cookie
cj=cookielib.LWPCookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

#Login
user_data={'userid':'联付科技',
    'password':'lfkj_jaja95178',
    'loginflag':'1'
}
url_data=urlencode(user_data)
login_r=opener.open("http://yqms.istarshine.com/Login/doLogin", url_data)
url="http://yqms3.istarshine.com/Index/index/" #urltype=1"
result=session_requests.post(url)
print(result.text)
