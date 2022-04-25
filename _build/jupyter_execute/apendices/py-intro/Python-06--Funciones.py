#!/usr/bin/env python
# coding: utf-8

# # Funciones

# Las funciones son objetos que permiten realizar tareas específicas de una manera más ordenada, sin hacer copias innecesarias del código. Esto facilita enormemente el mantenimiento del código.

# ## Funciones como objetos

# En Python las funciones también son **objetos**, que pueden, por ejemplo, 
# * copiarse
# * ser miembro de una colección (lista, tupla, diccionario)
# * pasarse como un argumento de otra función

# In[1]:


type(max)


# ### ser miembro de una colección

# In[2]:


from math import sin, cos, tan, pi

𝜋 = pi

trigonometricas = (sin, cos, tan)
[f(𝜋/3) for f in trigonometricas]


# ### copiarse

# In[3]:


coseno = cos
coseno(𝜋/3)


# ### pasarse como argumento de otra función

# In[4]:


from scipy import integrate

integrate.quad(cos, 0, 𝜋/2)[0]


# # Definiendo funciones
# 
# Una función se crea usando la palabra clave `def` (definition) seguida de un nombre de su escogencia y paréntesis `( )`.
# 
# El programador puede escoger cualquier nombre para una función, excepto las palabras claves de Python y el nombre de funciones integradas existentes.
# 
# Esta línea debe terminar con un `:`, luego deben seguir las instrucciones que la función ejecuta cuando es llamada, en líneas indentadas.
# 
# Por tanto, la sintaxis se ve así:
# ```
# def function-name( ):
#     statements-to-be-executed
#     statements-to-be-executed
# ```    

# Para averiguar las palabras claves de Python:

# In[5]:


import keyword
print(keyword.kwlist)


# ## Una función sin argumentos

# In[6]:


def hello( ):
    print('Hello')
    print('Welcome to the UCR!')


# Para correr esta función

# In[7]:


hello()


# In[8]:


saludar = hello


# In[9]:


saludar()


# ## Una función con argumentos
# 
# Supongamos que deseamos escribir una función para convertir un dato de temperatura de Celsius a Fahrenheit. Para ello, sabemos que:
# $$F = \tfrac{9}{5}C + 32 = 1.8C + 32$$

# In[10]:


def c2f(c):
    f = 1.8 * c + 32
    print(f'{c:.1f}° Celsius es igual a {f:.1f}° Fahrenheit')

c2f(15)


# In[11]:


y = c2f(100)


# In[12]:


type(y)


# ## Una función que retorna un valor

# In[13]:


def c2f(c):
    f = 1.8 * c + 32
    return f


# In[14]:


x = c2f(15)
print(x)


# ## Una función con parámetros predeterminados

# In[15]:


def c2f(c, *, mayuscula=False, mostrar=False):
    f = 1.8 * c + 32
    if mostrar:
        if mayuscula:
            print(f'{c:.1f}° CELSIUS = {f:.1f} FAHRENHEIT')
        else:
            print(f'{c:.1f}° Celsius = {f:.1f} Fahrenheit')
    return f

c2f(15)


# In[16]:


c2f(15, mostrar=True, mayuscula=True)


# In[17]:


c2f(15, mostrar=True)


# ## Una función con un número indefinido de parámetros posicionales
# 
# Supongamos que queremos escribir una función que dependa de un número indefinido de parámetros. Por ejemplo, la función `print` imprime un número arbitrario de elementos:

# In[18]:


print(3, 4, 6)


# In[19]:


print(5,3,7,1,"perro")


# Claramente no sería práctico hacer una función distinta para cada posible número de argumentos. Para ello utilizamos `*args` (**arg**ument**s**) en la definición de la función. Por ejemplo, para escribir una operación de suma:

# In[20]:


def imprimir_suma(*args):
    numeros = (str(x) for x in args)
    sumando = ' + '.join(numeros) 
    resultado = sum(args)
    print(sumando, " = ", resultado)
    print(f'\nEjecutando imprimir_suma con args = ', args, sep='\n')
    print(f'\nEjecutando imprimir suma con *args = ', *args, sep='\n')


