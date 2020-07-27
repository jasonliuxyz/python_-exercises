# 利用map函数，把用户输入的不规范的英文，编成首字母大写，其他小写的规范的名字，比如说：["ADMAm","LISA","JACK"]["Admam", "Lisa","Jack"]

def ToName(s):
    t = s.lower()
    t = t.capitalize()
    return t

list(map(ToName, ["ADMAm","LISA","JACK"]))
