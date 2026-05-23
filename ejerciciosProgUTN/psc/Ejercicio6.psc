Algoritmo Ejercicio6
	
	Definir lado, fila, columna Como Entero
	
	Escribir "Ingrese lado del cuadrado (Numero entero)"
	Leer lado
	
	Mientras lado <= 0 Hacer
		Escribir "ERROR: El lado debe ser mayor a 0"
		Escribir "Intente nuevamente:"
		Leer lado
	FinMientras
	
	Escribir "Dibujando cuadrado"
	Escribir ""
	
	Para fila <- 1 Hasta lado Hacer
		Para columna <- 1 Hasta lado Hacer 
			Escribir " * " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
FinAlgoritmo