import os
os.system("cls")

shopping_cart = [
    'camisas',
    'tenis',
    'calcetas',
    'panalones'
]
print(shopping_cart[3])  # Se crea una lista nueva y la original queda intacta
print(shopping_cart[0])
print(shopping_cart[2])
print(shopping_cart[1])


# [Inicio : fin]
# [0:4], imprimirá del indice 0 al índice 3, el 4 no se toma en cuenta
print(shopping_cart[0:4])
print(shopping_cart[0:3])
print(shopping_cart[0:2])
print(shopping_cart[0:1])

# Copiar una lista sin afectar a la original

# afectando a la original
print('\n--- Copiando lista original Shopping_cart a una nueva new_cart ---\n')
print('\n--- Lista Original ---')
print(shopping_cart)
new_cart = shopping_cart
print('--- Lista copiada igual a la original ---')
print(new_cart)
new_cart[0] = 'Playeras'
new_cart[1] = 'Zapatos'
print('\n--- Se modifica lista copiada new_cart de camisas a playeras y de tenis a Zapatos  ---\n')
print('--- Lista original Shopping_cart se ve afectada cambia ---')
print(shopping_cart)
print('--- Lista copiada new_cart tambien cambia ---')
print(new_cart)

# Ulitizando slicing [:] para evitar modificar la variable original
shopping_cart = [
    'camisas',
    'tenis',
    'calcetas',
    'panalones'
]
print(
    '\n--- Copiando lista original Shopping_cart a una nueva new_cart con slicing [:] ---\n')
print('\n--- Lista Original ---')
print(shopping_cart)
new_cart = shopping_cart[:]
print('--- Lista copiada igual a la original ---')
print(new_cart)
new_cart[0] = 'Playeras'
new_cart[1] = 'Zapatos'
print('\n--- Se modifica lista copiada new_cart de camisas a playeras y de tenis a Zapatos  ---\n')
print('--- Lista original Shopping_cart se mantiene sin cambios ---')
print(shopping_cart)
print('--- Lista copiada new_cart cambia ---')
print(new_cart)
