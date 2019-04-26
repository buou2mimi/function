# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 14:39
# 文件名称：greeter.py
# 开发软件：PyCharm
def greet_user(username):
    """显示简单的问候语"""
    print("Hello,{}!".format(username.title()))
greet_user('alan')
greet_user('lisa')