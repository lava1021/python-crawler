# a demo to get http  request from www.baidu.com using python
from urllib import request

#resp = request.urlopen('http://www.baidu.com')   # using urlopen function to get html

#print(resp.read())
#print(resp.read(10))
#print(resp.readline())
#print(resp.readlines())
#print(resp.getcode())
request.urlretrieve('http://www.baidu.com', 'baidu.html')  # using urlretrieve funtion to download info from the website