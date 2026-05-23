Ejercicio 7
Desarrolle un programa que actúe como un traductor de
caliﬁcaciones. El usuario deberá ingresar una letra que represente la
nota ﬁnal del alumno (A, B, C, D o F). Utilizando la estructura de control
alternativa múltiple (Segun), el sistema debe procesar la opción tanto
en mayúsculas como en minúsculas y devolver un mensaje
descriptivo personalizado sobre el rendimiento del estudiante (ej:
"Excelente", "Insuﬁciente", "Reprobado")


Algoritmo Ejercicio7
	
	Definir nota Como Caracter
	
	Escribir "Traductor de calificaciones"
	Escribir "Ingrese nota final (A, B, C, D, F):"
	Leer nota
	
	Segun nota Hacer
		"A", "a":
			Escribir "Excelente"
		"B", "b":
			Escribir "Muy bien"
		"C", "c":
			Escribir "Bien"
		"D", "d":
			Escribir "Insuficiente"
		"F", "f":
			Escribir "Reprobado"
		De Otro Modo:
			Escribir "ERROR: La letra no es una calificacion"
	FinSegun
	
	
FinAlgoritmo
