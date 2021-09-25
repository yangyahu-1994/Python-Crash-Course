# 循环
while True:
    first_number = input("\n请输入一个数： ")
    if first_number == 'q':
        break
    second_number = input("请输入另一个数： ")
    if second_number == 'q':
        break
    
    try:
        # ValueError异常处理
        numbers_sum = int(first_number) + int(second_number)
        print(f"您输入的两个数字之和为： {numbers_sum}")
    except ValueError:
        print("抱歉，您输入的不是两个数字！")