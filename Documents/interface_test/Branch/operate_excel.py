# -*- coding: utf-8 -*-
import os, xlrd
from Branch.log import Log
from config import globalparam

log_path = globalparam.log_path
file_path = globalparam.data_path

def readexcel(filepath):
    """
    读取xlsx文件，将每列的数据保存到list里
    """
    try:
        file = xlrd.open_workbook(filepath)
        first_line = file.sheets()[0]
        lines = first_line.nrows
        list_id = []
        list_module = []
        list_name = []
        list_key = []
        list_param = []
        list_place = []
        list_url = []
        list_way = []
        list_expect1 = []
        list_expect2 = []
        list_expect3 = []
        list_expect4 = []
        for i in range(1, lines):
            list_id.append(first_line.cell(i, 0).value)
            list_module.append(first_line.cell(i, 1).value)
            list_name.append(first_line.cell(i, 2).value)
            list_key.append(first_line.cell(i, 3).value)
            list_param.append(first_line.cell(i, 4).value)
            list_place.append(first_line.cell(i, 5).value)
            list_url.append(first_line.cell(i, 6).value)
            list_way.append((first_line.cell(i, 7).value))
            list_expect1.append((first_line.cell(i, 8).value))
            list_expect2.append((first_line.cell(i, 9).value))
            list_expect3.append((first_line.cell(i, 10).value))
            list_expect4.append((first_line.cell(i, 11).value))
        return list_id, list_module, list_name, list_key, list_param, list_place, list_url, list_way,\
               list_expect1, list_expect2,  list_expect3,  list_expect4
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def data(case_name='liguo'):
    """
    将列表转换成字典，以便于取值，也可用于ddt数驱
    :param a: 用例序号1,2,3...
    :return: 字典
    """
    path = file_path + "/" + "case_{0}.xlsx".format(case_name)
    list_id, list_module, list_name, list_key, list_param, list_place, list_url, list_way, list_expect1, \
    list_expect2, list_expect3, list_expect4=readexcel(path)
    make_data1 = []
    try:
        for i in range(len(list_id)):
            make_data1.append({'id': list_id[i], 'module':list_module[i], 'url': list_url[i], 'name': list_name[i],  'key': list_key[i],
                               'param':list_param[i], 'place': list_place[i],'way': list_way[i], 'expect1': list_expect1[i],
                               'expect2': list_expect2[i], 'expect3': list_expect3[i], 'expect4': list_expect4[i]})
            i += 1
        return make_data1
    except:
        Log().error('打开测试用例失败，原因是:%s' % Exception)

def mergedata():
    """
    将多个Excel文件用例整合到一起
    :return: 字典
    """
    # 获取文件下文件个数
    count = 0
    make_data = []
    for root, dirs, files in os.walk(file_path):
        for each in files:
            count += 1
        print(count)
    #用例整合
    for case in range(count):
        case += 1
        for i in data(case):
            make_data.append(i)
    return make_data

def get_palce(case_num, case_name='liguo'):
    """
    将Excel中数据库列用字典保存
    :param num: 用例序号0,1,2...
    :return:{'db': 'sit', 'sql': "select status_code from ...", 'database': 'trade'}
    """
    try:
        place = data(case_name)[case_num]['place']
        list1 = ['db', 'database', 'sql']
        list2 = place.split(';')
        dict_place = dict(zip(list1,list2))
        return dict_place
    except:
        Log().error('整合Excel中数据库信息字段失败')
        raise

def change(asserexpect):
    """
    更改期望值格式，['code=4001'] --> {'code': '4001'}
    :return {'code': '4001'}
    """
    if len(asserexpect.split('=')) > 1:
        data = asserexpect.split('&')   #
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        Log().info('填写测试预期值')
        raise {"code": 1, 'result': '填写测试预期值'}

# def assert_in(asserqiwang, fanhuijson):
#     if len(asserqiwang.split('=')) > 1:
#         data = asserqiwang.split('&')
#         result = dict([(item.split('=')) for item in data])
#         value1 = ([(str(fanhuijson[key])) for key in result.keys()])
#         value2 = ([(str(value)) for value in result.values()])
#         if value1 == value2:
#             return {'code': 0, "result": 'pass'}
#         else:
#             return {'code': 1, 'result': 'fail'}
#     else:
#         Log().info('填写测试预期值')
#         return {"code": 2, 'result': '填写测试预期值'}
