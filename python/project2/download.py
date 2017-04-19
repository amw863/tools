from urllib.request import urlopen

url = 'http://www.avtb7.com/file/7395/1/38b0959df6f3cb7e5949/1476112509/mobile/7395.mp4';
f = urlopen(url)
data = f.read()
with open('a.mp4','wb') as code:
    code.write(data)
