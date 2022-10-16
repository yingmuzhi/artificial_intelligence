
'''
Python 标准库是一组模块，即其他程序员写好的模块
需要注意的是模块名往往小写，而类名的首字母往往大写
'''

from random import randint  # 随机返回两个参数中间的值
print(randint(1, 6))

from random import choice   # 将一个list或tuple作为参数传入，随机返回其中的一个元素
players = ["max", "ymz", "scj"]
first_up = choice(players)
print(first_up)