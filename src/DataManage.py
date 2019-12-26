import json
import datetime
import time
import os
from Recordbook import *
from LoginSYS import *
#from Mission import *

# 建立一個list --全部紀錄
all_list = []
spend_list = []  # style = 1
earn_list = []  # style = 2

def write():
    pwdata = []
    with open('ID_data.json', 'r' , encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data :
        Localid = x["account_id"]
    with open('register.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for d in data:
        if (Localid == d["account_id"]):
            pwdata.append({'account_id': d['account_id'], 'account': d['account'], 'password': d['password'], 'character': 2})
        else:
            pwdata.append({'account_id': d['account_id'], 'account': d['account'], 'password': d['password'],'character': int(d['character'])})
    with open('register.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
        json.dump(pwdata, f)

def ReadforRecordbook(year,month):
    filepath = str(year) + '_' + str(month)+'.json'
    if os.path.isfile(filepath):
        with open(str(year) + '_' + str(month) + '.json', 'r', encoding='utf-8-sig') as f:  # 讀檔
            data = json.load(f)
        for d in data:
            all_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                             'date': int(d['date']), 'time': d['time'], 'amount': float(d['amount'])})
        for d in data:
            if (d['style'] == 1):
                spend_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                                   'date': int(d['date']), 'time': d['time'], 'amount': float(d['amount'])})
        for d in data:
            if (d['style'] == 2):
                earn_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                                  'date': int(d['date']), 'time': d['time'], 'amount': float(d['amount'])})

def MonthlyRecord(year,month,date,all_list,ttime,selection):#每月新增金錢record
    all_list.clear()
    spend_list.clear()
    earn_list.clear()
    ReadforRecordbook(year,month)
    if (selection == 1):  # 紀錄花費
        amount = int(input("How much did you cost: "))
        tmp = {'style': 1, 'year': year, 'month': month,
               'date': date, 'time': ttime, 'amount': amount}
        print("Record: %d-%d-%d %-10s -%d" %
              (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
        _just = input("Input Anything To Continue...")
        all_list.append(tmp)
    elif (selection == 2):  # 紀錄收入
        amount = int(input("How much did you earn: "))
        tmp = {'style': 2, 'year': year, 'month': month,
               'date': date, 'time': ttime, 'amount': amount}
        print("Record: %d-%d-%d %-10s +%d" %
              (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
        _just = input("Input Anything To Continue...")
        all_list.append(tmp)
        with open(str(year) + '_' + str(month) + '.json', 'a', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
            json.dump(all_list, f)

def Income(year,month):
    all_list.clear()
    spend_list.clear()
    earn_list.clear()
    total_amount = 0
    ReadforRecordbook(year, month)
    print("  -- 收入記錄 --")  # title
    for i in range(len(earn_list)):
        if (earn_list[i]['year'] == year and earn_list[i]['month'] == month):
            print("%d-%d-%d %-10s $%.2f" % (earn_list[i]['year'], earn_list[i]['month'],
                                            earn_list[i]['date'], earn_list[i]['time'],
                                            earn_list[i]['amount']))
            total_amount += earn_list[i]['amount']  # 計算總收入
    if (total_amount == 0):
        print("你沒有%d年-%d月的收入記錄" % (year, month))
    else:
        print("總收入: $%.2f 元" % (total_amount))  # 輸出總收入
    _just = input("Input Anything To Continue...")

def Payment(year,month):
    all_list.clear()
    spend_list.clear()
    earn_list.clear()
    total_amount = 0
    ReadforRecordbook(year, month)
    print("  -- 支出記錄 --")  # title
    for i in range(len(spend_list)):
        if (spend_list[i]['year'] == year and spend_list[i]['month'] == month):
            print("%d-%d-%d %-10s $%.2f" % (spend_list[i]['year'], spend_list[i]['month'],
                                            spend_list[i]['date'], spend_list[i]['time'],
                                            spend_list[i]['amount']))
            total_amount += spend_list[i]['amount']  # 計算總支出
    if (total_amount == 0):
        print("你沒有%d年-%d月的支出記錄" % (year, month))
    else:
        print("總支出: $%.2f 元" % (total_amount))  # 輸出總支出
    _just = input("Input Anything To Continue...")

def totalecon(year,month):
    all_list.clear()
    spend_list.clear()
    earn_list.clear()
    total_amount = 0
    ReadforRecordbook(year, month)
    print("  -- 總開銷 --")  # title
    for i in range(len(all_list)):
        if (all_list[i]['year'] == year and all_list[i]['month'] == month):
            if (all_list[i]['style'] == 1):
                print("%d-%d-%d %-10s -%.2f" % (all_list[i]['year'], all_list[i]['month'],
                                                all_list[i]['date'], all_list[i]['time'],
                                                all_list[i]['amount']))
                total_amount -= all_list[i]['amount']
            elif (all_list[i]['style'] == 2):
                print("%d-%d-%d %-10s +%.2f" % (all_list[i]['year'], all_list[i]['month'],
                                                all_list[i]['date'], all_list[i]['time'],
                                                all_list[i]['amount']))
                total_amount += all_list[i]['amount']
    print("這個月的總開銷 %.2f 元" % (total_amount))
    if (len(all_list) == 0):
        print("你沒有%d年-%d月的支出記錄" % (year, month))
    _just = input("Input Anything To Continue...")