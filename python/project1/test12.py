from urllib import request

url = 'http://pan.baidu.com/share/link?shareid=1051708271&uk=607064979'

response = request.urlopen(url)
content = response.read()
f = open('./pan.html')
f.write(str(content))
f.close()
