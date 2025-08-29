def save_file(users, filename):
    with open(filename, 'w') as f:
        for user in users:
            f.write(f"User ID: {user['id']}, Name: {user['name']}\n")
    print(f"Users data saved to {filename}")

def load_file(filename):
    result = []
    with open(filename, 'r') as f:
        data = f.read()
        for line in data.splitlines():
            parts = line.strip().split(", ")
            if len(parts) == 2:
                user_id = int(parts[0].split(": ")[1])
                user_name = parts[1].split(": ")[1]
                result.append({"id": user_id, "name": user_name})
    return result

users = [   {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},   
    {"id": 4, "name": "Diana"}]
save_file(users, "user_data.txt")

users = load_file("user_data.txt")
print("Loaded users from file:")
for user in users:   
    print(f"User ID: {user['id']}, Name: {user['name']}")


