import cv2
import time

while True:
    gender = input("請輸入性別(男/女):")
    if gender == "男":
        imgB = cv2.imread('boy.jpg')
        cv2.namedWindow('model', cv2.WINDOW_NORMAL)
        cv2.imshow('model', imgB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('myModel.jpg', imgB)
        break
    elif gender == "女":
        imgG = cv2.imread('girl.jpg')
        cv2.namedWindow('model', cv2.WINDOW_NORMAL)
        cv2.imshow('model', imgG)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('myModel.jpg', imgG)
        break
time.sleep(2)

print("現在是早上7點，開始第一項任務吧:\n")
time.sleep(2)
print("今日要打電話關心父母，並告知自己近況，讓長輩放心\n")
time.sleep(4)
while True:
    result = input("現在是晚上9點，今日任務有達成嗎? (有/無)")
    grade = 0
    if result == "有":
        grade += 20
        print("太棒了!!!就知道你可以辦到!!!\n")
        time.sleep(2)
        print("自信心數值 + 20 !\n目前分數: ", grade)
        print("good night!\n")
        break
    elif result == "無":
        print("怎麼會這樣(哭)~想想自己為甚麼沒辦到 ?? 一定要改掉缺點，這樣才會進步哟!!!\n")
        time.sleep(2)
        print("目前分數:", grade)
        print("別氣餒，早點睡，明天繼續奮鬥喔\n")
        break
time.sleep(3)

print("現在是早上7點，接著第二項任務吧:\n")
time.sleep(2)
print("今日要自己準備早餐 + 搭公車上學\n")
time.sleep(4)
while True:
    result = input("現在是晚上9點，今日任務有達成嗎? (有/無)")
    if result == "有":
        grade += 20
        print("太棒了!!!突破自己!!!\n")
        time.sleep(2)
        print("自信心數值 + 20 !\n目前分數: ", grade)
        print("good night!\n")
        break
    elif result == "無":
        print("差哪一步沒完成呢 ?? 如何才能達成 ??\n")
        time.sleep(2)
        print("目前分數:", grade)
        print("加油 別多想，早點睡，明天繼續奮鬥喔\n")
        break
time.sleep(3)

print("現在是早上7點，再來第三項任務吧:\n")
time.sleep(2)
print("今日要連續運動 1小時，健康是一輩子的事~\n")
time.sleep(4)
while True:
    result = input("現在是晚上9點，今日任務有達成嗎? (有/無)")
    if result == "有":
        grade += 20
        print("恭喜您達成健康又維持完美體態!!!\n")
        time.sleep(2)
        print("自信心數值 + 20 !\n目前分數: ", grade)
        print("good night!\n")
        break
    elif result == "無":
        print("為甚麼偷懶 ?? 想想讓自己樂意去運動的動力是甚麼???\n")
        time.sleep(2)
        print("目前分數:", grade)
        print("加油! 努力把失去補回來，早點睡，明天繼續奮鬥喔\n")
        break
time.sleep(3)

print("現在是早上7點，再來第四項任務吧:")
time.sleep(2)
print("再撐一下~假日近在眼前~\n")
print("今日唸書 3小時\n")
time.sleep(4)
while True:
    result = input("現在是晚上9點，今日任務有達成嗎? (有/無)")
    if result == "有":
        grade += 20
        print("太美好了~有充實一天，學習到知識，'knowledge is power!'\n")
        time.sleep(2)
        print("自信心數值 + 20 !\n目前分數: ", grade)
        print("good night!\n")
        break
    elif result == "無":
        print("打瞌睡 ?? 怎樣時間才夠用???\n")
        time.sleep(2)
        print("目前分數:", grade)
        print("加油! 記得之後要補唸沒唸完的書，早點睡，明天繼續奮鬥喔\n")
        break
time.sleep(3)

print("現在是早上7點，本周第五項任務:\n")
time.sleep(2)
print("今日回家要洗碗 + 打掃房間\n")
time.sleep(2)
print("今天happy Friday!以愉悅的心面對一整天!今晚可以稍稍晚點睡 :) \n")
time.sleep(4)
while True:
    result = input("現在是晚上9點，今日任務有達成嗎? (有/無)")
    if result == "有":
        grade += 20
        print("太好了~懂得生活，享受生活，是人生很重要的一門哲學'\n")
        time.sleep(2)
        print("自信心數值 + 20 !\n目前分數: ", grade)
        print("Have a sweet dream! Have a wonderful weekend >0< \n")
        break;
    elif result == "無":
        print("不能偷懶喔~~時間要如何分配給各方面呢??? (朋友+家人+課業+休閒+運動+生活) ???\n")
        time.sleep(2)
        print("目前分數:", grade)
        print("加油! 想想如何才能成為更好的人，一起努力，早點睡，補充能量!!! \n")
        break;

time.sleep(3)
print("本次任務累積分數:", grade, "\n")
time.sleep(2)
if grade >= 80:
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
                cv2.imwrite('myModel.jpg', imgBNew)
                break
            elif option == 2:
                imgBNew = cv2.imread('streetBoy.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgBNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite('myModel.jpg', imgBNew)
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
                cv2.imwrite('myModel.jpg', imgGNew)
                break
            elif option == 2:
                imgGNew = cv2.imread('longGirl.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgGNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite('myModel.jpg', imgGNew)
                break
            elif option == 3:
                imgGNew = cv2.imread('curlGirl.jpg')
                cv2.namedWindow('model', cv2.WINDOW_NORMAL)
                print("請看---->")
                time.sleep(1.5)
                cv2.imshow('model', imgGNew)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite('myModel.jpg', imgGNew)
                break

else:
    print("未達標準~~要繼續追求更好的自己!\n")

