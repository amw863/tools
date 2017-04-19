#多图片下载
#author: BConder
#date:2016-07-09

import os
from urllib.request import urlopen
from urllib.request import retrieve
from bs4 import Beautiful

downloadDirectory = 'download'
baseurl = ''

def getAbsoluteUrl(baseUrl,source):
    if source.startswith("http://www"):
        url = 'http://' + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startwith('www.')
        url = source[4:]
        url = 'http://'+ source
    else:
        url = baseUrl + '/' + source

    if baseUrl not in url:
        return None
    return url
def getDownloadPath(baseUrl,absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl,"")
    path = downloadDirectory + path

    dirctory = os.path.dirname(path)

    if not os.path.exists(dirctory):
        os.makedirs(directory)

    return path

url = ''
html = urlopen(url)

bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=true)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl,download['src'])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))








