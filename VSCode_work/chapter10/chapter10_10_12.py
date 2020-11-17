# 导入必要的模块
import json

# 文件名称
filename = 'liked_number'
try:
    with open(filename) as file_object:
        liked_number = json.load(file_object)
except FileNotFoundError:
    liked_number = input("Please enter the number you like. ")
    with open(filename, 'w') as file_object:
        json.dump(liked_number, file_object)
else:
    print("I know your favorite number! It's " + liked_number + ".")