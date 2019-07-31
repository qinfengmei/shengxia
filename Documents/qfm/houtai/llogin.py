import requests
response = requests.get("http://www.baidu.com")
print(response.cookies)


for key,value in response.cookies.items():
    print(key+"="+value)


def select_user():
    session = requests.Session()
    r = session.get("http://www.baidu.com").cookies
    # cookie = requests.utils.dict_from_cookiejar(r)
    # print(cookie)
    # print(r.text)
    r.encoding = 'utf-8'
    cookie = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookie)
    # token = cookie['token']
    # return token
    return cookie
select_user()