def greet(person_name):
    return f'Hello, {person_name}!'
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email  
    def introduce(self):
        return f'My name is {self.username} and my email is {self.email}.'
name ='Alice'
hi = greet(name)
print(hi)
age = 30
height = 5.5
print(f'{name} is {age} years old and {height} feet tall.')
user = User(name, 'alice@gmmail.com')
user_intro = user.introduce()
print(user_intro)



