# _*_ coding :UTF-8 _*_
# 开发人员：C
# 开发时间：2019/4/26 14:45
# 文件名称：printing_functions.py
# 开发软件：PyCharm
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model:{}".format(current_design))
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)