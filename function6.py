# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 21:42
# 文件名称：function6.py
# 开发软件：PyCharm
def city_country(name,country):
    city='"{},{}"'.format(name.title(),country.title())
    return city
c_c=city_country("yangzhou","china")
print(c_c)
c_c=city_country("new york","america")
print(c_c)
c_c=city_country("london","britain")
print(c_c)