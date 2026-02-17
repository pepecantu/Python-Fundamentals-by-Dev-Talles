import os
os.system('cls')

user = {
    "name": "José Angel",
    "age": 69,
    "email": "jacantu@hotmail.com",
    (19.432695223377202, -99.13201714547445): "Palacio Nacional Cd. Mx"
}

print(user)
print(user["name"])

# Cambiando valores
user["name"] = "Pepe"
user["age"] = 55
print(user["name"])
print(user["age"])
print(user)

# Agregando elementos 
user["country"] = "México"
print(user)

print(user[(19.432695223377202, -99.13201714547445)])
