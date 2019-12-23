import json
import datetime
import time
import os

# 建立一個list --全部紀錄
all_list = []
spend_list = []  # style = 1
earn_list = []  # style = 2

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

def Enterdata():
    print("Entry")  # title
    print("1. Spend")  # 紀錄花費
    print("2. Earn")  # 紀錄收入
    while (1):
        selection = int(input("Choose: "))
        if (selection <= 0 or selection > 3):
            print("Please choose 1 - 3.")
        else:
            print("------------------------------")
            break
    print("1.Today")
    print("2.Other")
    while 1:
        cmd = int(input("Choose: "))
        if cmd == 1:
            year = int(datetime.datetime.today().year)
            month = int(datetime.datetime.today().month)
            date = int(datetime.datetime.today().day)
            time_hour = int(time.strftime("%H", time.localtime()))
            if (time_hour >= 4 and time_hour < 11):  # 4-11 早上
                ttime = "morning"
            elif (time_hour >= 11 and time_hour < 14):  # 11-14 中午
                ttime = "noon"
            elif (time_hour >= 14 and time_hour < 18):  # 14-18 下午
                ttime = "afternoon"
            elif (time_hour >= 18 and time_hour < 22):  # 18-22 晚上
                ttime = "evening"
            else:  # 22-4 清晨
                ttime = "night"
            break
        elif cmd == 2:
            year = int(input("year: "))
            month = int(input("month: "))
            date = int(input("date: "))
            print("1.morning( 4-11 早上)")
            print("2.noon( 11-14 中午)")
            print("3.afternoon( 14-18 下午)")
            print("4.evening( 18-22 晚上)")
            print("5.night( 22-4 清晨)")
            while 1:
                temp = int(input("Choose time hour: "))
                if temp == 1:  # 4-11 早上
                    ttime = "morning"
                    break
                elif temp == 2:  # 11-14 中午
                    ttime = "noon"
                    break
                elif temp == 3:  # 14-18 下午
                    ttime = "afternoon"
                    break
                elif temp == 4:  # 18-22 晚上
                    ttime = "evening"
                    break
                elif temp == 5:  # 22-4 清晨
                    ttime = "night"
                    break
                else:
                    print("Please choose 1 - 5.")
            break
        else:
            print("Please choose 1 - 2.")
    if (selection == 1):  # 紀錄花費
        amount = int(input("How much did you cost: "))
        tmp = {'style': 1, 'year': year, 'month': month,
               'date': date, 'time': ttime, 'amount': amount}
        print("Record: %d-%d-%d %-10s -%d" %
              (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
        _just = input("Input Anything To Continue...")
        spend_list.append(tmp)
        all_list.append(tmp)
    elif (selection == 2):  # 紀錄收入
        amount = int(input("How much did you earn: "))
        tmp = {'style': 2, 'year': year, 'month': month,
               'date': date, 'time': ttime, 'amount': amount}
        print("Record: %d-%d-%d %-10s +%d" %
              (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
        _just = input("Input Anything To Continue...")
        earn_list.append(tmp)
        all_list.append(tmp)
    with open(str(year) + '_' + str(month) + '.json', 'a', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
        json.dump(all_list, f)
    all_list.clear()
    spend_list.clear()
    earn_list.clear()

def Record_Book():
    while (1):
        print("------------------------------")
        print("Record Book")  # title
        print("1. Show Record")  # 顯示紀錄
        print("2. Entry")  # 記帳
        print("3. Exit Record Book")  # 離開
        while (1):  # 輸入錯誤 重新輸入
            selection = int(input("Choose: "))
            if (selection <= 0 or selection > 3):
                print("Please choose 1 - 3.")
                selection = int(input("Choose: "))
            else:
                print("------------------------------")
                break
        if (selection == 1):  # 顯示紀錄
            show()
        elif (selection == 2):  # 記帳
           Enterdata()
        elif (selection == 3):  # 離開
            _just = input("Input Anything To Exit...")
            break
