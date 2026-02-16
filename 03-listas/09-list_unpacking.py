import os
os.system('cls')

# Asignar valores de una lista a variables independientes, 

listNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listNums)

# Desenpaquetando (unpacked) asignando valores a variables independientes
a, b, c, d, *listNums = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Usando el (*) para evitar errores en la paridad de asignaciones

print(f'valor de a: {a}')
print(f'valor de b: {b}')
print(f'valor de c: {c}')
print(f'valor de d: {d}')


print(f"{listNums}  valores de la lista no fueron asignados a variables")

"""
Se imprimirá de la siguiente forma:
1
2
3
4
[5, 6, 7, 8, 9]

"""
# Asignando otra variable después de imprimir los valores restantes, se asignará el úlimo valor

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, c, d, *listaNumeros, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Usando el (*) para evitar errores en la paridad de asignaciones

print(f'valor de a: {a}')
print(f'valor de b: {b}')
print(f'valor de c: {c}')
print(f'valor de d: {d}')
print(listaNumeros)
print(f'valor de e: {e}') #Asigando valor a la variable e despúes de el nombre de la variable, se le asignará el último valor (9)

print(f"{listaNumeros}  valores restantes no asignados a variables")
