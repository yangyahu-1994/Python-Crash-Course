def find_file(filename):
    """
    尝试读取文件，将其内容打印到屏幕上。
    并在文件不存在时，捕获异常，打印一
    条友好的消息。
    """
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = f"Sorry, the file {filename} does not exist."
        print(message)
    else:
        
        print(contents.rstrip())

filenames = ['/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/cats.txt',
             '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/dogs.txt']
for filename in filenames:
    find_file(filename)