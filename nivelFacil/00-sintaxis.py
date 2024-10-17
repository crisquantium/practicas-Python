'''EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 '''

#https://www.python.org/

# Comentario de una linea

'''Comentario de 
lineas multiples
'''

mensaje = "Hola Mundo"

""" En Python no existe las variables constantes, porque toda variable en este 
lenguaje cambia. Pero por convencion se puede declarar la variable como
constante, con el nombre de la misma en mayusculas"""
PI = 3.14592

num = 25
temperatura = 19.5
text = "florecitas en el campo"
apagado = False

nomb_lenguaje = "Python"

print("¡Hola," + nomb_lenguaje + "!")

print(type(num))
print(type(temperatura))
print(type(text))
print(type(apagado))
