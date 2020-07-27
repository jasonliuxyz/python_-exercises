# 9、用户输入关键字以及开始搜索的路径，搜索关键字是否存在某个文件名中，如果遇到文件夹，则进入该文件夹继续搜索
# in 去判断target这个字符串是否在文件的名字中

import os

start_dir = input("please input start_directory:")
target = input("enter your name:")

def search_file(start_dir, target):
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir):
        if target in each_file:
            print(os.getcwd() + os.sep + each_file)
            
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)
            
search_file(start_dir, target)
