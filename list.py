users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},   
    {"id": 4, "name": "Diana"},
]
for user in users:
    print(f"User ID: {user['id']}, Name: {user['name']}")

users.append({"id": 5, "name": "Eve"})
print("After adding a new user:")
for user in users:
    print(f"User ID: {user['id']}, Name: {user['name']}")