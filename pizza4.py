# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/26 11:27
# 文件名称：pizza4.py
# 开发软件：PyCharm
def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a {}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("-{}".format(topping))