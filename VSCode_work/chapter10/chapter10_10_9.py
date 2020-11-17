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
        pass
    else:
        print(contents.rstrip())

# 文件列表
filenames = ['cats.txt', 'dogs.txt']
# 调用函数
for filename in filenames:
    find_file(filename)