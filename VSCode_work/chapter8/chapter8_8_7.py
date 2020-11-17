# 定义函数
def make_album(singer_name, album_name, number_of_songs = ''):
    """返回一个描述音乐专辑的字典"""
    music_album = {'singer': singer_name, 'album': album_name}
    if number_of_songs:
        music_album['number_of_songs'] = number_of_songs
    return music_album

# 调用函数
album_0 = make_album('李建', '《深海之寻》', 2)
print(album_0) 
album_1 = make_album('李建', '《美若黎明》', 12)
print(album_1)
album_2 = make_album('李建', '《美若黎明》')
print(album_2)

