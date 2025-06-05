#1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#de cada letra en la cadena. Los espacios no deben ser considerados.

def cadena(frase):
    """retorna un diccionario con la frecuencia de cada caracter en la frase.No se deben contar los espacios en blanco.

    Args:
        frase (str): Una cadena de caracteres introducida.

    Returns:
        _type_: Un diccionario con la frecuencia de cada caracter en la frase.
    """
    frec = {}
    for caracter in frase.replace(' ',''):
     frec[caracter] = frec.get(caracter,0) + 1
    return frec
    
frase = "Buenos dias"
conteo= cadena(frase)
print(conteo)

# Resultado: {'B': 1, 'u': 1, 'e': 1, 'n': 1, 'o': 1, 's': 2, 'd': 1, 'i': 1, 'a': 1}
#Me resulto un poco complicado el encontrar la manera de no contar los espacios en blanco.


#2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
def num_cuadrado(x):
    """Convierte una lista de numeros en una lista de sus cuadrados.

    Args:
        x (int): Un numero entero.

    Returns:
        list: Una lista con los cuadrados de los numeros de la lista original.
    """
    return x**2

num=[1,8,53,24]
cuadrados = list(map(num_cuadrado,num))
print(cuadrados)

#Resultado: [1, 64, 2809, 576]


#3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
#devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def palabra_contenida_en_palabras(palabra, palabras):
    """Retorna una lista con las palabras que contienen la palabra dada.

    Args:
        palabra (str): Una palabra.
        palabras (list): Una lista de palabras.

    Returns:
        list: Una lista con las palabras que contienen la palabra dada.
    """
    resultado = []
    for caractereres in palabras:
        if palabra in caractereres:
            resultado.append(caractereres)
    return resultado

lista_carateres = ['agua','leche', 'aceite', 'ázucar']
palabro = 'a'
resultado = palabra_contenida_en_palabras(palabro, lista_carateres)
print(resultado)

#Resultado: ['agua', 'aceite', 'ázucar']
#Tuve problemas en mostrar el resultado ya que en la condicion if puse las variables al reves y solo me mostraba si coincidian las palabras.


#4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def diferencia_entre_listas(lista1, lista2):
    """Retorna una lista con los elementos que estan en la lista1 y no en la lista2.

    Args:
        lista1 (list): Una lista de elementos.
        lista2 (list): Una lista de elementos.

    Returns:
        list: Una lista con los elementos que estan en la lista1 y no en la lista2.
    """
    if len(lista1) == len(lista2):
        return list(map(lambda x,y: x-y, lista1, lista2))
    else:
        return print("Las listas no tienen la misma longitud")
    
lista_1 = [1,2,3,4,5]
lista_2 = [1,3,5,7,9]
resultado = diferencia_entre_listas(lista_1, lista_2)
print(resultado)
#Resultado: [0, -1, -2, -3, -4]

#Aqui tengo la duda de si se refiere a la diferencia entre los valores de las listas o a la diferencia entre los elementos de las listas, y que imprima la diferencia entre los elementos de las listas.
#En este caso lo hice con la diferencia entre los valores de las listas.


#5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
#defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
#que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#una tupla que contenga la media y el estado.

def media(lista, nota_aprobado=5):
    """Retorna la media de los elementos de la lista,y si son mayores que la nota de aprobado devolvera aprobrado y si no suspenso.

    Args:
        lista (list): Una lista de numeros.
        nota_aprobado (int, optional): La nota minima para aprobar. Por defecto es 5.

    Returns:
        float: La media de la lista de numeros y si aprueba o suspende.
    """
    media = sum(lista)/len(lista)
    if media >= nota_aprobado:
        return f"Aprobado con una media de {media}"
    else:
        return f"Suspendido con una media de {media}"
    
lista_notas = [5, 8, 3, 6]
nota_corte = 7
media_notas =media(lista_notas, nota_corte)
print(media_notas)

#Resultado: Suspendido con una media de 5.5


#6. Escribe una función que calcule el factorial de un número de manera recursiva.
def factorial(numero_f):
    """Realiza el factorial de un numero.(Dicho numero se va multiplicando por sus anteriores hasta llegar a 1)

    Args:
        numero_f (int): Un numero entero.

    Returns:
        int: El factorial del numero.
    """
    if numero_f == 0:
        return 1
    else:
        return numero_f * factorial(numero_f -1)
    
numero = 5
factorial_numero = factorial(numero)
print(factorial_numero)

#Resultado: 120
#Tuve problemas ya que me salia un error de recursion, pero lo solucione poniendo el caso base en 0. Es algo que me costo entender, tuve que buscar informacion para entenderlo.


#7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def lista_de_strings(lista_tuplas):
    """Retorna una lista de strings con los elementos de cada tupla.

    Args:
        lista_tuplas (list): Una lista de tuplas.

    Returns:
        list: Una lista de strings con todos los valores de las tuplas.
    """
    return list(map(str,[elemento for tupla in lista_tuplas for elemento in tupla]))

lista_de_tuplas = [(1,2,3,4,5,6)]
tuplas_a_string = lista_de_strings(lista_de_tuplas)
print(tuplas_a_string)

