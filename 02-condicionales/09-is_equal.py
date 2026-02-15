import os
os.system("cls")  # Clear the console

# Equal o igualdad

print(5 == 5)       # True
print(True == 1)    # True
print('' == 1)      # False
print([] == 1)      # False
print(10 == 10.0)   # True

new_list = {1}
other_list = {1}
print(new_list == other_list)   # True

new_list = [1, 2]
other_list = [1]
print(new_list == other_list)   # False

# # is compara en memoria 0x123ab (num exadecimal), si existen valores en memoria significa que esa variable es única
new_list = []
other_list = []
print(new_list is other_list)   # False
print(new_list == other_list)   # True

# Y el = compara los valores
new_list = []
other_list = []
print(new_list is other_list)   # False
print(new_list == other_list)   # True
