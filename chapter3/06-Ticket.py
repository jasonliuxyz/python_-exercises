#### 门票系统
#- 门票的价格是100元
#- 当周末的时候门票涨价20%
#- 小孩子半票
#- 计算2个成人和1个小孩的平日票价

class Ticket():
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
            
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
            
    def cal_price(self, num):
        return self.exp * self.inc * self.discount * num
    
adult = Ticket()
child = Ticket(child=True)

print("2个成人和1个小孩的平日票价是{}".format(adult.cal_price(2) + child.cal_price(1)))
