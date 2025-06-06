from functools import reduce

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




# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al 
# número quinientos setenta y dos (572). Usa la función reduce()
def lista_a_numeros(lista):
    """Retorna el numero correspondiente al unir los numeros de una lista dada.

    Args:
        numero (int): Un numero entero.

    Returns:
        list: El numero correspondiente al unir los numeros de una lista dada.

    """
    return reduce(lambda x,y: str(x)+str(y), lista)

# Aqui tuve que convertir los numeros en strings para poder concatenarlos. Me ha costado saber que tenia que convertirlos en strings para poder concatenarlos.

lista_de_numeros = [22,11,0,3,4]
numero = lista_a_numeros(lista_de_numeros)
print(numero)
# Resultado: 2211034


# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
estudiantes = [
    {"nombre":'Juan','edad:':22, 'calificacion':85},
    {"nombre":'Maria','edad:':23, 'calificacion':90},
    {"nombre":'Alejandro','edad:':40, 'calificacion':75},
    {"nombre":'Edu','edad:':30, 'calificacion':100}
]
# Aqui no sabia como hacerlo y tube que buscar en internet, aun asi no entiendo como funciona.

def es_sobresaliente(estudiante):
    return estudiante["calificacion"] >= 90
    
sobresalientes = list(filter(es_sobresaliente, estudiantes))
print("Estudiantes con calificación mayor o igual a 90:")
for estudiante in sobresalientes:
    print(estudiante)

# Resultado:
# Estudiantes con calificación mayor o igual a 90:
# {'nombre': 'Maria', 'edad:': 23, 'calificacion': 90}
# {'nombre': 'Edu', 'edad:': 30, 'calificacion': 100}


# 19. Crea una función lambda que filtre los números impares de una lista dada.
num_impares = [1,13,2,24,7,151,232,0,-1]
impares = list(filter(lambda x: x%2!=0,num_impares))
print(impares)

# Resultado: [1, 13, 7, 151, -1]


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
lista_mezclada = ['hola', 22, 13, 'Antonio', 0, 6]
lista_int= list(filter(lambda x: type(x) == int, lista_mezclada))
print(lista_int)

# Resultado: [22, 13, 0, 6]


# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
def numero_al_cubo():
    """Retorna el numero al cubo.

    Args:
        numero (int): Un numero entero.

    Returns:
        int: El numero al cubo.
    """
    return lambda x: x**3

#Tambien se prodira haber utilizado la funcion pow(numero,3), pero he decidido dejarlo asi para tenerlo yo mas claro en un principio.
# He tenido problemas porque me daba un error que no sabia cual era, y era porque en la funcion ponia num_cubo y luego utilizo la funcion lambda, cuando esto solo devuelve la funcion y no devuelve un valor concreto.

num_cubo = 7
cubo = numero_al_cubo()
print(cubo(num_cubo))

# Resultado: 343


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().
lista_num2 = [1,2,3,4,5,6]
producto = reduce(lambda x, y: x*y, lista_num2)
print(producto)

# Resultado: 720


# 23. Concatena una lista de palabras.Usa la función reduce().
lista_palabras = ['Casa','Coche','Brocoli','Escoba']
concat_palabras = reduce(lambda x,y: x + y, lista_palabras)
print(concat_palabras)

# Resultado: CasaCocheBrocoliEscoba



#24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
lista_diferencia = [52, 12, 8, -13, 1]
diferencia = reduce(lambda x, y: x - y, lista_diferencia)
print(diferencia)

# Resultado: 44



# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
def numero_caracteres(num_caracteres):
    """Retorna el numero de caracteres de una cadena.

    Args:
        num_caracteres (str): Una cadena de caracteres.

    Returns:
        int: El numero de caracteres de la cadena.
    """
    return len(num_caracteres)
    

comida = 'lentejas con chorizo'
num_caracteres = numero_caracteres(comida)
print(num_caracteres)

# Resultado: 20


# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.
n1 = 5
n2 = 10
resto_division = lambda x,y: x%y
print(resto_division(n1,n2))
#Utilizamos % porque eso nos da el resto de la division.

# Resultado: 5



# 27. Crea una función que calcule el promedio de una lista de números.
def promedio_numeros(lista_numeros):
    """Retorna el promedio de los numeros de la lista.

    Args:
        lista (list): Una lista de numeros.

    Returns:
        float: El promedio de los numeros de la lista.
    """
    return reduce(lambda x,y: x+y, lista_numeros)/len(lista_numeros)

#Utilizamos reduce para iterar sobre la lista y sumar todos los elementos, y luego dividimos por la longitud de la lista para obtener el promedio.
#Aqui no he tenido en cuenta si la lista esta vacia porque el ejercicio no me lo especificaba, pero se podria hacer con un try except.

lista_numeros = [1,2,3,4,5,6]
promedio = promedio_numeros(lista_numeros)
print(promedio)

# Resultado: 3.5



# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
def primer_valor_repetido(lista):
    """Encuentra el primer valor repetido en una lista.

    Args:
        lista (list): Lista de elementos.

    Returns:
        any: El primer valor repetido o None si no hay repetidos.
    """
    vistos = set()  # Usamos un conjunto para almacenar los valores vistos

    for elemento in lista:
        if elemento in vistos:  # Si ya lo vimos antes, es el primer repetido
            return elemento
        vistos.add(elemento)  # Agregamos el elemento al conjunto

    return None  # Si no hay repetidos, devolvemos None

#Tuve que buscar ayuda porque pensaba que habiar que utilizar alguna funcion de lambda, pero no daba con lo que era. 
#Al final se lo que hace el codigo, pero no hubiera sido capaz de hacerlo yo solo. Creamos un conjunto para almacenar los valores vistos, 
# y si el elemento ya esta en el conjunto, lo devolvemos, si no lo añadimos al conjunto.

elementos = [1,22, 23, 17, 1, 8, 17]
repetido = primer_valor_repetido(elementos)
print(repetido)

# Resultado: 1



# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
# carácter '#', excepto los últimos cuatro.
def enmascarar_valor(valor):
    """Enmascara un valor con almohadilla.

    Args:
        valor (str, int, float): Un valor.

    Returns:
        str: El valor enmascarado.
    """
    return '#' * len(str(valor))

#Aqui transformamos el valor en un string y luego multiplicamos el numero de almohadillas por la longitud del string.

valor = 'Phthon'
enmascarado = enmascarar_valor(valor)
print(enmascarado)
# Resultado: ######


# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
# pero en diferente orden.
def anagrama(palabra1, palabra2):
    """Te dice si dos palabras son anagramas.

    Args:
        palabra1 (str): Una palabra.
        palabra2 (str): Otra palabra.

    Returns:
        bool: True si son anagramas, False si no lo son.
    """
    anag =sorted(palabra1) == sorted(palabra2)
    if anag==True:
        return 'Son anagramas'
    else:
        return 'No son anagramas'
    
#Utilizamos la funcion sorted para ordenar las letras de cada palabra y luego comprobamos si son iguales entre si.
palabra = 'cosa'
palabra2 = 'saco'
anagramas = anagrama(palabra, palabra2)
print(anagramas)
# Resultado: Son anagramas



# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.
def buscar_en_lista_nombres():
    """Busca un nombre en una lista de nombres.

    Returns:
        str: Mensaje indicando si el nombre se encuentra en la lista o no.
    """
    lista_nombres = []

    while True:
        print('Introduce un nombre o pulsa Enter para terminar:')
        nombre = input()
        if nombre == '':
            break
        lista_nombres.append(nombre)

    buscar_nombre = input('Introduce el nombre a buscar: ')

    if buscar_nombre in lista_nombres:
          return 'El nombre se encuentra dentro de la lista'
    else:
         return 'El nombre no se encuentra dentro de la lista'
    
