import os
os.system('cls')

# Matriz es una lista que contiene listas

matrix = [
    [1, 2, 3],  # lista 0, valores: índice 0 =1, índice 1 = 2, índice 2 = 3
    [4, 10, 6], # lista 1, valores: índice 0 = 4, índice 1 = 10, índice 2 = 6
    [7, 8, 9],  # lista 2, valores: índice 0 = 7, índice 1 = 8, índice 2 = 9
]
print(matrix)

# Accediendo a una lista en particular: Lista 1 = [4, 10, 6]
print(matrix[1])

# Accediendo a un valor de una lista en particular = 10, se encuentra en el índice 1 de la lista 1
print(matrix[1][1])
print(matrix)
# Cambiando el valor que esta en el índice 1 de la lista 1, es el 10, cambiar por un 5
matrix[1][1] = 5
print(matrix[1][1]) # = 5
print(matrix)
