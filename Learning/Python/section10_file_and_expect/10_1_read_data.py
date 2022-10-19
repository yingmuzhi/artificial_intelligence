import os, sys
project_path = os.path.dirname(__file__)
sys.path.append(project_path)
# --- 读取文件，将内容显示到屏幕上 ---
# open()返回一个表示文件的对象
# 关键字with在不再需要访问文件后将其关闭，即由python确定何时调用close()关闭文件
# 使用read()方法读取文件对象的全部内容，并将值赋值给contents变量
# read()结果在结尾会多一个空行，使用rstrip()删除空行
# r"" 字符串表示不变转义字符解释，windows中常用如'\t'这种; 或者可以使用"C:\\path"双斜杠解决问题
with open(project_path + r"/pi_digits.txt") as file_object: 
    contents = file_object.read()
print(contents.rstrip())

# --- 文件路径 ---
with open(project_path + r"/test/file_name.txt") as file_object:
    contents = file_object.read()
print(contents.rstrip())

# 逐行读取
# 通过对 文件对象 执行循环遍历来实现
filename = project_path + "/pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:    # 逐行读取
        print(line.rstrip())

#%%
# 使用list存储文件内容，使得在with外面也能访问文件内容
# 可以用文件对象的readlines()实现：readlines()从文件中读取每一行，并存储在一个列表中，每一个元素是一行的内容。
# 也可以通过循环遍历文件对象实现
file_name = "pi_digits.txt"

with open(file_name) as file_object:
    # lines = file_object.readlines()
    lines = []
    for line in file_object:
        lines.append(line)  # 将硬盘上文件内容 读入 内存中

for line in lines:
    print(line.rsplit())
# %%
# 强制转换
# 从文件中读取数据默认数据类型是str, 使用int()强制转换为int类型, 是用float()强制转换为float类型.
a = "11"
print(type(a))
print(type(float(a)))
print(type(int(a)))

# %%
# 用 if...in 判断文件中是否含有你需要的字符串
# 
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string:str = ""
for line in lines:
    pi_string += line.strip()

if "3.14" in pi_string:
    print("True")

# %%
