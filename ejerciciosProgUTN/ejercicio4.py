"""   Ejercicio 4
    Desarrolle un algoritmo para analizar la economia semanal en base a un vector (arreglo unidimesional)
   de 7 posiciones, donde cada indice representa un dia de la semana. El usuario debe cargar el gasto en comida de cada dia
    el programa debera calcular el promedio general de gasto diario. posteriormente, realice un segundo recorrido
   sobre el vector para filtrar un mostrar en ptanlla unicamente los dias cuyos gastos especficion haya superado dicho promedio
""" 

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
gastos = [0, 0, 0, 0, 0, 0, 0]

# Carga de gastos
for i in range(7):
    gastos[i] = float(input(f"Ingresá el gasto del {dias[i]}: "))

# Cálculo del promedio
total = 0
for i in range(7):
    total = total + gastos[i]

promedio = total / 7

print(f"\nPromedio general de gasto diario: ${promedio:.2f}")

# Segundo recorrido: días que superaron el promedio
print("\nDías que superaron el promedio:")
for i in range(7):
    if gastos[i] > promedio:
        print(f"{dias[i]}: ${gastos[i]:.2f}")S