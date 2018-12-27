def make_album(singer, album, number=''):
    msg = {'singer': singer, 'album': album}
    if number:
        msg['number'] = number
    return msg


singer_1 = make_album('Zhou', '1', 3)
singer_2 = make_album('Wang', '2')
singer_3 = make_album('Zhang', '3')
print(singer_1)
print(singer_2)
print(singer_3)

while True:
    print("Please input the name and album of singer: ")
    print("(enter 'q' at any time to quit)")

    name = input("Name: ")
    if name == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break

    msg_singer = make_album(name, album)
    print(msg_singer)
