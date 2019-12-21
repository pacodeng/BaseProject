
import json
import datetime
import time

def Record_Book():
    with open('孫苡菱_提醒系統-記帳本.json', 'r', encoding='utf-8-sig') as f:  # 讀檔
        data = json.load(f)
    # 建立一個list --全部紀錄
    all_list = []
    spend_list = []  # style = 1
    earn_list = []  # style = 2
    for d in data:
        all_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                         'date': int(d['date']), 'time': d['time'], 'amount': int(d['amount'])})
    for d in data:
        if(d['style'] == 1):
            spend_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                               'date': int(d['date']), 'time': d['time'], 'amount': int(d['amount'])})
    for d in data:
        if(d['style'] == 2):
            earn_list.append({'style': int(d['style']), 'year': int(d['year']), 'month': int(d['month']),
                              'date': int(d['date']), 'time': d['time'], 'amount': int(d['amount'])})
    while(1):
        print("------------------------------")
        print("Record Book")  # title
        print("1. Show Record")  # 顯示紀錄
        print("2. Entry")  # 記帳
        print("3. Exit Record Book")  # 離開
        while(1):  # 輸入錯誤 重新輸入
            selection = int(input("Choose: "))
            if(selection <= 0 or selection > 3):
                print("Please choose 1 - 3.")
                selection = int(input("Choose: "))
            else:
                print("------------------------------")
                break
        if(selection == 1):  # 顯示紀錄
            year = int(input("Which year: "))  # 想要顯示紀錄的年份
            month = int(input("Which month: "))  # 想要顯示紀錄的月份
            print("Record Type")  # title
            print("1. Spend Record")  # 支出紀錄
            print("2. Earn Record")  # 收入紀錄
            print("3. Balance")  # 顯示收入支出兩種的紀錄
            while(1):  # 輸入錯誤 重新輸入
                selection = int(input("Choose: "))
                if(selection <= 0 or selection > 3):
                    print("Please choose 1 - 3.")
                    selection = int(input("Choose: "))
                else:
                    break
            total_amount = int(0)
            if(selection == 1):
                print("  -- SPEND RECORD --")  # title
                for i in range(len(spend_list)):
                    if(spend_list[i]['year'] == year and spend_list[i]['month'] == month):
                        print("%d-%d-%d %-10s $%d" % (spend_list[i]['year'], spend_list[i]['month'],
                                                      spend_list[i]['date'], spend_list[i]['time'], spend_list[i]['amount']))
                        total_amount += spend_list[i]['amount']  # 計算總支出
                if(total_amount == 0):
                    print("There is no record on %d-%d" % (year, month))
                else:
                    print("The sum of expense: $%d dollars" %
                          (total_amount))  # 輸出總支出
                _just = input("Input Anything To Continue...")
            elif(selection == 2):
                print("  -- EARN RECORD --")  # title
                for i in range(len(earn_list)):
                    if(earn_list[i]['year'] == year and earn_list[i]['month'] == month):
                        print("%d-%d-%d %-10s $%d" % (earn_list[i]['year'], earn_list[i]['month'],
                                                      earn_list[i]['date'], earn_list[i]['time'], earn_list[i]['amount']))
                        total_amount += earn_list[i]['amount']  # 計算總收入
                if(total_amount == 0):
                    print("There is no record on %d-%d" % (year, month))
                else:
                    print("The sum of earnings: $%d dollars" %
                          (total_amount))  # 輸出總收入
                _just = input("Input Anything To Continue...")
            elif(selection == 3):
                for i in range(len(all_list)):
                    if(all_list[i]['year'] == year and all_list[i]['month'] == month):
                        if(all_list[i]['style'] == 1):
                            print("%d-%d-%d %-10s -$%d" % (all_list[i]['year'], all_list[i]['month'],
                                                           all_list[i]['date'], all_list[i]['time'], all_list[i]['amount']))
                            total_amount -= all_list[i]['amount']
                        elif(all_list[i]['style'] == 2):
                            print("%d-%d-%d %-10s +$%d" % (all_list[i]['year'], all_list[i]['month'],
                                                           all_list[i]['date'], all_list[i]['time'], all_list[i]['amount']))
                            total_amount += all_list[i]['amount']
                if(total_amount == 0):
                    print("There is no record on %d-%d" % (year, month))
                elif(total_amount > 0):
                    print("The balance of earnings and expense: $%d dollars" %
                          (total_amount))
                else:
                    print("The balance of earnings and expense: -$%d dollars" %
                          (total_amount))
                _just = input("Input Anything To Continue...")
        elif(selection == 2):  # 記帳
            print("Entry")  # title
            print("1. Spend")  # 紀錄花費
            print("2. Earn")  # 紀錄收入
            while(1):
                selection = int(input("Choose: "))
                if(selection <= 0 or selection > 3):
                    print("Please choose 1 - 3.")
                    selection = int(input("Choose: "))
                else:
                    print("------------------------------")
                    break
            year = int(datetime.datetime.today().year)
            month = int(datetime.datetime.today().month)
            date = int(datetime.datetime.today().day)
            time_hour = int(time.strftime("%H", time.localtime()))
            if(time_hour >= 4 and time_hour < 11):  # 4-11 早上
                ttime = "morning"
            elif(time_hour >= 11 and time_hour < 14):  # 11-14 中午
                ttime = "noon"
            elif(time_hour >= 14 and time_hour < 18):  # 14-18 下午
                ttime = "afternoon"
            elif(time_hour >= 18 and time_hour < 22):  # 18-22 晚上
                ttime = "evening"
            else:  # 22-4 清晨
                ttime = "night"
            if(selection == 1):  # 紀錄花費
                amount = int(input("How much did you cost: "))
                tmp = {'style': 1, 'year': year, 'month': month,
                       'date': date, 'time': ttime, 'amount': amount}
                print("Record: %d-%d-%d %-10s -%d" %
                      (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
                _just = input("Input Anything To Continue...")
                spend_list.append(tmp)
                all_list.append(tmp)
            elif(selection == 2):  # 紀錄收入
                amount = int(input("How much did you earn: "))
                tmp = {'style': 2, 'year': year, 'month': month,
                       'date': date, 'time': ttime, 'amount': amount}
                print("Record: %d-%d-%d %-10s +%d" %
                      (tmp['year'], tmp['month'], tmp['date'], tmp['time'], tmp['amount']))
                _just = input("Input Anything To Continue...")
                earn_list.append(tmp)
                all_list.append(tmp)
        elif(selection == 3):  # 離開
            _just = input("Input Anything To Exit...")
            break

    with open('孫苡菱_提醒系統-記帳本.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
        json.dump(all_list, f)


num = int(input("Input 1 to test the func. of Record_BookI"))
if num == 1:
    Record_Book()

print('1.角色資料 2.任務牆 3.好友 4.記帳本 5.登出 ')
point = int(input("請輸入功能選項"))
while(1):
    if point == 1:
        Record_Book()
    elif point == 2:
        
    else:
        print("Error")