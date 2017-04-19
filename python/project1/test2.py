import urllib.request

url = 'http://www.baidu.com'
respon = urllib.request.urlopen(url)
res = respon.read()
print('%s',res)
