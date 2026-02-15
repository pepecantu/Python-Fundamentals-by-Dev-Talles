import os
os.system("cls")  # limpia la consola


# if is_student:
#     print("Licencia de estudiante")
# else:
#     print("Licencia normal")

'''
Opreador ternario if else en una sola línea
True if condición else False
Primero va el mensaje si es verdadero la condición se cumple (True),
luego la condición if is_strudent else
y al final el mensaje si es falso o la condición no se cumple (False)
True if condición else false
'''

is_student = True

get_license = "(True)= El es un estudiante" if is_student else "(False)= El no es un estudiante"
print(get_license)
