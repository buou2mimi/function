# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 21:33
# 文件名称：function12.py
# 开发软件：PyCharm
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print('-{}'.format(topping))
make_sandwich('egg')
make_sandwich('egg','vegetable')
make_sandwich('egg','vetetable','ham sausage')