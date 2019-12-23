import json
import datetime
import time
import os

def show(): # 1 . 支出$ 2.收入$ 3.both 日月 show + - total show $ -> same file + Create file every month
    while 1:
        all_list.clear()
        spend_list.clear()
        earn_list.clear()
        total_amount = 0
        print("1.支出金額 2.收入金額 3.總開銷 4.返回主頁")
        cmd = int(input("請輸入功能選項"))

        if (cmd == 1): #支出$
            year = int(input("Which year: "))
            month = int(input("Which month: "))
            ReadforRecordbook(year,month)
            print("  -- 支出記錄 --")  # title
            for i in range(len(spend_list)):
                if (spend_list[i]['year'] == year and spend_list[i]['month'] == month ):
                    print("%d-%d-%d %-10s $%.2f" % (spend_list[i]['year'], spend_list[i]['month'],
                                                  spend_list[i]['date'], spend_list[i]['time'],
                                                  spend_list[i]['amount']))
                    total_amount += spend_list[i]['amount']  # 計算總支出
            if (total_amount == 0):
                print("你沒有%d年-%d月的支出記錄" % (year, month))
            else:
                print("The sum of expense: $%.2f dollars" % (total_amount))  # 輸出總支出
            _just = input("Input Anything To Continue...")

        if (cmd == 2): #2.收入
            year = int(input("Which year: "))
            month = int(input("Which month: "))
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
                print("The sum of earnings: $%.2f dollars" % (total_amount))  # 輸出總收入
            _just = input("Input Anything To Continue...")

        elif cmd == 3 : #3.both 日月 show + - total show $ -> same file + Create file every month
            year = int(input("Which year: "))
            month = int(input("Which month: "))
            ReadforRecordbook(year, month)
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
            print("The sum of month %.2f dollars" %(total_amount))
            if (len(all_list)==0):
                print("There is no record on %d-%d" % (year, month))
            _just = input("Input Anything To Continue...")
        elif cmd == 4 :
            break
        else :
            print("請輸入1-4的功能選項")

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
