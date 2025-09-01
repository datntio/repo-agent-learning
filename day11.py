from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class bird(Animal):
    def speak(self):
        return "Chirp!"
animals = [Dog(), Cat(), bird()]
for animal in animals:
    print(animal.speak())

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."
class Bike(Vehicle):
    def start_engine(self):
        return "Bike engine started."
class Plane(Vehicle):
    def start_engine(self):
        return "Plane engine started."
vehicles = [Car(), Bike(), Plane()]
for vehicle in vehicles:
    print(vehicle.start_engine())

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."
class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} using PayPal."
class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} in Cash."
payments = [CreditCardPayment(), PayPalPayment(), CashPayment()]
for payment in payments:
    print(payment.pay(100))


