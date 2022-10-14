# range()函数做for循环
for value in range(0, 5):
    print(value)
# 使用list()函数将range转换为数组
number = list(range(0, 5))
print(number)
# 使用range()和for循环往list中增加数据
squares = []
for value in range(11):
    square = value ** 2
    squares.append(square)
print(squares)
# 计算一些样本的数字特征，统计值
print(min(squares)) # 选最小值
print(max(squares)) # 选最大值
print(sum(squares)) # 计算总和
# 列表解析, 生成list
squares = [value**2 for value in range(1, 11)]
print(squares)

#%%
'''
experiment 4-3
'''
for i in range(20):
    print(i + 1)
# %%
'''
4-4
'''
my_list = [i+1 for i in range(1_000_000)]
for i in range(1_000_000):
    print(my_list[i])
# %%
'''
4-5
'''
my_list = [i+1 for i in range(1_000_000)]
print("the min is {}, the max is {}".format(min(my_list), max(my_list)))
print("ths sum is {}".format(sum(my_list)))
# %%
'''
4-6
'''
for i in range(0, 20, 2):
    print(i+1)
# %%