# In[21]:


imprimir_suma(3,2,5)


# In[22]:


imprimir_suma(1,1,1,1,1)


# Vemos que a lo interno de la función, `args` es una tupla, mientras que `*args` son los elementos individuales de esa tupla.

# ## Una función con un número indefinido de parámetros de palabra clave
# 
# Supongamos que queremos escribir una función que dependa de un número indefinido de parámetros de palabras clave (usualmente para especificar opciones). Para ello, agrupamos esos parámetros en la variable `**kwargs` (**k**ey**w**ord **arg**ument**s**)

# In[23]:


def imprimir_opciones(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro, " = ", valor)
    
    print(f'\nEjecutando imprimir_suma con kargs = ', kwargs, sep='\n')


# In[24]:


imprimir_opciones(color='rojo', modelo='2018', marca='Honda', estilo='SUV')


# Vemos que a lo interno de la función, `**kwargs` es un diccionario. Esta característica de Python es muy útil para fijar un grupo de opciones en un diccionario y pasarlas repetidamente a funciones. Por ejemplo, la función `print` separa elementos con un espacio y termina la operación con un salto de linea:

# In[25]:


get_ipython().run_line_magic('pinfo', 'print')


# Podemos cambiar estos valores repetidamente así:

# In[26]:


print(1,2,3)
print(4,5,6)


# In[27]:


OPCIONES = {'sep': ' /*\ ', 'end': '\n\n'}

print(1,2,3, **OPCIONES)
print(4,5,6, **OPCIONES)


# In[28]:


print(3,2,5, OPCIONES)


# En la práctica, podemos combinar ambas características:

# In[29]:


def imprimir_operacion(*numeros, **print_options):
    print('Sin tomar en cuenta las opciones, la tupla de números es ')
    print(*numeros)
    print('pero tomando en cuenta las opciones, la tupla de números es ')
    print(*numeros, **print_options)


# In[30]:


imprimir_operacion(2,5,3,6,8,1)


# In[31]:


OPCIONES = dict(sep = ' * ', end = ' = ¿quién sabe?!!\n')
imprimir_operacion(2,5,3,6,8,1, **OPCIONES)


# Vemos que lo importante de `*args` y `**kwargs` es el número de asteriscos, no el nombre mismo de la variable.

# # Documentando una función
# 
# ¡Es muy importante documentar lo que hace su código!

# In[32]:


def c2f(c, show=False):
    """
    Convierte dato de temperatura de grados Celsius a grados Fahrenheit
    
    Parámetros:
      c: un número escalar, grados en Celsius
      show: un boolean, imprime el resultado si `True`
    Resultado:
      un número escalar, grados en Fahrenheit
    Ejemplo:
      c2f(0)  # da 32.0 por resultado
    """
    f = 1.8 * c + 32
    if show:
        print(f'{c:.1f}° Celsius = {f:.1f} Fahrenheit')
    return f

z = c2f(15)


# In[33]:


help(c2f)


# In[34]:


get_ipython().run_line_magic('pinfo', 'c2f')


# # Entendiendo el ámbito de una variable

# Cuando una función encuentra una variable dentro de su definición que no hay sido definida dentro de la función, buscará su definición en el ambiente donde la función fue definida.

# In[35]:


pi = 3.1415

def area(r):
    A = pi * r**2
    return A


# In[36]:


pi


# In[37]:


print(area(10))


# La siguiente línea da un error, porque `A` es una variable definida a lo interno de la función `area`, por lo que no es visible desde "fuera" de la función:

# In[38]:


print(A)


# Ahora cambiamos el valor de `pi`, y ejectamos `area` de nuevo:

# In[39]:


pi = 9
area(10)


# Vemos que el resultado cambia!!! Esto se debe a que la función `area` busca el valor de `pi` cada vez que es ejecutada, **no** al momento de definir la función.
