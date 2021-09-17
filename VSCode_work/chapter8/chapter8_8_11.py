# 定义函数
def make_great(magicians, new_magicians):
    """显示魔术师"""
    while magicians:
        current_magician = magicians.pop()
        new_magician = f"the Great {current_magician}"
        new_magicians.append(new_magician)
    
    return new_magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# 定义列表
magicians = ['ling', 'hui', 'he']
new_magicians = []

# 调用函数
returned_new_magicians = make_great(magicians[:], new_magicians)
show_magicians(magicians)
print("---------------我是分割线------------------")
show_magicians(returned_new_magicians)
