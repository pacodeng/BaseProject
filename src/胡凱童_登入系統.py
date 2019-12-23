import json

def resigter(): #save ac , id , pw -> same file
    while 1 :
        account = input("    Enter Account: ")
        length_username = len(account)
        if length_username < 5 :
            print("    username less than 5, enter again")
            continue
        else:
            break
    while 1:
        password = input("    Enter Password: ")
        length_password = len(password)#大小數字
        upper = 0
        lower = 0
        digit = 0
        for n in password:
            if(n.isdigit()):
                digit = 1
            elif(n.isupper()):
                upper = 1
            elif(n.islower()):
                lower = 1
        if length_password < 8:
            print("     password less than 8, enter again")
        elif(digit == 1 and upper == 1 and lower == 1):
            pwdata = []
            with open('register.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            for d in data:
                pwdata.append({'account_id': d['account_id'], 'account':  d['account'], 'password':  d['password']})
            load = {'account_id': "1", 'account': account, 'password': password}       #ID will be random
            pwdata.append(load)
            break
        else:
            print("    Passwords must contain: a minimum of 1 lower case letter [a-z] , 1 upper case letter")

    with open('register.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
        json.dump(pwdata, f)

def login():
    flag = 0
    while 1:
        done = 0
        user = input("    Enter Account: ")
        pwd = input("    Enter Password: ")
        if user == '' or pwd == '':
            print("    Please enter account and password");
            continue;
        with open('register.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        for x in data :
            if user == x['account'] and pwd == x['password']:
                id = x['account_id']
                done = 1
                print("    Welcome\n")
                break
        if done == 1:
            Iddata = []
            load = {'account_id': id}
            Iddata.append(load)
            with open('ID_data.json', 'w', encoding='utf-8-sig') as f:  # 寫檔 更新資料庫
                json.dump(Iddata, f)
            break
        elif done != 1:
            print("    Account Or Password Not Correct, Please Enter Again\n")
            flag = flag + 1
            if flag == 3:
                print('    Are you sure this is your account ?')
