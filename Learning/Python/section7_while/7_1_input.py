# example1 使用input获取输入
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# example2
prompt = "if you tell us who you're we will welcome you."
prompt += "So, tell us who you are."
name = input(prompt)
print(name)
#%%
# 将字符串转换为int
age = input("how old are you?")
print(type(age))
age = int(age)
print(type(age))
# %%
height = int(input("what is your height?"))
print(type(height))
# %%
# 求余，使用求模运算符实现
print(4%3)
# %%
# 使用求余判断是奇数（odd）还是偶数（even）
number = int(input("Enter a number, I will tell the odd or even"))
if number % 2 == 0:
    print("this is a even a number")
else:
    print("this is a odd number")

# %%
