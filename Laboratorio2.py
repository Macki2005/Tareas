print ("Ejercicio 1")
print ("La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.")
print()
def max_in_list(numeros):
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    
    return maximo

print(max_in_list([20, 51, 32, 91, 22]))  
print(max_in_list([1030, 2311, 552, 783, 9319]))  
print(max_in_list([-15120, -2120, -5312, -121]))  


print()

print ("Ejercicio 2")
print ("Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.")
print()
def mas_larga(palabras):
    palabra_mas_larga = palabras[0]
    
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    return palabra_mas_larga

print(mas_larga(["llego", "solia", "salio", "sin"]))  
print(mas_larga(["la", "revela", "en", "el"]))  
print(mas_larga(["alcohol", "buscando", "una"]))  
  
print()

print("Ejercicio 3")
print("Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres..")
print()
def filtrar_palabras(palabras, n):

    palabras_filtradas = []

    for palabra in palabras:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)
    
    return palabras_filtradas


print(filtrar_palabras(["salida", "de", "esa", "relacion", "de mentira"], 5))  
print(filtrar_palabras(["mami", "ya vi", "como", "me mira"], 4))  
print(filtrar_palabras(["te lo", "repito", "por si", "se te"], 3))  


print()

print ("Ejercicio 4")
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
 
 
print()

print("Ejercicio 5")
print("Construir un pequeño programa que convierta números binarios en enteros")
print()
def binario_a_entero(binario):
    return int(binario, 2)

numero_binario = input("Por favor, ingrese un número binario: ")

numero_entero = binario_a_entero(numero_binario)

print(f"El número binario {numero_binario} convertido a entero es: {numero_entero}")


print()

print("Ejercico 6")
print("Escribir un pequeño programa donde: Se ingresa el año en curso. Se ingresa el nombre y el año de nacimiento de tres personas. Se calcula cuántos años cumplirán durante el año en curso. Se imprime en pantalla.")
print()
try:
    año_actual = int(input("Ingrese el ano en curso: "))
except ValueError:
    print("Por favor, ingrese un número válido para el ano.")
    exit()

personas = []

for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    
    try:
        año_nacimiento = int(input(f"Ingrese el ano de nacimiento de {nombre}: "))
    except ValueError:
        print("Por favor, ingrese un número válido para el ano de nacimiento.")
        exit()
    
    edad = año_actual - año_nacimiento
    
    personas.append((nombre, edad))

print("\nEdades durante el ano en curso:")
for nombre, edad in personas:
    print(f"{nombre} cumplirá {edad} anos en el año {año_actual}.")



print()

print("Ejercicio 7")
print("Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese las edades..")
print()
edades = (12, 21, 36, 11, 32, 16, 12, 3, 16, 68)

conteo_mayores_de_20 = 0

for edad in edades:
    if edad > 20:
        conteo_mayores_de_20 += 1

print(f"Cantidad de personas con edades superiores a 20: {conteo_mayores_de_20}")


print()

print("Ejercicio 8")
print("Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a También se puede hacer elegir al usuario la letra a buscar.")
print()

nombres = ["Luffy", "Zoro", "Amapola", "Nami", "Ariana", "Franky", "Azuquita", "Robin", "Jinbe"]

letra_a_buscar = 'a'

conteo_nombres = 0

for nombre in nombres:
    if nombre.lower().startswith(letra_a_buscar):
        conteo_nombres += 1

print(f"Cantidad de nombres que comienzan con la letra '{letra_a_buscar}': {conteo_nombres}")


print()

print("Ejercicio 9")
print("Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras a tiene, cuantas letras e tiene y así hasta completar todas las vocales. Se puede hacer que el usuario sea quien elija la palabra.")
print()

def contar_vocales(palabra):

    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    palabra = palabra.lower()

    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1

    return conteo_vocales

palabra_usuario = input("Ingrese una palabra para contar las vocales: ")

resultado = contar_vocales(palabra_usuario)

print("\nConteo de vocales:")
for vocal, cantidad in resultado.items():
    print(f"Cantidad de '{vocal}': {cantidad}")

print()

print("Ejercicio 10")
print("Escriba una función es_bisiesto() que determine si un año determinado es un añobisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400")
print()
def es_bisiesto(ano):

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False


ano_usuario = int(input("Ingrese un año para verificar si es bisiesto: "))


if es_bisiesto(ano_usuario):
    print(f"El año {ano_usuario} es bisiesto.")
else:
    print(f"El año {ano_usuario} no es bisiesto.")





