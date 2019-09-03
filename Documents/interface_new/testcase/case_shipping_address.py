# -*- coding: utf-8 -*-
# @Date    : 2019-06-10
# @Author  : 立果
# @model   ：收货地址管理
import unittest
import json
from time import sleep
from Public.select_request import TestApi
from Branch import operate_excel
from Branch.log import Log
from Branch import operate_db

class MyTest(unittest.TestCase):
    """收货地址管理"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=35):
        """新增地址"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        global address_id1
        address_id1 = apijson2["data"]
        actual_two = address_id1
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        expect_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two, actual_two, msg='预期和返回不一致')
                Log().info('对【地址id】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【地址id】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise

    def testCase2(self, id=36):
        """查看地址"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["data"]["addresses"][-1]["id"]
        actual_two = apijson1["data"]["addresses"][-1]["isDefault"]
        try:
            self.assertEqual(int(address_id1), actual_one, msg='预期和返回不一致')
            Log().info('对【地址id】断言,断言结果--预期值%s == 实际值%s' % (address_id1, actual_one))
        except:
            Log().warning('对【地址id】断言,断言结果--预期值%s != 实际值%s' % (address_id1, actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['isDefault'], str(actual_two), msg='预期和返回不一致')
                Log().info('对【是否为默认地址】断言,断言结果--预期值%s == 实际值%s' % (expect_two['isDefault'], actual_two))
            except:
                Log().warning('对【是否为默认地址】断言,断言结果--预期值%s != 实际值%s' % (expect_two['isDefault'], actual_two))
                raise

    def testCase3(self, id=37):
        """设置默认地址"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(address_id1), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'].format(address_id1), data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        global address_id
        address_id = apijson1["data"]["addresses"][0]["id"]
        actual_one = apijson1["data"]["addresses"][0]["isDefault"]
        try:
            self.assertEqual(expect_one['isDefault'], str(actual_one), msg='预期和返回不一致')
            Log().info('地址【%s】是否为默认地址,断言结果--预期值%s == 实际值%s' % (address_id, expect_one['isDefault'], actual_one))
        except:
            Log().warning('地址【%s】是否为默认地址,断言结果--预期值%s != 实际值%s' % (address_id, expect_one['isDefault'], actual_one))
            raise

    def testCase4(self, id=38):
        """编辑地址"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'].replace("{0}", str(address_id1)),
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'].replace("{0}", str(address_id1)), data_test['way']))
        apijson2 = json.loads(apijson)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        actual_one = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        global address_id2
        address_id2 = apijson2["data"]
        try:
            self.assertEqual(expect_one['fullName'], actual_one, msg='预期和返回不一致')
            Log().info('重新生成地址id【%s】，对【fullName】断言,断言结果--预期值%s == 实际值%s' % (address_id2, expect_one['fullName'], actual_one))
        except:
            Log().warning('重新生成地址id【%s】，对【fullName】断言,断言结果--预期值%s != 实际值%s' % (address_id2, expect_one['fullName'], actual_one))
            raise

    def testCase5(self, id=39):
        """删除地址"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'].replace("{0}", str(address_id2)),
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id)['sql'].format(address_id2)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['COUNT(*)']), actual_two, msg='预期和返回不一致')
                Log().info('对【删除结果数】断言,断言结果--预期值%s == 实际值%s' % (expect_two['COUNT(*)'], actual_two))
            except:
                Log().warning('对【删除结果数】断言,断言结果--预期值%s != 实际值%s' % (expect_two['COUNT(*)'], actual_two))
                raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
