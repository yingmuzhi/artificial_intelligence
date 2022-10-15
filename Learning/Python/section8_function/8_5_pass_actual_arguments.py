
# 传递任意数量的实参
def make_pizza(*toppings):  # *号的意思是让python创建一个名为toppings的空元组，并将收到的所有值封装到这个元组中
    """打印顾客点的所有配料
    """
    print(toppings)
    for topping in toppings:
        print(topping)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):    # **号的意思是让python创建一个名为user_info的空字典，并将收到的所有键值对放到这个空字典中
    """创建字典，包含我们知道的有关用户的一切信息

    Args:
        first (_type_): _description_
        last (_type_): _description_
    """
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location = "princeton", field = "physics")
print(user_profile)

