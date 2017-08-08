# --------------------------------------#
#
# Created by Fu4ng on 2017/8/8.
#
# 博文地址:
# --------------------------------------#



import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LQoSc"
postdata = urllib.parse.urlencode({
    'username': 'weisuen',
    'password': 'aA123456'
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
data = urllib.request.urlopen(req).read()
f = open('ChinaUnix.html', 'wb')
f.write(data)
f.close()
url2 = 'http://bbs.chinaunix.net/home.php?mod=space&do=pm'
req2 = urllib.request.Request(url2, postdata)
req2.add_header('User-Agent',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
data2 = urllib.request.urlopen(req2).read()
f2 = open('ChinaUnix2.html', 'wb')
f2.write(data2)
f2.close()
