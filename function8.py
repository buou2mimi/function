# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 15:30
# 文件名称：function8.py
# 开发软件：PyCharm
def make_album(name,album,song=''):
    if song=='':
        albunm_information={'name':name.title(),'album':album.title()}
    else:
        albunm_information={'name':name.title(),'album':album.title(),'song':song.title()}
    return albunm_information


active=True
while active:
    print("\n(enter 'q' at any time to quit)")
    name=input("Please enter one of your favorite singers' name:")
    if name == 'q':
        break
    album=input("Please enter the singer's album:")
    if album=='q':
        break
    song=input("If you want,you enter one song of the album:")
    if song=='q':
        break
    user_informations=make_album(name,album,song)
    print(user_informations)
