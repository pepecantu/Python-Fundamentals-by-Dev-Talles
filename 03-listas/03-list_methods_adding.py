import os
os.system('cls')

# Metodos de adición
numbres_list = [1, 2, 3, 4, 5]
print(numbres_list)

# append o añadir, añade el valor al último de la lista
numbres_list.append(100)
numbres_list.append(200)
print(numbres_list)

# insert = insertamos el 200 en el espacio del índice 1, valor 500
numbres_list.insert(1, 500)
print(numbres_list)

# Extends agrega una lista dentro de otra lista.
numbres_list.extend([11, 22, 33])
print(numbres_list)
