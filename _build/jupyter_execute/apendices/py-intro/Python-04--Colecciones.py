#!/usr/bin/env python
# coding: utf-8

# # Colecciones

# ## Tipos de colecciones 
# Los tipos de colecciones más utilizados son
# * `list` una lista ordenada y mutable de valores
# * `tuple` una lista ordenada e inmutable de valores
# * `set` una lista mutable pero no ordenada de valores
# * `dict` un diccionario no ordenado

# Antes de ver los tipos de colecciones, veremos un truco muy útil para imprimir el resultado de una expresión junto con la expresión que la genera. Algunos ejemplos:

# In[1]:


print(f'{11 + 22 = }')


# In[2]:


x = 4
print(f'{x = }')
print(f'{x**2 = }')
print(f'{x / 6 = }')

print(f'x al cuadrado es {x**2 = }')


# # Listas

# ## Haciendo listas
# Para hacer una lista, enumeramos sus elemento entre un par de ```[ ]```

# In[3]:


seasons = ['Spring', 'Summer','Autumn','Winter']
seasons


# ![seasons](figures/list-diagram.png)

# Las listas pueden tener elementos heterogéneos (aunque generalmente no es una buena idea)

# In[4]:


mylist = [4, 3.0, 'abc', 5, 8, -3, 0 , 2]


# In[5]:


mylist


# ### Para obtener los elementos de la lista:

# In[6]:


seasons[2]


# In[7]:


seasons[-3]


# ### Para modificar los elementos de la lista:

# In[8]:


seasons[2] = 'Fall'
seasons


# ## *Slicing*

# Definamos la siguiente lista, con números de la secuencia de Fibonacci:
# 
# ![fibonacci](figures/fibonacci.png)

# In[9]:


fibonacci =  [1,1,2,3,5,8,13,21,34,55]
fibonacci


# Para obtener una franja de datos, usamos el operador de dos puntos ":"

# In[10]:


fibonacci[4:7]


# Es decir, `unalista[a:b]` da los elementos desde la posición `a` (incluída) hasta la posición `b` (excluída). Una manera más sencilla de entenderlo es imaginar que los enteros `a` y `b` hacen referencia a los "bordes" entre los elementos (ver figura arriba), en cuyo caso `unalista[a:b]` da por resultado otra lista con todos los elementos entres los bordes `a` y `b`.

# Si omitimos el primer índice, se sobreentiende que es desde el inicio de la lista. Por ejemplo, los primeros tres elementos

# In[11]:


fibonacci[:3]


# Si omitimos el segundo índice, se sobreentiende que es hasta el **final** de la lista. Por ejemplo, para *omitir* los primeros cinco elementos

# In[12]:


fibonacci[5:]


# También podemos contar desde el final, usando índices negativos. Por ejemplo, los últimos dos elementos

# In[13]:


fibonacci[-2:]


# In[14]:


fibonacci[-6:-3]


# o incluso combinar índices positivos y negativos: acá "quitamos" los primeros 2 elementos y los últimos tres:

# In[15]:


fibonacci[2:-3]


# Note que las dos operaciones siguientes dan por resultado el elemento del índice 3, pero la primera es una lista de un elemento y la segunda es el elemento mismo:

# In[16]:


fibonacci[3:4] # a pesar de que es un solo elemento, retorna una lista


# In[17]:


fibonacci[3]


# Si los dos índices son iguales, tendremos una lista vacía:

# In[18]:


fibonacci[3:3] 


# También podemos especificar cada cuántos elementos tomar, agregando un segundo ":" y un entero que indique cada cuántos elementos

# In[19]:


fibonacci[1:7:2]


# Podemos omitir el primer y segundo índice como antes. Por ejemplo, para rescatar los elementos en índices pares

# In[20]:


fibonacci[::2]


# y los índices impares

# In[21]:


fibonacci[1::2]


# ## Copiando una lista
# 
# ### `nueva_lista = vieja_lista` hace una variable nueva que apunta a la **misma** lista que la lista anterior:

# In[22]:


otralista = fibonacci


# In[23]:


otralista


# In[24]:


otralista[0] = 99999

print(f'{otralista=} \n{fibonacci=}')


# Vemos que es la misma lista al comparar sus `id` (que es como el número de identificación del objeto en memoria):

# In[25]:


print(f'{id(otralista)=} \n{id(fibonacci)=}')


# Con la palabra clave `is` podemos comprobar que dos variables hacen referencia a un mismo objeto:

# In[26]:


otralista is fibonacci


# ### `nueva_lista = vieja_lista.copy()` hace una copia *independiente* de la original:

# In[27]:


fibonacci[0] = 1

copialista = fibonacci.copy()
copialista[-1] = 999999

print(f'{otralista=} \n{fibonacci=} \n{copialista=}\n')
print(f'{id(otralista)=} \n{id(fibonacci)=} \n{id(copialista)=}')


# ## Manipulando listas

# Hagamos una lista de frutas. Vemos que el código es más legible si le damos a la lista un nombre *sustantivo plural* que indique la naturaleza de sus elementos:

# In[28]:


frutas = ['manzana','naranja','uva','kiwi']


# ##### ```list.append(x)``` Agrega el elemento ```x``` al final de la lista

# In[29]:


frutas.append('manzana')
frutas


# ##### ```list.extend(L)``` Agrega todos los elementos de la lista ```L``` al final de la lista

# In[30]:


frutas.extend(['mango','banano','kiwi'])
frutas


# ##### ```list.insert(i,x)``` Inserta el elemento ```x``` en la posición de índice ```i```

# In[31]:


frutas.insert(2,'guayava')
frutas


