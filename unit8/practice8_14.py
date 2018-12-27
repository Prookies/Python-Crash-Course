def make_car(manufacturer, model, **car_info):
    """概述要制作的汽车"""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car_1 = make_car('BMW', 'Q5',
                 color='white', parts='navigation')
print(car_1)
