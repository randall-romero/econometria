---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Módulos

<div class = "video-w">
    <div class = "video-container">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/-KnsVpFhh3M" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
</div>


## Importando módulos


* Las definiciones de funciones en Python en uno o más archivos separados para facilitar su manteniniento y para permitir usarlos en varios programas sin copiar las definiciones en cada uno.

* Cada archivo que almacenda definciones de funciones se llama “módulo” y el nombre del módulo es igual al del archivo pero sin la extensión “.py”.

* Las funciones almacenadas en un módulo están disponibles para un programa usando la palabra clave ```import``` seguida del nombre del módulo.

* Aunque no es esencial, se acostumbra poner las instrucciones ```import``` al inicio del programa.

* Las funciones importadas pueden usarse llamando su nombre como un "punto-sufijo" luego del nombre del módulo. Por ejemplo, una función `sqrt` de un módulo importado `numpy` puede llamarse con `numpy.sqrt()`



## Algunos paquetes (módulos) muy útiles

En nuestro curso, los siguientes paquetes (= colecciones de módulos) serán muy útiles
* `numpy` Paquete base para arreglos N-dimensional. Operaciones matemáticas, especialmente álgebra lineal
* `matplotlib` gráficos 2D
* `pandas` estructuras para almacenar y analizar datos
* `scipy` librería fundamental para computación científica
* `bccr` ofrece funciones para descargar datos del Banco Central de Costa Rica
* `macrodemos` contiene demos de conceptos macroeconométricos, por ejemplo los modelos ARMA
* `compecon` Para resolver modelos de economía computacional



### Algunos ejemplos:

Para importar `numpy`

```{code-cell} ipython3
import numpy
numpy.sqrt(9)
```

Mismo ejemplo, pero dándolo un “alias” al módulo

```{code-cell} ipython3
import numpy as np
np.sqrt(9)
```

Mismo ejemplo, pero importando solo la función `sqrt`

```{code-cell} ipython3
from numpy import sqrt, cos, sin
sqrt(9)
```

## ¿Por qué trabajar con módulos?

* Una ventaja de organizar el código en módulos y paquetes es evitar desordenar el espacio de nombres.
* Los módulos permites tener funciones del mismo nombre en espacios de nombre separados, obligándonos a ser explícitos acerca de cuál es la que usamos.



Por ejemplo, tanto `math` como `numpy` tienen una función `cos` para computar el coseno, pero su implementación es muy distinta.

### Con `numpy`:

```{code-cell} ipython3
import numpy as np
π = np.pi
print(np.cos(0))
print(np.cos([0,   1,   π]))
```

### Con `math`:

```{code-cell} ipython3
:tags: ["raises-exception"]
import math
print(math.cos(0))
print(math.cos([0,1, π]))
```

## Iteración más rápida

```{code-cell} ipython3
nrep = 12_000
values = list(range(nrep))
```

```{code-cell} ipython3
%%timeit
option0 = np.empty_like(values)

for i, x in enumerate(values):
    option0[i] = math.cos(x)
```

```{code-cell} ipython3
%%timeit
option1 = list()
for x in values:
    option1.append(math.cos(x))
```

```{code-cell} ipython3
%%timeit
option2 = [math.cos(x) for x in values]
```

```{code-cell} ipython3
%%timeit
option3 = np.cos(values)
```



## Ejemplo de módulo: Trabajando con decimales

Los programas de cómputo que ejecutan aritmética con números de punto flotante pueden producir resultados inesperados e imprecisos porque los números de punto flotante no pueden representar adecuadamente todos los número decimales.

```{code-cell} ipython3
item, rate = 0.70, 1.05
tax = item * rate
total = item + tax
txt, val = ['item','tax','total'], [item,tax,total]

for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.2f}')
```

Con más decimales

```{code-cell} ipython3
for tt, vv in zip(txt, val):
    print(f'{tt:8s} = {vv:.20f}')
```

Los errores de la aritmética de punto flotante pueden evitarse usando el módulo de Python `decimal`. Este módulo contiene un objeto `Decimal()` con el cual los números de punto flotante pueden representarse con más precisión.

```{code-cell} ipython3
from decimal import Decimal
item, rate = Decimal('0.70'), Decimal('1.05')
tax = item * rate
total = item + tax

txt, val = ['item','tax','total'], [item,tax,total]

for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.2f}')
```

With more decimals

```{code-cell} ipython3
for tt, vv in zip(txt, val):
    print(f'{tt:5s} = {vv:.20f}')
```

## Creando un módulo

Los módulo son muy convenientes para almacenar funciones relacionadas en un solo archivo, de manera que podamos mantener el orden en nuestro proyecto y además reutilizar esas funciones en distintos lugares.

Por ejemplo, archivo **temperaturas.py** que está en la misma carpeta que este cuaderno de Jupyter contiene dos funciones, `f2c` y `c2f`, para convertir datos de temperatura.

El archivo **temperaturas.py** contiene
```python
""" Módulo temperaturas

Este módulo tiene apenas nos funciones, c2f y f2c, para convertir temperaturas
de Celsius a Fahrenheit y viceversa.
"""

def c2f(c):
    return 1.8 * c + 32

def f2c(f):
    return (f-32) / 1.8
```

Para usarlo

```{code-cell} ipython3
import temperaturas as tm

tm.f2c(90)
```

```{code-cell} ipython3
tm.c2f(40)
```

Para crear un módulo, simplemente almacenamos una o más definiciones (de funciones, variables, clases) en un archivo con extensión **.py**. Si el archivo está en la misma carpeta que el archivo de Python en ejecución, lo podemos importar directamente.
