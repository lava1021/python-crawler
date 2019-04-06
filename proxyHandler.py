# using proxy to prevent ip configuration

from urllib import request

url = 'http://httpbin.org/ip'
# construct a proxyhandler
handler = request.ProxyHandler({'http': '59.62.6.225'})
#using the handler to construct a opener
opener = request.build_opener(handler)
# sending a request from the opener
resp = opener.open(url)
print(resp.read())