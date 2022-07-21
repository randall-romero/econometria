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

# Funciones

Las funciones son objetos que permiten realizar tareas específicas de una manera más ordenada, sin hacer copias innecesarias del código. Esto facilita enormemente el mantenimiento del código.

<div class = "video-w">
    <div class = "video-container">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/cU0otOOh6nc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
</div>

## Funciones como objetos



En Python las funciones también son **objetos**, que pueden, por ejemplo,
* copiarse
* ser miembro de una colección (lista, tupla, diccionario)
* pasarse como un argumento de otra función

```{code-cell} ipython3
type(max)
```

### ser miembro de una colección

```{code-cell} ipython3
from math import sin, cos, tan, pi

𝜋 = pi

trigonometricas = (sin, cos, tan)
[f(𝜋/3) for f in trigonometricas]
```

### copiarse

```{code-cell} ipython3
coseno = cos
coseno(𝜋/3)
```

### pasarse como argumento de otra función

```{code-cell} ipython3
from scipy import integrate

integrate.quad(cos, 0, 𝜋/2)[0]
```



## Definiendo funciones

Una función se crea usando la palabra clave `def` (definition) seguida de un nombre de su escogencia y paréntesis `( )`.

El programador puede escoger cualquier nombre para una función, excepto las palabras claves de Python y el nombre de funciones integradas existentes.

Esta línea debe terminar con un `:`, luego deben seguir las instrucciones que la función ejecuta cuando es llamada, en líneas indentadas.

Por tanto, la sintaxis se ve así:
```
def function-name( ):
    statements-to-be-executed
    statements-to-be-executed
```    


Para averiguar las palabras claves de Python:

```{code-cell} ipython3
import keyword
print(*keyword.kwlist, sep='\n')
```


### Una función sin argumentos

```{code-cell} ipython3
def hello( ):
    print('Hello')
    print('Welcome to the UCR!')
```

Para correr esta función

```{code-cell} ipython3
hello()
```

```{code-cell} ipython3
saludar = hello
```

```{code-cell} ipython3
saludar()
```

### Una función con argumentos

Supongamos que deseamos escribir una función para convertir un dato de temperatura de Celsius a Fahrenheit. Para ello, sabemos que:
\begin{equation*}
F = \tfrac{9}{5}C + 32 = 1.8C + 32
\end{equation*}

```{code-cell} ipython3
def c2f(c):
    f = 1.8 * c + 32
    print(f'{c:.1f}° Celsius es igual a {f:.1f}° Fahrenheit')

c2f(15)
```

```{code-cell} ipython3
y = c2f(100)
```

```{code-cell} ipython3
type(y)
```



### Una función que retorna un valor

```{code-cell} ipython3
def c2f(c):
    f = 1.8 * c + 32
    return f


x = c2f(15)
print(x)
```



### Una función con parámetros predeterminados

```{code-cell} ipython3
def c2f(c, *, mayuscula=False, mostrar=False):
    f = 1.8 * c + 32
    if mostrar:
        if mayuscula:
            print(f'{c:.1f}° CELSIUS = {f:.1f} FAHRENHEIT')
        else:
            print(f'{c:.1f}° Celsius = {f:.1f} Fahrenheit')
    return f

c2f(15)
```

```{code-cell} ipython3
c2f(15, mostrar=True, mayuscula=True)
```

```{code-cell} ipython3
c2f(15, mostrar=True)
```



## Una función con un número indefinido de parámetros posicionales

Supongamos que queremos escribir una función que dependa de un número indefinido de parámetros. Por ejemplo, la función `print` imprime un número arbitrario de elementos:

```{code-cell} ipython3
print(3, 4, 6)
```

```{code-cell} ipython3
print(5,3,7,1,"perro")
```

Claramente no sería práctico hacer una función distinta para cada posible número de argumentos. Para ello utilizamos `*args` en la definición de la función. Por ejemplo, para *escribir* una operación de suma:

