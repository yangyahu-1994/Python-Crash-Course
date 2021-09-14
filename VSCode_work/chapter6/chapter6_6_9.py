# 创建字典
favorite_places = {
    'yang yahu': ['Qinghai Lake', 'Skyland', 'Lhasa'],
    'gao xiangzhou': ['Zhangjiajie'],
    'yang yuhang': ['Haerbin', 'Urumqi'],
    }

# 遍历字典
for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are as following:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite place is { places[0].title()}")