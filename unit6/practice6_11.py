cities = {
    'shanghai': {
        'country': 'China',
        'population': 2000,
        'fact': 'it is a beautiful city',
    },
    'london': {
        'country': 'England',
        'population': 1500,
        'fact': 'it is the capital of England'
    },
    'new york': {
        'country': 'US',
        'population': 2500,
        'fact': 'it is the economic center of the US',
    },
}
for city, city_info in cities.items():
    print("Name: " + city)
    for key, value in city_info.items():
        print(key + " : " + str(value))
    print('\n')

