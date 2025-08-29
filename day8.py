class Employee:
    def __init__(self, name, salary):
        self.name = name  # Private attribute
        self._salary = salary  # Private attribute

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        if salary >= 0:
            self._salary = salary
        else:
            raise ValueError("Salary cannot be negative")
    def introduce(self):
        print(f"Employee Name: {self.name}, Salary: {self._salary}")
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department  # Public attribute

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department
    def introduce(self):
        print(f"Manager Name: {self.name}, Salary: {self._salary}, Department: {self.department}")

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand  # Public attribute
        self.speed = speed  # Public attribute

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}, Speed: {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self.model = model  # Public attribute

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Speed: {self.speed} km/h")


empnormal = Employee("Alice", 60000)
empnormal.introduce()
mamager = Manager("Bob", 80000, "Sales")
mamager.introduce()

veh = Vehicle("Toyota", 180)
veh.display_info()
car = Car("Honda", 200, "Civic")
car.display_info()