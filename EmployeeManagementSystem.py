#Employee class
class Employee:
    company_name = "ABC Corp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company_name}")
    
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def is_salary_high(salary):
        return salary > 50000



#creating employee objects
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

#displaying employee details
employee1.display_details()
employee2.display_details()

#changing company name
Employee.change_company("XYZ Corp")

#displaying employee details
employee1.display_details()
employee2.display_details()

#checking if salary is high
print(Employee.is_salary_high(employee1.salary))
print(Employee.is_salary_high(employee2.salary))