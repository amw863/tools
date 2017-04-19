#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import sqlite3

print('---------------Start to Get------------------------')
db = './project2/csv/xingu.db'
drp_tb_sql = 'drop table if exists xingu'
crt_tb_sql = """
create table if not exists xingu(
id INTEGER primary key autoincrement unique not null,
code int not null default 0,
name varchar(16) not null default '',
t_count int not null default 0,
net_t_count int not null default 0,
apply_limit int not null default 0,
apply_limit_cost int not null default 0,
price int not null default 0
)
"""

conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(drp_tb_sql)
cur.execute(crt_tb_sql)
insert_sql = "insert into xingu(code,name, t_count, net_t_count, apply_limit, apply_limit_cost, price) values (?,?,?,?,?,?,?)"

csvFile = open('./project2/csv/xingu.csv', 'w+')
writer = csv.writer(csvFile)
csvTitle = ('代码','简称', '申购代码', '发行总数(万股)', '网上发行(万股)', '申购上限(万股)', '定格申购(万)', '发行价格', '发行使用率', '行业市盈率', '申购日期', '中签率(%)', '中签号', '中签缴款日期', '上市日期', '打新收益', '涨停数量', '新股详情')

writer.writerow(csvTitle)

for i in range(1, 36):
    try:
        url = 'http://data.10jqka.com.cn/ipo/xgsgyzq/board/all/field/SGDATE/page/'+str(i)+'/order/desc/ajax/1/'
        html = urlopen(url)
        bsObj = BeautifulSoup(html,'html.parser' ,from_encoding='gbk')
    
        res = bsObj.find('tbody').find_all('tr')
        ret = []

        for tr in res:
            temp = []
            for td in tr.find_all('td'):
                temp.append(td.get_text())
                #print('[+] ' + '\t\t'.join(temp))
            cur.execute(insert_sql, (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6]))
            writer.writerow((temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13],temp[14],temp[15],temp[16],temp[17]))
            print('[+]' + temp[0] + '-' + temp[1] + 'save success!')
        conn.commit()
    except Exception as e:
        print(e)
cur.close()
conn.close()
csvFile.close()

print('--------------END To -------------')
    
