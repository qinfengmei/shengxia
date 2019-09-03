# -*- coding: utf-8 -*-
# @Date    : 2019-05-27
# @Author  : 立果
# @model   ：商品交易
import unittest
import decimal
from time import sleep
import json
from Public.select_request import TestApi
from Branch import operate_excel
from Branch import operate_db
from Branch.log import Log

class MyTest(unittest.TestCase):
    """商品交易"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=0):
        """确认订单信息"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]    #从Excel获取第1条测试用例
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])    #获取期望值1，从Excel获取
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])    #获取期望值2，从Excel获取
        Log().info('获取用例数据:%s' % data_test)
        # 接口请求，得到响应体
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        #接口返回的false和true无法解析，先替换为0
        apijson1 = apijson.replace('false', '"false"')
        apijson2 = apijson1.replace('true', '"true"')
        apijson3 = json.loads(apijson2)                           #json转化成字典
        actual_one = apijson3['data']['totalPrice']               #获取实际值1，从响应体获取
        actual_two = apijson3['data']['items'][id]['itemZhName']   #获取实际值2，从响应体获取
        # 期望值1和实际值1进行对比校验
        try:
            self.assertEqual(float(expect_one['totalPrice']), actual_one, msg='预期和返回不一致')

            Log().info('对【商品价格】断言,断言结果--预期值%s == 实际值%s' % (expect_one['totalPrice'], actual_one))
        except:
            Log().warning('对【商品价格】断言,断言结果--预期值%s != 实际值%s' % (expect_one['totalPrice'], actual_one))
            raise
        finally:
        #期望值2和实际值2进行对比校验
            try:
                self.assertEqual(expect_two['itemZhName'], actual_two, msg='预期和返回不一致')
                Log().info('对【商品名称】断言,断言结果--预期值%s == 实际值%s' % (expect_two['itemZhName'], actual_two))
            except:
                Log().warning('对【商品名称】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise

    def testCase2(self, id=1):
        """提交订单成功未支付"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 =json.loads(apijson)
        global actual
        actual = apijson1["data"]["orderNumber"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(actual)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertIsNotNone(actual, msg='实际值不存在')
            Log().info('对【订单号】断言,生成订单号%s' % (actual))
        except:
            Log().warning('对【订单号】断言，订单号生成失败')
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['tradestatus']), actual_two, msg='预期和返回不一致')
                Log().info('对【订单状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
            except:
                Log().warning('对【订单状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['tradestatus'], actual_two))
                raise

    # def testCase3(self, id=3):
    #     """支付页校验用户余额"""
    #     data_test = operate_excel.data(a='liguo')[id]
    #     expect_one = operate_excel.change(asserexpect=data_test['expect1'])
    #     expect_two = operate_excel.change(asserexpect=data_test['expect2'])
    #     Log().info('获取用例数据:%s' % data_test)
    #     apijson = TestApi(url2=data_test['url'].format(actual), key=data_test['key'], param=data_test['param'],
    #                       way=data_test['way']).selectway()
    #     Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'].format(actual), data_test['key'],
    #                data_test['param'], data_test['way']))
    #     apijson1 = apijson.replace('false', '"false"')
    #     apijson2 = apijson1.replace('true', '"true"')
    #     apijson3 = json.loads(apijson2)
    #     actual_one = apijson3["data"][0]["msg"]
    #     actual_two = apijson3["data"][0]["selectable"]
    #     try:
    #         self.assertEqual(expect_one['msg'], actual_one, msg='预期和返回不一致')
    #         Log().info('对【余额】断言,断言结果--预期值%s == 实际值%s' % (expect_one['msg'], actual_one))
    #     except:
    #         Log().warning('对【余额】断言,断言结果--预期值%s != 实际值%s' % (expect_one['msg'], actual_one))
    #         raise
    #     try:
    #         self.assertEqual(expect_two['selectable'], actual_two, msg='预期和返回不一致')
    #         Log().info('对【余额支付状态】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_two['selectable'], actual_two))
    #     except:
    #         Log().warning('对【余额支付状态】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_two['selectable'], actual_two))
    #         raise
    #
    # def testCase4(self, id=5):
    #     """支付短信验证码发送成功"""
    #     data_test = operate_excel.data(a='liguo')[id]
    #     expect_one = operate_excel.change(asserexpect=data_test['expect1'])
    #     expect_two = operate_excel.change(asserexpect=data_test['expect2'])
    #     Log().info('获取用例数据:%s' % data_test)
    #     apijson = TestApi(url2=data_test['url'].format(actual), key=data_test['key'], param=data_test['param'],
    #                       way=data_test['way']).selectway()
    #     Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'].format(actual), data_test['key'],
    #                                                        data_test['param'], data_test['way']))
    #     apijson2 = json.loads(apijson)
    #     actual_one = apijson2["isSuccess"]
    #     actual_two = apijson2["msg"]
    #     try:
    #         self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
    #         Log().info('对【店铺名称】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
    #     except:
    #         Log().warning('对【店铺名称】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
    #         raise
    #     try:
    #         self.assertEqual(expect_two['msg'], actual_two, msg='预期和返回不一致')
    #         Log().info('对【关联微信名称】断言,断言结果--预期值%s == 实际值%s' % (expect_two['msg'], actual_two))
    #     except:
    #         Log().warning('对【关联微信名称】断言,断言结果--预期值%s != 实际值%s' % (expect_two['msg'], actual_two))
    #         raise

    # def testCase4(self, id=4):
    #     """校验订单号和订单状态"""
    #     data_test = operate_excel.data(a='liguo')[id]
    #     expect_one = operate_excel.change(asserexpect=data_test['expect1'])
    #     Log().info('获取用例数据:%s' % data_test)
    #     apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
    #                       way=data_test['way']).selectway()
    #     Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
    #                                                        data_test['param'], data_test['way']))
    #     apijson1 = apijson.replace('false', '"false"')
    #     apijson2 = apijson1.replace('true', '"true"')
    #     apijson3 = json.loads(apijson2)
    #     actual_one = apijson3['data']['result']
    #     actual_two = apijson3['data']['orderNumber']
    #     try:
    #         self.assertEqual(expect_one['result'], actual_one, msg='预期和返回不一致')
    #         Log().info('对【订单】断言,断言结果--预期值%s == 实际值%s' % (expect_one['result'], actual_one))
    #     except:
    #         Log().warning('对【订单】断言,断言结果--预期值%s != 实际值%s' % (expect_one['result'], actual_one))
    #         raise
    #     try:
    #         self.assertEqual(actual, actual_two, msg='预期和返回不一致')
    #         Log().info('对【订单号】断言,断言结果--支付成功预期值%s == 实际值%s' % (actual, actual_two))
    #     except:
    #         Log().warning('对【订单号】断言,断言结果--支付成功预期值%s != 实际值%s' % (actual, actual_two))
    #         raise
    #
    def testCase3(self, id=2):
        """使用余额支付成功(测试桩)"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(actual), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'].format(actual), data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(actual)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【订购结果】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【订购结果】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['tradestatus']), actual_two, msg='预期和返回不一致')
                Log().info('对【订单状态】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
            except:
                Log().warning('对【订单状态】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_two['tradestatus'], actual_two))
                raise

    def testCase4(self, id=3):
        """发送支付成功和收益到账通知"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        expect_three = operate_excel.change(asserexpect=data_test['expect3'])
        expect_four = operate_excel.change(asserexpect=data_test['expect4'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_str1 = apijson2["data"][1]["content"]
        actual_one = json.loads(actual_str1)["title"]
        actual_two = json.loads(actual_str1)["messageSubLines"][0]["content"]
        actual_str2 = apijson2["data"][0]["content"]
        actual_three = json.loads(actual_str2)["title"]
        actual_four = json.loads(actual_str2)["messageSubLines"][0]["content"]
        try:
            self.assertEqual(expect_one['title'], actual_one, msg='预期和返回不一致')
            Log().info('对支付成功消息【title】断言,断言结果--预期值%s == 实际值%s' % (expect_one['title'], actual_one))
        except:
            Log().warning('对支付成功消息【title】断言,断言结果--预期值%s != 实际值%s' % (expect_one['title'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['content'], actual_two, msg='预期和返回不一致')
                Log().info('对支付成功消息【金额】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_two['content'], actual_two))
            except:
                Log().warning('对支付成功消息【金额】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_two['content'], actual_two))
                raise
            finally:
                try:
                    self.assertEqual(expect_three['title'], actual_three, msg='预期和返回不一致')
                    Log().info('对收益到账消息【title】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_three['title'], actual_three))
                except:
                    Log().warning('对收益到账消息【title】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_three['title'], actual_three))
                    raise
                finally:
                    try:
                        self.assertEqual(expect_four['content'], actual_four, msg='预期和返回不一致')
                        Log().info('对收益到账消息【金额】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_four['content'], actual_four))
                    except:
                        Log().warning('对收益到账消息【金额】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_four['content'], actual_four))
                        raise

    def testCase5(self, id=4):
        """订单详情收益和上级佣金"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        expect_three = operate_excel.change(asserexpect=data_test['expect3'])
        expect_four = operate_excel.change(asserexpect=data_test['expect4'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(actual), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'].format(actual), data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["data"]["tradePageInfoVO"]["orderDirectCommission"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        actual_com = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).more_perform()
        actual_two = str(decimal.Decimal(actual_com[0]['commission']))
        actual_three = str(decimal.Decimal(actual_com[1]['commission']))
        actual_four = str(decimal.Decimal(actual_com[2]['commission']))
        try:
            self.assertEqual(float(expect_one['orderDirectCommission']), actual_one, msg='预期和返回不一致')
            Log().info('对详情页【收益】断言,断言结果--预期值%s == 实际值%s' % (expect_one['orderDirectCommission'], actual_one))
        except:
            Log().warning('对详情页【收益】断言,断言结果--预期值%s != 实际值%s' % (expect_one['orderDirectCommission'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['invite'], actual_two, msg='预期和返回不一致')
                Log().info('对邀请人【佣金】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_two['invite'], actual_two))
            except:
                Log().warning('对邀请人【佣金】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_two['invite'], actual_two))
                raise
            finally:
                try:
                    self.assertEqual(expect_three['guwen'], actual_three, msg='预期和返回不一致')
                    Log().info('对客户代表/营销顾问【佣金】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_three['guwen'], actual_three))
                except:
                    Log().warning('对客户代表/营销顾问【佣金】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_three['guwen'], actual_three))
                    raise
                finally:
                    try:
                        self.assertEqual(expect_four['jinli'], actual_four, msg='预期和返回不一致')
                        Log().info('对市场经理【佣金】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_four['jinli'], actual_four))
                    except:
                        Log().warning('对市场经理【佣金】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_four['jinli'], actual_four))
                        raise

    def testCase6(self, id=9):
        """订单取消成功"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(actual), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(actual)
        sleep(1)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【订购结果】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【订购结果】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['tradestatus']), actual_two, msg='预期和返回不一致')
                Log().info('对【订单状态】断言,断言结果--支付成功预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
            except:
                Log().warning('对【订单状态】断言,断言结果--支付成功预期值%s != 实际值%s' % (expect_two['tradestatus'], actual_two))
                raise

    def testCase7(self, id=10):
        """发送订单退款通知"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"][0]["content"]
        try:
            self.assertEqual(expect_one['content'], actual_one, msg='预期和返回不一致')
            Log().info('对支付成功消息【content】断言,断言结果--预期值%s == 实际值%s' % (expect_one['content'], actual_one))
        except:
            Log().warning('对支付成功消息【content】断言,断言结果--预期值%s != 实际值%s' % (expect_one['content'], actual_one))
            raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
