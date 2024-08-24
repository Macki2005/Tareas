print ("Ejercicio 1")
print ("Escribir un programa que solicite al usuario su nombre y edad, y luego imprima un mensaje de bienvenida que incluya ambos.")
nombre = input("Por favor, introduce tu nombre: ")

edad = input("Por favor, introduce tu edad: ")

print(f"Ki ubo {nombre}! Apoco con {edad} anios. Ya con una pata en el panteon")
print ("Ejercicio 2")
print ("Crear un programa que pida al usuario dos numeros enteros y muestre su suma, resta, multiplicacion y division.")
print()
num1 = int(input("Introduce el primer número entero: "))

num2 = int(input("Introduce el segundo número entero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}")
print(f"La division de {num1} y {num2} es: {division}")

print ("Ejercicio 3")
print ("Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.")
print()
def contar_mayusculas(cadena):
    contador_mayusculas = 0
    
    for caracter in cadena:
        if caracter.isupper():
            contador_mayusculas += 1
    
    return contador_mayusculas

cadena_usuario = input("Por favor, ingrese una cadena: ")

cantidad_mayusculas = contar_mayusculas(cadena_usuario)

print(f"La cadena ingresada tiene {cantidad_mayusculas} letra(s) mayúscula(s).")
print("Ejercicio 4")
print("Hacer un programa que pida al usuario su fecha de nacimiento y luego imprima cuantos dias han pasado desde entonces.")
print()
from datetime import datetime

fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
hoy = datetime.now()
dias_transcurridos = (hoy - fecha_nacimiento).days

print(f"Han pasado {dias_transcurridos} dias desde tu fecha de nacimiento.")

print("Ejercicio 5")
print("Crear un programa que reciba un numero flotante y lo muestre redondeado a dos decimales.")
print()

numero = float(input("Introduce un numero flotante: "))
redondeado = round(numero, 2)
print(f"Numero redondeado a dos decimales: {redondeado}")

print("Ejercico 6")
print("Escribir un programa que pida al usuario un archivo de texto y luego muestre el contenido del archivo en la pantalla..")
print()
nombre_archivo = input("Introduce el nombre del archivo de texto: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no se encontro.")


print("Ejercicio 7")
print("Desarrollar un programa que lea una lista de numeros separados por comas y luego imprima la suma de esos numeros.")
print()
numeros = input("Introduce una lista de numeros separados por comas: ")
lista_numeros = [float(num) for num in numeros.split(',')]
suma = sum(lista_numeros)
print(f"La suma de los numeros es: {suma}")


print("Ejercicio 8")
print("Hacer un script que pida al usuario dos cadenas de texto y las imprima concatenadas..")
print()
cadena1 = input("Introduce la primera cadena de texto: ")
cadena2 = input("Introduce la segunda cadena de texto: ")
concatenado = cadena1 + cadena2
print(f"Las cadenas concatenadas son: {concatenado}")


print("Ejercicio 9")
print("Crear un programa que pida al usuario su nombre y luego lo imprima invertido.")
print()
nombre = input("Introduce tu nombre: ")
nombre_invertido = nombre[::-1]
print(f"Tu nombre invertido es: {nombre_invertido}")


print("Ejercicio 10")
print("Escribir un programa que reciba una serie de calificaciones y luego imprima el promedio")
print()
calificaciones = input("Introduce una serie de calificaciones separadas por comas: ")
lista_calificaciones = [float(cal) for cal in calificaciones.split(',')]
promedio = sum(lista_calificaciones) / len(lista_calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")

print("Ejercicio 11")
print(" Desarrollar un programa que solicite al usuario su peso y altura, y calcule su indice de masa corporal (IMC)")
print()
peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

print("Ejercicio 12")
print("Hacer un programa que genere un numero aleatorio entre 1 y 100, y pida al usuario adivinarlo, dando pistas si el numero es mayor o menor.")
print()
import random

numero_aleatorio = random.randint(1, 100)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número entre 1 y 100: "))
    
    if intento < numero_aleatorio:
        print("El número es mayor.")
    elif intento > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Correcto! Has adivinado el número.")
        adivinado = True

print("Ejercicio 13")
print("Hacer un programa que pida al usuario una lista de nombres y los ordene alfabeticamente.")
print()
nombres = input("Introduce una lista de nombres separados por comas: ")
lista_nombres = [nombre.strip() for nombre in nombres.split(',')]
lista_nombres.sort()
print("Nombres ordenados alfabéticamente:")
for nombre in lista_nombres:
    print(nombre)

print("Ejercicio 14")
print("Escribir un programa que genere y muestre la tabla de multiplicar de un numero introducido por el usuario")
print()
numero = int(input("Introduce un número para generar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


print("Ejercicio 15")
print("Desarrollar un script que pida al usuario una oracion y cuente cuantas palabras tiene.")
print()
oracion = input("Introduce una oración: ")
palabras = oracion.split()
numero_palabras = len(palabras)
print(f"La oración tiene {numero_palabras} palabras.")
