# a demo to get http  request from www.baidu.com using python
from urllib import request

resp = request.urlopen('http://www.baidu.com')

print(resp.read())
