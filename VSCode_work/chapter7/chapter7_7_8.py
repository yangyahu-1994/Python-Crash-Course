# 创建列表
sandwich_orders = ['Pice','Noy','Pop']
finished_sandwiches = []

# 循环
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

# 打印确认
print(finished_sandwiches)

# 列出三明治
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())