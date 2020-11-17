# 创建字典
favorite_places = {
    'yang yahu': ['Qinghai Lake', 'Skyland', 'Lhasa'],
    'gao xiangzhou': ['Zhangjiajie'],
    'yang yuhang': ['Haerbin', 'Urumqi'],
    }

# 遍历字典
for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + "'s favorite places are as following:")
        for place in places:
            print("\t" + place.title())
    else:
        print("\n" + name.title() + "'s favorite place is " + places[0].title())