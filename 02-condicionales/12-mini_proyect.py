import os
os.system("cls")
# Instrucciones:
# Crearás un programa de evaluación de candidatos potenciales en Python para RH.
# Obtendrás el nombre, años de experiencia y habilidades.

# Evalarás:
# Si el coandidato sabe Python/Django, tiene +3 años de experiencia: Candidato Optimo.
# Si el candidato sabe Python/Django, tiene +1 año de experiencia: Buen candidato.
# Si el candidato sabe Python/Django: Posible candidato
# Si el candidato no sabe Python: No optimo, se guardará CV

# Consejo: Ocupa los metodos .split()
name = input("Nombre del candidato: ")
experience = int(input("años de experiencia: "))
skills = input(
    "Ingrese sus habilidades separadas por comas (ej. Python, Laravel, Gloang, Django, etc): ").split(",")

evaluate_skills = "Python" in skills or "Django" in skills


if evaluate_skills:
    if experience >= 3:
        result = "Candidato optimo"
    elif experience >= 1:
        result = "Buen candidato"
    else:
        result = "Posible candiidato"
else:
    result = "No apto, se guardará CV para futuras ofertas"

print(f"El candidato {name} es: {result}")
