"""Ejercicio 3
Desarrolle un sistema automatizado de control de acceso para la
atracción extrema de un parque de diversiones. El programa debe
solicitar la estatura del cliente (en metros) y preguntar si posee un
pase VIP mediante una respuesta de texto (S/N). Utilizando
operadores lógicos, evalúe la autorización: un usuario puede ingresar
únicamente si mide más de 1.50 metros Y además cuenta con el pase
VIP habilitado. El resultado final debe ser un valor lógico (Verdadero o
Falso)
"""



print("Bienvenido al control de acceso.")
estatura = float(input("Ingrese estatura en metros (ejemplo 1.65): "))

while estatura < 0.5 or estatura > 2.5:
    print("ERROR: La estatura debe ser en metros (ejemplo 1.80)")
    estatura = float(input("Ingrese su estatura correctamente: "))

vip = input("Posee VIP? (S/N): ")

if vip == "S" or vip == "s":
    tieneVip = True
else:
    tieneVip = False

puedeIngresar = (estatura > 1.50) and (tieneVip == True)

print(f"Puede ingresar?: {puedeIngresar}")

if puedeIngresar:
    print("¡Acceso concedido!")
else:
    print("Acceso denegado.")