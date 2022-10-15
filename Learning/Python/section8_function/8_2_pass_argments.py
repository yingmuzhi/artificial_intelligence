# 按顺序传递实参
pass
# 关键字实参
def describe_pet(animal_type, pet_name):
    """show info of pet

    Args:
        animal_type (_type_): _description_
        pet_name (_type_): _description_
    """
    print("I have a {}, and its name is {}".format(animal_type, pet_name))

describe_pet(animal_type="hamster", pet_name="harry")
# describe_pet({"animal_type": "hamster", "pet_name": "harry"})
describe_pet(pet_name="harry", animal_type="hamster")   # 跟顺序无关
# 默认值形参
def describe_pet(animal_type, pet_name = "ymz"):    # 有默认值的形参应该放在最后给出
    print("I have a {}, and its name is {}".format(animal_type, pet_name))

describe_pet("tiger")
