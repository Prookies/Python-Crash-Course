def city_country(city='Shanghai', country='China'):
    """接受城市的名称及其所属的国家，并将其格式化"""
    msg = '"' + city + ', ' + country + '"'
    return msg


city_1 = city_country('Santiago', 'Chile')
print(city_1 + "\n")
city_2 = city_country('Guangzhou', 'China')
print(city_2 + "\n")
city_3 = city_country('London', 'UK')
print(city_3 + "\n")
