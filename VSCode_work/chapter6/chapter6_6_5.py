# 创建字典
rivers = {'nile': 'egypt',
          'Yangtze river': 'china',
          'Yellow river': 'china',
          }

# 为每条河流打印一条消息
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 打印每条河流的名字
for river in rivers.keys():
    print(river.title())
# 另一种表达
#for river in rivers:
#   print(river.title())
# 打印每个国家的名字
for country in set(rivers.values()):
    print(country.title())