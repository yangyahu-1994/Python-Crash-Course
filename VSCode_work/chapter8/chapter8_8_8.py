# 定义函数
def make_album(singer_name, album_name, number_of_songs = ''):
    """返回一个描述音乐专辑的字典"""
    music_album = {'singer': singer_name, 'album': album_name}
    if number_of_songs:
        music_album['number_of_songs'] = number_of_songs
    return music_album

while True:
    print("\nPlease enter the artist and name of an album:")
    print("(You can press 'q' at any time to quit.)")
    
    s_name = input("Singer name: ")
    if s_name == 'q':
        break

    a_name = input("Album name: ")
    if a_name == 'q':
        break

    n_of_songs = input("Number of songs: ")
    if n_of_songs == 'q':
        break

    album = make_album(s_name, a_name, n_of_songs)
    print(album)



