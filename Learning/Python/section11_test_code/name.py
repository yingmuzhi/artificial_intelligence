def get_formatted_name(first, last):
    """生成名字

    Args:
        first (_type_): _description_
        last (_type_): _description_
    """
    full_name = "{} {}".format(first, last)
    return full_name.title()