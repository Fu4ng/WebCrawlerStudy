# --------------------------------------#
#
# Created by Fu4ng on 2017/8/8.
#
# 博文地址:
# --------------------------------------#


import urllib.request
import urllib.parse
import http.cookiejar

# 登录信息
acount_data = {
    'username': '13015957906',
    'password': 'kkuu9038'
}
# 获取真实的登录地址
login_url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# 模拟浏览器
postdata = urllib.parse.urlencode(acount_data).encode('utf-8')
login_req = urllib.request.Request(login_url, postdata)
login_req.add_header('User-Agent',
                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
login_data = urllib.request.urlopen(login_url).read()
f = open('CSDN.html', 'wb')
f.write(login_data)
f.close()


# 爬取第二个网页
