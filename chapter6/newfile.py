# 1、编写一个程序，接收用户输入的内容，并且保存为新的文件，如果用户输入:w，表示文件保存退出

with open(r'/Users/liucheng/Desktop/input2.txt', 'w') as f:
    while True:
        instring = input("请输入内容:")
        if instring != ':w':
            f.write("%s\n" % instring)
        else:
            break
