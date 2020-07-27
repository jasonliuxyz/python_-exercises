# 10、用户输入关键字以及开始搜索的路径，搜索关键字是否存在某个文件名中，如果遇到文件夹，则进入该文件夹继续搜索；
# 最后保存我们的文件存在的地方到我们指定的路径


import os

start_dir = input("please input start_directory:")
target = input("enter your name:")
backup = []

def search_file(start_dir, target):
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir):
        if target in each_file:
            backup_file = os.getcwd() + os.sep + each_file
            backup.append(backup_file)
            
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)
    return backup

rd = search_file(start_dir, target)

with open(os.getcwd() + os.sep + "backup.txt", 'wb') as f:
    f.write("\n".join(rd).encode("utf-8"))
