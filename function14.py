# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/26 10:52
# 文件名称：function14.py
# 开发软件：PyCharm
def make_car(manufacturer,model,**information):
    car_information={}
    car_information['manufacturer']=manufacturer
    car_information['model']=model
    for key,value in information.items():
        car_information[key]=value
    return car_information
car=make_car('subaru','outback',color='bule',tow_package=True)
print(car)