import os
os.system('cls')

number_list = [1, 2, 3, 4, 5]
print(number_list)

# pop() retira el último elemento de la lista
number_list.pop()
print(number_list)

# añadiendo el número del índice elimina el indicado
number_list.pop(0)
print(number_list)

# remove() elimina el valor no el índice, si queremos eliminar el No 4 de la lista
number_list.remove(4)
print(number_list)

# pop() elimina el primer número que encuentre, si hay un 3 repetido, elimina el primero
number_list = [1, 2, 3, 4, 3, 5]
print(number_list)

number_list.remove(3)
print(number_list)

# clear() elimina toda la lista
number_list.clear()
print(number_list)
