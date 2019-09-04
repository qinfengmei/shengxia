# -*- coding: utf-8 -*-
# @Date    : 2019-06-20
# @Author  : 海妖
# @model   ：商品交易

import unittest
from time import sleep
import json
from Public.select_request import TestApi
from Branch import operate_excel
from Branch import operate_db
from Branch.log import Log
import urllib.request

class MyTest(unittest.TestCase):
    """商品交易"""

    name = 'zhuoxw1'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase01(self, id=0):
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

    def testCase02(self, id=1):
        """提交订单成功未支付"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 =json.loads(apijson)
        global actual
        actual = apijson1["data"]["orderNumber"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(actual)
        actual_one = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertIsNotNone(actual, msg='实际值不存在')
            Log().info('对【订单号】断言,生成订单号%s' % (actual))
        except:
            Log().warning('对【订单号】断言，订单号生成失败')
            raise
        finally:
            try:
                self.assertEqual(int(expect_one['tradestatus']), actual_one, msg='预期和返回不一致')
                Log().info('对【订单状态】断言,断言结果--预期值%s == 实际值%s' % (expect_one['tradestatus'], actual_one))
            except:
                Log().warning('对【订单状态】断言,断言结果--预期值%s != 实际值%s' % (expect_one['tradestatus'], actual_one))
                raise

    def testCase03(self, id=2):
        """使用余额支付成功"""
        #校验下单前收益明细详情
        '''sql = 'SELECT commission from shop_commission where shop_id = 546082 limit 1'
        re_comm_Cumulative,re_comm_sale,re_comm_today,banlance = operate_db.Operate_db(self,casenum=id,sql=sql).income_db()
        print('下单前累计收益：' % re_comm_Cumulative)
        print('下单前销售收益：'% re_comm_sale)
        print('下单前今日收益：'% re_comm_today)
        print('下单前账户余额：' % banlance)'''
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
        actual_two = operate_db.Operate_db(case_num=id, sql=sql,case_name=MyTest.name).Perform()
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

    def testCase04(self, id=3):
        """下单成功发送站内信"""
        '''message_url = 'https://shop.m.showjoy.com.cn/api/message/count?userId=9082723'
        with urllib.request.urlopen(message_url) as resp:
            res = resp.read()
            print('下单前消息数count：', res['count'])'''
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'], way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % ( data_test['url'], data_test['key'], data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1['data'][0]['content']
        time = apijson1['data'][0]['time']
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        excuse_sql = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        json_dict = json.loads(excuse_sql)
        messageSubLines = json_dict['messageSubLines'][0]['content']
        actual_two = messageSubLines
        try:
            self.assertIn(expect_one['content'], actual_one,msg='预期和返回不一致')
            Log().info('%s,对【下单成功消息内容】断言,断言结果--预期值%s == 实际值%s' % (time, expect_one['content'], actual_one))
        except:
            Log().warning('%s,对【下单成功消息内容】断言,断言结果--预期值%s == 实际值%s' % (time, expect_one['content'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['price'], actual_two,msg='预期和返回不一致')
                Log().info(
                    '对【下单成功消息展示订单实付金额】断言,断言结果--预期值%s == 实际值%s' % (expect_two['price'], actual_two))
            except:
                Log().warning(
                    '对【下单成功消息展示订单实付金额】断言,断言结果--预期值%s == 实际值%s' % (expect_two['price'], actual_two))
                raise

    def testCase05(self, id=4):
        """下单优惠劵后台配置"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (
        data_test['url'], data_test['key'], data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1['data'][0]['couponId']
        actual_two = apijson1['data'][0]['value']
        read_coupon_url = apijson1['data'][0]['remainCount']
        if read_coupon_url == 0:
            data_test1 = operate_excel.data(case_name=MyTest.name)[5]
            TestApi(url2=data_test1['url'], key=data_test1['key'], param=data_test1['param'],
                    way=data_test1['way']).selectway()
        try:
            self.assertEqual(int(expect_one['couponId']), actual_one, msg='预期和返回不一致')
            Log().info('对【后台优惠劵id】断言,断言结果--预期值%s == 实际值%s' % (expect_one['couponId'], actual_one))
        except:
            Log().warning('对【后台优惠劵id】断言,断言结果--预期值%s == 实际值%s' % (expect_one['couponId'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['value']), actual_two, msg='预期和返回不一致')
                Log().info('对【后台优惠劵面额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_two['value']), actual_two))
            except:
                Log().warning('对【后台优惠劵面额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_two['value']), actual_one))
                raise

    def testCase06(self, id=6):
        """下单返优惠劵和佣金"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        expect_three = operate_excel.change(asserexpect=data_test['expect3'])
        expect_four = operate_excel.change(asserexpect=data_test['expect4'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'], way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1['data'][0]['templateId']
        actual_two = apijson1['data'][0]['giftName']
        actual_three = apijson1['data'][0]['discountPrice']
        sql = operate_excel.get_palce(case_num=7,case_name=MyTest.name)['sql']
        actual_four = operate_db.Operate_db(case_num=7, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['templateId']), actual_one,msg='预期和返回不一致')
            Log().info('对【下单发放优惠劵id】断言,断言结果--预期值%s == 实际值%s' % (expect_one['templateId'], actual_one))
        except:
            Log().warning('对【下单发放优惠劵id】断言,断言结果--预期值%s == 实际值%s' % (expect_one['templateId'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['giftName'], actual_two, msg='预期和返回不一致')
                Log().info('对【下单发放优惠劵title】断言,断言结果--预期值%s == 实际值%s' % (expect_two['giftName'], actual_two))
            except:
                Log().warning('对【下单发放优惠劵title】断言,断言结果--预期值%s == 实际值%s' % (expect_two['giftName'], actual_two))
                raise
            finally:
                try:
                    self.assertEqual(int(expect_three['worth']), actual_three, msg='预期和返回不一致')
                    Log().info('对【下单发放优惠劵面额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_three['worth']), actual_three))
                except:
                    Log().warning('对【下单发放优惠劵面额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_three['worth']), actual_three))
                    raise
                finally:
                    try:
                        self.assertEqual(float(expect_four['orderDirectCommission']), actual_four, msg='预期和返回不一致')
                        Log().info(
                            '对【订单佣金】断言,断言结果--预期值%s == 实际值%s' % (expect_four['orderDirectCommission'], actual_four))
                    except:
                        Log().warning(
                            '对【订单佣金】断言,断言结果--预期值%s != 实际值%s' % (expect_four['orderDirectCommission'], actual_four))
                        raise
        '''
         校验下单成功后，收益明细详情
        now_comm_Cumulative, now_comm_sale, now_comm_today,banlance = operate_db.Operate_db.income_db()
        print('下单后累计收益：' % now_comm_Cumulative)
        print('下单后销售收益：' % now_comm_sale)
        print('下单后今日收益：' % now_comm_today)
        print('下单后账户余额：' % banlance)'''

    def testCase07(self, id=8):
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
        '''校验取消订单后，收益明细详情
        cancel_comm_Cumulative, cancel_comm_sale, cancel_comm_today = operate_db.Operate_db.income_db()
        print('取消订单后累计收益：' % cancel_comm_Cumulative)
        print('取消订单后下单收益：' % cancel_comm_sale)
        print('取消订单后今日收益：' % cancel_comm_today)'''

    def testCase08(self, id=9):
        """取消成功发送站内信"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'], way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % ( data_test['url'], data_test['key'], data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1['data'][0]['content']
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        excuse_sql = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        message_dict = json.loads(excuse_sql)
        actual_two = message_dict['messageSubLines'][0]['content']
        try:
            self.assertEqual(expect_one['content'], actual_one,msg='预期和返回不一致')
            Log().info('对【消息内容】断言,断言结果--预期值%s == 实际值%s' % (expect_one['content'], actual_one))
        except:
            Log().warning('对【消息内容】断言,断言结果--预期值%s != 实际值%s' % (expect_one['content'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(actual, actual_two,msg='预期和返回不一致')
                Log().info('对【取消订单消息展示订单号】断言,断言结果--预期值%s == 实际值%s' % (actual, actual_two))
            except:
                Log().warning(
                    '对【取消订单消息展示订单号】断言,断言结果--预期值%s == 实际值%s' % (actual, actual_two))
                raise
    '''def testCase5(self,id=6):
        #订单售后流程:判断订单状态
        #api端
        #下单后，处理数据库订单30分钟时间
        paid_time_sql = 'select b.* from trade_order_pay_record_r a left join trade_pay_record b on a.pay_record_id = b.id where a.ORDER_NUMBER = %d' %(actual)
        update_paidtime_sql = 'update trade_pay_record b join trade_pay_record_r a on b.ID=a.PAY_RECORD_ID set b.PAID_TIME = date_sub(now(), interval 1 hour) where a.ORDER_NUMBER=%d' %(actual)
        aftersale_url = 'https://shop.m.showjoy.com.cn/shop/afterSales/apply?orderNumber=%d' %(actual)
        #线上售后：wait 30分钟
        #sleep(3600)
        #生成售后订单号post
        global after_data
        after_data = json.loads(aftersale_url)['data']
        print(after_data)
        #后台部分
        #查询售后订单get
        web_aftersale = 'https://console-shop.showjoy.com.cn/shop/v1/after-sales/orders/get?afterSalesOrderNumber=%d&endTime&orderNumber=&expressNumber&page=1&pageSize=10&startTime&status=[0]&lossStatus=0&supplierId_begin&supplierId_end&supplierId&type=0&urgencyStatus=0' %(after_data)
        #获取售后订单详情get
        web_orderdetails = 'https://console-shop.showjoy.com.cn/shop/v1/after-sales/details?afterSalesOrderNumber=%d' %(after_data)
        #审核售后订单:客服post
        web_kefu_submit = 'https://shop.m.showjoy.com.cn/shop/afterSales/apply?afterSalesOrderNumber=%d' %(after_data)
        # 审核售后订单:供应商post
        web_yys_submit = 'https://console-shop.showjoy.com.cn/shop/v1/after-sales/loss/supplier/agree?afterSalesOrderNumber=%d'  %(after_data)

        test_data = operate_excel.data('zhuoxw')[id]
        expect_one = operate_excel.change(asserexpect=test_data['expect1'])
        expect_two = operate_excel.change(asserexpect=test_data['expect2'])
        Log().info('获取用例数据:%s' % test_data)
        apijson = TestApi(url2=test_data['url'].format(actual), key=test_data['key'], param=test_data['param'],
                              way=test_data['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (test_data['url'], test_data['key'],
                                                               test_data['param'], test_data['way']))
        apijson2 = json.loads(apijson)
        #期望值1
        actual_one = apijson2['isSuccess']
        sql = operate_excel.get_palce(num=id)['sql'].format(actual)
        #期望值2
        actual_two = operate_db.Operate_db(casenum=id,sql=sql).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']),actual_one,msg='预期和返回不一致')
            Log.info('对【订单售后是否成功】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【订单售后是否成功】断言,断言结果--售后成功预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))

        try:
            self.assertEqual('对【售后订单状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
            Log.info('对【售后订单状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
        except:
            Log().warning('对【售后订单状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['tradestatus'], actual_two))
            raise
    '''

    def testCase09(self,id=15):
        """下单选择优惠劵"""
        #consumption = 'SELECT CONSUMPTION_LIMIT FROM assets_coupon where USER_ID= 10464749 and IS_DELETE=0 and START_TIME <= NOW() and END_TIME > NOW() AND GMT_USED is null ORDER BY START_TIME '
        #sku_price = 'select price from pc_sku where id = 226287'
        data_test = operate_excel.data('zhuoxw1')[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],data_test['param'], data_test['way']))

        apijson1 = json.loads(apijson)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        quan = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).more_perform()
        global actual_couponid, actual_couponworth
        actual_couponid = quan['ID']
        actual_couponworth = quan['WORTH']
        try:
            self.assertIsNotNone(actual_couponid, msg='实际值不存在')
            Log().info('对【优惠劵列表】断言,获取第一张优惠劵id%s' % (actual_couponid))
        except:
            Log().warning('对【优惠劵列表】断言，无可用优惠劵')
            raise
        finally:
            try:
                self.assertEqual(int(expect_one['id']), actual_couponid,msg='预期和返回不一致')
                Log().info('对【获取可用优惠劵】断言,断言结果--预期值{0} == 实际值{1}'.format(expect_one['id'], actual_couponid))
            except:
                Log().warning('对【获取可用优惠劵】断言,断言结果--预期值%s == 实际值%s' % (expect_one['id'], actual_couponid))
                raise

    def testCase10(self,id=16):
        """优惠劵抵扣订单金额确认"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(actual_couponid), key=data_test['key'], param=data_test['param'],way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'], data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1['data']['itemsTotalPrice']
        expect_totalPrice = float(expect_one['itemsTotalPrice']) - actual_couponworth
        actual_totalPrice = actual_one - actual_couponworth
        if expect_totalPrice == actual_totalPrice:
            Log().info('抵扣优惠卷金额正确：预期值%s == 实际值%s' % (expect_totalPrice,actual_totalPrice))
        else:
            Log().warning('抵扣优惠卷金额不正确:预期值%s != 实际值%s' % (expect_totalPrice,actual_totalPrice))
        try:
            self.assertEqual(int(expect_one['itemsTotalPrice']), actual_one,msg='预期和返回不一致')
            Log().info('对【订单金额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_one['itemsTotalPrice']), actual_one))
        except:
            Log().warning('对【订单金额】断言,断言结果--预期值%s == 实际值%s' % (int(expect_one['itemsTotalPrice']), actual_one))
            raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
