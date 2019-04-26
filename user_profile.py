# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 21:16
# 文件名称：user_profile.py
# 开发软件：PyCharm
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
#user_profile=build_profile('albert','einstein',location='princeton',field='physics')
#print(user_profile)