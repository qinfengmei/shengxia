import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import json
import urllib.request
from Branch.log import Log
import requests

def Send_dingding(cases, fail_case, fail_result):
    url = "https://oapi.dingtalk.com/robot/send?access_token=7b7bfd8536388cd11d8fe6dbafa43dacdfd889451f83f9206bac7b5ceada6dc4"  # url为机器人的webhook
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    try:
        content = "{0}\n" \
                  "{1}\n" \
                  "功能模块：达人圈、订单交易、地址管理、购物车、个人中心操作\n" \
                  "执行过程：\n" \
                  "1.达人圈-发布达人圈，请求接口publishNote,对返回的isSuccess和msg字段断言\n" \
                  "2.达人圈-获取发布内容，请求接口getUserPublish,对返回的content和noteid字段断言\n" \
                  "3.达人圈-点赞内容，请求接口like,对返回的isSuccess和like_num字段断言\n" \
                  "4.达人圈-收藏内容，请求接口collection,对返回的isSuccess和collect_num字段断言\n" \
                  "失败用例名称：{2}\n" \
                  "请登录http://47.99.83.80:8881/jenkins/job/interface_online/HTML_20Report/ 查看详细报告，账密admin/showjoy@123".format(cases, fail_case, fail_result)
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        sendData = json.dumps(data)
        sendData = sendData.encode("utf-8")
        request = requests.post(url=url, data=sendData, headers=header)
        opener = urllib.request.urlopen(request)
        Log().info('钉钉通知成功{0}'.format(opener.read()))
    except:
        Log().info('钉钉通知失败')
        raise
