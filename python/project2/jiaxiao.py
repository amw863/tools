from  urllib.request import urlopen
from  bs4 import BeautifulSoup
import csv,time

print('---------------开始抓取---------------------------------')
years = ['201605','201604','201603','201602','201601','201512','201511','201510','201509','201508']
for year in years:
    csvFile = open('./project2/csv/jiaxiao'+year+'.csv', 'w+')
    writer = csv.writer(csvFile)
    csvTitle = ('驾校名称','3年内违法率','3年内肇事率','人数','科目一合格率','科目二合格率')
    writer.writerow(csvTitle)
    print('[start]\t\t驾校名称\t\t3年内违法率\t\t3年内肇事率\t\t人数\t\t科目一合格率\t\t科目二合格率')
    
    for i in range(1, 17):
        url = 'https://sh.122.gov.cn/publicitypage?size=20&page='+str(i)+'&tjyf='+year+'&fzjg=%E6%B2%AAA&fwdmgl=3001'
    
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'html.parser')
        res = bsObj.find('table').find_all('tr')
        ret = []
    
        for tr in res:
            temp = []
            for td in tr.find_all('td'):
                temp.append(td.get_text())
        
            print('[+]'+temp[0]+'\t\t'+temp[1]+'\t\t'+temp[2]+'\t\t'+temp[3]+'\t\t'+temp[4]+'\t\t'+temp[5])
            writer.writerow((temp[0],temp[1],temp[2],temp[3],temp[4],temp[5]))

        time.sleep(2)
    print('-------------------第 '+year+' 月份抓取结束--------------------------')
    time.sleep(3)
    
    
