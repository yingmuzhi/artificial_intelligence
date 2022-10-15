# 使用 if  ... in 判断列表中是否有特定元素
# 使用 for ... in 循环遍历列表，使用 if 对特定元素做出逻辑
requested_toppings = ["mushrooms", "cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "mushrooms":
        print("we are out of {} right now".format(requested_topping))
    else:
        print("ok, full of {}".format(requested_topping))

# 多列表
list1 = [1, 2, 3]
list2 = ["1", "2", "3"]
for i in list1:
    if "1" in list2:
        print("this is round {}, \tand there is \"1\"in list2".format(i))
