'''
Desarrolle una herramienta financiera de conversion de moneda extranjera en paralelo. El sistema debe solicitar al usuario 
una cantidad de dinero base en pesos locales, seguide de la contizacion actual del dolar estadounidense y del euro
 en el mercado del dia. EL algoritmo debe calcular de forma secuencial y mostrar simuntaneamente a cuantos dolares 
y a cuantos euros equivale el monto incial de pesos que se ingreso.
'''

print("------------------------------------------------------------------------")
print("Herramienta de financiera de conversion de moneda extranjera en paralelo")
print("------------------------------------------------------------------------")


pesos= int(input("Ingrese valor en pesos para hacer conversion: "))
dolar= int(input("Ingrese la cotizacion actual del dolar: "))
euro = int(input("Ingrese la cotizacion actual del euro: "))

resultado_dolar = pesos / dolar
resultado_euro  = pesos / euro


print(f"\n{pesos} pesos equivalen a:")
print(f"  USD: {resultado_dolar:.2f} dólares")
print(f"  EUR: {resultado_euro:.2f} euros")



