# -*- coding=utf-8 -*-
import requests

session=requests.Session()
login_url="http://yqms.istarshine.com/Login/doLogin"

params={'loginflag':'1','userid':'联付科技','password':'lfkj_jaja95178'}
s=session.post(login_url,data=params,headers=dict(referer=login_url))
#print(s.cookies.get_dict())

url="http://yqms3.istarshine.com/Index/index/urltype=1"
s=session.get(url)
print(s.text)
