# split the list
players = ["ymz", "miko", "miku", "max"]
print(players[0: 3])    # 序列0-2
print(players[-3: ])    # 序列2-···
# 遍历list的一部分
for player in players[:-2]:
    print(player)
# !!!并不是复制列表，只是赋予了一个指向该列表的指针!!!
friend_list = players
players.pop()
print(friend_list)
# !!!复制列表
friend_list = players[:]
players.append("mx")
print(friend_list)
'''
split string
'''
my_string = "the first three items in the list are:"
print(my_string[:3])
