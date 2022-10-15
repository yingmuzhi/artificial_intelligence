# 一个简单的函数
def greet_user():
    """say hello
    """
    print("Hello!\n")

greet_user()
# 函数传参
def greet_user(username):
    """say hello
    """
    print("hello, {}".format(username))

greet_user("max")