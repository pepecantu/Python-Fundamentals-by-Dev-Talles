import os
os.system("cls")  # limpia la consola

# Truthy y Falsey en Python
# truthy (Verdadero) Si es int siempre es diferente de 0
print('---truthy ---\n')
print(bool(True))  # True booleano
print(bool(1))  # True numero entero
print(bool(123))  # True numero entero
print(bool(1.1))  # True numero decimal
print(bool(-1))  # True numero entero negativo
print(bool(1j))  # True  número complejo
print(bool(" "))  # True espacio
print(bool('Hola'))  # True string
print(bool([1, 2, 3]))  # True list
print(bool((1, 2, 3)))  # True tuple
print(bool({1, 2, 3}))  # True set
print('\n')

# falsey (Falso) Si es int siempre es igual a 0, esta vacío o es None
print('---falsey ---\n')
print(bool(False))  # False booleano
print(bool(0))  # False numero entero
print(bool(000))  # False numero ceros
print(bool(0.0))  # False numero decimal
print(bool(-0))  # False numero cero negativo
print(bool(0j))  # False numero complejo
print(bool(""))  # False string vacio
print(bool([]))  # False list vacia
print(bool(()))  # False tupla vacia
print(bool({}))  # False dict vacio
print(bool(None))  # False NoneType
