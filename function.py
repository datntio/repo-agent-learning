def add_user(Users, user_id, user_name):
    Users.append({"id": user_id, "name": user_name})
    return Users
def find_user_by_id(Users, user_name):
    for user in Users:
        if user["name"] == user_name:
            return user
    return None
def list_users(Users):
    for user in Users:
        print(f"User ID: {user['id']}, Name: {user['name']}")
users =[]
users = add_user(users, 1, "Alice")
users = add_user(users, 2, "Bob")
users = add_user(users, 3, "Charlie")
users = add_user(users, 4, "Diana")
list_users(users)
print ("find user by name:  Bob")
user = find_user_by_id(users, "Bob")
print(user)
