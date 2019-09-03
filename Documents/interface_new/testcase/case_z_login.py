# -*- coding: utf-8 -*-
# @Date    : 2019-05-27
# @Author  : 立果
# @model   ：用户登录注册
import unittest
from time import sleep
import json
from Public.select_request import TestApi
from Branch import operate_excel
from Branch import operate_db
from Branch.log import Log

class MyTest(unittest.TestCase):
    """注册登录"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=11):
        """用户未注册"""
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
        actual_two = apijson2["msg"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['msg'], actual_two, msg='预期和返回不一致')
                Log().info('对【msg】断言,断言结果--预期值%s == 实际值%s' % (expect_two['msg'], actual_two))
            except:
                Log().warning('对【msg】断言,断言结果--预期值%s != 实际值%s' % (expect_two['msg'], actual_two))
                raise

    def testCase2(self, id=12):
        """短验注册登录成功"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = apijson.replace('false', '"false"')
        apijson2 = json.loads(apijson1)
        actual_one = apijson2['data']['mobileLoginUser'][0]["tel"]
        actual_two = apijson2['data']['mobileLoginUser'][0]["userId"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        expect_two = operate_db.Operate_db(case_num=9, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(expect_one['tel'], actual_one, msg='预期和返回不一致')
            Log().info('对【手机号】断言,断言结果--预期值%s == 实际值%s' % (expect_one['tel'], actual_one))
        except:
            Log().warning('对【手机号】断言,断言结果--预期值%s != 实际值%s' % (expect_one['tel'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two), actual_two, msg='预期和返回不一致')
                Log().info('对【userId】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【userId】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise

    def testCase3(self, id=13):
        """获取折扣码当前店主"""
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
        actual_two = apijson2['data'][0]["name"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['name'], actual_two, msg='预期和返回不一致')
                Log().info('对【邀请人name】断言,断言结果--预期值%s == 实际值%s' % (expect_two['name'], actual_two))
            except:
                Log().warning('对【邀请人name】断言,断言结果--预期值%s != 实际值%s' % (expect_two['name'], actual_two))
                raise
        # sql1 = operate_excel.get_palce(num=8)['sql']
        # operate_db.Operate_db(casenum=8, sql=sql1).Perform()

    def testCase4(self, id=14):
        """绑定折扣码"""
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
        actual_one = apijson3['data']['parentId']
        actual_two = apijson3['data']['name']
        sql = operate_excel.get_palce(case_num=11, case_name=MyTest.name)['sql']
        expect_two = operate_db.Operate_db(case_num=11, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['parentId']), actual_one, msg='预期和返回不一致')
            Log().info('对【parentId】断言,断言结果--预期值%s == 实际值%s' % (expect_one['parentId'], actual_one))
        except:
            Log().warning('对【parentId】断言,断言结果--预期值%s != 实际值%s' % (expect_one['parentId'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two, actual_two, msg='预期和返回不一致')
                Log().info('对【邀请人】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【邀请人】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise
        sleep(1)
        sql1 = operate_excel.get_palce(case_num=8, case_name=MyTest.name)['sql']
        operate_db.Operate_db(case_num=8, sql=sql1, case_name=MyTest.name).Perform()

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
