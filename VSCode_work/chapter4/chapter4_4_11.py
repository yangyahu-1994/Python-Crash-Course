# 创建列表
my_pizzas = ['Seafood pizza','Sausage pizza','Cheese pizza','Beef pizza','Corn pizza','Chicken pizza']
for pizza in my_pizzas:
    print(f"I like {pizza.lower()}.\n")

print("I really love pizzas.")

# 创建列表副本
friend_pizzas = my_pizzas[:]

# 添加元素
my_pizzas.append('New York Style Pizza')
friend_pizzas.append('Chicago-style pizza')

# 核实列表
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
