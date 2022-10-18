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
filename = project_path + "/pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:    # 逐行读取
        print(line.rstrip())