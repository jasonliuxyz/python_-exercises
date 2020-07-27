# 3、编写程序，当用户输入文件名和行数的时候，将该文件的前N行内容打印到屏幕上

file_name = input("请输入文件名：")
line = input("请输入行数：")

def print_content(file_name, line):
    f = open(file_name)
#    l = f.readlines()
#    for i in range(0, int(line)):
#        print(l[i])

    for i in range(int(line)):
        print(f.readline())
        
    f.close()
        
print_content(file_name, line)
