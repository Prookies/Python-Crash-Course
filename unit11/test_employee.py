import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试雇员类"""

    def setUp(self):
        """创建一个雇员对象"""
        self.first_name = 'xu'
        self.last_name = 'hua'
        self.salary = 200000
        self.employee = Employee(self.first_name, self.last_name, self.salary)

    def test_give_default_raise(self):
        """测试雇员薪水增加为默认值"""
        self.employee.give_raise()
        self.assertEqual(self.salary + 5000, self.employee.salary)

    def test_give_custom_raise(self):
        """测试雇员薪水增加为给定值"""
        self.employee.give_raise(10000)
        self.assertEqual(self.salary + 10000, self.employee.salary)


if __name__ == "__main__":
    unittest.main()
