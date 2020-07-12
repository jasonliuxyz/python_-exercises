# 给用户三次机会，猜想我们程序生成的一个数字A，每次用户猜想过后会提示数字是否正确以及用户输入数字是大于还是小于A，
# 当机会用尽后会提示用户已经输掉了游戏

import random
num = random.randint(1, 100)
guest_count = 0

while guest_count < 3:
    guest_num = input("请输入数字：")
    if guest_num.isdigit():
        guest_num = int(guest_num)
        if guest_num < num:
            print("num is low")
        elif guest_num > num:
            print("num is upper")
        else:
            print("bingo")
            break
        guest_count+=1
    else:
        print("not number")
        
if guest_count >= 3:
    print("you are lost")
