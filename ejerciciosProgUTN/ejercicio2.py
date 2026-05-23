""" Ejercicio 2
Desarrolle un simulador de ticket de compra básico. El programa debe
solicitar al usuario el precio unitario de un producto (número real) y la
cantidad de unidades compradas (número entero). A partir de estos
datos, debe calcular el subtotal. Luego, aplique de forma automática el
impuesto al valor agregado (IVA) del 21% para obtener el total neto a
abonar. Muestra el desglose final detallado en pantalla utilizando
delimitadores de texto adecuados.
"""

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad comprada: "))

subtotal = precio * cantidad
iva = subtotal * 0.21
total = subtotal + iva

print(f"Subtotal: {subtotal:.2f}")
print(f"IVA (21%): {iva:.2f}")
print(f"Total: {total:.2f}")