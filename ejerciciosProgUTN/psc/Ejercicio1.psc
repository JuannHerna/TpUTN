Algoritmo Ejercicio1
	
	Definir venta, total Como Real
	Definir cantidad Como Entero
	
	total <- 0
	cantidad <- 0
	
	Escribir "Ingrese el monto de la venta (0 para cerrar caja)"
	Leer venta
	
	Mientras venta <> 0 Hacer
		
		Si venta < 0 Entonces
			Escribir "ERROR: el monto no debe ser negativo"
		Sino
			total <- total + venta
			cantidad <- cantidad + 1
		FinSi
		
		Escribir "Ingrese la siguiente venta o 0 para cerrar"
		Leer venta
		
	FinMientras
	
	Escribir "Total de ventas: ", cantidad
	Escribir "Total dinero: ", total
	
FinAlgoritmo