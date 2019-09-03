# -*- coding: utf-8 -*-
import os, json
import pymysql, redis, re
from Branch.log import Log
from config.readyaml import Getyaml
from Branch import operate_excel
from config import globalparam

# 获取db.yaml数据
curPath = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(curPath, "db.yaml")

class Operate_db():
    """
    连接执行数据库
    """
    trade_state = 1
    def __init__(self, case_num, sql, case_name):
        """
        :param casenum: 用例序号0,1,2...
        :param sql: sql语句
        """
        self.case_num = case_num
        self.sql = sql
        self.case_name = case_name

    def connect_db(self):
        """
        连接数据库
        :return:连接信息
        """
        data = Getyaml().get_data(self.case_num, self.case_name)
        self.database = operate_excel.get_palce(self.case_num, self.case_name)['database']
        db1 = pymysql.connect(data[0], data[1], data[2],self.database ,charset='utf8')
        Log().info("连接数据库成功")
        return db1

    def Perform(self):
        """
        增删改查操作,返回单个字段和记录
        :return: {"key": "value"}
        """
        db = self.connect_db()
        cursor = db.cursor()
        environment = operate_excel.get_palce(self.case_num, self.case_name)['db']
        version = db.server_version
        Log().info('成功登录%s环境数据库：%s，版本为：%s，执行SQL：%s' % (environment, self.database, version, self.sql))
        if "SELECT" in self.sql or "select" in self.sql:
            try:
                cursor.execute(self.sql)
                results = cursor.fetchall()
                Log().info('查询结果：%s' % results[0][0])
                return results[0][0]
            except:
                Log().info("Error: unable to fetch data")
                raise
        elif "UPDATE" in self.sql or "update" in self.sql:
            try:
                cursor.execute(self.sql)
                db.commit()
                Log().info("更新数据成功")
            except:
                db.rollback()
                Log().info("Error：Has been rolled back")
                raise
        db.close()

    def more_perform(self):
        """
        增删改查操作,返回多个字段和记录
        :return: [{"key1": "value1", "key2", "value2"},{"key1": "value1", "key2", "value2"} ....]
        """
        db = self.connect_db()
        cursor = db.cursor()
        environment = operate_excel.get_palce(self.case_num, self.case_name)['db']
        version = db.server_version
        Log().info('成功登录%s环境数据库：%s，版本为：%s，执行SQL：%s' % (environment, self.database, version, self.sql))
        try:
            cursor.execute(self.sql)
            results = cursor.fetchall()
            Log().info('sql查询结果：{0}'.format(results))
            sql1 = self.sql.replace(' ', '')
            find_keys = re.findall("^select(.+?)from", sql1)
            keys = find_keys[0].split(",")
            list_result = []
            for i in results:
                for num in range(len(i)):
                    dict_result = {}
                    dict_result[keys[num]] = i[num]
                list_result.append(dict_result)
            if len(results) == 1:
                return dict_result
            elif len(results) > 1:
                return list_result
        except:
            Log().info("Error: unable to fetch data")
            raise
        db.close()

    def income_db(self):
        """
        收益计算
        :return: 累计收益/销售收益/今日收益/账户余额
        """
        db = self.connect_db()
        cursor = db.cursor()
        # 累计收益-增加
        comm_Cumulative_add = 'select ROUND(coalesce(sum(COMMISSION),0),2) from shop.shop_commission sc where sc.commission_type in (200,201,300,301,210,211,310,311,500,501,800,704) and sc.is_delete = 0 and sc.shop_id = 546082'
        # 累计收益-减少
        comm_back = 'select rc.commission from shop.refund_commission rc where rc.commission_freeze = 0 and rc.shop_id = 546082'
        # 累计收益
        comm_Cumulative = comm_Cumulative_add - comm_back
        # 销售收益-增加
        comm_sale_add = 'SELECT ROUND(coalesce(sum(COMMISSION), 0), 2) FROM shop_commission WHERE SHOP_ID = 546082 AND IS_DELETE = 0 AND COMMISSION_TYPE IN(200, 300, 210, 310)'
        # 销售收益-减少
        comm_sale_reduce = 'SELECT SUM(COMMISSION) FROM refund_commission WHERE SHOP_ID = 546082 AND COMMISSION_FREEZE = 0'
        # 销售收益
        comm_sale = comm_sale_add - comm_sale_reduce
        # 今日收益-增加
        comm_today_add = 'SELECT ROUND(coalesce(sum(COMMISSION), 0), 2) FROM shop_commission WHERE SHOP_ID = 546082 AND GMT_CREATE <= now() and GMT_CREATE > DATE_SUB(CURDATE(), INTERVAL 0 day) AND COMMISSION_TYPE in (200, 201, 301, 300, 500, 501, 210, 211, 311, 310) AND IS_DELETE = 0'
        # 今日收益-减少
        comm_today_reduce = 'SELECT IFNULL(sum(commission), 0) FROM refund_commission WHERE REFUND_RECORD_ID IN(SELECT ID FROM refund_record WHERE order_number in (select order_number from shop_commission, shop_commission_order_r where shop_commission.ID = shop_commission_order_r.SHOP_COMMISSION_ID and shop_commission.SHOP_ID = 546082 and shop_commission.GMT_CREATE <= now() and shop_commission.GMT_CREATE > DATE_SUB(CURDATE(), INTERVAL 0 day) and shop_commission_order_r.IS_DELETE = 0 and shop_commission.IS_DELETE = 0 GROUP BY order_number) and source_shop_id = 380800 and status in (2, 4) and refund_record.IS_DELETED = false ) AND shop_Id = 546082 and commission_freeze = 0 and commission_freeze = 0'
        # 今日收益
        comm_today = comm_today_add - comm_today_reduce
        # 账户余额-增加
        banlance_add = 'SELECT ROUND(coalesce(sum(COMMISSION), 0), 2) FROM shop_commission WHERE SHOP_ID = 546082 AND IS_DELETE = 0 and IS_FREEZE = 1'
        # 账户余额-减少
        banlance_reduce = 'SELECT SUM(COMMISSION) FROM refund_commission WHERE SHOP_ID = 546082 AND COMMISSION_FREEZE = 0'
        # 账户余额
        banlance = banlance_add - banlance_reduce
        return comm_Cumulative, comm_sale, comm_today, banlance
        db.close()

class Operate_redis():
    """
    连接操作redis
    """
    def __init__(self, name='shop-ui:login', key='15868147450', env='kf'):
        self.name = name
        self.key = key
        self.env = env
    def connect(self):
        con_info = Getyaml().get_redis(env=self.env)
        try:
            r = redis.Redis(host=con_info[0], port=con_info[1], password=con_info[2], db=0)
            data1 = str(r.hget(name='showjoy_login_captcha_cache:{0}'.format(self.name), key='15868147451'), encoding = "utf8")
            data2 = data1.replace("false", "0")
            data3 = json.loads(data2.replace("true", "0"))
            data = data3['code']
            Log().info('查询结果：{0}'.format(data))
            return data
        except:
            Log().info('查询redis失败')
            raise

# Operate_redis().connect()
# sql2 = "select sum(collect_num),sum(like_num),sum(share_num) from interaction_info where note_id in (select note_id from note_info_shadow where user_id = '9140391') or note_id in (select id from note_info where user_id = '9140391')"
# Operate_db(24,sql2).more_perform()