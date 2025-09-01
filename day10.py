class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self, age):
        if(age > 0):
            self.__age = age
        else:    
            raise ValueError("Age cannot be negative")
    def study(self):
        return f"{self.__name} is studying."

david = Student("David", 20)
print(f"Student Name: {david.get_name()}, Age: {david._Student__age}")
david.set_name(10)   
print(f"Updated Age: {david._Student__age}")

class  Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary cannot be negative")
    def work(self):
        return f"{self.name} is working."
emma = Employee("Emma", 70000)
print(f"Employee Name: {emma.name}, Salary: {emma.get_salary()}")

class ShoppingCart:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            raise ValueError("Item not found in cart")
    def get_items(self):
        return self.__items
    
cart = ShoppingCart()
cart.add_item("Laptop") 
cart.add_item("Smartphone")
print("Items in cart:", cart.get_items())   
cart.remove_item("Laptop")
print("Items in cart after removal:", cart.get_items()) 
