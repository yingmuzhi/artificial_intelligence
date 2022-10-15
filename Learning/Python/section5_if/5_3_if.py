
'''
if 语句
'''
age = 19
if age >= 18:
    print("undergraduate")

age = 12
if age < 4:
    print("free\n")
elif age < 18:
    print("25\n")
else:
    print("40\n")

#%%
'''
5-7
'''
favorite_fruits = ["apple", "melon", "grape", ]
favorite_fruits.sort()
for i in range(3):
    favorite_fruits[i] = favorite_fruits[i].title()
# 检查
if "Apple" in favorite_fruits:
    print("Apple is in")
if "banana" in favorite_fruits:
    print("banana in\n")
elif "banana" not in favorite_fruits:
    print("banana is not in\n")
else:
    print("your program go wrong\n")