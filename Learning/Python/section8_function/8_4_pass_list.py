# 将list作为变量传入
def greet_users(names):
    """向列表中的各位用户发出简单的问候

    Args:
        names (_type_): _description_
    """
    for name in names:
        msg = "hello, {}".format(name)
        print(msg)

user_names = ["max".title(), "ymz".upper(), "SCJ".lower()]
greet_users(user_names)
#%%
# 修改传入实参值
def print_models(unprinted_designs, completed_models):
    """打印模型

    Args:
        unprinted_designs (_type_): _description_
        completed_models (_type_): _description_
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("this one has been finished --- {}".format(current_design))
        completed_models.append(current_design)

def show_completed_models(completed_models):
    if completed_models:
        for model in completed_models:
            print(model)
    else:
        print("there is noting!")

unprinted_designs = ["case", "kernel", ]
completed_models = []
show_completed_models(completed_models)
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# %%
# 禁止函数修改传入的列表，我们可以复制一个列表传入
show_completed_models(completed_models[:])  # 在函数中进行的操作并不会影响自变量，即作为实参传入的list