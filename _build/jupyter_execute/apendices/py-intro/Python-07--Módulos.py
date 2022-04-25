#!/usr/bin/env python
# coding: utf-8

# # Módulos

# # Importando módulos

# * Las definiciones de funciones en Python en uno o más archivos separados para facilitar su manteniniento y para permitir usarlos en varios programas sin copiar las definiciones en cada uno.
# 
# * Cada archivo que almacenda definciones de funciones se llama “módulo” y el nombre del módulo es igual al del archivo pero sin la extensión “.py”.
# 
# * Las funciones almacenadas en un módulo están disponibles para un programa usando la palabra clave ```import``` seguida del nombre del módulo.
# 
# * Aunque no es esencial, se acostumbra poner las instrucciones ```import``` al inicio del programa.
# 
# * Las funciones importadas pueden usarse llamando su nombre como un "punto-sufijo" luego del nombre del módulo. Por ejemplo, una función `sqrt` de un módulo importado `numpy` puede llamarse con `numpy.sqrt()`

# ## Algunos paquetes (módulos) muy útiles
# 
# En nuestro curso, los siguientes paquetes (= colecciones de módulos) serán muy útiles
# * `numpy` Paquete base para arreglos N-dimensional. Operaciones matemáticas, especialmente álgebra lineal
# * `matplotlib` gráficos 2D
# * `pandas` estructuras para almacenar y analizar datos
# * `scipy` librería fundamental para computación científica
# * `bccr` ofrece funciones para descargar datos del Banco Central de Costa Rica
# * `macrodemos` contiene demos de conceptos macroeconométricos, por ejemplo los modelos ARMA
# * `compecon` Para resolver modelos de economía computacional

# ### Algunos ejemplos:
# 
# Para importar `numpy`

# In[1]:


import numpy
numpy.sqrt(9)


# Mismo ejemplo, pero dándolo un “alias” al módulo

# In[2]:


import numpy as np
np.sqrt(9)


# Mismo ejemplo, pero importando solo la función `sqrt`

# In[3]:


from numpy import sqrt, cos, sin
sqrt(9)


# ## ¿Por qué trabajar con módulos?
# 
# * Una ventaja de organizar el código en módulos y paquetes es evitar desordenar el espacio de nombres.
# * Los módulos permites tener funciones del mismo nombre en espacios de nombre separados, obligándonos a ser explícitos acerca de cuál es la que usamos.

# Por ejemplo, tanto `math` como `numpy` tienen una función `cos` para computar el coseno, pero su implementación es muy distinta.
# 
# ### Con `numpy`:

# $\pi$

# In[4]:


π = np.pi


# In[5]:


np.cos(π)


# In[6]:


import numpy as np
print(np.cos(0))
print(np.cos([0,   1,   np.pi]))


# ### Con `math`:

# Esta celda da un  error, porque la función `math.cos` fue definida para calcular el coseno de un único número, no de una lista de números a la vez (como sí lo hace la función `np.cos`)

# In[7]:


import math
print(math.cos(0))
print(math.cos([0,1, np.pi]))


# ## Iteración más rápida

# In[8]:


nrep = 12_000
values = list(range(nrep))


# In[9]:


get_ipython().run_cell_magic('timeit', '', 'option0 = np.empty_like(values)\n\nfor i, x in enumerate(values):\n    option0[i] = math.cos(x)')


# In[10]:


get_ipython().run_cell_magic('timeit', '', 'option1 = list()\nfor x in values:\n    option1.append(math.cos(x))')


# In[11]:


get_ipython().run_cell_magic('timeit', '', 'option2 = [math.cos(x) for x in values]')


# In[12]:


get_ipython().run_cell_magic('timeit', '', 'option3 = np.cos(values)')


# ## Ejemplo de módulo: Trabajando con decimales
# 
# Los programas de cómputo que ejecutan aritmética con números de punto flotante pueden producir resultados inesperados e imprecisos porque los números de punto flotante no pueden representar adecuadamente todos los número decimales.

# In[13]:


item, rate = 0.70, 1.05
tax = item * rate
total = item + tax
txt, val = ['item','tax','total'], [item,tax,total]

for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.2f}')


# Con más decimales

# In[14]:


for tt, vv in zip(txt, val):
    print(f'{tt:8s} = {vv:.20f}')


# Los errores de la aritmética de punto flotante pueden evitarse usando el módulo de Python `decimal`. Este módulo contiene un objeto `Decimal()` con el cual los números de punto flotante pueden representarse con más precisión.

# In[15]:


from decimal import Decimal
item, rate = Decimal('0.70'), Decimal('1.05')
tax = item * rate
total = item + tax

txt, val = ['item','tax','total'], [item,tax,total]

for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.2f}')


# Con más decimales

# In[16]:


for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.20f}')


# # Creando un módulo
# 
# Los módulo son muy convenientes para almacenar funciones relacionadas en un solo archivo, de manera que podamos mantener el orden en nuestro proyecto y además reutilizar esas funciones en distintos lugares.

# Por ejemplo, archivo **módulo_sencillo.py** que está en la misma carpeta que este cuaderno de Jupyter contiene una función llamada `hola`, con la saludamos. Además, hay una variable "string" llamada `fecha`, donde guardé la fecha en que hice este módulo.

# In[17]:


from módulo_sencillo import hola, fecha


# Para crear un módulo, simplemente almacenamos una o más definiciones (de funciones, variables, clases) en un archivo con extensión **.py**. Si el archivo está en la misma carpeta que el archivo de Python en ejecución, lo podemos importar directamente.

# In[18]:


hola()


# In[19]:


fecha


# Otra manera es cargar el módulo completo, en cuyo caso

# In[20]:


import módulo_sencillo


# In[21]:


módulo_sencillo.hola()


# In[22]:


módulo_sencillo.fecha


# Como no es práctico escribir `módulo_sencillo` cada vez que usamos una de sus definiciones, le podemos poner un nombre más corto al importarlo, por ejemplo

# In[23]:


import módulo_sencillo as ms

ms.hola()


# In[24]:


ms.fecha

