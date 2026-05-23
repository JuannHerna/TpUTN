	Algoritmo ConversionMoneda
		
		Definir pesos Como Real
		Definir dolar Como Real
		Definir euro Como Real
		Definir resultado_dolar Como Real
		Definir resultado_euro Como Real
		
		Escribir "---------------------------------------------"
		Escribir " Herramienta de conversion de moneda "
		Escribir "---------------------------------------------"
		
		Escribir "Ingrese el valor en pesos:"
		Leer pesos
		
		Escribir "Ingrese la cotizacion actual del dolar:"
		Leer dolar
		
		Escribir "Ingrese la cotizacion actual del euro:"
		Leer euro
		
		resultado_dolar <- pesos / dolar
		resultado_euro <- pesos / euro
		
		Escribir ""
		Escribir pesos, " pesos equivalen a:"
		
		Escribir "USD: ", resultado_dolar, " dolares"
		Escribir "EUR: ", resultado_euro, " euros"
		
FinAlgoritmo
