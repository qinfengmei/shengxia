import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import requests
import json
from time import sleep
from Branch.log import Log
from config import globalparam
from Branch.operate_db import Operate_redis

class Lg_in():
    """
    从登录接口获取token传到其他接口上，维持登录状态
    """
    def __init__(self):
        self.url1 = globalparam.app_path
        self.cms_url = globalparam.cms_path
        self.headers = {"User-Agent": "okhttp/3.11.0"}
        self.cookies = {"JSESSIONID": "CD41221E64FE5148BFA6B75C792E609E"}

    def click_msg(self):
        """获取验证码"""
        url2 = '/api/shop/login/getLoginCode?tel=18069425303'
        try:
            r = requests.get(url=self.url1 + url2, cookies=self.cookies, headers=self.headers)
            r.encoding = 'UTF-8'
            response_text = r.text
            response_text1 = json.loads(response_text)['msg']
            Log().info('get请求发送验证码，验证码发送{0}'.format(response_text1))
            sleep(5)
        except Exception as e:
            Log().error('get请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}


    def Login(self):
        """APP接口--登录用户"""
        # self.click_msg()
        # msg = Operate_redis().connect()
        url2 = '/api/shop/shopLogin?tel=18069425303&code=123456'
        try:
            r = requests.get(url=self.url1+url2, cookies=self.cookies, headers=self.headers)
            r.encoding = 'UTF-8'
            response_text = r.text
            response_text1 = json.loads(response_text)['data']['token']
            Log().info('18069425303用户开始登录，返回登录信息{0}'.format(response_text1))
            return response_text1
        except Exception as e:
            Log().error('get请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}

    def select_user(self):
        """APP接口--多个账号，选择一个账号登录"""
        url3 = '/api/shop/login/selectUser'
        data = {'tel': '18069425303', 'userId': '10474262', 'token': self.Login(), 'isShop': 'false'}
        try:
            session = requests.Session()
            r = session.post(url=self.url1+url3, cookies=self.cookies, headers=self.headers, data=data)
            r.encoding = 'UTF-8'
            cookie = requests.utils.dict_from_cookiejar(session.cookies)
            umbrella_token = cookie['umbrella_token']
            Log().info('18069425303登录成功，返回token<{0}>'.format(umbrella_token))
            return umbrella_token
        except Exception as e:
            Log().error('get请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s' % e}
# Lg_in().select_user()