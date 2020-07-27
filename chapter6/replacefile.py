# 5、编写一个程序，实现”全部替换"的功能
# 打开一个文件
# 把文件中 xxx这样的字符串，替换成sss
# open打开文件
# readline 读取文件内容
# replace 替换

file_name = input("请输入你要打开的文件名：")
rep_word = input("请输入你要替换的字符：")
new_word= input("请输入替换的新的字符串：")
def file_replace(file_name, rep_word, new_word):
    f = open(file_name)
    content = []
    
    for eachline in f:
        if rep_word in eachline:
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)
            
    decide = input("你确定要这样做吗？YES|NO：")
    if decide in ["YES", "Yes", "yes"]:
        f_write = open(file_name, 'w')
        f_write.write(''.join(content))
        f_write.close()
        
file_replace(file_name, rep_word, new_word)
