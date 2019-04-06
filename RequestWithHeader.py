# using Request class to add headers to the url in order to get User-Agent, which could better work under some website that have anti-crawler system.

from urllib import request

url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

#resp = request.urlopen(url)
#print(resp.read())

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read())
