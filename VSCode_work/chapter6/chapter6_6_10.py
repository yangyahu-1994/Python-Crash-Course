# 创建字典
like_numbers = {
    'yang yahu': [666, 777, 888, 999, 111, 222, 333, 444, 555],
    'gao xiangzhou': [777, 675, 256, 342, 278, 999],
    'yang yuhang': [888, 111, 125, 567, 789],
    'li jianfeng': [999, 123, 234, 345, 456, 567, 678],
    'yuan li': [256, 356, 456, 567, 678],
    }

# 打印名字及喜欢的数字
for name, numbers in like_numbers.items():
    print(f"\n{name.title()} likes these numbers: ")
    for number in numbers:
        print(f"\t{number}")
