# 定义函数
def count_numbers(filename):
    """获取指定的文件，并计算单词'the'在每个文件中出现的次数"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + "does not exits.")
    else:
        # 计算出现的次数
        numbers = contents.lower().count('the')
        print("The word 'the' appears " + str(numbers) + " times in file " + filename + ".")

# 获取文件
filenames = ['63558-0.txt', '63559-0.txt', '63560-0.txt']
for filename in filenames:
    count_numbers(filename)
        