#游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编程
#假设游戏场景为范围(x,y)为0<=x<=10,0<=y<=10
#游戏生成1只乌龟和10条鱼
#他们的移动方向均随机
#乌龟的最大移动能力是2(乌龟可以随机选择移动是1还是2),鱼的最大移动能力是1
#当移动到场景边缘，自动向反方向移动
#乌龟的初始化体力为100(上限）
#乌龟每移动一次，体力消耗1
#当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力增加20
#鱼不计算体力
#当乌龟体力值为0或者鱼的数量为0时，游戏结束

import random
class Tortoise():
    def __init__(self):
        self.power = 100
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        
    def eat(self):
        if self.power + 20 >= 100:
            self.power =100
        else:
            self.power += 20
            
        
    def move(self):
        new_x = random.choice([1, 2, -1, -2]) + self.x
        new_y = random.choice([1, 2, -1, -2]) + self.y
        
        if new_x < 0:
            self.x = 0 - (new_x -0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
            
        if new_y < 0:
            self.y = 0 - (new_y -0)
        elif new_y > 10:
            self.y = 10 - (new_x - 10)
        else:
            self.y = new_y
            
        self.power -= 1
        return (self.x, self.y)
    
class Fish(object):
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)
        
    def move(self):
        new_x = self.x + random.choice([1,-1])
        new_y = self.y + random.choice([1,-1])
        
        if new_x < 0:
            self.x = 0 - (new_x -0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y -0)
        elif new_y > 10:
            self.y = 10 - (new_x - 10)
        else:
            self.y = new_y
        
        return (self.x, self.y)

t = Tortoise()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼被吃完，game over')
        break
    if not t.power:
        print('体力耗尽，game over')
        break
    
    pos = t.move()
    for each_fish in fish[:]:
        if each_fish.move() == pos:
            t.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃掉了')
