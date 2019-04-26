# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/24 16:37
# 文件名称：printing_models.py
# 开发软件：PyCharm
unprint_designs=['iphone case','robot pendant','dodecahedron']
completd_models=[]
while unprint_designs:
    current_design=unprint_designs.pop()
    print("Printing model:{}".format(current_design))
    completd_models.append(current_design)
print("\nThe following models have been printed:")
for completd_model in completd_models:
    print(completd_model)