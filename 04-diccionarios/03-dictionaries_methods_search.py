import os
os.system('cls')

user = {
    "name": "José Angel",
    "age": 69,
    "greet": "Hola Mundo",
    "numbers": [1, 2, 3]
}

print(user["name"])

# get
print(user.get("name"))

# in busca solamente en las llaves porque contiene un método .keys() por default
print('name' in user)
print('age' in user)

# values
print("José Angel" in user.values())
print(user.values())
print(user.items())
