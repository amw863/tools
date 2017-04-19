from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re

url = 'http://www.meizitu.com/a/5404.html'

try:
    html = urlopen(url)
except HTTPError as e:
    print('[-]请求地址出现异常')
else:
    bsObj = BeautifulSoup(html)
    urlList = bsObj.findAll('img',{"src":re.compile('http:\/\/pic\.meizitu\.com\/wp-content\/uploads\/2016a\/07\/02\/.*\.jpg')})

    print('---------------Begin----------------------')
    for img in urlList:
        urlretrieve(img)
        print("[+]" + img["src"])
    print('---------------End-------------------------')
