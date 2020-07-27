# 4、在上道题基础上，增加功能，使用户可以随意的需要显示的行数
# 12:42 显示12行到42行
# : 显示所有内容
# 用以上的形式来表示我们想要打印的起始和结束行数

file_name = input("请输入文件名：")
linenum = input("请输入要显示的行数，格式为1:9或者:")

def print_line(file_name, linenum):
    f = open(file_name)
    
    begin,end = linenum.split(':')
    if begin == '':
        begin = 1
    if end == '':
        end = -1
        
    begin = int(begin) - 1
    end = int(end)
    
    lines = end - begin
    
#    for i in range(begin):
#        f.readline()
    length=0
    for i in range(begin):
        length += len(f.readline())
    print(length)
    f.seek(length, 0)
        
    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())
    f.close()
    
print_line(file_name, linenum)
