# 获取用户输入
name = input("Please enter your name: ")

# 文件名称
filename = '/home/yyh/Documents/VSCode_work/chapter10/guest.txt'

# 以写入模式打开文件
with open(filename, 'w') as file_object:
    file_object.write(name)