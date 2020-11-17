# 文件名称
filename = '/home/yyh/Documents/VSCode_work/chapter10/causes.txt'

# 循环
while True:
    cause = input("Why do you like programming?(to quit, please press quit): ")
    if cause == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(cause + "\n")