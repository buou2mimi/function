# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 21:08
# 文件名称：pizza3.py
# 开发软件：PyCharm
def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print("\nMaking a {}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print("-{}".format(topping))
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
