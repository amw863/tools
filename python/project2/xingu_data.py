#!/usr/bin/env python

import sqlite3

db = './project2/csv/xingu.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

select_sql = 'select * from xingu limit 10'
cur.execute(select_sql)
stock_list_data = cur.fetchall()

select_sql = 'select * from sqlite_master where type="table"'
cur.execute(select_sql)
print(cur.fetchall())

for stock in stock_list_data:
    print(stock)

cur.close()
conn.close()
