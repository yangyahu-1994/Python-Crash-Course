# 定义函数
def sandwich_ingredients(*toppings):
    """打印一条消息，对顾客点的三明治进行概述"""
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# 调用函数
sandwich_ingredients('Toast', 'Six eggs')
sandwich_ingredients('Tomato slices', 'Lettuce leaves')
sandwich_ingredients('Jinhua ham')