users = [
    {"id": 1, "name": "Alice","age":30},
    {"id": 2, "name": "Bob","age":25},  
    {"id": 3, "name": "Charlie","age":35},
    {"id": 4, "name": "Diana","age":28},
    {"id": 5, "name": "Ken","age":48},
]
users_age = sorted(users, key=lambda x: x['age'])
for user in users_age:
    print(f"User ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")

users_by_age_28 = [user for user in users if user['age'] > 28]

print("Users older than 28:")   

for user in users_by_age_28:
    print(f"User ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")

ages = {user['name']: user['age'] for user in users }
print("Ages dictionary:", ages) 
