def get_formatted_city(city, country, population=0):
    if population:
        formatted_city = city.title() + ", " + country.title() + " - population " + str(population)
    else:
        formatted_city = city.title() + ", " + country.title()
    return formatted_city
