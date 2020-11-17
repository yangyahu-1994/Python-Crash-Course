# 用户输入
number = input("How many people are dining? ")

# 比较判断
number = int(number)
if number > 8:
    print("\nNo free tables.")
else:
    print("\nFree tables.")