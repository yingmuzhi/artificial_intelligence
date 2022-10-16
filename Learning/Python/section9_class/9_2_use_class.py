# 类
class Car:
    """一次模拟汽车的尝试
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

    def get_descriptive_name(self):
        """返回整洁信息
        """
        long_name = "this car is made by {} in {}".format(self.make, self.year)
        return long_name


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())


# 给属性指定默认值
class Car:

    def __init__(self, model):
        """初始化描述汽车的属性

        Args:
            model (_type_): _description_
        """
        self.make = "China"
        self.model = model
    
    def modify_make(self, make):
        """修改产地
        """
        self.make = make


my_car = Car("audi")
print(my_car.make)
my_car.modify_make("US")
print(my_car.make)

