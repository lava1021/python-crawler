# using Request class to add headers to the url in order to get User-Agent, which could better work under some website that have anti-crawler system.

from urllib import request
from urllib import parse

#url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

#resp = request.urlopen(url)
#print(resp.read())

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='   # using referer to better pretend as a browser
           }

data = {
    'first': 'true',
    'pn': 1,         # page number
    'kd': 'python'   # keyword
}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
