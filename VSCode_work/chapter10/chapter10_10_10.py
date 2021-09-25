# 定义函数
def count_numbers(filename):
    """获取指定的文件，并计算单词'the'在每个文件中出现的次数"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exits.")
    else:
        # 计算出现的次数
        numbers = contents.lower().count('the')
        print(f"The word 'the' appears {numbers} times in file {filename}.")

# 获取文件
filenames = ['/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/63558-0.txt', 
             '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/63559-0.txt', 
             '/home/yyh/Documents/Python_Crash_Course/Python-Crash-Course/VSCode_work/chapter10/data/63560-0.txt']
for filename in filenames:
    count_numbers(filename)
        