# 使用列表解析生成一个列表
cubes = [value ** 3 for value in range(1,11)]
print(cubes)

# 打印列表的前三个元素
print("\nThe first three items in the list are:")
print(cubes[:3])

# 打印列表的中间四个元素
print("\nFour items from the middle of the list are:")
print(cubes[-7:-3])

# 打印列表末尾的三个元素
print("\nThe last three items in the list are:")
print(cubes[-3:])