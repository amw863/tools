from urllib.request import urlopen
from urllib.request import HTTPError
from datetime import datetime
from bs4 import BeautifulSoup
import csv

#html = urlopen('file:///D:/Program%20Files/Python3/project2/a.html')
#bsObj = BeautifulSoup(html,"html.parser")
#t = bsObj.find_all('div',{'id':"showImgWrap"})
print(t)
exit()
def getLinks(articleUrl):
    try:
        html = urlopen(articleUrl)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html,"html.parser")
    except AttributeError as e:
        return None
    return bsObj.find('div',{'id':"img-container"}).find_all('div',{'class':'img_inner_wrapper'})

def getBigPicLinks(url,num):
    #print(url)
    #print(num)

    count = 1
    basePath = 'http://www.mmxzg.com'
    bigPicPath = []; 
    while count <= int(num):
        if count <= 1:
            tempUrl = basePath + url
        else:
            tempUrl = basePath + url.replace('.html', '_' + str(count) + '.html')
        count = count + 1
        #print(tempUrl)
        try:
            html = urlopen(tempUrl)
        except HTTPError as e:
            pass
        try:
            bsObj = BeautifulSoup(html,"html.parser")
        except AttributeError as e:
            pass
        try:
            images = bsObj.find('div',{'id':'showImgWrap'}).find_all('img')
        except AttributeError as e:
            print(e)
        print(images)
        for img in images:
            bigPicPath.append(basePath + img['src'])
    return bigPicPath
def outCsv(url):
    basePath = 'http://www.mmxzg.com'
    tempUrl = basePath + url
    links = getLinks(tempUrl)
    #print(links)
    csvFile = open('./csv/meizi.csv', 'w+')
    print('---------------\t' + str(datetime.now()) + '\t' + '------------------')
    print('---------------------------\t 一路向西\t============================')
    i = 0
    try:
        writer = csv.writer(csvFile)
        csvTitle = ('编号','标题','张数','地址','详情url')
        writer.writerow(csvTitle)
       
        for link in links:
            i = i + 1
            if i>=5:
                break
            print('第['+str(i)+']号佳丽\t'+str(datetime.now())+' 时 开始')
            print('编号\t\t标题\t\t'+'、\t\t共/张\t\t资源地址\t\t详情')
            title = link.find('img').attrs['title']
            #icon = link.find('img').attrs['src']
            num = link.find('span', {'class':'num'}).label.get_text()        
            source = link.find('div',{'class':'title'}).a['href']
            writer.writerow((i,title,num,source,''))
            #获取单个url详情
            detailPath = getBigPicLinks(source,num)
            print("%d\t%s"%(i,title+'\t'+num+'\t'+source+'\t\t'))
            j = 1
            for path in detailPath:
                print("\t\t\t\t\t\t\t\tthis is No.[%d]:%s"%(j,path))
                j = j + 1
                writer.writerow(('','','','','',path))
            print('第['+str(i)+ ']号'+ str(datetime.now()) +' 时 结束')
        print('------------------->旅行愉快============')
        print('---------------' + str(datetime.now()) + '------------------')
    finally:
        csvFile.close()
#url = '/mote/'
#outCsv(url)
r = getBigPicLinks('/mote/1429.html',2)
print(r)
