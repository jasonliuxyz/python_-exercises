#定义一个集合的操作类
#包括的方法
#集合元素添加：add_setinfo()
#集合的交集： get_intersection()
#集合的并集：get_union()
#集合的差集：del_difference()

class SetInfo(object):
    def __init__(self, set):
        self.set = set
        
    def add_setinfo(self, key):
        self.set.add(key)
        return self.set
        print('add success')
        
    def get_intersection(self, set2):
        if isinstance(set2, set):      
            return self.set.intersection(set2)
        else:
            return 'no set'

    def get_union(self, set2):
        if isinstance(set2, set):
            return self.set.union(set2)
        else:
            return 'no set'
    
    def get_difference(self, set2):
        if isinstance(set2, set):     
            return self.set.difference(set2)
        else:
            return 'no set'
    
s = SetInfo({1, 3, 5})
s.add_setinfo(7)

s.get_intersection({2, 5, 8})
s.get_union({2, 5, 8})
s.get_difference({2, 5, 8})
