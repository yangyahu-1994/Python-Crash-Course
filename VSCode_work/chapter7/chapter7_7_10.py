# 创建字典
places = {}

# 设置一个标志，指出调查是否继续
polling_avtive = True

while polling_avtive:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    respose = input("If you could visit one place in the world, where would you go? ")

    # 将回答存储在字典中
    places[name] = respose

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_avtive = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, respose in places.items():
    print(name + "'s dream resort is " + respose + ".")