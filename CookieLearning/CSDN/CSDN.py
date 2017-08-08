# --------------------------------------#
#
# Created by Fu4ng on 2017/8/8.
#
# 博文地址:
# --------------------------------------#


# csdn的登录表单有5个数据，其中有3个隐藏的，明天再完整代码。已找到思路：
# 获取登录界面的代码，在用正则表达式拿到2个动态分配的数据，done
import urllib.request
import urllib.parse
import http.cookiejar


# 获取真实的登录地址
login_url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# 模拟浏览器
postdata = urllib.parse.urlencode(acount_data).encode('utf-8')
login_req = urllib.request.Request(login_url, postdata)
login_req.add_header('User-Agent',
                     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11')
# Cookie
cjar = http.cookiejar.CookieJar()
login_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(login_opener)
# 保存到本地
login_data = urllib.request.urlopen(login_url).read()
f = open('D:\GitHubRepository\WebCrawlerStudy\CookieLearning\CSDN\CSDN.html', 'wb')
f.write(login_data)
f.close()

# 爬取第二个网页
bloglist_url = 'http://write.blog.csdn.net/postlist'
bloglist_data = urllib.request.urlopen(bloglist_url).read()
f2 = open('D:\GitHubRepository\WebCrawlerStudy\CookieLearning\CSDN\CSDN2.html', 'wb')
f2.write(bloglist_data)
f2.close()