```{code-cell} ipython3
def imprimir_suma(*args):
    numeros = (str(x) for x in args)
    sumando = ' + '.join(numeros)
    resultado = sum(args)
    print(sumando, " = ", resultado)
    print('args = ', args, sep="\n")
    print('*args = ', *args, sep="\n")
```

```{code-cell} ipython3
imprimir_suma(3,2,5)
```

```{code-cell} ipython3
imprimir_suma(1,1,1,1,1)
```

Vemos que a lo interno de la función, `args` es una tupla, mientras que `*args` son los elementos individuales de esa tupla.



### Una función con un número indefinido de parámetros de palabra clave

Supongamos que queremos escribir una función que dependa de un número indefinido de parámetros de palabras clave (usualmente para especificar opciones). Para ello, agrupamos esos parámetros en la variable `**kwargs`

```{code-cell} ipython3
def imprimir_opciones(**kwargs):
    for parametro, valor in kwargs.items():
        print(parametro, " = ", valor)
    print('kwargs = ', kwargs)
```

```{code-cell} ipython3
imprimir_opciones(color='rojo', modelo='2018', marca='Honda', estilo='SUV')
```

Vemos que a lo interno de la función, `**kwargs` es un diccionario. Esta característica de Python es muy útil para fijar un grupo de opciones en un diccionario y pasarlas repetidamente a funciones. Por ejemplo, la función `print` separa elementos con un espacio y termina la operación con un salto de linea:

```{code-cell} ipython3
?print
```

Podemos cambiar estos valores repetidamente así:

```{code-cell} ipython3
print(1,2,3)
print(4,5,6)
```

```{code-cell} ipython3
OPCIONES = {'sep': ' /*\ ', 'end': '\n\n'}
print(1,2,3, **OPCIONES)
print(4,5,6, **OPCIONES)
```

En la práctica, podemos combinar ambas características:

```{code-cell} ipython3
def imprimir_operacion(*numeros, **print_options):
    print('Sin tomar en cuenta las opciones, la tupla de números es ')
    print(*numeros)
    print('pero tomando en cuenta las opciones, la tupla de números es ')
    print(*numeros, **print_options)

imprimir_operacion(2,5,3,6,8,1)
```

```{code-cell} ipython3
OPCIONES = dict(sep = ' * ', end = ' = ¿quién sabe?!!\n')
imprimir_operacion(2,5,3,6,8,1, **OPCIONES)
```

Vemos que lo importante de `*args` y `**kwargs` es el número de asteriscos, no el nombre mismo de la variable.


## Documentando una función

¡Es muy importante documentar lo que hace su código!

```{code-cell} ipython3
def c2f(c, show=False):
    """
    Converts temperature data from Celsius degrees to Fahrenheit degrees

    Input:
      c: a scalar number, degrees in Celsius
      show: a boolean, whether to print the outcome
    Output:
      a scalar number, degrees in Fahrenheit
    Example:
      c2f(0)  # returns 32.0
    """
    f = 1.8 * c + 32
    if show:
        print(f'{c:.1f}° Celsius = {f:.1f} Fahrenheit')
    return f

z = c2f(15)
```

```{code-cell} ipython3
help(c2f)
```

```{code-cell} ipython3
?c2f
```



## Entendiendo el ámbito de una variable



Cuando una función encuentra una variable dentro de su definición que no hay sido definida dentro de la función, buscará su definición en el ambiente donde la función fue definida.

```{code-cell} ipython3
pi = 3.1415

def area(r):
    A = pi * r**2
    return A
```

```{code-cell} ipython3
pi
```

```{code-cell} ipython3
print(area(10))
```

Esta linea genera un error, porque `A` fue definida dentro de la función `area`, no existe en el ámbito exterior a esa función:
```{code-cell} ipython3
:tags: ["raises-exception"]
print(A)
```

Al cambiar el valor de `pi`, la próxima vez que ejecutamos `area(10)` obtenemos un valor distinto, porque las funciones buscan el valor que falta en el ambiente que fue definida **cada vez que se ejecuta la función**, no al momento de de definir la función (podría incluso no existir aún en ese momento):
```{code-cell} ipython3
pi = 9
area(10)
```
