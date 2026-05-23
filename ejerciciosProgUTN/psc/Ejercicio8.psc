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


Algoritmo Ejercicio8

Definir usuario, clave Como Cadena

Repetir

    Leer usuario
    Leer clave

    Si Longitud(usuario) < 4 Entonces
        Escribir "ERROR: usuario minimo 4 caracteres"
    FinSi

    Si Longitud(clave) <> 6 Entonces
        Escribir "ERROR: clave debe tener 6 caracteres"
    FinSi

Hasta Que (Longitud(usuario) >= 4) Y (Longitud(clave) = 6)

Escribir "Registro exitoso"

FinAlgoritmo