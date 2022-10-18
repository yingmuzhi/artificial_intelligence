'''
判断逻辑
'''
#%%
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    elif car == "audi":
        print(car.lower())
    else:
        print(car.title())
# %%
# 判断语句，使用==判断相等，!=判断不等
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("not equal")
# %%
# and和or 代表 与/或
age = 44
if (age >= 21) and (age <= 99):
    print("call it")


# %%
# 使用 if...in 判断 list 中是否含有特定值
my_list = ["is", "ymz"]
if "ymzc" not in my_list:
    print("I'm not in")
# %%
