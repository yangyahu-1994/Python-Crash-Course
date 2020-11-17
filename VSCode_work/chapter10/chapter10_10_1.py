# 文件名称
filename = '/home/yyh/Documents/VSCode_work/chapter10/learning_python.txt'

print("---------第一次打印：读取整个文件----------")
with open(filename) as file_object:
    contents = file_object.read() # 函数read()读取文件对象的全部内容
    print(contents.rstrip())

print("--------第二次打印：遍历文件对象------")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("-------第三次打印：将各行存储在一个列表中---------")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

