# 定义函数
def show_magicians(magicians, new_magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician = 'the Great ' + current_magician
        new_magicians.append(current_magician)

def make_great(new_magicians):
    for new_magician in new_magicians:
        print(new_magician)


# 创建列表
magicians = ['hannah', 'ty', 'margot']
new_magicians = []

# 调用函数
show_magicians(magicians, new_magicians)
make_great(new_magicians)

