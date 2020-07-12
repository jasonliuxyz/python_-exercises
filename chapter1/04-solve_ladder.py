# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩余1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶，只有每步上7阶，最后刚好一阶不剩
# 编写程序求该阶梯至少有多少阶

x=1
while x < 1000:
    if x%2 == 1 and x%3 == 2 and x%5 == 4 and x%6 == 5 and x%7 == 0:
        print(x)
    x+=1