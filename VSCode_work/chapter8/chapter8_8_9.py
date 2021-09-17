# 定义函数
def show_magicians(magicians):
    """显示每个魔术师"""
    for magician in magicians:
        print(magician.title())

# 创建列表
magicians = ['hannah', 'ty', 'margot']
show_magicians(magicians)