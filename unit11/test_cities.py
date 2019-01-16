import unittest
from city_functions import get_formatted_city


class CitiesTestCase(unittest.TestCase):
    """测试city_functions"""

    def test_city_country(self):
        formatted_city = get_formatted_city('chile', 'Santiago')
        self.assertEqual(formatted_city, 'Chile, Santiago')

    def test_city_country_population(self):
        formatted_city = get_formatted_city('chile', 'Santiago', 5000)
        self.assertEqual(formatted_city, 'Chile, Santiago - population 5000')


if __name__ == "__main__":
    unittest.main()
