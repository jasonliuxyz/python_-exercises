#定义一个字典类：DictClass，完成如下功能
#1.删除某个key del_dict(key)
#2.判断某个键是否存在字典里，如果在返回键对应的值，不存在返回'not found' get_dict()
#3.返回键组成的列表，返回类型：list get_key()
#4.合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()

class DictClass(object):
    def __init__(self, dict):
        self.dict = dict
        
    def del_dict(self, key):
        if key not in self.dict.keys():
            return 'key不在字典'
        else:
            self.dict.pop(key)
            return '删除成功'
    
    def get_dict(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'
        
    def get_key(self):
        return list(self.dict.keys())
    
#    def update_dict(self, dict):
#        for k,v in dict.items():
#            self.dict[k]=v
#        return list(self.dict.values())

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return list(self.dict.values())
    
d = DictClass({"a":1, "b":2})
#d.del_dict("a")
print(d.get_dict('b'))
print(d.get_key())
print(d.update_dict({'c':3}))
