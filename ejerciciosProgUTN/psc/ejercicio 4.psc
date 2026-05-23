	Algoritmo EconomiaSemanal
		
		Definir dias Como Cadena
		Definir gastos Como Real
		Definir i Como Entero
		Definir total Como Real
		Definir promedio Como Real
		
		Dimension dias[7]
		Dimension gastos[7]
		
		dias[1] <- "Lunes"
		dias[2] <- "Martes"
		dias[3] <- "Miercoles"
		dias[4] <- "Jueves"
		dias[5] <- "Viernes"
		dias[6] <- "Sabado"
		dias[7] <- "Domingo"
		
		// Carga de gastos
		Para i <- 1 Hasta 7 Hacer
			Escribir "Ingrese el gasto del ", dias[i], ": "
			Leer gastos[i]
		FinPara
		
		// Calculo del promedio
		total <- 0
		
		Para i <- 1 Hasta 7 Hacer
			total <- total + gastos[i]
		FinPara
		
		promedio <- total / 7
		
		Escribir ""
		Escribir "Promedio general de gasto diario: $", promedio
		
		// Dias que superaron el promedio
		Escribir ""
		Escribir "Dias que superaron el promedio:"
		
		Para i <- 1 Hasta 7 Hacer
			
			Si gastos[i] > promedio Entonces
				Escribir dias[i], ": $", gastos[i]
			FinSi
			
		FinPara
		
FinAlgoritmo
