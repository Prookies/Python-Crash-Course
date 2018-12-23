rivers = {
    'Changjiang': 'China',
    'The Nile': 'Egypt',
    'Amazon': 'Brazil',
}

for river, country in rivers.items():
    print(river+" run through "+country)

print('\n')
for river in rivers.keys():
    print(river)

print('\n')
for country in rivers.values():
    print(country)
