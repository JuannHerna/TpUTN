"""
Ejercicio 8
Desarrolle un módulo de seguridad para el registro de nuevos usuarios
en una plataforma. El sistema debe solicitar obligatoriamente un
nombre de usuario y una contraseña. Empleando un bucle de control
que evalúa al final del ciclo, obligando al usuario a repetir la carga de
datos de manera indefinida hasta que se cumplan estrictamente las
dos condiciones de longitud:
- El nombre de usuario debe poseer un mínimo de 4 caracteres
- La clave debe tener exactamente 6 caracteres.
- Despliegue mensajes de error específicos si alguna de las dos
condiciones falla.
"""


while True:
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")

    if len(usuario) < 4:
        print("ERROR: usuario minimo 4 caracteres")

    if len(clave) != 6:
        print("ERROR: clave debe tener 6 caracteres")

    if len(usuario) >= 4 and len(clave) == 6:
        break

print("Registro exitoso")