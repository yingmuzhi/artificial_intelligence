'''
测试函数
'''
from name import get_formatted_name

first = input("input your first name\n")
last  = input("input your last name\n")
print(get_formatted_name(first, last))

# %%
# 各种测试
# **单元测试**用于核实函数的某个方面没有问题
# **测试用例**是一组单元测试，一道核实函数在各种情形下的行为都符合要求。
# **全覆盖**的测试用例包含一整套单元测试，古代各种可能的函数使用方式
import unittest
from name import get_formatted_name

class NamesTestCase(unittest.TestCase): # 必须继承自测试类
    """测试name.py

    Args:
        unittest (_type_): _description_
    """

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？
        """
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

# 若这个文件作为主程序执行，__name__将被设置为"__main__"，将自动运行冒号后面的内容
# 若这个文件/.py/module被测试框架导入，变量__name__将不是"__main__"，因此不会运行后面的内容
if __name__ == "__main__":  
    unittest.main()
# %%
