def make_album(artist, title, songs=None):
    dictionary = {'artist': artist, 'title': title}
    if songs:
        dictionary['songs'] = songs
    return dictionary


print(make_album('Slayer', 'Reign in Blood'))
print(make_album('Metallica', 'Load'))
print(make_album('Rammstein', 'Zeit', 11))
