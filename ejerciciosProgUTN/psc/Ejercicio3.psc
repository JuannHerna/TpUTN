Algoritmo Ejercicio3
	
	Definir estatura Como Real
	Definir vip Como Caracter
	Definir tieneVip, puedeIngresar Como Logico
	
	Escribir "Bienvenido al control de acceso."
	Escribir "Ingrese estatura en metros (ejemplo 1.65)"
	Leer estatura
	
	Mientras estatura < 0.5 O estatura > 2.5 Hacer
		Escribir "ERROR: La estatura debe ser en metros (ejemplo 1.80)"
		Escribir "Ingrese su estatura correctamente:"
		Leer estatura
	FinMientras
	
	Escribir "Posee VIP? (S/N)"
	Leer vip
	
	Si vip = "S" O vip = "s" Entonces
		tieneVip <- Verdadero
	Sino
		tieneVip <- Falso
	FinSi
	
	puedeIngresar <- (estatura > 1.50) Y (tieneVip = Verdadero)
	
	Escribir "Puede ingresar?: ", puedeIngresar
	
	Si puedeIngresar Entonces
		Escribir "¡Acceso concedido!"
	Sino
		Escribir "Acceso denegado."
	FinSi
	
FinAlgoritmo