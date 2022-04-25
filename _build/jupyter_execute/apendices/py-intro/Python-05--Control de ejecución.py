#!/usr/bin/env python
# coding: utf-8

# # Control de ejecución

# * Los programas usualmente se ejecutan corriendo cada instrucción en el orden en que aparecen
# * Pero en ocasiones, necesitamos ejecutar las  instrucciones de otra manera.
# * Para ello, usamos instrucciones de control de ejecución:
# - ```if, elif, else``` ejecuta algunas instrucciones una vez, pero solo si cierta condición es verdadera
# - ```while``` ejecuta algunas instrucciones varias veces, solo mientras que cierta condición sea verdadera
# - ```for``` ejecuta algunas instrucciones varias veces, iterando sobre un iterable
# - ```continue``` brinca a la siguiente iteraciónde un bucle  `while` o `for`
# - ```break``` detiene la ejecución de un bucle `while` o `for`

# # Ejecución condicional con `if`
# 
# * La palabra clave ```if``` evalua una expresión para obtener un valor `True` o `False`.
# * Esto permite que un programa proceda en diferentes direcciones de acuerdo con el resultado del test.
# * La expresión evaluada debe ser seguida de dos puntos ```:```, luego las instrucciones que se evaluan si el test es verdadero deben escribirse en líneas separadas e indentadas respecto a la línea que contiene el ```if```.
# * El tamaño de la indentación no es importante, pero debe ser el mismo en cada línea.
# * Por tanto, la sintaxis se ve así:
# ```
# if test-expression:
#    statements-to-execute-when-test-expression-is-True
#    statements-to-execute-when-test-expression-is-True
# ```   

# Por ejemplo, para determinar si un número ```m``` es par o impar:

# In[ ]:


m = 7
if m % 2 == 0:
    print('m es par')
else:
    print('m es impar')


# El test no necesariamente tiene que ser un boolean. El número `0`, el valor `None`, y un texto vacío `''`, lista vacía `[]`, tupla vacía `()` o conjunto vacío `{}`, todos son interpretados como  `False`.

# In[ ]:


if m % 5:
    print('m no es divisible entre 5')
else:
    print('m es divisible entre 5')


# In[ ]:


horas = 10

if horas < 12:
    ampm = 'a.m.'
else:
    ampm = 'p.m.'
    
ampm


# ## Examinando condiciones
# Algunas veces necesitamos asignar un valor dependiendo de una condición, como así
# ```
# if testExpression:
#     x = ifTrueThis
# else:
#     x = ifFalseThis
# ```
# Esto es equivalente a :
# ```
# x = ifTrueThis if testExpression else ifFalseThis
# ```
# Por ejemplo, el código anterior, en el que queremos definir una variable que depende de una condición, podemos escribirlo más compacto así:

# In[ ]:


ampm1 = 'a.m.' if horas < 12 else 'p.m.'
ampm1


# Otro ejemplo

# In[ ]:


n = 18
z = "n is " +  ("impar" if n % 2 else "par")

z


# # Iterando `while` true i
# 
# * Un bucle es una pieza de código que automáticamente se repite.
# * Una ejecución completa de todas las instrucciones dentro de un bucle se llama una “iteración”.
# * El tamaño del buche se controla con un test condicional que se ejecuta dentro del bucle.
# * Mientras que la expresión evaluada sea  ```True``` el bucle continuará –-- hasta que la expresión sea ```False```, punto en el cual el bucle termina.
# * En programas de Python, la palabra clave ```while``` crea un bucle. Es seguida por la expresion a evaluar y dos puntos ```:```.
# * Las instrucciones que se deben evaluar cuando el test pasa (sea ```True```) deben seguir abajo en líneas separadas, y cada línea debe estar indentada con el mismo espacio respecto a la línea que tiene el ```while```.
# * Este bloque de instrucciones debe incluir una instrucción que en algún momento cambie el resultado del test a ```False``` --- de lo contrario el bucle será infinito.
# * Por tanto, la sintaxis se ve así:
# 
# ```
# while test-expression :
#     statements-to-execute-when-test-expression-is-True
#     statements-to-execute-when-test-expression-is-True
# ```    

# Por ejemplo, para obtener la serie de Fibonacci hasta 100

# In[ ]:


a, b = 0, 1

while b < 100:
    print(b, end=', ')
    a, b = b, a + b


# Un enfoque distinto, pero que incluye el primer elemento que se pasa de 100

# In[ ]:


fib = [1, 1]

while fib[-1]<100:
    fib.append(fib[-2] + fib[-1])
else:
    fib.pop()
    
    
fib


# ## La función ```range```
# Algunas veces necesitamos iterar sobre los enteros. Podemos generarlos con la función ```range```.

# In[ ]:


range(6)


# Para ahorrar memoria, ```range``` retorna sus elementos uno a la vez, solo cuando se necesita, para evitar usar demasiada memoria. Por ejemplo

# In[ ]:


import sys


# In[ ]:


N = 1_000

print(f'{sys.getsizeof(range(N))=}')
print(f'{sys.getsizeof(list(range(N)))=}')

print(f'{sys.getsizeof(range(1000*N))=}')
print(f'{sys.getsizeof(list(range(1000*N)))=}')


# En los ejemplos que siguen convertimos objetos ```range``` en listas únicamente para poder imprimir sus elementos.

# `range(n)` retorna enteros de ```0``` a ```n-1```

