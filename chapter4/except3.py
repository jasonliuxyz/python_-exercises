# 自己定义一个异常类，继承Exception类，捕获下面的过程：判断输入的字符串长度是否小于5

class MyError(Exception):
    def __init__(self, str):
        self.str = str
        
    def process(self):
        if len(self.str) < 5:
            print("字符串的长度必须大于5")
        else:
            print("bingo")
            
try:
    er = MyError("sssdd")
    er.process()
except MyError as err:
    print(error)
