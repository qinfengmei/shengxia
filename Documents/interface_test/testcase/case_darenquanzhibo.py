# -*- coding: utf-8 -*-
# @Date    : 2019-05-27
# @Author  : 立果
# @model   ：达人圈
import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import unittest
import json
from time import sleep
from Public.select_request import TestApi
from Branch import operate_excel
from Branch.log import Log
from Branch import operate_db


class MyTest(unittest.TestCase):
    """达人圈"""

    name = 'shengxia'


    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase01(self, id=0):
        """发布达人圈直播"""
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
        actual_two = apijson1["msg"]
        actual_three = apijson1["data"]["noteId"]
        global note_Id
        note_Id = actual_three
        print(note_Id)
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two['msg'], actual_two, msg='预期和返回不一致')
                Log().info('对【发布结果】断言,断言结果--预期值%s == 实际值%s' % (expect_two['msg'], actual_two))
            except:
                Log().warning('对【发布结果】断言,断言结果--预期值%s != 实际值%s' % (expect_two['msg'], actual_two))
                raise

    def testCase02(self,id=1):
        """直播推流成功"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据：%s' % data_test)
        apijson2 = TestApi(url2=data_test['url'],key=data_test['key'],param=data_test['param'].replace("{0}",str(note_Id)),
                           way=data_test['way']).selectway()

        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                    data_test['param'], data_test['way']))
        print(apijson2)
        apijson1 = json.loads(apijson2)
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        actual_one = apijson1["isSuccess"]
        actual_two = operate_db.Operate_db(case_num=id,sql=sql,case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']),actual_one,msg='预期和返回不一致')
            Log().info('推流成功，对【isSuccess】断言,断言结果--预期值%s == 实际值%s'%(expect_one['isSuccess'],actual_one))
        except:
            Log().warning('推流失败，对【isSuccess】断言,断言结果--预期值%s == 实际值%s'%(expect_one['isSuccess'],actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['live_status']), actual_two, msg='预期和返回不一致')
                Log().info('对【直播状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对【直播状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise

    def testCase03(self,id =2):
        """观看直播人数"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据：%s' % data_test)
        apijson2 = TestApi(url2=data_test['url'].format(note_Id), key=data_test['key'],
                           param=data_test['param'],
                           way=data_test['way']).selectway()

        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        print(apijson2)
        apijson1 = json.loads(apijson2)
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_Id)
        actual_one = apijson1["isSuccess"]
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('有人数观看，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('无人数观看，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['live_status']), actual_two, msg='预期和返回不一致')
                Log().info('对观看人数断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对观看人数断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise
    def testCase04(self,id=3):
        """观众加入直播"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据：%s' % data_test)
        apijson2 = TestApi(url2=data_test['url'].format(note_Id), key=data_test['key'],
                           param=data_test['param'],
                           way=data_test['way']).selectway()

        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))

        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_Id)
        expect_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        print(apijson2)
        apijson1 = json.loads(apijson2)
        actual_one = apijson1["isSuccess"]
        sleep(1)
        actual_two = apijson1["data"]["pullUrl"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('加入成功，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('加入失败，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two, actual_two, msg='预期和返回不一致')
                Log().info('对【加入状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【加入状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise
    def testCase05(self,id=4):
        """观众对直播点赞"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取测试用例：%s'%data_test)
        apijson = TestApi(url2=data_test['url'],param=data_test['param'].replace("{0}",str(note_Id)),key=data_test['key'],way=data_test['way']).selectway()
        Log().info('请求传入的数据：url:%s,way:%s,param:%s,key:%s'%(data_test['url'],data_test['way'],data_test['param']
                                                            ,data_test['key']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id,case_name=MyTest.name)['sql'].format(note_Id)
        actual_two = operate_db.Operate_db(case_num=id,sql=sql,case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']),actual_one,msg='预期和返回不一致')
            Log().info('点赞成功，对【isSuccess】断言，断言结果--预期值%s==实际值%s'%(expect_one['isSuccess'],actual_one))
        except:
            Log().warning('点赞失败，对【isSuccess】断言，断言结果--预期值%s==实际值%s'%(expect_one['isSuccess'],actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['live_status']),actual_two,msg='预期和返回不一致')
                Log().info('对【直播状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对【直播状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise

    def testCase06(self,id=5):

        """观众对主播进行关注/取关/互相关注"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('开始执行测试用例:%s'% data_test)
        apijson = TestApi(url2=data_test['url'],param=data_test['param'],key=data_test['key'],way=data_test['way']).selectway()
        Log().info('请求传入的数据：url：%s,param：%s，key：%s，way：%s'%(data_test['url'],data_test['param'],data_test['key'],data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id,case_name=MyTest.name)['sql'].format(note_Id)
        actual_two = operate_db.Operate_db(case_num=id,sql=sql,case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int((expect_one)['isSuccess']),actual_one,msg='预期和返回不一致')
            Log().info('关注/取关/互关成功，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('关注/取关/互关失败，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
            raise

        finally:
            try:
                self.assertEqual(int(expect_two['live_status']), actual_two, msg='预期和返回不一致')
                Log().info('对【直播状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对【直播状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise

    def testCase07(self,id=6):
        """结束直播"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('开始执行测试用例：%s'% data_test)
        apijson = TestApi(url2=data_test['url'],key=data_test['key'],param=data_test['param'].replace("{0}",str(note_Id)),way=data_test['way']).selectway()
        Log().info('请求传入的数据：url:%s,key:%s,param:%s,way:%s'%(data_test['url'],data_test['key'],data_test['param'],data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        sql = operate_excel.get_palce(case_num=id,case_name=MyTest.name)['sql'].format(note_Id)
        actual_two = operate_db.Operate_db(case_name=MyTest.name,case_num=id,sql=sql).Perform()
        try:
            self.assertEqual(int((expect_one)['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('结束直播成功，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('结束直播失败，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['live_status']), actual_two, msg='预期和返回不一致')
                Log().info('对【直播状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对【直播状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise
    def testCase08(self,id =7):
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('测试用例开始执行：%s'% data_test)
        apijson = TestApi(url2=data_test['url'].replace("{0}",str(note_Id)),key= data_test['key'],param=data_test['param'],way=data_test['way']).selectway()
        Log().info('请求传入的数据：url:%s,key:%s,param:%s,way:%s'%(data_test['url'],data_test['key'],data_test['param'],data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["isSuccess"]
        sql = operate_excel.get_palce(case_num=id,case_name=MyTest.name)['sql'].format(note_Id)
        actual_two = operate_db.Operate_db(case_name=MyTest.name,case_num=id,sql=sql).Perform()
        try:
            self.assertEqual(int((expect_one)['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('结束直播成功，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('结束直播失败，对【isSuccess】断言，断言结果--预期值%s==实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['live_status']), actual_two, msg='预期和返回不一致')
                Log().info('对【直播状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['live_status'], actual_two))
            except:
                Log().warning('对【直播状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['live_status'], actual_two))
                raise
    def testCase09(self,id=8):
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('测试用例开始执行：%s'%data_test)
        apijson = TestApi(url2=data_test['url'].format(note_Id),param=data_test['param'],way=data_test['way'],key=data_test['key']).selectway()
        Log().info('请求传入的数据：url:%s,param:%s,way:%s,key:%s'%(data_test['url'],data_test['param'],data_test['way'],data_test['key']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["msg"]
        sql = operate_excel.get_palce(case_name=MyTest.name,case_num=id)['sql'].format(note_Id)
        actual_two = operate_db.Operate_db(case_num=id,case_name=MyTest.name,sql=sql).Perform()
        try:
            self.assertEqual((expect_one)['msg'],actual_one,msg='预期和返回不一致')
            Log().info('删除直播成功，对【msg】断言，断言结果--预期值%s==实际值%s'%(expect_one['msg'],actual_one))
        except:
            Log().info('删除直播成功，对【msg】断言，断言结果--预期值%s==实际值%s'%(expect_one['msg'],actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['COUNT(*)']),actual_two,msg='预期和返回不一致')
                Log().info('对【删除结果】断言，断言结果--预期结果%s==实际值%s'%(expect_two['COUNT(*)'],actual_two))
            except:
                Log().warning('对【删除结果】断言，断言结果--预期结果%s!=实际值%s'%(expect_two['COUNT(*)'],actual_two))

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')
if __name__ == "__main__":
    unittest.main()

