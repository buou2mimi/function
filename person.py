# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 21:08
# 文件名称：person.py
# 开发软件：PyCharm
def build_person(first_name,last_name,age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician=build_person('jimi','hendrix',age=27)
print(musician)