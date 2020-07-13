#定义一个列表的操作类 ListInfo
#包括的方法
#1.列表元素添加 add_key()
#2.列表元素取值 get_key()
#3.列表合并 update_key()
#4.删除并且返回最后一个元素 del_key()

class ListInfo(object):
    def __init__(self, list):
        self.list = list
        
    def add_key(self, key):
        self.list.append(key)
        print(self.list)
    
    def get_key(self, index):
        if 0 <= index and index < len(self.list):
            return self.list[index]
    
    def update_key(self, list1):
        self.list.extend(list1) 
        print(self.list)
        
    def del_key(self, key):
        if len(self.list) >= 0:
            return self.list.remove(key)
        else:
            return "list is null"
    
l = ListInfo([1, 2, 3, 4, 5])
l.add_key(6)

l.update_key([7, 8])

temp = l.del_key(8)
print(temp)

print(l.get_key(3))