# In[ ]:


list(range(6))


# `range(m, n)` retorna enteros de ```m``` a ```n-1```

# In[ ]:


list(range(2,8))


# `range(m, n, s)` retorna enteros de ```m``` a ```n-1```, de ```s``` en ```s```

# In[ ]:


list(range(2,9,3))


# También podemos crear un ```range``` con el orden invertido:

# In[ ]:


list(range(4, 0,-1))


# # Iterando sobre los elementos de un iterable: `for`
# 
# En Python la palabra clave ```for``` itera sobre todos los elementos de cualquier iterable que aparezca luego de la palabra clave ```in```.
# 
# La sintaxis se ve así:
# 
# ```
# for item in iterable :
#     statements-to-execute-on-each-iteration
#     statements-to-execute-on-each-iteration
# ```    
# 
# Ejemplos de iterables:
# * rangos
# * listas, tuplas, conjutos, diccionarios
# * textos
# * archivos de texto
# * arreglos de números

# ### Iterando sobre textos

# In[ ]:


for letra in 'abcd':
    print(letra.upper())


# ### Iterando sobre enteros

# In[ ]:


for k in range(1, 6):
    print(k**2)


# ### Iterando líneas de un archivo de texto

# In[ ]:


with open("../data/HimnoNacional.txt", 'r', encoding='utf-8') as archivo_himno:
    for linea in archivo_himno:
        print(linea, sep='')


# In[ ]:


temp = open("../data/HimnoNacional.txt", 'r', encoding='utf-8')


# In[ ]:


dir(temp)


# In[3]:


temp = open("../data/HimnoNacional.txt", 'r', encoding='utf-8')


# In[4]:


dir(temp)


# ### Iterando los elemetos de un diccionario

# In[ ]:


king = {'name': 'John Snow',
        'age': 24,
        'home': 'Castle Black',
        'lover': 'Ygritte',
        'knows': None}

for llave, valor in king.items():
    print(f'king["{llave}"] = {valor}')


# ## enumerate
# 
# En ocasiones, además de iterar los elemento de una colección, necesitamos llevar cuenta del número de iteración. Una forma de hacerlo es ésta:

# In[ ]:


eltexto = 'abcde'


# esta es la forma "fea" que tendríamos que usar en otros lenguajes de programación
for i in range(len(eltexto)):
    letra = eltexto[i]
    print(f'iteración {i} da por resultado  {letra}')
    


# Como esta situación es tan común, Python tiene una forma elegante de hacerlo, usando la función ```enumerate``` 

# In[ ]:


eltexto = 'abcde'

# esta es la forma elegante usando Python
for i, letra in enumerate(eltexto):
    print(f'iteración {i} da por resultado  {letra}')
    


# ## zip
# 
# De manera similar, en ocasiones debemos iterar sobre dos o más colecciones en paralelo. Una forma es

# In[ ]:


quantities = [3, 2, 4, 6]
fruits = ('apple','banana','coconut')

# este código dará un error, porque las colecciones no son del mismo tamaño!
for i in range(len(quantities)):
    n = quantities[i]
    fruit = fruits[i]
    print(f'{n} {fruit}s')


# Para iterar dos iterables en paralelo, es más elegante y fácil que usemos `zip`

# In[ ]:


quantities = [3, 2, 4, 8]
fruits = ('apple','banana','coconut')

for n, fruit in zip(quantities,fruits):
    print(f'{n} {fruit}s')


# ## *List comprehensions*
# 
# * *List comprehension* es una manera elegante de definir una lista basado en otra colección (un iterable).
# * Generalmente son más compactas y rápidas que los bucles tradicionales.
# * No obstante, debemos evitar *list comprenhension* demasiado largas para que el código sea claro.
# 
# 

# ### Caso más sencillo

# A veces necesitamos hacer una lista de elementos a partir de otro iterable, como con este código
# 
# ```
# lst = list()
# for item in iterable:
#     lst.append(expression)
# ```
# 
# Esto puede hacer más sucintamente con
# 
# ```
# lst = [expression for item in iterable]
# ```

# Por ejemplo, para obtener una lista de los cuadrados de los números del 1 al 14:

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'miscuadrados = []\n\nfor k in range(1,15):\n    miscuadrados.append(k**2)\n    \nmiscuadrados')


# Este código es más sencillo de entender, y más compacto. Además, usualmente es más rápido.

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'miscuadrados2 = [k**2 for k in range(1,15)]\nmiscuadrados2')


# In[ ]:


[k**2 for k in range(1,15) if k%2==1]


# Otro ejemplo: para contar las letras en una lista de palabras

# In[ ]:


frutas = ['apple','banana','carrot','grape','kiwi']

[len(palabra) for palabra in frutas]


# ### Caso con un condicional

# A veces necesitamos además que se satisfaga alguna condición en la iteración, como con este código
# ```
# lst = list()
# for item in iterable:
#     if conditional:
#         lst.append(expression)
# ```
# 
# Esto puede hacer más sucintamente con
# 
# ```
# lst = [expression for item in iterable if conditional]
# ```

# Por ejemplo, para generar los cuadrados de los números pares menores que 12

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'lista1 = list()\n\nfor k in range(1,12):\n    if k % 2 == 0:\n        lista1.append(k**2)\n\nlista1')


# Esta es una versión más compacta:

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'lista2 = [k**2 for k in range(1, 12) if not k%2]\nlista2')

