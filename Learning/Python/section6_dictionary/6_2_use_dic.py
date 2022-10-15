# 访问键值对
alien_0 = {"color": "green", "points": 5}
print("I am in, and the alien's color is {}".format(alien_0["color"]))
# 添加键值对
alien_0["x_position"] = 0
print(alien_0)
# 创建空字典
alien_1 = {}
alien_1["color"] = "blue"
alien_1["points"] = 10
print(alien_1)
# 修改键值对的值
alien_1["points"] = 15
print(alien_1)
# 删除键值对
alien_1["append"] = "NULL"
print(alien_1)
del alien_1["append"]
print(alien_1)
# 使用get()方法来访问值, 基本不用
alien_1_position = alien_1.get("position", "no position assigned\n")
print(alien_1_position)