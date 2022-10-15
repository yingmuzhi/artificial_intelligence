import os
print(dir(os))
print(os.__doc__)
print(os.__file__)

def make_pizza(size, *toppings):
    """概述制作pizza的topping

    Args:
        size (_type_): _description_
    """
    for topping in toppings:
        print(topping)