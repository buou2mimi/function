# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 20:59
# 文件名称：pizza2.py
# 开发软件：PyCharm
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')