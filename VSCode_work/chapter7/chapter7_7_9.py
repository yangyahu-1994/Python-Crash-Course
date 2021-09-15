# 创建列表
sandwich_orders = ['Pice','Noy','Pop','pastrami','pastrami','pastrami','pastrami']
finished_sandwiches = []

# 打印消息
print("The five cigarette pastrami at the deli is sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

# 打印确认
print(finished_sandwiches)

# 列出三明治
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())