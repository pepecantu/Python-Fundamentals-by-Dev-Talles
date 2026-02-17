import os
os.system('cls')

user = {
    "name": "José Angel",
    "age": 69,
    "greet": "Hola Mundo",
    "numbers": [1, 2, 3]
}

user_copy = user.copy()
print(user)
print(user_copy)

# alterando el dicionario copia
user_copy ['age']  = 25
print(user_copy)

# .pop()
user.pop('age')
print(user)

# pop item() elimina el último elemento de un diccionario
user.popitem()
print(user)

# .update()
user.update({'name': 'Pepe'}) # actualizando valores
print(user)

user.update({'cats': 2})
print(user)

# .append()
user['skills'] = user.get('skils', [])
print(user)

# Agregando una lista ['Python', 'Dyango']
user['skills'].append('Python')
user['skills'].append('Dyango')
print(user)
