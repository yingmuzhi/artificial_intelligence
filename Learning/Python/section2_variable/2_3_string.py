
# 名字大小写变化
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
# 字符串替换
first_name = "ada"
last_name = "lovelace"
full_name = "{0} {1}".format(first_name, last_name)
print(full_name)
# 去除空白
favorite_language = "        python       "
favorite_language1 = favorite_language.rstrip() # 剔除尾部空白  right
favorite_language2 = favorite_language.lstrip() # 剔除首部空白  left
favorite_language3 = favorite_language.strip()  # 剔除首位空白
print(favorite_language1)
print(favorite_language2)
print(favorite_language3)
# 转义字符
print("my name is max.\t\twhat's your name?\nmy name is ymz.")