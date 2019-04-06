

from urllib import parse
# using urlparse funtion to split an url into different parts.
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&oq=%25E9%25A9%25AC%25E4%25BA%2591&rsv_pq=887fa87d000f4a67&rsv_t=8660gXAupb%2F68nC0Bo6YJpxsgurNHKcoNGuFxMLkljfbqdtD%2BpGi%2BllbbkM&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=1&rsv_sug7=001&rsv_sug2=0&inputT=1550&rsv_sug4=1550&rsv_sug=9'
result = parse.urlparse(url)
#print(result)
print('scheme:', result.scheme)
print('host:', result.netloc)
print('path:', result.path)
print('query:', result.query)