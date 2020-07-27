# 6、编写一个程序，统计当前目录下每个文件类型的文件数

import os

all_files = os.listdir(os.curdir)
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault("文件夹", 0)
        type_dict["文件夹"] += 1
        
    else:
        ext = os.path.splitext(each_file)[1]
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1
        
for each_type in type_dict:
    print("该文件夹下有类型为{}的文件有{}个".format(each_type, type_dict[each_type]))
