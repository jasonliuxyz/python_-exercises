# 写一个程序来管理用于登录系统的用户信息：登录名和密码。登录用户账号建立后，已存在用户可以用登录名字和密码重返系统，新用户不能用别人的
# 用户名建立用户账号（此处只是练习dict用法）

user_pasw = {'jason':'test'}
user = input("请输入用户名：")
pasw = input("请输入密码：")

if user in user_pasw.keys():
    print('the user is in')
else:
    user_pasw[user] = pasw   
print(user_pasw)

if user not in user_pasw.keys():
    print("请先注册")
elif pasw != user_pasw[user]:
    print("密码错误")
else:
    print("登录成功")
