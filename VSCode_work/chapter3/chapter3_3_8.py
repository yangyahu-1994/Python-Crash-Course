# 创建原始列表并打印
travel_places = ['lhasa','lijiang','qinghai lake','skyland']
print(travel_places)

# 按字母顺序打印该列表，同时不要修改原始列表
print("\n这里是按照字母顺序打印的列表：")
print(sorted(travel_places))

# 再次打印该列表，核实顺序未变
print("\n这个是原始列表：")
print(travel_places)

# 按与字母顺序相反的顺序打印这个列表，同时不要修改它
print("\n这个是与字母顺序相反的列表：")
print(sorted(travel_places,reverse = True))

# 再次打印该列表，核实顺序未变
print("\n这个是原始列表：")
print(travel_places)

# 修改列表元素的排列顺序
print("\n这个是逆序排列的列表：")
travel_places.reverse()
# 核实排列顺序
print(travel_places)

# 再次修改列表元素的排列顺序
print("\n这个是正序排列的列表：")
travel_places.reverse()
# 核实排列顺序
print(travel_places)

# 修改列表，使其元素按照字母顺序排序
travel_places.sort()
# 核实排列顺序
print(travel_places)

# 修改列表，使其元素按与字母顺序相反的顺序排列
travel_places.sort(reverse = True)
# 核实排列顺序
print(travel_places)