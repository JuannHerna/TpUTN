'''
Ejercicio 7
Desarrolle un programa que actúe como un traductor de
calificaciones. El usuario deberá ingresar una letra que represente la
nota final del alumno (A, B, C, D o F). Utilizando la estructura de control
alternativa múltiple (Segun), el sistema debe procesar la opción tanto
en mayúsculas como en minúsculas y devolver un mensaje
descriptivo personalizado sobre el rendimiento del estudiante (ej:
"Excelente", "Insuficiente", "Reprobado").
'''

nota = input("Ingrese nota: ")
nota = nota.upper()

match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Muy bien")
    case "C":
        print("Bien")
    case "D":
        print("Regular")
    case "F":
        print("Reprobado")
    case _:
        print("Valor invalido")