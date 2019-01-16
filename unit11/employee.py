class Employee:
    """收集雇员信息"""

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_add=5000):
        """增加雇员的薪水"""
        self.salary += salary_add