#Resultado: ['1', '2', '3', '4', '5', '6']

#Tuve problemas en entender como se podia hacer para que me devolviera una lista de strings con los elementos de las tuplas. Tuve que buscar informacion
# para entenderlo porque no lograba entender como podia hacerlo. Y aun asi me costo un poco entenderlo.
# Ahora entiendo la ultima parte de la funcion, para cada tupla en lista_tuplas: para cada elemento en tupla: agregalo a la nueva lista.


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
# o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.

try:
    print ('Por favor ingrese un numero')
    numero = int(input())
    print ('Por favor ingrese otro numero')
    numero2 = int(input())
    print(numero/numero2)
except ZeroDivisionError:
    print('No se puede dividir por cero')
except ValueError:
    print('Has introducido un valor incorrecto')

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def lista_de_mascotas(mascotas):
    """Retorna una lista de mascotas excluyendo ciertas mascotas.

    Args:
        mascotas (list): Una lista de mascotas.

    Returns:
        list: Una lista de mascotas excluyendo cieras mascotas.
       """
    return list(filter(lambda x: x != 'mapache' and x != 'tigre' and x!='serpiente piton' and x!= 'cocodrilo' and x!='oso', mascotas))

# Hacemos un filtro para excluir las mascotas que no queremos sobre la lista de mascotas utilizando una funcion lambda.

lista_mascotas= ['perro', 'gato', 'mapache', 'tigre', 'serpiente piton', 'cocodrilo', 'oso']
mascotas_permitidas= lista_de_mascotas(lista_mascotas)
print(mascotas_permitidas)

# Resultado: ['perro', 'gato']

# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción 
# personalizada y maneja el error adecuadamente.

def promedio_lista_numeros(lista):
    """Retorna el promedio de los numeros de la lista.

    Args:
        lista (list): Una lista de numeros.

    Returns:
        float: El promedio de los numeros de la lista.
    """
    try:
        return sum(lista)/len(lista)
    except ZeroDivisionError:
        return print('La lista esta vacia')
    
lista_num=(4,7,5,10,22,-1)
promedio = promedio_lista_numeros(lista_num)
print(promedio)

# Resultado: 7.833333333333333

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
# valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.

try:
    print('Por favor ingrese su edad')
    edad = int(input())
except ValueError:
    print('Por favor ingrese un valor numerico')
else:
    if edad <0 or edad>120:
        print('Por favor ingrese una edad valida')

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def frase_longitud_palabras(frase):
    """Retorna una lista con la longitud de cada palabra de la frase.

    Args:
        frase (str): Una frase.

    Returns:
        list: Una lista con la longitud de cada palabra de la frase.
    """
    return list(map(len, frase.split()))

frase = "Hola caracola"
longitud_frase = frase_longitud_palabras(frase)
print(longitud_frase)
# Resultado: [4, 8]

# 13. Genera una la cual, para un conjunto de caracteres,devuelva una lista de tuplas con cada letra en mayusculas y minusculas. 
# las letras no pueden estar repetidas. Usa la funcion map()

def mayusculas_minusculas(caracteres):
    caracteres_unicos = list(set(caracteres.lower()))
    return list(map(lambda c: (c.upper(), c.lower()), caracteres_unicos))

resultado = mayusculas_minusculas('Esternocleidomastoideo')
print(resultado)

# Resultado: [('N', 'n'), ('S', 's'), ('O', 'o'), ('C', 'c'), ('A', 'a'), ('M', 'm'), ('E', 'e'), ('T', 't'), ('R', 'r'), ('L', 'l'), ('I', 'i'), ('D', 'd')]

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def lista_comienzo_letra(letra, lista):
    """Retorna una lista con los elementos que comienzan con la letra dada.

    Args:
        letra (str): Una letra.
        lista (list): Una lista de palabras.

    Returns:
        list: Una lista con los elementos que comienzan con la letra dada.
    """
    return list(filter(lambda x: x[0] == letra, lista))

lista_palabres = ['coche', 'avion', 'helicoptero', 'casa', 'cama']
letra = 'c'
resultado = lista_comienzo_letra(letra, lista_palabres)
print(resultado)

# Resultado: ['coche', 'casa', 'cama']

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
print (list(map(lambda x: x+3,lista_numeros)))

# Resultado: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
# todas las palabras que sean más largas que n. Usa la función filter()

def lista_mas_larga_que(lista, longitud):
    """Retorna una lista con las palabras que tienen una longitud mayor que la dada.

    Args:
        lista (list): Una lista de palabras.
        longitud (int): Una longitud.

    Returns:
        list: Una lista con las palabras que tienen una longitud mayor que la dada.
    """
    return list(filter(lambda x: len(x) > longitud, lista))
# Aqui hacemos un filto de la longitud de las palabras de la lista de palabras utilizando una funcion lambda.

lista_palabras = ['coche', 'avion', 'helicoptero', 'casa', 'cama']
longitud = 4
resultado = lista_mas_larga_que(lista_palabras, longitud)
print(resultado)

# Resultado: ['coche', 'avion', 'helicoptero']