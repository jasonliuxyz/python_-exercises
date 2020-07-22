# 编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常

def subduction(a, b):
    if a < b:
        raise BaseException("被减数不能小于减数")
    else:
        return a-b
    
try:
    subduction(3, 7)
except BaseException as error:
    print("好像出错了，出错的内容是:{}".format(error))
