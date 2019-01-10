class Restaurant:
    """描述一个餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is open!")


restaurant_1 = Restaurant('the 2000 year', 'Cantonese')
restaurant_2 = Restaurant('yahui', 'hubei')
restaurant_3 = Restaurant('hougongji', 'sichuan')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
