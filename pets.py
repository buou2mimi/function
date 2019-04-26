# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 15:05
# 文件名称：pets.py
# 开发软件：PyCharm
def describle_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type,pet_name.title()))
describle_pet('hamster','harry')
describle_pet('dog','wangcai')
describle_pet(animal_type='cat',pet_name='zhaocai')
describle_pet(pet_name='xueli',animal_type='bird')
describle_pet(pet_name='huotuirou')