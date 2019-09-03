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

    name = 'liguo'

    def setUp(self):
        Log().info('测试用例开始执行')

    def testCase01(self, id=23):
        """发布达人圈"""
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
                Log().info('对【发布结果】断言,断言结果--预期值%s == 实际值%s' % (expect_two['msg'], actual_two))
            except:
                Log().warning('对【发布结果】断言,断言结果--预期值%s != 实际值%s' % (expect_two['msg'], actual_two))
                raise

    def testCase02(self, id=24):
        """获取个人发布内容"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        sql = operate_excel.get_palce(case_num=id)['sql']
        expect_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson1 = json.loads(apijson)
        actual_one = apijson1["data"][0]["noteBaseInfo"]["content"]
        actual_two = apijson1["data"][0]["noteBaseInfo"]["noteId"]
        global note_id
        note_id = actual_two
        try:
            self.assertEqual(expect_one['content'], actual_one, msg='预期和返回不一致')
            Log().info('对【发布内容】断言,断言结果--预期值%s == 实际值%s' % (expect_one['content'], actual_one))
        except:
            Log().warning('对【发布内容】断言,断言结果--预期值%s != 实际值%s' % (expect_one['content'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(expect_two, actual_two, msg='预期和返回不一致')
                Log().info('对【发布内容id】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【发布内容id】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise

    def testCase03(self, id=25):
        """点赞内容"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(note_id), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_id)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('点赞成功，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('点赞成功，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['like_num']), actual_two, msg='预期和返回不一致')
                Log().info('对【点赞状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['like_num'], actual_two))
            except:
                Log().warning('对【点赞状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['like_num'], actual_two))
                raise

    def testCase04(self, id=26):
        """收藏内容"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(note_id), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_id)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('收藏成功，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('收藏失败，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['collect_num']), actual_two, msg='预期和返回不一致')
                Log().info('对【收藏状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['collect_num'], actual_two))
            except:
                Log().warning('对【收藏状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['collect_num'], actual_two))
                raise

    def testCase05(self, id=27):
        """关注他人"""
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
        actual_two = apijson2["data"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('关注成功，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('关注失败，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['data']), actual_two, msg='预期和返回不一致')
                Log().info('对【已关注人数】断言,断言结果--预期值%s == 实际值%s' % (expect_two['data'], actual_two))
            except:
                Log().warning('对【已关注人数】断言,断言结果--预期值%s != 实际值%s' % (expect_two['data'], actual_two))
                raise

    def testCase06(self, id=28):
        """查看已关注的用户信息"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"][0]["userName"]
        actual_two = apijson2["data"][0]["shopId"]
        try:
            self.assertEqual(expect_one['userName'], actual_one, msg='预期和返回不一致')
            Log().info('对【用户名】断言,断言结果--预期值%s == 实际值%s' % (expect_one['userName'], actual_one))
        except:
            Log().warning('对【用户名】断言,断言结果--预期值%s != 实际值%s' % (expect_one['userName'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['shopId']), actual_two, msg='预期和返回不一致')
                Log().info('对【店铺id】断言,断言结果--预期值%s == 实际值%s' % (expect_two['shopId'], actual_two))
            except:
                Log().warning('对【店铺id】断言,断言结果--预期值%s != 实际值%s' % (expect_two['shopId'], actual_two))
                raise

    def testCase07(self, id=29):
        """查看获赞和收藏数"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        sql = operate_excel.get_palce(case_num=id)['sql']
        expects = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).more_perform()
        expect_one = expects['sum(collect_num)']
        expect_two = expects['sum(like_num)']
        expect_three = expects['sum(share_num)']
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                   data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["data"]["collectedNum"]
        actual_two = apijson2["data"]["likedNum"]
        actual_three = apijson2["data"]["sharedNum"]
        try:
            self.assertEqual(int(expect_one), actual_one, msg='预期和返回不一致')
            Log().info('对【收藏数】断言,断言结果--预期值%s == 实际值%s' % (expect_one, actual_one))
        except :
            Log().warning('对【收藏数】断言,断言结果--预期值%s != 实际值%s' % (expect_one, actual_one))
            raise
        else:
            Log().info('第1条断言成功')
        finally:
            try:
                self.assertEqual(int(expect_two), actual_two, msg='预期和返回不一致')
                Log().info('对【点赞数】断言,断言结果--预期值%s == 实际值%s' % (expect_two, actual_two))
            except:
                Log().warning('对【点赞数】断言,断言结果--预期值%s != 实际值%s' % (expect_two, actual_two))
                raise
            finally:
                try:
                    self.assertEqual(int(expect_three), actual_three, msg='预期和返回不一致')
                    Log().info('对【被分享数】断言,断言结果--预期值%s == 实际值%s' % (expect_three, actual_three))
                except :
                    Log().warning('对【被分享数】断言,断言结果--预期值%s != 实际值%s' % (expect_three, actual_three))
                    raise

    def testCase08(self, id=30):
        """取消点赞"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(note_id), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_id)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('取消点赞，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('取消点赞，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['like_num']), actual_two, msg='预期和返回不一致')
                Log().info('对【点赞状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['like_num'], actual_two))
            except:
                Log().warning('对【点赞状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['like_num'], actual_two))
                raise

    def testCase09(self, id=31):
        """取消收藏"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(note_id), key=data_test['key'], param=data_test['param'],
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["isSuccess"]
        sleep(1)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_id)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('取消收藏，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('取消收藏，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['collect_num']), actual_two, msg='预期和返回不一致')
                Log().info('对【收藏状态】断言,断言结果--预期值%s == 实际值%s' % (expect_two['collect_num'], actual_two))
            except:
                Log().warning('对【收藏状态】断言,断言结果--预期值%s != 实际值%s' % (expect_two['collect_num'], actual_two))
                raise

    def testCase10(self, id=32):
        """取消关注"""
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
        actual_two = apijson2["data"]
        try:
            self.assertEqual(int(expect_one['isSuccess']), actual_one, msg='预期和返回不一致')
            Log().info('取消关注，对【isSuccess】断言,断言结果--预期值%s == 实际值%s' % (expect_one['isSuccess'], actual_one))
        except:
            Log().warning('取消关注，对【isSuccess】断言,断言结果--预期值%s != 实际值%s' % (expect_one['isSuccess'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['data']), actual_two, msg='预期和返回不一致')
                Log().info('对【已关注人数】断言,断言结果--预期值%s == 实际值%s' % (expect_two['data'], actual_two))
            except:
                Log().warning('对【已关注人数】断言,断言结果--预期值%s != 实际值%s' % (expect_two['data'], actual_two))
                raise

    def testCase11(self, id=33):
        """发表评论"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'], key=data_test['key'], param=data_test['param'].replace("{0}", str(note_id)),
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql']
        actual_one = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        actual_two = apijson2["data"]
        try:
            self.assertEqual(expect_one['comment_text'], actual_one, msg='预期和返回不一致')
            Log().info('对【评论内容】断言,断言结果--预期值%s == 实际值%s' % (expect_one['comment_text'], actual_one))
        except:
            Log().warning('对【评论内容】断言,断言结果--预期值%s != 实际值%s' % (expect_one['comment_text'], actual_one))
            raise
        finally:
            try:
                self.assertIsNotNone(actual_two, msg='实际值不存在')
                Log().info('已发送【%s】条评论' % (actual_two))
            except:
                Log().warning('评论发送失败')
                raise

    def testCase12(self, id=34):
        """删除发布内容"""
        data_test = operate_excel.data(case_name=MyTest.name)[id]
        expect_one = operate_excel.change(asserexpect=data_test['expect1'])
        expect_two = operate_excel.change(asserexpect=data_test['expect2'])
        Log().info('获取用例数据:%s' % data_test)
        apijson = TestApi(url2=data_test['url'].format(note_id), key=data_test['key'], param=data_test['param'].format(note_id),
                          way=data_test['way']).selectway()
        Log().info('请求传入数据：url:%s,key:%s,参数:%s,请求方式：%s' % (data_test['url'], data_test['key'],
                                                           data_test['param'], data_test['way']))
        apijson2 = json.loads(apijson)
        actual_one = apijson2["msg"]
        sql = operate_excel.get_palce(case_num=id, case_name=MyTest.name)['sql'].format(note_id)
        actual_two = operate_db.Operate_db(case_num=id, sql=sql, case_name=MyTest.name).Perform()
        try:
            self.assertEqual(expect_one['msg'], actual_one, msg='预期和返回不一致')
            Log().info('删除成功，对【删除结果】断言,断言结果--预期值%s == 实际值%s' % (expect_one['msg'], actual_one))
        except:
            Log().warning('删除失败，对【删除结果】断言,断言结果--预期值%s != 实际值%s' % (expect_one['msg'], actual_one))
            raise
        finally:
            try:
                self.assertEqual(int(expect_two['COUNT(*)']), actual_two, msg='预期和返回不一致')
                Log().info('对【删除数】断言,断言结果--预期值%s == 实际值%s' % (expect_two['COUNT(*)'], actual_two))
            except:
                Log().warning('对【删除数】断言,断言结果--预期值%s != 实际值%s' % (expect_two['COUNT(*)'], actual_two))
                raise

    def tearDown(self):
        Log().info('测试用例执行完毕')
        Log().info('----------------------------------')

if __name__ == "__main__":
    unittest.main()
