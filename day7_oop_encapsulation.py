class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self.__salary = salary  # Private attribute

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")
class Product:
    def __init__(self, name, price):
        self.name = name  # Public attribute
        self.__price = price  # Private attribute

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price cannot be negative")

bob = Employee("Bob", 50000)
print(f"Employee Name: {bob.get_name()}, Salary: {bob.get_salary()}")

iphone = Product("iPhone", 999)
print(f"Product Name: {iphone.get_name()}, Price: {iphone.get_price()}")