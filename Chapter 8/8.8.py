def make_album(artist, title, songs=None):
    dictionary = {'artist': artist, 'title': title}
    if songs:
        dictionary['songs'] = songs
    return dictionary


while True:
    artist = input('Please, enter an artist name (q tu quit): ')
    if artist == 'q':
        break
    title = input('Please, enter an album title (q tu quit): ')
    if title == 'q':
        break
    print(make_album(artist, title))

