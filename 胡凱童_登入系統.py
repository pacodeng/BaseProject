import json


flag = 0
username = []
password = []
temp = []
i = 0
while 1:
    cmd = input('''
    1：註冊系統
    2：登入系統
    3：退出系統
    請輸入您的操作：''')
    if cmd.isdigit() and int(cmd) == 3:
        exit()
    elif cmd.isdigit() and int(cmd) == 1:
        username = input("    Enter Account: ")
        password = input("    Enter Password: ")
        length_username = len(username)
        length_password = len(password)
        if length_username < 10 or length_password < 10:
            print("    username or password less than 16, enter again")
            continue;
        if username == '' or password == '':
            print("    Please enter account and password")
            continue;
        temp = 'Account:' + username + '\n' + 'Password:' + password
        f = open("register.json", "w")
        f.write(temp)
        print('    Register Successful')
    elif cmd.isdigit() and int(cmd) == 2:
        user = input("    Enter Account: ")
        pwd = input("    Enter Password: ")
        if user == '' or pwd == '':
            print("    Please enter account and password");
            continue;
        f = open('register.json', 'r')
        if user != username or password != pwd:
            print("    Account Or Password Not Correct, Please Enter Again\n")
            flag = flag+1
            if flag == 3:
                print('    Are you sure this is your account ?')
            continue
        elif user == username and password == pwd:
            print("    Welcome\n")
            break;
