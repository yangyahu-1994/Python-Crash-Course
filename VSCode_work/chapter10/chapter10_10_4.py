# 文件名称
filename = '/home/yyh/Documents/VSCode_work/chapter10/guest_book.txt'

# 循环
while True:
    name = input("Please enter you name(to quit, please press quit): ")
    if name == 'quit':
        break
    else:
        print("Hello, " + name + "!")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
           

    