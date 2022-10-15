
# while 和 list 结合
unconfirmed_users = ["ymz", "scj"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print("1")
# 使用 while 删除 list中特定值的所有元素
# list.remove()方法只能删除出现该值的第一个元素，所以要删除所有元素得使用while循环
pets = ["dog", "cat", "dog", "tiger", "dog", ]
while "dog" in pets:
    pets.remove("dog")
print(pets)
#%%
# 使用用户输入来填充字典
responses = {}
active = True   # 设置一个标志，判断调查是否继续
while active:
    name = input("your name?")
    response = input("ok, what is your Q?")
    responses[name] = response
    if response != "quit":
        print("next")
        # continue
    else:
        print("over")
        active = False
        # break
for name, response in responses.items():
    print("name is {}, and the response is {}".format(name, response))
# %%
