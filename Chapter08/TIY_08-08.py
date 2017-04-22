def make_album():
    album = {}
    number = 0

    while True:
        artist_name = input("Enter artist name or 'quit' to exit: ")

        if artist_name.lower() == 'quit':
            break

        album_name = input("Enter album name: ")

        album[number] = {
            'artist_name': artist_name,
            'album_name': album_name
        }

        number += 1

    return album


my_album = make_album()

print(my_album)

