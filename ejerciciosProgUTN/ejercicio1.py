''' Ejericio 1
Desarrolle un programa para registrar las ventas diarias de un comercio. El Usuario debera ingresar el monto de cada venta de forma sucesiva.
 el programa debe continuar solicitando montos hasta que se ingrese una venta igual a 0, lo cual indicara el cierre de la caja
 al finalizar el sistema debera mostrar en pantalla la cantidad total de ventas precesadas y el dinero total acumulado. ResticcionL evite
 que se sumen montos negativos mostrandi un mje de advertencia.
'''



total = 0
cantidad = 0

venta = float(input("Ingrese el monto de la venta (0 para cerrar caja): "))

while venta != 0:

    if venta < 0:
        print("ERROR: el monto no debe ser negativo")
    else:
        total = total + venta
        cantidad = cantidad + 1

    venta = float(input("Ingrese la siguiente venta o 0 para cerrar: "))

print(f"Total de ventas: {cantidad}")
print(f"Total dinero: {total:.2f}")





