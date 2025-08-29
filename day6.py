class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model  
        self.year = year
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def introduce(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

ford = car("Ford", "Mustang", 2020)
ford.display_info() 
vinfast = car("Vinfast", "Lux A2.0", 2021)
vinfast.display_info()
g63 = car("Mercedes-Benz", "G63", 2022)
g63.display_info()
alice = Student("Alice", "A")
alice.introduce()
bob = Student("Bob", "B")
bob.introduce()
charlie = Student("Charlie", "A+")
charlie.introduce()
