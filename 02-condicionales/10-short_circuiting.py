import os
os.system("cls")
" Corto circuito"

# OR
True or print("Hola mundo")
False or print("Hola mundo con True OR Print()\nFalse OR print()")

True or print("Hola mundo") or True
False or print("Hola mundo con True OR print() OR True\nFalse or print()")

# AND

False and print("Hola Mundo")
True and print("Hola Mundo con True y AND")

name = "José"
print(name.upper())

# name = None
# print(name.Upper)

# Como usar el .Upper en los falsys que no lo permiten
name = None
print(name and name.Upper)

name = False
print(name and name.Upper)

name = 0
print(name and name.Upper)

name = []
print(name and name.Upper)
