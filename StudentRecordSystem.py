#student class 
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    @staticmethod
    def school_info():
        print("Displaying student details...")

    @classmethod
    def create(cls, name, roll_number, grade):
        return cls(name, roll_number, grade)

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.roll_number}")
        print(f"Grade: {self.grade}")


#student objects 
student1 = Student("Alice", 1234, "A")
student2 = Student("Bob", 5678, "B")

#creating student objects using class method
student3 = Student.create("Charlie", 6789, "C")

#displaying school info
Student.school_info()

#displaying student details
student1.display_details()
student2.display_details()
student3.display_details()
