'''
写入文件
'''
#%%
# 写入空文件
# open(filename, [''])  open方法中可以指定参数，若不指定则默认以只读方式打开文件
#                       "r" - 读取; "w" - 写入; "a" - 附加; "r+" - 读写;
#                           需要注意的是，若以写入模式打卡且原本就存在文件，python会在返回文件对象前清空该文件的内容; python只会写入字符串，用好str()
file_name = "programming.txt"
with open(file_name, "w") as file_object:
    file_object.write("I love cpp.")

# %%
file_name = "programming.txt"
with open(file_name, "w") as file_object:
    file_object.write("I love cpp,\n")
    file_object.write("and i also like python.\n")
# %%
file_name = "programming.txt"
with open(file_name, "a") as file_object:
    file_object.write("I love cpp too,\n")
    file_object.write("and i also like python too.")

# %%
