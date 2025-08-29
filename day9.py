class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")  
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
        import math
        return math.pi * (self.radius ** 2)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

ahapes = [
    Rectangle(4, 5),
    Circle(3), 
    Triangle(6, 7)
]
print("Areas of different shapes:")
for shape in ahapes:    
    print(f"{shape.__class__.__name__} area: {shape.area()}")

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method") 
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")
class cashPayment(Payment):
    def pay(self, amount):
        print(f"Processing cash payment of ${amount:.2f}")
payments = [
    CreditCardPayment(),    
    PayPalPayment(),
    cashPayment()
]
amount = 100.0
print("\nProcessing different payment methods:")
for payment in payments:
    payment.pay(amount)