# 2、编写一个程序，比较用户输入的文件是否相同，如果不同，显示出所有不同内容的行号

def diff_file(file1, file2):
    line = 0
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    
    for line1 in f1:
        line2 = f2.readline()
        
        line += 1
        #print(line1 + '\n' + line2)
        if line1 != line2:
            print(line)
    f1.close()
    f2.close()
        
diff_file('/Users/liucheng/Desktop/input2.txt', '/Users/liucheng/Desktop/input.txt')

