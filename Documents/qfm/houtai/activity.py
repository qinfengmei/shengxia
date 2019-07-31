# 后台--运营管理--活动管理


#!usr/bin/env python
#-*- coding:utf-8-*-
import requests
from houtai.denglu import  select_user
import json
url = "https://console-shop.showjoy.com/shop/v1/activity/list/get?page=1&pageSize=20&activityId=&name=&skuId=&status=0&type=0"
data = {
    "page": 1,
    "pageSize": 20,
    "activityId"
    "name"
    "skuId"
    "status": 0,
    "type": 0
}
cookie = {
    "shop_console_login_username":"qfm",
    "shop_console_login_remember":"true",
    "shop_console_commodity_tablehead":"[{%22name%22:%22%E4%B8%BB%E5%9B%BE%22%2C%22param%22:%22spuMasterImage%22%2C%22value%22:true}%2C{%22name%22:%22spuId%22%2C%22param%22:%22spuId%22%2C%22value%22:true}%2C{%22name%22:%22%E5%95%86%E5%93%81%E5%90%8D%E7%A7%B0%22%2C%22param%22:%22title%22%2C%22value%22:true}%2C{%22name%22:%22%E5%93%81%E7%89%8C%22%2C%22param%22:%22brandName%22%2C%22value%22:true}%2C{%22name%22:%22%E7%B1%BB%E7%9B%AE%22%2C%22param%22:%22cateNames%22%2C%22value%22:true}%2C{%22name%22:%22%E4%BE%9B%E5%BA%94%E5%95%86%22%2C%22param%22:%22supplierName%22%2C%22value%22:true}%2C{%22name%22:%22%E5%AE%9E%E5%90%8D%E8%AE%A4%E8%AF%81%22%2C%22param%22:%22isNeedCardType%22%2C%22value%22:false}%2C{%22name%22:%22%E8%BF%90%E8%B4%B9%E6%A8%A1%E6%9D%BF%22%2C%22param%22:%22freightTemplateId%22%2C%22value%22:false}%2C{%22name%22:%22%E9%99%90%E5%94%AE%E6%A8%A1%E6%9D%BF%22%2C%22param%22:%22restrictedSaleId%22%2C%22value%22:false}%2C{%22name%22:%22%E6%90%9C%E7%B4%A2%E7%8A%B6%E6%80%81%22%2C%22param%22:%22searchStatus%22%2C%22value%22:false}%2C{%22name%22:%22skuId%22%2C%22param%22:%22skuId%22%2C%22value%22:true}%2C{%22name%22:%22%E8%A7%84%E6%A0%BC%22%2C%22param%22:%22spec%22%2C%22value%22:true}%2C{%22name%22:%22%E5%B8%82%E5%9C%BA%E4%BB%B7%22%2C%22param%22:%22originalPrice%22%2C%22value%22:false%2C%22hide%22:true}%2C{%22name%22:%22%E8%BE%BE%E4%BA%BA%E5%BA%97%E4%BB%B7%22%2C%22param%22:%22shopPrice%22%2C%22value%22:false%2C%22hide%22:true}%2C{%22name%22:%22%E4%BD%A3%E9%87%91%E7%8E%87%22%2C%22param%22:%22commissionRate%22%2C%22value%22:false%2C%22hide%22:true}%2C{%22name%22:%22%E8%99%9A%E6%8B%9F%E5%BA%93%E5%AD%98%22%2C%22param%22:%22inventory%22%2C%22value%22:true}%2C{%22name%22:%22%E9%94%80%E5%94%AE%E7%8A%B6%E6%80%81%22%2C%22param%22:%22onsaleStatus%22%2C%22value%22:true}%2C{%22name%22:%22%E9%80%80%E8%B4%A7%E5%9C%B0%E5%9D%80%22%2C%22param%22:%22refundAddressId%22%2C%22value%22:true%2C%22innerHide%22:true}]",
    "token":select_user(),
    "shop_console_userinfo":"{%22email%22:%22%22%2C%22gmtCreate%22:1539332120000%2C%22gmtModified%22:1555751499000%2C%22id%22:9340790%2C%22image%22:%22https://cdn1.showjoy.com/shop/user_head/20190505/WTTDFFMBSXCZNRK8ACSN1557049061261.jpg%22%2C%22isEnable%22:true%2C%22isFake%22:0%2C%22nick%22:%22qfm%22%2C%22sexType%22:%22%22%2C%22tel%22:%2218768278576%22%2C%22username%22:%22qfm%22%2C%22account_type%22:1%2C%22byname%22:%22%E7%9B%9B%E5%A4%8F%22%2C%22realName%22:%22%E7%9B%9B%E5%A4%8F%22%2C%22supplierId%22:[640]}",
}
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"

}
aa = requests.get(url=url,data=data,headers=headers, cookies=cookie)
print(aa)
bb = aa.text
cc = json.loads(bb)
# cc = json.dumps(bb)
# print(cc['data']['activityId'])
print(cc)
print(cc['data'][0]['activityId'])
