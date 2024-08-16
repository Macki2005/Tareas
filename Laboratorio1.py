print ("Ejercicio 1")
print ("Definir una funcion max() que tome como argumento dos numeros y devuelva el mayorde ellos")
print()
def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(1, 3))  
print(max(15, 36))  
print(max(100, 100))  

print()

print ("Ejercicio 2")
print ("Definir una funcion max de tres() que tome tres numeros como argumentos y devuelva elmayor de ellos")
print()
def maximo_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(maximo_de_tres(10020, 30040, 1))  
print(maximo_de_tres(100000, 1232103, 2))  
print(maximo_de_tres(312938, 3, 402340))  

print()

print("Ejercicio 3")
print("Definir una funcion que calcule la longitud de una lista o una cadena dada.")
print()
def calcular_longitud(elemento):
    longitud = 0
    
    for _ in elemento:
        longitud += 1
    
    return longitud

cadena = "Hola, mundo!"
print("Longitud de la cadena:", calcular_longitud(cadena))

lista = [1, 2, 3, 4, 5]
print("Longitud de la lista:", calcular_longitud(lista))

print()

print ("Ejercicio 4")
print ("Escribir una funcion que tome un caracter y devuelva True si es una vocal, de lo contrario devuelve False")
print()
def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales
print(es_vocal('o')) 
print(es_vocal('E'))  
print(es_vocal('I'))  
print(es_vocal('Z')) 
print(es_vocal('Y'))  
 
print()

print("Ejercicio 5")
print("Escribir una funcion sum() y una funcion multip() que sumen y multipliquen respectivamente todos los numeros de una lista. Porejemplo: sum([1,2,3,4]) deberia devolver10 y multip([1,2,3,4]) deberia devolver24..")
print()
def suma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total
def multiplicacion(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado
numeros = [5, 15, 10, 20]
print("La suma de la lista es:", suma(numeros))         
print("La multiplicacion de la lista es:", multiplicacion(numeros))  

print()

print("Ejercico 6")
print("Definir una funcion inversa() que calculela inversion de una cadena. Por ejemplo, la cadena estoy probando deberia devolver la cadena odnaborp yotse")
print()

def inversa(cadena):
    return cadena[::-1]

print("Luffy sera el rey de los piratas")
cadena = "Luffy sera el rey de los piratas"
print("La cadena invertida es:", inversa(cadena)) 

print()

print("Ejercicio 7")
print("Definir una funcion es palindromo() que reconoce palindromos (es decir, palabras quetienen el mismo aspecto escritas invertidas).Ejemplo: es palindromo (radar) tendria que devolver True.")
print()
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()

    return palabra == palabra[::-1]

print(es_palindromo("radar"))  
print(es_palindromo("madam"))  
print(es_palindromo("Preso")) 
print(es_palindromo("De la carcel de tus besos")) 
print(es_palindromo("Anita lava la tina"))  

print()

print("Ejercicio 8")
print("Definir una funcion superposicion() quetome dos listas y devuelva True si tienen al menos un miembro en comun o devuelva False de lo contrario. Escribir la funcion usando el bucle for anidado.")
print()

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False
lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

print(superposicion(lista1, lista2))
print(superposicion(lista1, lista3))

print()

print("Ejercicio 9")
print("Definir una funcion generar n caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar n caracteres(5,x) deberia devolver xxxxx")
print()

def generar_n_caracteres(n, caracter):
    return caracter * n
print(generar_n_caracteres(5, "x")) 
print(generar_n_caracteres(3, "*"))  
print(generar_n_caracteres(7, "-"))

print()

print("Ejercicio 10")
print("Definir un procedimiento histograma() que  tome una lista de numeros enteros e imprima un histograma en la pantalla. Ejemplo: histograma([4, 9, 7]) deberia imprimir lo siguiente:**** ********* *******")
print()
def histograma(lista):

    for numero in lista:
        print('*' * numero)
histograma([2, 3, 5])




