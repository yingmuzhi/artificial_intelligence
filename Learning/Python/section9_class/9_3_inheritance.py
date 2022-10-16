'''
子类继承父类所有属性和方法，还可以定义自己的属性和方法
'''


class Car:
    """车的基类
    """

    def __init__(self, make, model, year):
        """初始汽车

        Args:
            make (_type_): _description_
            model (_type_): _description_
            year (_type_): _description_
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回基本信息
        """
        # long_name = "this car is made by {} in {}".format(self.make, self.year)
        long_name = "{} {} {}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        print("this car has {} miles on it".format(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't go back")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# 创建派生类
class ElectricCar(Car):
    """电动车独特之处

    Args:
        Car (_type_): _description_
    """

    def __init__(self, make, model, year):
        """初始化父类属性

        Args:
            make (_type_): _description_
            model (_type_): _description_
            year (_type_): _description_
        """
        super().__init__(make, model, year) # 父类也称为超类superclass

my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
