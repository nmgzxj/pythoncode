# -*- coding=utf-8 -*-
import requests

session=requests.Session()
#login_url="http://yqms.istarshine.com/Login/doLogin"

#params={'loginflag':'1','userid':'qmsk','password':'china95178'}
#s=session.post(login_url,data=params,headers=dict(referer=login_url))
#print(s.cookies.get_dict())

url="http://www.cp.com.cn"
s=session.get(url)
print(s.text)
