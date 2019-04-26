# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 20:26
# 文件名称：function5.py
# 开发软件：PyCharm
def describe_city(name,country='China'):
    print('{} is in {}.'.format(name.title(),country.title()))
describe_city('yangzhou')
describe_city('sicuan')
describe_city('new york','america')