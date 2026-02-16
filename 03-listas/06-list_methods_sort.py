import os
os.system('cls')

letters = ['a', 'b', 'm', 'o', 'c', 'z', 'g', 'd', 'e']
print(letters)

# Sort()
# letters.sort()
# print(letters)

#Función sorted(para no modificar la lista original)
# new_letters = sorted(letters)
# print(new_letters)
# print(letters)

# new_letters = letters[:] # crea la nueva lista con List slicing
# new_letters.sort()       # ordena la lista con sort
# print(new_letters)

new_letters = letters.copy()    # copiando la lista       
new_letters.sort()              # Oredenando con .sort
print(new_letters)

# Método reverse
letters.reverse()
print(letters)
