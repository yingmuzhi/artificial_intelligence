'''
将函数存储在模块中

导入整个模块，模块即扩展名为.py的文件
'''
# 导入模块  以下四种导包方式
import test
from test import make_pizza
# from test import make_pizza as mp
from test import *

test.make_pizza(1, 2, 3)