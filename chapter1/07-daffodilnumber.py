# 编写一个程序，求100-999之间的所有水仙花数
# 如果一个3位数等于其他各位数字的立方和，则称这个数为水仙花数，例如：153=1^3 + 5^3 + 3^3，因此153就是一个水仙花数

for i in range(100, 1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    
    if a**3 + b**3 + c**3 == i:
        print(i)

for i in range(100, 1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    
    if a**3 + b**3 + c**3 == i:
        print(i)
