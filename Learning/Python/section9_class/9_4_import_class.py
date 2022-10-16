
'''
导入类
'''

from car import Car # 导入类，类名往往大写。根据大写可判断是类
from car import Car, ElectricCar    # 从一个module(指一个.py文件)中导入多个class

my_new_car = Car("audi")
my_new_car.print_car()