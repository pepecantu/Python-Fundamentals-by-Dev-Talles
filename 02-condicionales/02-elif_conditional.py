import os
os.system("cls")  # limpia la consola


is_old = False
is_licenced = False

if is_old:
    print("Tienes edad para manejar")
elif is_licenced:
    print("No tienes edad, pero tienes licencia")
    print("Puedes manejar con tu licencia en la ciudad")
else:
    print("No tienes edad y no tienes licencia")
    print("Espera a cumplir la mayoría de edad o tramita tu licencia")
