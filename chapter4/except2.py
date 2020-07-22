# 定义一个函数func(filename) filename文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误

import os
def func(filename):
    try:
        file = open(filename)
    except Exception as error:
        print("出错拉，出错的内容是{}".format(error))
    else:
        print(file.read())
        file.close()
        
func('test.txt')
