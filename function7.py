# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/21 21:55
# 文件名称：function7.py
# 开发软件：PyCharm
def make_album(name,album,song=''):
    if song=='':
        albunm_information={'name':name.title(),'album':album.title()}
    else:
        albunm_information={'name':name.title(),'album':album.title(),'song':song.title()}
    return albunm_information
a_i1=make_album('jay chou','ye hu mei')
print(a_i1)
a_i2=make_album('jay chou','initial j','qilixiang')
print(a_i2)