# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 16:15
# 文件名称：greet_users.py
# 开发软件：PyCharm
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg="Hello,{}!".format(name.title())
        print(msg)
usernames=['hannah','ty','margot']
greet_users(usernames)