# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 20:30
# 文件名称：function10.py
# 开发软件：PyCharm
def make_great(unmodified_magician_names,modified_magician_names):
    while unmodified_magician_names:
        current_magician_name=unmodified_magician_names.pop()
        modified_magician_names.append("the Great "+current_magician_name)

def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name.title())
u_m_n=['chee ling qua','david copperfield','liu qian','daryl']
m_n=[]
make_great(u_m_n[:],m_n)
show_magicians(m_n)
show_magicians(u_m_n)