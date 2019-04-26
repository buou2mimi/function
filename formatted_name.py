# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 20:31
# 文件名称：formatted_name.py
# 开发软件：PyCharm
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return  full_name.title()
musician=get_formatted_name('john','hooker','lee')
print(musician)
musician=get_formatted_name('jimi','hendrix')
print(musician)