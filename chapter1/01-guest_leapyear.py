# 写一个程序，判断给定年份是否为闰年
# 闰年的定义：能够被4整除的年份

year = input("请输入年份：")
if year.isdigit:
    year = int(year)

    if (year % 4 == 0):
        print(str(year) + "是闰年")
    else:
        print(str(year) + "不是闰年")
