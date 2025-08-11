def make_album(singer, name, amount=None):
    album_info = {'Singer': singer, 'Album_name' : name}
    if amount:
        album_info['Amount'] = amount
    return album_info

while True:
    print("Please tell me the singer and album name:")
    print("Enter 'q' at anytime to quit")

    singer = input("Singer:")
    if singer == 'q':
        break

    name = input("Album name:")
    if name == 'q':
        break

    amount = input("Amount:")
    if amount == 'q':
        break

    album_information = make_album(singer, name, amount)
    print(f"The album's name is {name.title()}  by {singer.title()}, and the amount of the song is {amount} ")