#!/usr/bin/env python
# coding: utf-8

# # Variables y operaciones básicas

# ## Utilizando variables
# 
# * Una variable es un contenedor en el cual un dato puede almacenarse en la memoria de la computadora.
# * El valor almacenado puede luego ser referido usando el nombre de la variable.

# In[1]:


mosqueteros = 3 
pi = 3.14
nombres = "Fulano y Mengano"
hoyLlueve = True

print(mosqueteros, pi, nombres, hoyLlueve, sep="\n")


# ## Tipos de datos básicos
# Hay cuatro tipos básicos de datos
# * `int` enteros
# * `float` punto flotantes (números decimales)
# * `bool` boolean (True o False)
# * `str` texto

# In[2]:


type(mosqueteros)


# In[3]:


type(nombres)


# In[4]:


type(pi)


# In[5]:


type(hoyLlueve)


# ### Cuidado con float:
# 
# Los floats en general representan **aproximaciones** de los números reales. No siempre son los números exactos porque hay errores de redondeo al almacenar un número en binario con un tamaño finito.

# In[6]:


(1e-18 + 1) - 1


# In[7]:


1e-18 + (1 - 1)


# In[8]:


z = 0.1
f"z = 0.1 queda almacenado como {z:.24f}"


# ## Tipos de colecciones 
# Los tipos de colecciones más utilizados son
# * `list` una **lista** ordenada y mutable de valores
# * `tuple` una **tupla** ordenada e inmutable de valores
# * `set` un **conjunto** mutable pero no ordenada de valores
# * `dict` un **diccionario** no ordenado

# In[9]:


colores = ['azul', 'rojo', 'verde']   # list
primos = (2,3,5,7)  # tuple
inflacion = {'CRI': 2.0, 'SLV': 0.8, 'GTM': 4.0, 
             'HND': 4.0, 'NIC': 5.2, 'DOM': 4.5}  # dict
cuadrados = {1,1,1,4,4,9,9,16}  # set


# In[10]:


cuadrados


# ## Definiendo múltiples variables
# En Python es posible definir varias variables en una sola instrucción:

# * Si escribimos una colección ordenada del lado derecho del =, podemos asignar variables a cada elemento individual. Por ejemplo:

# In[11]:


a,r,v = colores
a


# In[12]:


n, a, b = 12, -2.0, 2.0


# * Si escribimos varios signos =, todas las variables tendrán el mismo valor:

# In[13]:


x = y = z = 1


# In[14]:


y


# ## Cambiando tipos de datos: *casting*

# In[15]:


'8' + '4'


# In[16]:


'8' * 4


# ##### ```int(x)``` Convierte ```x``` a un número entero

# In[17]:


int('8') + int('4')


# ##### ```float(x)``` Convierte ```x``` a un número de punto flotante

# In[18]:


float('8') + float('4')


# ##### ```str(x)``` Convierte ```x``` a una representación de texto

# In[19]:


str(8) + str(4)


# # Operadores básicos

# ## Operaciones aritméticos

# ##### Suma:  `+`

# In[20]:


2 + 3


# ##### Resta:  `-`

# In[21]:


5 - 1.0


# ##### Multiplicación:  `*`

# In[22]:


4 * 4


# ##### División:   `/`

# In[23]:


9 / 3


# ##### Módulo:  `%`

# In[24]:


10 % 3


# ##### División entera:  `//`

# In[25]:


10 // 3


# ##### Exponente:  `**`

# In[26]:


5 ** 2


# ## Asignando valores por medio de operadores

# ##### a `=` b    $\qquad\Rightarrow\qquad$ a = b

# In[27]:


x = 2 + 1
x


# ##### a `+=` b    $\qquad\Rightarrow\qquad$ a = a + b

# In[28]:


x += 1
x


# ##### a `-=` b    $\qquad\Rightarrow\qquad$ a = a - b

# In[29]:


x -= 2
x


# ##### a `*=` b    $\qquad\Rightarrow\qquad$ a = a \* b

# In[30]:


x *= 3
x


# ##### a `/=` b    $\qquad\Rightarrow\qquad$ a = a / b

# In[31]:


x /= 0.25
x


# ##### a `%=` b    $\qquad\Rightarrow\qquad$ a = a % b

# In[32]:


x %=  5
x


# ##### a `//=` b    $\qquad\Rightarrow\qquad$ a = a // b

# In[33]:


x //= 1.25
x


# ##### a `**`= b    $\qquad\Rightarrow\qquad$ a = a \*\* b

# In[34]:


x **= 2
x


# ## Comparando valores

# ##### Igualdad    `==`

# In[35]:


5 == 5.0


# In[36]:


"A" == "a"


# ##### Desigualdad  `!=`

# In[37]:


4 != 4.0


# In[38]:


7 != 4


# ##### Mayor que `> `

# In[39]:


5 > 4


# In[40]:


4 > 5


# ##### Menor que `<`

# In[41]:


5 < 4


# In[42]:


4 < 5


# ##### Mayor o igual que `>=`

# In[43]:


4 >=4


# ##### Menor o igual que `<=`

# In[44]:


5 <= 5


# ## Operaciones lógicas

# #####  AND lógico:  `and`

# In[45]:


1 > 2 and 1 < 4


# ##### OR lógico:  `or`

# In[46]:


1 > 2 or 1 < 4


# ##### NOT lógico   `not`

# In[47]:


not 5 > 4

