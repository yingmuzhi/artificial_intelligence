'''
使用json是一种在程序之间共享数据的简单方式

存储数据一般使用模块json
JSON - JavaScript Object Notation
'''
import os, sys
project_path = os.path.dirname(__file__)
# 使用 json.dump() 和 json.load()
import json

numbers = [2, 3, 5, 7,]

filename = os.path.join(project_path, "numbers.json")
print(filename)
with open(filename, "w") as f:
    json.dump(numbers, f)   # 使用 json.dump() 存储数据到外存上

#%%
# 使用 json.load() 将外存数据读取到内存中
import json
filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

# %%
# 使用 json 保护和读取用户生成的数据
import json
import os


filename = os.path.join(os.path.dirname(__file__), "username.json")
# try...
try:
    # read
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("what is your name?")
    # write
    with open(filename, "w") as f:
        json.dump(username, f)
        print("we will remember you when you come back, {}".format(username))
else:
    print("welcome back, {}".format(username))
# %%
# 重构 - 代码重构，指改进代码，使得代码更清晰，易于理解和扩展
