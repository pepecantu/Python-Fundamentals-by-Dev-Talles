import os
os.system('cls')

# Crear una lista de números utilizando una clase (list) se le incluye otra clase (Range) y un tope (100)
numbers = list(range(100))  # Crea una lista de números del 0 al 99
print(numbers)

# ' '.Join().- Función que requiere un iterable para crear un string a partir de una lista de [strings]
# Junta todos lo valores de la lista y los convierte en un string
# Dejar un string vacío o espacio antes del .join

sentence = ' '.join(['Hola', 'Mundo', 'desde', 'un', 'join', 'saludos'])

print(sentence)  # Regresa este string = Hola Mundo desde un join saludos

# Utilizando la funcion sum() para sumar los valores de la lista numbers
total = sum (numbers)
print(total)

mayor = max(numbers)
print(mayor)
menor = min(numbers)
print(menor)
elements = len(numbers)
print(elements)
