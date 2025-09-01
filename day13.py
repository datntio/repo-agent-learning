def divide(a, b):
    try:
        result = a / b  
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Invalid input type. Please provide numbers."
    else:
        return result
    finally:
        print("Execution completed.")
print(divide(10, 2))
print(divide(10, 0))  
print(divide(10, 'a'))  
print(divide(10, None))

def user_input():
    while True:
        try:
            value = int(input("Enter a positive integer: "))
            if value < 0:
                raise ValueError("Negative value entered.")
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
        else:
            print(f"You entered: {value}")
            break
        finally:
            print("Attempt to get user input completed.")
# user_input()

class InvalidAgeError(Exception):   
    def __init__(self, age):
        self.age = age  
    def set_age(self):
        if self.age < 0 or self.age > 150:
            raise InvalidAgeError(self.age)
        else:
            return self.age 

input_ages = [25, -5, 200, 45]
for age in input_ages:
    try:
        person = InvalidAgeError(age)
        valid_age = person.set_age()
    except InvalidAgeError as e:
        print(f"Invalid age: {e.age}. Age must be between 0 and 150.")
    else:
        print(f"Valid age entered: {valid_age}")


            
          
