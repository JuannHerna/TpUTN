"""
Desarrolle un algoritmo gráfico por consola utilizando estructuras
repetitivas anidadas. El programa debe pedir al usuario que introduzca
un número entero que represente la longitud del lado de un cuadrado.
Utilizando bucles para filas y columnas, dibuje en pantalla un cuadrado
relleno con caracteres de asteriscos ( * ), asegurando el correcto salto
de línea al finalizar cada fila. 
"""

lado = int(input("Ingrese lado del cuadrado (Numero entero): "))

while lado <= 0:
    print("ERROR: El lado debe ser mayor a 0")
    lado = int(input("Intente nuevamente: "))

print("Dibujando cuadrado")
print()

for fila in range(lado):
    for columna in range(lado):
        print(" * ", end="")
    print()