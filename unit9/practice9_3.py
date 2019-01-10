class Restaurant:
    """描述一个餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name.title() + ".")
        print("The restaurant's cuisine type is " + self.cuisine_type + ".")
        print("There are " + str(self.number_served) + " people in restaurant")

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_serverd(self, number):
        """将参观人数设定为指定的值"""
        self.number_served = number

    def increment_number_served(self, number):
        """将参观人数递增"""
        self.number_served += number


restaurant_1 = Restaurant('the 2000 year', 'Cantonese')
restaurant_2 = Restaurant('yahui', 'hubei')
restaurant_3 = Restaurant('hougongji', 'sichuan')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print('\n')
restaurant_1.describe_restaurant()
restaurant_1.number_served = 10
restaurant_1.describe_restaurant()

print('\n')
restaurant_2.set_number_serverd(200)
restaurant_2.describe_restaurant()
restaurant_2.increment_number_served(300)
restaurant_2.describe_restaurant()