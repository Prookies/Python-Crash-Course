favorite_places = {
    'hua': ['zhuhai', 'wuhan', 'shanghai'],
    'jun': ['guangzhou', 'beijing'],
    'peng': ['nanchang', 'xiameng'],
}

for name, places in favorite_places.items():
    print("Name: "+name)
    print("He favorite place: ")
    for place in places:
        print(place+"\t")
