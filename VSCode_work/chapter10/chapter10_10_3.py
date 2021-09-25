# 获取用户输入
user_name = input("Please enter your name: ")

# 文件名称
filename = '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/guest.txt'

# 以写入模式打开文件
with open(filename, 'w') as file_object:
    file_object.write(user_name)