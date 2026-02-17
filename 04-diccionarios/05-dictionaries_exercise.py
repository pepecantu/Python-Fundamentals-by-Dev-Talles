import os
os.system('cls')

students = {
    "Ana": [5, 7, 4],
    "Luis": [6, 5, 7],
    "Sofía": [10, 9, 10]
}
print(students)

# Agregar un nuevo estudiante
students["José"] = [8,9,9]
print(students)

# Sacar el promedio de un estudiante existente
name = "Ana"
if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0] + student_grades[1] + student_grades[2]) / 3
    
    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")
        
else:
    print("El estudiante no esta registrado")
    
name = "Ricardo"
if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0] + student_grades[1] + student_grades[2]) / 3
    
    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")
        
else:
    print("El estudiante no esta registrado")  

name = "José"
if name in students:
    student_grades = students[name]
    total_grade = (student_grades[0] + student_grades[1] + student_grades[2]) / 3
    
    if total_grade >= 6.0:
        print(f"{name} aprobó con un promedio de: {total_grade:.2f}")
    else:
        print(f"{name} reprobó con un promedio de: {total_grade:.2f}")
        
else:
    print("El estudiante no esta registrado")