lista_nombres = buscar_en_lista_nombres()
print(lista_nombres)



# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.
def buscar_nombre_completo_en_lista():
    """Busca un nombre completo en una lista de nombres.

    Returns:
        str: Mensaje indicando si el nombre se encuentra en la lista o no, de ser, tambien devuelve el trabajo que tiene.
    """
    lista_nombres = [
        {'nombre': 'Juan', 'apellido':'Montoro','trabajo': 'programador'},
        {'nombre': 'Maria', 'apellido':'Segovia','trabajo': 'medico'},
        {'nombre': 'Alejandro', 'apellido':'Carmona','trabajo': 'data scientist'},
        {'nombre': 'Edu', 'apellido':'Ilustrisima','trabajo': 'profesor'}
    ]
    buscar_nombre = input('Introduce el nombre a buscar: ')
    
    for nombre in lista_nombres:
        if nombre['nombre'] == buscar_nombre:
            return f'El nombre se encuentra en la lista y su trabajo es {nombre["trabajo"]}'
    return f'{buscar_nombre} no trabaja con nosotros'

#He tenido problemas con el retorno de la parte del for, porque lo estaba poniendo con un else despues del if, y no me imprimia el mensaje correcto.
buscar_nombre_completo_en_lista()
# Resultado: 'Pedro no trabaja con nosotros'



# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
lista_num3 = [3,21,4,13,8,25]
lista_num4 = [1,2,3,4,5,6]
suma_listas = list(map(lambda x, y: x+y, lista_num3, lista_num4))
print(suma_listas)
# Resultado: [4, 23, 7, 17, 13, 31]



# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
# manipular la estructura del árbol.

# Código a seguir:

# - Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
# - Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
# * Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
# * Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
# * Implementar el método quitar_rama para eliminar una rama en una posición específica.
# * Implementar el método
# info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
# mismas.

# Caso de uso:
# * Crear un árbol.
# * Hacer crecer el tronco del árbol una unidad.
# * Añadir una nueva rama al árbol.
# * Hacer crecer todas las ramas del árbol una unidad.
# * Añadir dos nuevas ramas al árbol.
# * Retirar la rama situada en la posición 2.
# * Obtener información sobre el árbol.
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_ramas(self,posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion) #Elimina la rama en la posicion dada
        else:
            print('No se puede quitar la rama: la posicion {posicion} no es valida')

    def info_arbol(self):
        return (f'Longitud del tronco: {self.tronco}\n'
                f'Numero de ramas: {len(self.ramas)}\n'
                f'Longitudes de las ramas: {self.ramas}') 
    
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_ramas(self,posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion) #Elimina la rama en la posicion dada
        else:
            print('No se puede quitar la rama: la posicion {posicion} no es valida')

    def info_arbol(self):
        return (f'Longitud del tronco: {self.tronco}\n'
                f'Numero de ramas: {len(self.ramas)}\n'
                f'Longitudes de las ramas: {self.ramas}') 

# Caso de uso:

barbol = Arbol()
barbol.crecer_tronco() # El tronco crece a 2
barbol.tronco
# Resultado: 4
barbol.nueva_rama() # Añade una nueva rama de longitud 1
barbol.ramas
# Resultado: [1]
barbol.crecer_ramas() # Hace crecer todas las ramas en 1
barbol.ramas
# Resultado: [2]
barbol.nueva_rama() # Añade una nueva rama de longitud 1
barbol.nueva_rama() # Añade otra nueva rama de longitud 1
barbol.ramas
# Resultado: [2, 1, 1]
barbol.quitar_ramas(2) # Quita la rama en la posición 2
barbol.ramas
# Resultado: [2, 1]
print(barbol.info_arbol()) # Muestra la información del árbol
# Resultado: 
# Longitud del tronco: 4
# Numero de ramas: 2
# Longitudes de las ramas: [2, 1]