# 8、用户输入文件名以及开始搜索的路径，搜索改文件是否存在，如果遇到文件夹，则进入该文件夹继续搜索
# input接收用户输入的文件名和路径
# os.path.isdir 判断是否是文件夹，如果是的话，则需要进入该文件夹继续搜索，循环调用下我们的函数继续实行

import os

start_dir = input("请输入目录：")
target = input("请输入文件名：")

def search_file(start_dir, target):
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)
            
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)

search_file(start_dir, target)
