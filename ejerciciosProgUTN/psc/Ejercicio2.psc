Algoritmo Ejercicio2
	
	Definir precio, subtotal, iva, total Como Real
	Definir cantidad Como Entero
	
	Escribir "Ingrese el precio del producto:"
	Leer precio
	Escribir "Ingrese la cantidad comprada:"
	Leer cantidad
	
	subtotal <- precio * cantidad
	iva <- subtotal * 0.21
	total <- subtotal + iva
	
	Escribir "Subtotal: ", subtotal
	Escribir "IVA (21%): ", iva
	Escribir "Total: ", total

	
FinAlgoritmo