# ##### ```len(list)``` cuenta el número de elementos de la lista

# In[32]:


len(frutas)


# ##### ```list.remove(x)``` Elimina el primer elemento ```x``` de la lista

# In[33]:


frutas.remove('kiwi')
frutas


# ##### ```list.pop(i)``` Eliminina el elemento en la posición ```i``` y lo retorna

# In[34]:


frutas.pop()


# In[35]:


frutas


# ##### ```list.index(x)``` Retorna el índice del primer elemento ```x``` de la lista

# In[36]:


frutas.index('uva')


# ##### ```list.count(x)``` Retorna el número de veces que aparece ```x``` en la lista

# In[37]:


frutas.count('manzana')


# ##### ```list.sort()``` Ordena todos los elementos de la lista, in situ

# In[38]:


frutas.sort()
frutas


# ##### ```list.reverse()``` Revierte el orden de todos los elementos de la lista, in situ

# In[39]:


frutas.reverse()
frutas


# In[40]:


frutas.sort(reverse=True)
frutas


# # Tuplas
# 
# Una tupla es similar a una lista, pero una vez que se define **sus elementos no pueden cambiarse**. Se define enumerando sus elementos entre un par de  ```( )```

# In[41]:


seasons = ('Spring', 'Summer','Autumn','Winter')


# ![seasons](figures/tuple-diagram.png)

# Para obtener datos:

# In[42]:


seasons[2]


# In[43]:


seasons[-3]


# Sin embargo, los datos no se pueden modificar

# In[45]:


seasons[2] = 'Fall'


# Las tuplas también entienden de franjas

# In[46]:


M = ('Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul','Ago','Sep','Oct','Nov','Dic')


# In[47]:


# Separar los meses por trimestre:
Q1, Q2, Q3, Q4 = M[:3], M[3:6], M[6:9], M[9:]
Q2


# In[48]:


M


# In[49]:


mal = (9)
type(mal)


# Para hacer una tupla de un único elemento:

# In[50]:


solo = (55, )
type(solo)


# Los paréntesis no son del todo necesarios:

# In[51]:


solito = 77,
type(solito)


# In[52]:


colores = 'rojo', 'verde', 'azul'
print(f'{type(colores) = }, \n{colores = }')


# # Conjuntos
# Para hacer un conjunto, enumeramos sus elementos entre ```{ }```. Alternativamento, transformamos una lista en un conjunto usando la función ```set```.

# In[53]:


M2 = {2, 4, 6, 8, 10, 12, 14}
M3 = set([3, 6, 9, 12, 15])


# ##### ```set.add(x)``` Agrega un elemento ```x``` al conjunto

# In[54]:


M2.add(16)
M2


# ##### ```set.update([x,y,z])``` Agrega varios elementos al conjunto

# In[55]:


M3.update([18, 21])
M3


# ##### ```set.copy()``` Retorna una copia del conjunto

# In[56]:


M2c = M2.copy()
M2c


# ##### ```set.pop()``` Elimina al azar un elemento del conjunto

# In[57]:


M2c.pop()


# In[58]:


M2c


# ##### ```set.discard(x)``` Elimina el elemnto ```x``` del conjunto (si es miembro)

# In[59]:


M2c.discard(10)
M2c


# ##### ```set1.union(set2)``` Retorna elementos que aparecen en cualquiera de los conjuntos

# In[60]:


M2.union(M3)


# ##### ```set1.intersection(set2)``` Retorna elementos que aparecen en los dos conjuntos

# In[61]:


M3.intersection(M2)


# ##### ```set1.difference(set2)``` Retorna elementos del conjunto ```set1``` que no estén en ```set2```

# In[62]:


M2.difference(M3)


# ##### ```set1.isdisjoint(set2)``` True si los conjuntos no tienen elementos en común

# In[63]:


M2.isdisjoint(M3)


# # Diccionarios
# * En Python un “diccionario” es un contenedor de datos que puede almacenar múltiples elementos de datos como una lista de pares `llave:valor`.
# * A diferencia de las listas y tuplas, cuyos datos se obtienen por referencia a su índice, los valores almacenados en un diccionario se obtienen por referencia a su llave.
# * La llave debe ser única en el diccionario, usualmente se una un texto aunque también puede usarse números.

# In[64]:


rey = {'nombre': 'John Snow',
        'edad': 24,
        'hogar': 'Winterfell'}

rey


# Los diccionarios se pueden crear con la función ```dict```:

# In[65]:


amigo = dict(nombre='Samwell Tarly', edad=22)
amigo


# Obteniendo datos

# In[66]:


rey['edad']


# Modificando datos:

# In[67]:


rey['hogar'] = 'Castle Black'
rey


# Agregando datos:

# In[68]:


rey['amante'] = 'Ygritte'
rey['sabe'] = None
rey


# Borrando datos:

# In[69]:


del rey['amante'] # la mató Olly en la cuarta temporada!
rey


# Para almacenar un texto muy largo, podemos encerrarlo en triples comillas dobles:

# In[70]:


rey['reina'] = """Daenerys Stormborn of the House Targaryen, First of Her Name, 
The Unburnt, Queen of the Andals and the First Men, Khaleesi of the Great Grass Sea,
Breaker of Chains, and Mother of Dragons"""


# In[71]:


print(rey['reina'])


# Para obtener todas las llaves de un diccionario, usamos `.keys()`

# In[72]:


rey.keys()


# Para obtener todos los valores de un diccionario, usamos `.values()`

# In[73]:


rey.values()


# Para iterar sobre todos los elementos del diccionario, usamos `items()`

# In[74]:


for llave, valor in rey.items():
    print(f'rey["{llave}"] = {valor}')

