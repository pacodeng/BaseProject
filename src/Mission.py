import cv2
import time
import random
from Recordbook import *
from LoginSYS import *
from DataManage import *

value = 0
flag = 0
flag1 = 0

def createcharacter():
    pwdata = []
    with open('ID_data.json', 'r' , encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data :
        Localid = x["account_id"]
    while True:
        gender = input("請輸入性別(男/女):")
        if gender == "男":
            name = input("Name: ")
            imgB = cv2.imread('boy.jpg')
            cv2.namedWindow('model', cv2.WINDOW_NORMAL)
            cv2.imshow('model', imgB)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite(Localid+'.jpg', imgB)
            with open('ID_data.json', 'r', encoding='utf-8-sig') as j:
                data = json.load(j)
            for x in data:
                Localid = x["account_id"]
            with open('data.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            for d in data:
                pwdata.append({'account_id': d['account_id'], 'account_name': d['account_name'], 'self-confident': int(d['self-confident'])})
            load = {'account_id': Localid, 'account_name': name, 'self-confident': 0}
            pwdata.append(load)
            with open('data.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
                json.dump(pwdata, f)
            break
        elif gender == "女":
            name = input("Name: ")
            imgG = cv2.imread('girl.jpg')
            cv2.namedWindow('model', cv2.WINDOW_NORMAL)
            cv2.imshow('model', imgG)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imwrite(Localid+'.jpg', imgG)
            with open('ID_data.json', 'r', encoding='utf-8-sig') as j:
                data = json.load(j)
            for x in data:
                Localid = x["account_id"]
            with open('data.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            for d in data:
                pwdata.append({'account_id': d['account_id'], 'account_name': d['account_name'], 'self-confident': int(d['self-confident'])})
            load = {'account_id': Localid, 'account_name': name, 'self-confident': 0}
            pwdata.append(load)
            with open('data.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
                json.dump(pwdata, f)
            break

def confidentupgrade():
    pwdata = []
    with open('ID_data.json', 'r', encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data:
        Localid = x["account_id"]
    with open('data.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for d in data:
        if (Localid == d["account_id"]):
            pwdata.append({'account_id': d['account_id'], 'account_name': d['account_name'], 'self-confident': int(d['self-confident'])+20})
        else:
            pwdata.append({'account_id': d['account_id'], 'account_name': d['account_name'], 'self-confident': int(d['self-confident'])})
    with open('data.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
        json.dump(pwdata, f)

def mission():
    global flag
    global flag1
    global value
    with open('ID_data.json', 'r', encoding='utf-8-sig') as j:
        data = json.load(j)
    for x in data:
        Localid = x["account_id"]
    with open('data.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    for x in data :
        if(Localid == x["account_id"]):
            confident = int(x["self-confident"])
    while 1:
        if flag == 0:
            value = random.randint(1, 5)
            flag = 1
        elif value == 1:
            print("今日要打電話關心父母，並告知自己近況，讓長輩放心\n")
            break
        elif value == 2:
            print("今日要自己準備早餐 + 搭公車上學\n")
            break
        elif value == 3:
            print("今日要連續運動 1小時，健康是一輩子的事~\n")
            break
        elif value == 4:
            print("今日唸書 3小時\n")
            break
        elif value == 5:
            print("今日回家要洗碗 + 打掃房間\n")
            break
    if flag ==2 :
        while 1:
            result = input("任務有達成嗎? (yes / no)")
            if result == "yes":
                confident += 20
                confidentupgrade()
                print("太棒了!!!就知道你可以辦到!!!\n")
                time.sleep(2)
                print("自信心數值 + 20 !\n目前分數: ", confident)
                if confident >= 80 and flag1 == 0:
                    evolved()
                flag=3
                break
            elif result == "no":
                print("目前分數:", confident)
                print("\n")
                flag=4
                break
    elif flag == 3:
        print("今天沒有任務了")
    elif flag == 4:
        result = input("任務有達成嗎? (yes / no)")
        if result == "yes":
            if result == "yes":
                confident += 20
                confidentupgrade()
                print("太棒了!!!就知道你可以辦到!!!\n")
                time.sleep(2)
                print("自信心數值 + 20 !\n目前分數: ", confident)
                if grade >= 80 and flag1 == 0:
                    evolved()
                flag = 3
        else:
            print("目前分數:", confident)
            print("\n")
    if flag == 1:
        flag=2

def evolved():
    print("達到標準 80 分以上!\n獎勵是: 恭喜您成長，可以更改外表，變有魅力!\n")
    time.sleep(3)
    if gender == "男":
        while True:
            print("請選擇風格:")
            print("1.紳士西裝\n2.street style\n")
            option = int(input("請輸入選項(1 or 2):\n"))
            if option == 1:
                imgBNew = cv2.imread('suitBoy.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgBNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite(Localid+'.jpg', imgBNew)
                break
            elif option == 2:
                imgBNew = cv2.imread('streetBoy.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgBNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite(Localid+'.jpg', imgBNew)
                break
    elif gender == "女":
        while True:
            print("請選擇風格:")
            print("1.俏麗短髮\n2.浪漫長髮\n3.復古捲髮\n")
            option = int(input("請輸入選項(1 or 2 or 3):\n"))
            if option == 1:
                imgGNew = cv2.imread('shortGirl.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgGNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite(Localid+'.jpg', imgGNew)
                break
            elif option == 2:
                imgGNew = cv2.imread('longGirl.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgGNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite(Localid+'.jpg', imgGNew)
                break
            elif option == 3:
                imgGNew = cv2.imread('curlGirl.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgGNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite(Localid+'.jpg', imgGNew)
                break

