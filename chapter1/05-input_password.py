# 设计一个验证用户密码的程序，只有三次机会输入错误，不过如果用户输入的内容包括*则不计算在内

password = "abc012"
count = 0
while count < 3:
    pw = input("请输入密码：")
    
    if "*" not in pw:
        if pw == password:
            count+=1
            print("correct")
            break
        else:
            count+=1
            print("not correct")  
    else:
        print("密码中不能包含*")
