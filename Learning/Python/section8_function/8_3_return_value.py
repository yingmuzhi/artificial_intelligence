# 具有返回值的函数
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名

    Args:
        first_name (_type_): _description_
        last_name (_type_): _description_
    """
    full_name = "{} {}".format(first_name, last_name)
    return full_name.title()

musician = get_formatted_name("max", "shi")
print(musician)
# 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name = ""):
    if middle_name:
        full_name = "{} {} {}".format(first_name, middle_name, last_name)
    else:
        full_name = "{} {}".format(first_name, last_name)
    return full_name.title()

musician = get_formatted_name("max", "shi", "ymz")
print(musician)