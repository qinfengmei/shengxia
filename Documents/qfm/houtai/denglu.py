#!/usr/bin/env python
#-*- coding:utf-8 -*-
from distutils.log import Log

import requests
import json

from self import self

# url = "登录接口"
url = "https://console-shop.showjoy.com/shop/v1/login"
data = {
    "account": "qfm",  #用户名
    "password": "5c77db1eae5c2e0887a545e35444a473" #密码

}
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

# login = requests.post(url=url,data=data,headers=headers)
# cookies = login.cookies
# print(cookies)

def send_post(url):
        aa = requests.post(url=url,data=data,headers=headers)
        bb = aa.text  #输出接口返回信息
        cc = json.loads(bb) #将字符串返回信息转换成字典
        print(cc['data']['id']) #取出字典中某个值的value

#获取登录用户的cookie信息
def select_user():
    session = requests.Session()
    r = session.post(url=url,headers=headers,data=data).cookies
    # cookie = requests.utils.dict_from_cookiejar(r)
    # print(cookie)
    # print(r.text)
    r.encoding = 'utf-8'
    cookie = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookie)
    token = cookie['token']
    return token


if __name__=="__main__":
    select_user()
    send_post(url)