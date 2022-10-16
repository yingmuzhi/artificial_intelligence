
'''
一个用于表示汽车的类
'''

class Car(object):
    """汽车模拟"""

    def __init__(self, model):
        self.model = model

    def print_car(self):
        print("I am in")


class ElectricCar(object):
    pass