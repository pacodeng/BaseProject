import json
import cv2
from Reminder import *
from Recordbook import *
from LoginSYS import *
from Mission import *
from DataManage import *
from threading import Thread
from Chatroom import *

def Searchinfo():
    with open('ID_data.json', 'r' , encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data :
        Localid = x["account_id"]
    with open('data.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for x in data :
        if(Localid == x["account_id"]):
            name = x["account_name"]
            confident = int(x["self-confident"])
    print("賬號名稱 :" , name)
    print("自信心數值 :", confident)

def character():
    with open('ID_data.json', 'r' , encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data :
        Localid = x["account_id"]
    imgB = cv2.imread(Localid+'.jpg')
    cv2.namedWindow('model', cv2.WINDOW_NORMAL)
    cv2.imshow('model', imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    Thread(target=remind).start()
    while 1:
        print('1.註冊系統 2.登入系統 3.退出程序')
        cmd = int(input())
        if cmd == 1:
            resigter()
        elif cmd == 2:
            login()
            while 1:
                print('1.角色資料 2.任務牆 3.好友 4.記帳本 5.查詢角色資訊 6.登出 ')
                point = int(input("請輸入功能選項 : "))
                if point == 1:
                    character()
                elif point == 2:
                    mission()
                elif point == 3:
                    HOST = input('Enter host: ')
                    PORT = input('Enter port: ')
                    Thread(target=chatroom(HOST,PORT)).start()
                elif point == 4:
                    Record_Book()
                elif point == 5:
                    Searchinfo()
                elif point == 6:
                    break
                else:
                    print("請輸入1-6的功能選項")
        elif cmd == 3 :
           exit()
        else :
            continue
