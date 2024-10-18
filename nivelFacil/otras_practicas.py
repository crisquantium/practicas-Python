"""Crea un programa que pida dos numeros por teclado. El programa tendra una funcion llamada "DevuelveMax" encargada de devolver el numero mas alto de los dos introducidos"""

'''def DevuelveMax(n1, n2):
  if n1 > n2:
    return "El primer número introducido es el mayor"
  elif n2 > n1:
    return "El Segundo número introducido es el mayor"
  else:
    return "Los números son iguales"
  
print("Introduzca dos números enteros")
num1= int(input())
print("Introduzca el segundo número")
num2= int(input())

print(DevuelveMax(num1, num2))
'''

"""Crea un programa que pida por teclado "Nombre","Dirección","Telefono". Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: "Los datos personales son: nombre apellido telefono"(Se mostraran los datos introducidos por teclado)"""
'''
print("Introduzca sus datos personales: Nombre, Apellido, Telefono:")


nomb = input("Introduzca su nombre: ")
direc = input("Introduzca su dirección: ")
telef = input("Introduzca su telefono: ")


datos = [nomb, direc, telef]

print("Los datos personales son: " + datos[0] + " " + datos[1] + " " + datos[2])


datos = [input("Introduzca su nombre: "),input("Introduzca su dirección: "),input("Introduzca su telefono: ")]

print("Los datos personales son: " + datos[0] + " " + datos[1] + " " + datos[2])
'''
"""Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmetica de los números introducidos"""

def promedio(n1, n2, n3):
  prom = (n1 + n2 + n3) / 3
  return prom

print("Inserte tres numeros enteros positivos")
num1= int(input("Introduce el primer número "))
num2= int(input("Introduce el segundo número "))
num3= int(input("Introduce el tercero número "))



print("El promedio de los números es : ", promedio(num1, num2, num3))
