class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
    def area(self):
        return 3.14 * self.radius * self.radius
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
shapes = [Rectangle(4, 5), Circle(3), Triangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")

class Employee:
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
def print_salaries(emp : Employee):
    print(f"Salary: {emp.calculate_salary()}")
employees = [FullTimeEmployee(3000), PartTimeEmployee(20, 80)]
for emp in employees:
    print_salaries(emp)
