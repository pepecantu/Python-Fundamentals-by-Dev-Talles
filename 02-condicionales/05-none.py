import os
os.system("cls")  # limpia la consola

# None = False, vacío, ausecia de valor
# Null = None

user = "jacantu"  # no hay valor asignado a la variable user

if user:
    print("Este usuario esta registrado")  # no se ejecuta porque user es None
else:
    print("Usuario disponible")  # se ejecuta porque user es None

user_vacio = None

if user_vacio:
    print("Este usuario esta registrado")  # no se ejecuta porque user es None
else:
    print("Usuario disponible")  # se ejecuta porque user es None
