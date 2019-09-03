# -*- coding: utf-8 -*-
# @Date    : 2019-06-25
# @Author  : 立果
# @model   ：店铺管理
import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import json
import datetime
from Public.select_request import TestApi
from Branch import operate_excel
from Branch.log import Log

class MyTest(unittest.TestCase):
    """店铺管理"""

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase1(self, id=40):
        """查看店铺收益页面信息"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"]["shopCommissionDetail"]["totalCommission"]
        actual_two = apijson2["data"]["countChildrenShops"]
        try:
            self.assertEqual(int(expect_one['totalCommission']), actual_one, msg='预期和返回不一致')
            Log().info('对【店铺总收益】断言,断言结果--预期值%s == 实际值%s' % (expect_one['totalCommission'], actual_one))
        except:
            Log().warning('对【店铺总收益】断言,断言结果--预期值%s != 实际值%s' % (expect_one['totalCommission'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['countChildrenShops']), actual_two, msg='预期和返回不一致')
                Log().info('对【下级人数】断言,断言结果--预期值%s == 实际值%s' % (expect_two['countChildrenShops'], actual_two))
            except:
                Log().warning('对【下级】断言,断言结果--预期值%s != 实际值%s' % (expect_two['countChildrenShops'], actual_two))
                raise

    # def testCase2(self, id=41):
    #     """纳新收益明细"""
    #     data_test = operate_excel.data(a='liguo')[id]
    #     expect_one = operate_excel.change(asserexpect=data_test['expect1'])
    #     expect_two = operate_excel.change(asserexpect=data_test['expect2'])
    #     Log().info('获取用例数据:%s' % data_test)
    #     apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
    #                       way=data_test['way']).selectway()
    #     Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
    #                data_test['param'], data_test['way']))
    #     apijson2 = json.loads(apijson)
    #     actual_one = apijson2["data"]["nick"]
    #     actual_two = apijson2["data"]["tel"]
    #     try:
    #         self.assertEqual(expect_one['nick'], actual_one, msg='预期和返回不一致')
    #         Log().info('对【店铺名称】断言,断言结果--预期值%s == 实际值%s' % (expect_one['nick'], actual_one))
    #     except:
    #         Log().warning('对【店铺名称】断言,断言结果--预期值%s != 实际值%s' % (expect_one['nick'], actual_one))
    #         raise
    #     finally:
    #         try:
    #             self.assertEqual(expect_two['tel'], actual_two, msg='预期和返回不一致')
    #             Log().info('对【店铺手机号】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tel'], actual_two))
    #         except:
    #             Log().warning('对【店铺手机号】断言,断言结果--预期值%s != 实际值%s' % (expect_two['tel'], actual_two))
    #             raise

    def testCase3(self, id=42):
        """获取个人专属邀请码"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        actual_two = apijson1["data"]["inviteCode"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['inviteCode'], actual_two, msg='预期和返回不一致')
                Log().info('对【邀请码】断言,断言结果--预期值%s == 实际值%s' % (expect_two['inviteCode'], actual_two))
            except:
                Log().warning('对【邀请码】断言,断言结果--预期值%s != 实际值%s' % (expect_two['inviteCode'], actual_two))
                raise

    def testCase4(self, id=43):
        """客户管理信息"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = len(apijson1["data"]["familyMemberList"])
        list_data = []
        for shop_data in apijson1["data"]["familyMemberList"]:
            list_data.append(str(shop_data["shopId"]))
        actual_two = "、".join(list_data)
        try:
            self.assertEqual(int(expect_one['count']), actual_one, msg='预期和返回不一致')
            Log().info('对【下级总数】断言,断言结果--预期值%s == 实际值%s' % (expect_one['count'], actual_one))
        except:
            Log().warning('对【下级总数】断言,断言结果--预期值%s != 实际值%s' % (expect_one['count'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['shopId'], actual_two, msg='预期和返回不一致')
                Log().info('对【下级shopid】断言,断言结果--预期值%s == 实际值%s' % (expect_two['shopId'], actual_two))
            except:
                Log().warning('对【下级shopid】断言,断言结果--预期值%s != 实际值%s' % (expect_two['shopId'], actual_two))
                raise

    def testCase5(self, id=44):
        """校验最近订单收益明细"""
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
        apijson1 = json.loads(apijson)["data"][:3]
        num = 0
        for dict_data in apijson1:
            if dict_data["type"] == "余额支付":
                actual_one = apijson1[num]["commissionStr"]
            elif dict_data["type"] == "订单退款":
                actual_two = apijson1[num]["commissionStr"]
            elif dict_data["type"] == "本店销售":
                actual_three = apijson1[num]["commission"]
                actual_four = apijson1[num]["refundCommission"]
            num += 1
        try:
            self.assertEqual(expect_one['pay'], actual_one, msg='预期和返回不一致')
            Log().info('对【支付金额】断言,断言结果--预期值%s == 实际值%s' % (expect_one['pay'], actual_one))
        except:
            Log().warning('对【支付金额】断言,断言结果--预期值%s != 实际值%s' % (expect_one['pay'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['refund'], actual_two, msg='预期和返回不一致')
                Log().info('对【退款金额】断言,断言结果--预期值%s == 实际值%s' % (expect_two['refund'], actual_two))
            except:
                Log().warning('对【退款金额】断言,断言结果--预期值%s != 实际值%s' % (expect_two['refund'], actual_two))
                raise
            finally:
                try:
                    self.assertEqual(int(expect_three['commission']), actual_three, msg='预期和返回不一致')
                    Log().info('对【发放佣金】断言,断言结果--预期值%s == 实际值%s' % (expect_three['commission'], actual_three))
                except:
                    Log().warning('对【发放佣金】断言,断言结果--预期值%s != 实际值%s' % (expect_three['commission'], actual_three))
                    raise
                finally:
                    try:
                        self.assertEqual(int(expect_four['refundCommission']), actual_four, msg='预期和返回不一致')
                        Log().info('对【回收佣金】断言,断言结果--预期值%s == 实际值%s' % (expect_four['refundCommission'], actual_four))
                    except:
                        Log().warning('对【回收佣金】断言,断言结果--预期值%s != 实际值%s' % (expect_four['refundCommission'], actual_four))
                        raise

    def testCase6(self, id=45):
        """销售额历史信息"""
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(year, month), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["data"][0]["saleValue"]
        actual_two = apijson1["data"][0]["refundValue"]
        try:
            self.assertEqual(int(expect_one['saleValue']), actual_one, msg='预期和返回不一致')
            Log().info('对最新订单【销售金额】断言,断言结果--预期值%s == 实际值%s' % (expect_one['saleValue'], actual_one))
        except:
            Log().warning('对最新订单【销售金额】断言,断言结果--预期值%s != 实际值%s' % (expect_one['saleValue'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['refundValue']), actual_two, msg='预期和返回不一致')
                Log().info('对最新订单【退款金额】断言,断言结果--预期值%s == 实际值%s' % (expect_two['refundValue'], actual_two))
            except:
                Log().warning('对最新订单【退款金额】断言,断言结果--预期值%s != 实际值%s' % (expect_two['refundValue'], actual_two))
                raise

    def testCase7(self, id=46):
        """查看提现手机号和可提现金额"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["data"]["mobile"]
        actual_two = apijson1["data"]["withdrawCommission"]
        try:
            self.assertEqual(expect_one['mobile'], actual_one, msg='预期和返回不一致')
            Log().info('对【提现手机号】断言,断言结果--预期值%s == 实际值%s' % (expect_one['mobile'], actual_one))
        except:
            Log().warning('对【提现手机号】断言,断言结果--预期值%s != 实际值%s' % (expect_one['mobile'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['withdrawCommission']), actual_two, msg='预期和返回不一致')
                Log().info('对【可提现金额】断言,断言结果--预期值%s == 实际值%s' % (expect_two['withdrawCommission'], actual_two))
            except:
                Log().warning('对【可提现金额】断言,断言结果--预期值%s != 实际值%s' % (expect_two['withdrawCommission'], actual_two))
                raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
