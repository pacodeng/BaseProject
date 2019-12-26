import schedule
import time
import tkinter as tk
from Recordbook import *
from LoginSYS import *
from Mission import *
from DataManage import *


def missionjump():
    # 設定視窗
    window = tk.Tk()
    # 設定式標題 大小 背景顏色
    window.title("提醒視窗")
    window.geometry('300x200')
    window.configure(background='white')
    # 設定視窗內容
    header_label = tk.Label(window, text='提醒您')
    header_label.pack()
    text_label = tk.Label(window, text='任務更新了喔 !')
    text_label.pack()
    # 回到離開、主程式按鈕
    ok_lickk = tk.Button(window,text='去任務牆',command=window.destroy)
    ok_lickk.pack()
    exit_lickk = tk.Button(window,text='離開',command=window.destroy)
    exit_lickk.pack()
    window.mainloop()  # 運行主程式

def friendjump():
    # 設定視窗
    window = tk.Tk()
    # 設定式標題 大小 背景顏色
    window.title("提醒視窗")
    window.geometry('300x200')
    window.configure(background='white')
    # 設定視窗內容
    header_label = tk.Label(window, text='提醒您')
    header_label.pack()
    text_label = tk.Label(window, text='有人想要加你好友喔 !')
    text_label.pack()
    # 回到離開、主程式按鈕
    ok_lickk = tk.Button(window,text='去好友清單',command=window.destroy)
    ok_lickk.pack()
    exit_lickk = tk.Button(window,text='離開',command=window.destroy)
    exit_lickk.pack()
    window.mainloop()  # 運行主程式

def recordjump():
    # 設定視窗
    window = tk.Tk()
    # 設定式標題 大小 背景顏色
    window.title("提醒視窗")
    window.geometry('300x200')
    window.configure(background='white')
    # 設定視窗內容
    header_label = tk.Label(window, text='提醒您')
    header_label.pack()
    text_label = tk.Label(window, text='記帳時間到了喔 !')
    text_label.pack()
    # 回到離開、主程式按鈕
    ok_lickk = tk.Button(window,text='去記帳本',command=window.destroy)
    ok_lickk.pack()
    exit_lickk = tk.Button(window,text='離開',command=window.destroy)
    exit_lickk.pack()
    window.mainloop()  # 運行主程式

def remind():
    # 時間到 跳出視窗(時間可以改)
    schedule.every().day.at("15:55").do(missionjump) #任務更新跳出提醒
    schedule.every().day.at("00:47").do(friendjump) #有好友請求跳出提醒
    schedule.every().day.at("08:30").do(recordjump) #早上記帳提醒
    schedule.every().day.at("12:30").do(recordjump) #中午記帳提醒
    schedule.every().day.at("19:00").do(recordjump) #晚上記帳提醒
    # 在時間到已經 每1秒跑一次schedule
    while(1):
        schedule.run_pending()
        time.sleep(1)