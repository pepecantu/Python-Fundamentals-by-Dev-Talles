import os
os.system('cls')

number_list = [1, 2, 3, 4, 5]

# index
print(number_list.index(1))
print(number_list.index(2))
print(number_list.index(3))
print(number_list.index(4))
print(number_list.index(5))

# Start Stop
# Busca el 3, comenzando del índice 0 hasta la posición 5
print(number_list.index(3, 0, 5))   # Retorna que el No 3 esta en el índice 2

# in
# Busca si el 2 esta en la lista
print(1 in number_list)  # regresa True
print(2 in number_list)  # regresa True
print(3 in number_list)  # regresa True
print(4 in number_list)  # regresa True
print(5 in number_list)  # regresa True
print(6 in number_list)  # regresa False

# count
# Busca cuantas veces esta el No. en la lista
number_list1 = [1, 2, 3, 4, 5, 2, 9, 11, 2, 12, 2]
print(number_list1.count(2))    # regresa que se reptie 4 veces
