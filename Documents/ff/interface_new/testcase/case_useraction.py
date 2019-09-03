# -*- coding: utf-8 -*-
# @Date    : 2019-05-27
# @Author  : 立果
# @model   ：用户操作
import unittest
import json
from Public.select_request import TestApi
from Branch import operate_excel
from Branch.log import Log

class MyTest(unittest.TestCase):
    """用户操作"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=15):
        """首页信息展示"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        actual_two = str(apijson2["data"]["moduleNames"]).replace("'", '"')
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['moduleNames'], actual_two, msg='预期和返回不一致')
                Log().info('对【商品类别】断言,断言结果--预期值%s == 实际值%s' % (expect_two['moduleNames'], actual_two))
            except:
                Log().warning('对【商品类别】断言,断言结果--预期值%s != 实际值%s' % (expect_two['moduleNames'], actual_two))
                raise

    def testCase2(self, id=16):
        """店铺信息展示"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"]["nick"]
        actual_two = apijson2["data"]["tel"]
        try:
            self.assertEqual(expect_one['nick'], actual_one, msg='预期和返回不一致')
            Log().info('对【店铺名称】断言,断言结果--预期值%s == 实际值%s' % (expect_one['nick'], actual_one))
        except:
            Log().warning('对【店铺名称】断言,断言结果--预期值%s != 实际值%s' % (expect_one['nick'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['tel'], actual_two, msg='预期和返回不一致')
                Log().info('对【店铺手机号】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tel'], actual_two))
            except:
                Log().warning('对【店铺手机号】断言,断言结果--预期值%s != 实际值%s' % (expect_two['tel'], actual_two))
                raise

    def testCase3(self, id=17):
        """消息通知成功"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        msg = apijson2["count"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s,收到%s条消息' % (expect_one['isSuccess'], actual_one,msg))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise

    def testCase4(self, id=18):
        """个人信息展示"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson3 = json.loads(apijson)
        actual_one = apijson3["data"]["positionName"]
        actual_two = apijson3["data"]["shoppingCartNum"]
        try:
            self.assertEqual(expect_one['positionName'], actual_one, msg='预期和返回不一致')
            Log().info('对【用户类别】断言,断言结果--预期值%s == 实际值%s' % (expect_one['positionName'], actual_one))
        except:
            Log().warning('对【用户类别】断言,断言结果--预期值%s != 实际值%s' % (expect_one['positionName'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['shoppingCartNum']), actual_two, msg='预期和返回不一致')
                Log().info('对【购物车商品量】断言,断言结果--预期值%s == 实际值%s' % (expect_two['shoppingCartNum'], actual_two))
            except:
                Log().warning('对【购物车数量】断言,断言结果--预期值%s != 实际值%s' % (expect_two['shoppingCartNum'], actual_two))
                raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
