# 文件名称
filename = '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/guest_book.txt'

# 循环
while True:
    name = input("Please enter you name(to quit, please press quit): ")
    if name == 'quit':
        break
    else:
        print(f"Hello, {name}!")
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
           

    