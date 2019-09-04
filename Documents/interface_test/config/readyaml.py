# -*- coding: utf-8 -*-
from Branch import operate_excel
from yaml import load
import os

# 获取当前脚本所在文件夹路径
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")
config_path1 = os.path.join(curPath, "test_title.yaml")

class Getyaml():
    """
    读取操作yaml文件
    """
    def get_data(self, case_num, case_name):
        """
        根据用例数据库名找到yaml中对应的连接信息
        :param num: 用例序号0,1,2...
        :return: [ip, 账号, 密码]
        """
        with open(config_path, 'rb') as f:
            cont = f.read()
        cf = load(cont)
        database = operate_excel.get_palce(case_num, case_name)['database']
        db = operate_excel.get_palce(case_num, case_name)['db']
        data = cf.get(db)[database]
        return data

    def get_datas(self, get_case):
        """获取对应用例名"""
        with open(config_path1, 'rb') as f:
            cont = f.read()
        cf = load(cont)
        data = cf.get(get_case)
        return data

    def get_redis(self, env='kf'):
        """
        找到yaml中对应的redis连接信息
        :return: [ip, port, 密码]
        """
        with open(config_path, 'rb') as f:
            cont = f.read()
        cf = load(cont)
        data = cf.get('redis')[env]
        return data

    def port_db(self,db,num):
        #所请求的接口属于哪个库
        data = self.get_data(db, num)
        b = -1
        for a in list(data.keys()):
            b += 1
            if self.get_data(num, a).database in list(data[a]):
                c = list(data.keys())[b]
                return c
# Getyaml().get_redis()