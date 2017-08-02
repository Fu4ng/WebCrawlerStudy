# --------------------------------------#
#
# Created by Fu4ng on 2017/8/2.
#
# 博文地址:
# --------------------------------------#
import urllib.request
import urllib.parse

# # GET
# keyword = 'keyword'  # 你想搜索的关键字
# """
# 如果关键字是中文的话，涉及到编码
# keyword = "中文关键字"
# keyword_code = urllib.request.quote(keyword)
# url = "http://baidu.com/s?wd="+keyword_code
# """
# url = "http://baidu.com/s?wd=" + keyword
# req = urllib.request.Request(url)
# data = urllib.request.urlopen(req).read()
# print(data)

# # Post
# url = "http://www.iqianyue.com/mypost"
# postdata = urllib.parse.urlencode({"name": "test", "pass": "lolp"}).encode("utf-8")
# req = urllib.request.Request(url, postdata)
# # 模拟浏览器
# req.add_header(
#     'User-Agent',
#     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
# data = urllib.request.urlopen(req).read()
# fhandle = open("post.html", 'wb')
# fhandle.write(data)
# fhandle.close()


# #代理服务器的设置
# Error 10061
# def use_proxy(proxy_addr,url):
#     import urllib.request
#     proxy = urllib.request.ProxyHandler({'http':proxy_addr})
#     opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8')
#     return data
#
# proxy_addr = "202.75.210.45:7777"
# data = use_proxy(proxy_addr,"http://www.mi.com")
# print(len(data))
