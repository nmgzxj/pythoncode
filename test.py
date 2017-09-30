# -*- coding=utf-8 -*-

import requests

session = requests.Session()
login_url = "http://yqms.istarshine.com/Login/doLogin"

params={'loginflag':'1','userid':'qmsk','password':'china95178'}
s=session.post(login_url,data=params,headers=dict(referer=login_url))

url="http://yqms3.istarshine.com/Index/index/urltype=1"
s=session.get(url)
print(s.text)