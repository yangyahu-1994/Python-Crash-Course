# 导入模块
import json

# 获取数据
liked_number = input("Please enter the number you like. ")
# 文件名称
filename = '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/liked_number.json'
# 以写入方式打开文件
with open(filename, 'w') as file_object:
    json.dump(liked_number, file_object)

# 再从文件中读取数据
filename = '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/liked_number.json'
with open(filename) as file_object:
    liked_number = json.load(file_object)
    print(f"I know your favorite number! It's {liked_number}.")
