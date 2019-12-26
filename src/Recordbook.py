import json
import datetime
import time
import os
from LoginSYS import *
from Mission import *
from DataManage import *

def show(): # 1 . 支出$ 2.收入$ 3.both 日月 show + - total show $ -> same file + Create file every month
    while 1:
        print("1.支出金額 2.收入金額 3.總開銷 4.返回主頁")
        cmd = int(input("請輸入功能選項 :"))

        if (cmd == 1): #支出$
            year = int(input("請輸入年份: "))
            month = int(input("請輸入月份: "))
            Payment(year,month)

        if (cmd == 2): #2.收入
            year = int(input("請輸入年份: "))
            month = int(input("請輸入月份: "))
            Income(year,month)

        elif cmd == 3 : #3.both 日月 show + - total show $ -> same file + Create file every month
            year = int(input("請輸入年份: "))
            month = int(input("請輸入月份: "))
            totalecon(year,month)
        elif cmd == 4 :
            break
        else :
            print("請輸入1-4的功能選項")

def Enterdata():
    print("記帳")  # title
    print("1. 支出")  # 紀錄花費
    print("2. 收入")  # 紀錄收入
    while (1):
        selection = int(input("Choose: "))
        if (selection <= 0 or selection > 3):
            print("請輸入功能選項1-3 :")
        else:
            print("------------------------------")
            break
    print("1.當日")
    print("2.其他")
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
                    print("請輸入1-5的功能選項")
            break
        else:
            print("請輸入1-2的功能選項")
    MonthlyRecord(year,month,date,all_list,ttime,selection)

def Record_Book():
    while (1):
        print("------------------------------")
        print("記賬簿")  # title 記賬簿
        print("1. 顯示紀錄")  # 顯示紀錄
        print("2. 記帳")  # 記帳
        print("3. 離開記賬簿")  # 離開
        while (1):  # 輸入錯誤 重新輸入
            selection = int(input("請輸入功能選項1-3 : "))
            if (selection <= 0 or selection > 3):
                print("請輸入1-3的功能選項")
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