# 导入模块
import json

# 文件名称
filename = '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/liked_number.json'
try:
    with open(filename) as file_object:
        liked_number = json.load(file_object)
except FileNotFoundError:
    liked_number = input("Please enter the number you like. ")
    with open(filename, 'w') as file_object:
        json.dump(liked_number, file_object)
else:
    print(f"I know your favorite number! It's {liked_number}.")