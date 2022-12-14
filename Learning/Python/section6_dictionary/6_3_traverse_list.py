# 遍历字典
user_0 = {
    "t": 1,
    "username": "fermi",
    "first": "enrico",
    "last": "fermi",
}
for item in user_0.items(): # (key, value)类型返回是tuple
    print(type(item))

for key in user_0.keys():   # key类型为string
    print(type(key))

for value in user_0.values():   # value类型由value决定
    print(type(value))

# 遍历所有键值对
for key, value in user_0.items():
    print("key is {}, and value is {}".format(key, value))
# 遍历所有键
for key in user_0.keys():
    print(key.title()) 
for key in user_0:
    print(key.title())
# 顺序遍历键
for key in sorted(user_0.keys()):
    print(key.upper())
# 遍历值
for value in user_0.values():
    print(value.title())
# 遍历值，只遍历不重复的值
for value in set(user_0.values()):
    print(value)
# 集合，不以特定顺序存储非重复元素
my_set = {"python", "c", "c", "cpp"}
print(my_set)
