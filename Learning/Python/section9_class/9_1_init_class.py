'''
创建dog类
'''
class Dog:  # 类名首字母要大写
    """模拟小狗 # 文档说明符合下文空一格
    """

    def __init__(self, name, age):
        """_summary_

        Args:
            name (_type_): _description_
            age (_type_): _description_
        """
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令蹲下
        """
        print("{} is now setting".format(self.name))

    def roll_over(self):
        """模拟小狗打滚
        """
        print("{} is now rolling in deep".format(self.name))

    def length_of_tail(self):
        pass

    @staticmethod
    def ddd():
        return 0
        pass


a = Dog.ddd()
print(a)
# 实例化对象
my_dog = Dog("Willie", 6)
my_dog.name = "max"
my_dog.sit()
my_dog.roll_over()