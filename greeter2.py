# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 21:27
# 文件名称：greeter2.py
# 开发软件：PyCharm
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name=first_name+' '+last_name
    return full_name.title()
#这是一个循环!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name=input("First name:")
    if f_name=='q':
        break
    l_name=input("Last name:")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello,{}!".format(formatted_name))