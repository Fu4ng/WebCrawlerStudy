# --------------------------------------#
#
# Created by Fu4ng on 2017/7/31.
#
# 博文地址:
# --------------------------------------#
import urllib.request

# # 爬取一个没有任何反爬的网站
# url = 'http://www.baidu.com'
# file = urllib.request.urlopen(url)
# data = file.read()
# fhandle = open('baidu.html', 'wb')  # 写入本地文件
# fhandle.write(data)
# fhandle.close()
# # 快速保存到本地
# # file = urllib.request.urlretrieve('http://www.baidu.com' , filename='baidu.html')
#
#
# # 模仿浏览器
# # 使用build_opener()来修改报头
# url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
# headers = ("User-Agent",
#            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36")
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()  # 写入本地文件
# fhandle = open('D:/GitHubRepository/WebCrawlerStudy/3.html', 'wb')
# fhandle.write(data)
# fhandle.close()
#
# # 使用add_header()添加报头
# #
# url = 'http://www.hqu.edu.cn/'
# req = urllib.request.Request(url)
# req.add_header(
#     'User-Agent',
#     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
# data = urllib.request.urlopen(req).read()
# fhandle = open('D:/GitHubRepository/WebCrawlerStudy/3_1.html', 'wb')
# fhandle.write(data)
# fhandle.close()

# # 超时请求
# for i in range(1,100):
#     try :
#         file = urllib.request.urlopen("http://www.hqu.edu.cn/",timeout=0.5)
#         data = file.read()
#         print(len(data))
#     except Exception as e:
#         print("出现异常-----")
