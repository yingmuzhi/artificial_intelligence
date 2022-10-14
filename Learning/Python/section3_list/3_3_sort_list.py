# 使用list的sort()方法对列表中元素进行排序, 改变list
# sort使用快排实现
cars = ["bmw", "auto", "toyota"]   
cars.sort() # 正序排序
print(cars)
cars = ["bmw", "auto", "toyota"]   
cars.sort(reverse=True) # 倒序排序
print(cars)
# 排序，不改变list
cars = ["bmw", "auto", "toyota"]   
print(sorted(cars))
print(cars)
# 将list中元素按位置顺序反转, 改变list
cars = ["bmw", "auto", "toyota"]   
cars.reverse()
print(cars)
# 确定list长度
print(len(cars))
#%%
travel_list = ["UK", "China"]
print(sorted(travel_list))
travel_list.sort()
print(travel_list)
travel_list.reverse()
print(travel_list)
# %%
