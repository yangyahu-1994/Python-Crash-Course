# 文件名称
filename = '/home/yyh/Documents/VSCode_work/chapter10/learning_python.txt'

# 逐行读取
with open(filename) as file_object:
    for line in file_object:
        replaced_line = line.replace('Python', 'C')
        print(replaced_line.rstrip())