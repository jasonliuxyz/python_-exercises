# 假设，我们用一组tuple来表示学生的名字和成绩，L = [("Bob":75), ("Adam", 92), ("Bart":66), ("Lisa", 88)] 用sorted对上诉列表
# 按照名字排序

L = [("Bob", 75), ("Adam", 92), ("Bart",66), ("Lisa", 88)]
def by_name(s):
    s = sorted(s[0], key=str.lower)
    return s

L2 = sorted(L, key=by_name)
print(L2)

# 按照成绩排序

def by_score(s):
    s = sorted(range(s[1]), key=abs)
    return s

L3 = sorted(L, key=by_score)
print(L3)
