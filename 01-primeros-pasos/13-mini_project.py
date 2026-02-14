
# Recibir de forma dinámica de un cliente: nombre, año de nacimeinto y contraseña

name = input('¿Cuál es tu nombre? ')
year_of_birth = input('¿En que año naciste? ')
email = input('¿Cuál es tu email ')
password = input('Ingresa tu password ')

print(name)
print(year_of_birth)
print(email)
print(password)

# Con f formating
future_age = 2050 - int(year_of_birth)
password_length = len(password)
message = f'''
\nTe llamas: {name}
\ntu fecha de nacimiento es: {year_of_birth}
\ntu email es: {email}
\ny tu password es: {'*' * password_length}
\nEn el año 2050 tendras {future_age} años
'''
print(message)
