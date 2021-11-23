import mysql.connector
import pandas as pd
import sys
import datetime
cnx = mysql.connector.connect(user='knguyen', password='Passwd01',
                              host='127.0.0.1',
                              database='web')

cursor = cnx.cursor()



def excel(thanhpho):
    xlsx = pd.ExcelFile('1data/Book1.xlsx')
    df1 = pd.read_excel(xlsx, 'Số liệu vắc xin theo địa phương')
    data=[]
    for i in range(63):
        data.append(df1.loc[i])
    return data

def excel2():
    xlsx = pd.ExcelFile('1data/Book1.xlsx')
    df1 = pd.read_excel(xlsx, 'Địa điểm tiêm chủng')
    return df1

def tinhthanh():
    tinhthanh=[]
    h=0
    with open("thanhpho.txt", "r", encoding='utf-8') as thanhpho:
        for i in thanhpho:
            if i == 'Bắc Kạn': i = 'Bắc Kạnn'
            tinhthanh.append(i[:-1])
    return tinhthanh 

def insert_vaccine(cursor,cnx, data, today):
    for i in data:
        cmd = "insert into  web.tinhhinhvaccine (tentinhthanh, khphanbo, phanbothucte, danso, solieudatiem, ngaycapnhat) values ('%s', '%s', '%s', '%s', '%s', '%s');" % (i.values[1], str(i.values[2]), str(i.values[3]), str(i.values[4]), str(i.values[5]), today)
        print(cmd)
        cursor.execute(cmd)
        cnx.commit()

def insert_covid(cursor,cnx, today):
    data = []
    s=0
    with open("1data\socanhiem.txt", "r", encoding='utf-8') as scn:
        for i in scn:
            data.append(i.replace('\n', '').replace('.', '').replace('-', '0').replace('–', '-').replace('+', ''))

    while (s <= 248):
        cmd = "insert into  web.tinhhinhcovid (tentinhthanh, tongsoca, homnay, tuvong, ngaycapnhat) values ('%s', '%s', '%s', '%s', '%s');" % (data[s], str(data[s+1]), data[s+2], str(data[s+3]), today)
        print(cmd)
        cursor.execute(cmd)
        cnx.commit()
        s=s+4

        
to_day = datetime.datetime.now()
yesterday = to_day - datetime.timedelta(days=1)
mode = sys.argv[1]
if mode == 'vaccine': 
    print("---------- Cập nhật thông tin tiêm chủng ----------",)
    insert_vaccine(cursor, cnx, data=excel(tinhthanh()), today = (str(yesterday.strftime('%Y-%m-%d')) + ' 18:00:00'))
elif mode == 'covid':
    print("---------- Cập nhật thông tin Covid tại các địa phương ----------",)
    insert_covid(cursor, cnx, today = (str(yesterday.strftime('%Y-%m-%d')) + ' 18:00:00'))
else: print('Hãy nhập chế độ')


cnx.close()