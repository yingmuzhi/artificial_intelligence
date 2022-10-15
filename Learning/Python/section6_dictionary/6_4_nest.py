# list中套dic
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "black", "points": 10}
aliens = [alien_0, alien_1]
for alien in aliens:
    print(aliens)
# 用for自动填充list
aliens = []
for alien_number in range(30):
    alien = {"color": "green", "points": 5}
    aliens.append(alien)
for alien in aliens[:5]:    # 打印前5个数据
    print(alien)
print(len(aliens))          # 打印数组长度

# dic中套list
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
# 打印信息
print("you order a {} pizza, and your toppings are {}".format(
    pizza["crust"],
    pizza["toppings"][0],
))
for topping in pizza["toppings"]:
    print("topping is {}".format(topping), end="\t")
favorite_languages = {
    "Jen": ["python", "ruby"],
    "max": ["c", "c++", "python", "go"],
}
for name, languages in favorite_languages.items():
    print("")
    print("student {} like these languages:".format(name), end="\t")
    for language in languages:
        print(language, end=", ")
print("")

# dic中套dic
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcuries": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print("user name is {}".format(username))
    for key, value in user_info.items():
        print("\tkey is {} and value is {}".format(key, value))