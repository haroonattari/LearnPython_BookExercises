def make_album(artist_name, album_name, number_of_track = 0):
    album = \
        {
            'artist_name': artist_name,
            'album_name': album_name
        }

    if number_of_track > 0:
        album['number_of_track'] = number_of_track

    return album


album = make_album('an artist', 'an album', 99)

print(album)

