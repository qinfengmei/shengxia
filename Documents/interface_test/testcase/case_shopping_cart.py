# -*- coding: utf-8 -*-
# @Date    : 2019-05-27
# @Author  : 立果
# @model   ：购物车操作
import unittest
import json
from Public.select_request import TestApi
from Branch import operate_excel
from Branch.log import Log

class MyTest(unittest.TestCase):
    """购物车操作"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=19):
        """商品加入购物车"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"]
        try:
            self.assertEqual(int(expect_one['data']), actual_one, msg='预期和返回不一致')
            Log().info('成功加入购物车，对【data】断言,断言结果--预期值%s == 实际值%s' % (expect_one['data'], actual_one))
        except:
            Log().warning('成功加入购物车，对【data】断言,断言结果--预期值%s != 实际值%s' % (expect_one['data'], actual_one))
            raise
        else:
            Log().info('第1条断言成功')

    def testCase2(self, id=20):
        """查看购物车信息"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = apijson.replace('false', '"false"')
        apijson2 = apijson1.replace('true', '"true"')
        apijson3 = json.loads(apijson2)
        actual_one = apijson3["data"]["itemList"][0]["name"]
        actual_two = apijson3["data"]["itemList"][0]["price"]
        try:
            self.assertEqual(expect_one['name'], actual_one, msg='预期和返回不一致')
            Log().info('对【商品名称】断言,断言结果--预期值%s == 实际值%s' % (expect_one['name'], actual_one))
        except:
            Log().warning('对【商品名称】断言,断言结果--预期值%s != 实际值%s' % (expect_one['name'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(float(expect_two['price']), actual_two, msg='预期和返回不一致')
                Log().info('对【商品价格】断言,断言结果--预期值%s == 实际值%s' % (expect_two['price'], actual_two))
            except:
                Log().warning('对【商品价格】断言,断言结果--预期值%s != 实际值%s' % (expect_two['price'], actual_two))
                raise

    def testCase3(self, id=21):
        """增加商品数量"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = apijson.replace('false', '"false"')
        apijson2 = apijson1.replace('true', '"true"')
        apijson3 = json.loads(apijson2)
        actual_one = apijson3["data"]["itemList"][0]["quantity"]
        try:
            self.assertEqual(int(expect_one['quantity']), actual_one, msg='预期和返回不一致')
            Log().info('对【商品数量】断言,断言结果--预期值%s == 实际值%s' % (expect_one['quantity'], actual_one))
        except:
            Log().warning('对【商品数量】断言,断言结果--预期值%s != 实际值%s' % (expect_one['quantity'], actual_one))
            raise

    def testCase4(self, id=22):
        """删除购物车商品"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson1 = apijson.replace('false', '"false"')
        apijson2 = apijson1.replace('true', '"true"')
        apijson3 = json.loads(apijson2)
        actual_one = apijson3["data"]["itemList"]
        try:
            self.assertEqual(int(expect_one['itemList']), len(actual_one), msg='预期和返回不一致')
            Log().info('对【购物车商品】断言,断言结果--预期值%s == 实际值%s' % (expect_one['itemList'], len(actual_one)))
        except:
            Log().warning('对【购物车商品】断言,断言结果--预期值%s != 实际值%s' % (expect_one['itemList'], len(actual_one)))
            raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
