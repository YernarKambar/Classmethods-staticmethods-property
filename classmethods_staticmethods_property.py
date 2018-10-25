class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def create_new_employee(cls, new_employee_string):
        pass

    @staticmethod
    def calculate_salary_in_year(salary_in_month):
        pass

    @property
    def fullname_of_employee(self):
        pass

    @fullname_of_employee.setter
    def fullname_of_employee(self, new_fullname_of_employee):
        pass

    @fullname_of_employee.deleter
    def fullname_of_employee(self):
        pass
