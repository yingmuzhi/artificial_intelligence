'''
make some changes in list element
'''
# 修改list中元素值
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
# 添加元素
motorcycles.append("ducati")    # 尾部添加
print(motorcycles)
motorcycles.insert(0, "honda")  # 指定序列位置添加
print(motorcycles)
# 删除元素
del motorcycles[1]              # 删除指定序列元素
print(motorcycles)
popped_motorcycle = motorcycles.pop()   # 删除尾部元素，并且像栈一样弹出该元素
print(popped_motorcycle)
print(motorcycles)
popped_first = motorcycles.pop(0)   # 弹出第一个元素
print(popped_first)
print(motorcycles)
motorcycles.remove("yamaha")    # 删除特定值的元素
print(motorcycles)

#%%
'''
experiment 3-4
'''
dinner_list = ["ada lovelace", "qianjin guo", "wu liu", "klq", "hkt"]
print("I wanna invite these people to have dinner with me, they're {}, {}, {}, {}, {}".format(dinner_list[0], dinner_list[1], dinner_list[2],
    dinner_list[3], dinner_list[4], ))
# %%
'''
experiment 3-6
'''
dinner_list = ["ada lovelace", "qianjin guo", "wu liu", "klq", "hkt"]
dinner_list.append("sgc")
dinner_list.insert(-1, "hmy")
dinner_list.insert(len(dinner_list)//2, "lst")
print(dinner_list)
# %%
'''
experiment 3-7
'''
dinner_list = ["ada lovelace", "qianjin guo", "wu liu", "klq", "hkt"]
pop_visitor = dinner_list.pop()
print("dear {}, I am sorry that I can't have dinner with you".format(pop_visitor))
# %%
