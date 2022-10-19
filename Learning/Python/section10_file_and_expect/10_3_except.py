'''
处理异常

# Python 使用名为异常的特殊对象来管理程序执行期间发生的错误。
#   当发生错误而Python解释器不知所措的时候，会创建一个异常对象；
#   若你编写了处理异常的代码，程序将继续运行；
#   若未对异常处理，程序将停止并显示traceback，traceback包含有关异常的报告。
# 异常使用 try...except 代码块处理

发现异常坏处：有异常就有漏洞，黑客就会攻击

try...except...else
在 Python 的异常处理流程中还可添加一个 else 块，当 try 块没有出现异常时，程序会执行 else 块
'''

# %%
# show traceback --- ZeroDivisionError
from importlib.resources import contents


print(5/0)
# %%
# process ZeroDivisionError --- 如果try中代码出现错误，则直接运行except中代码
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# %%
# 使用异常避免崩溃
# division_calculator.py
print("Give me 2 numbers, dividing them.\nEnter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == "q":
        break
    second_number = input("second number:")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:   # 当try成功执行后，会执行else块
        print(answer)
# %%
# 处理 FileNotFoundError 异常
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f: # 参数 encoding , 在系统的默认编码与要读取的文件使用的编码不一致的时候需要这么使用
        contents = f.read
except FileNotFoundError:
    print("sorry, {} does not exit".format(filename))
# %%
# 分析文本
filename = "alice2.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()     #  read() 方法将文件中所有内容以字符串的形式读取到内存中
        print(contents)
        print(type(contents))
except FileNotFoundError:
    print("the {} does not exit".format(filename))
else:
    # 计算单词数
    words = contents.split()    # split对str进行分割，默认以空格为分隔符，并返回一个list
    num_words = len(words)
    print("{} has {} words".format(filename, num_words))
# %%
# 读取多个文件
def count_words(filename):
    """计算一个文件大致包含多少个单词

    Args:
        filename (_type_): _description_
    """
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()     #  read() 方法将文件中所有内容以字符串的形式读取到内存中
            # print(contents)
            # print(type(contents))
    except FileNotFoundError:
        print("the {} does not exit".format(filename))
    else:
        # 计算单词数
        words = contents.split()    # split对str进行分割，默认以空格为分隔符，并返回一个list
        num_words = len(words)
        print("{} has {} words".format(filename, num_words))

filenames = ["alice2.txt", "alice.txt", "pi_digits.txt", "programming.txt"]
for filename in filenames:
    count_words(filename)
# %%
# 静默
# 将except: 后的处理使用 pass 即保持静默，什么都不做。
#   pass 还充当占位符，提醒你在程序的某个地方什么都没作用，并且以后也许要在这里做什么
