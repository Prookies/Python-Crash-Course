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


class IceCreamStand(Restaurant):
    """描述一个冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_icecream(self):
        print("Here has these favors:")
        for flavor in self.flavors:
            print(flavor)


favors = ['banana', 'apple', 'chocolate']
icecreamstand_1 = IceCreamStand('tiantianwu', 'vanilla', favors)
icecreamstand_1.describe_restaurant()
icecreamstand_1.describe_icecream()
