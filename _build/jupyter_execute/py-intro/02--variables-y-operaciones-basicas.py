# Variables y operaciones básicas

En este cuaderno hacemos una pequeña introducción al lenguage de programación Python.

## Utilizando variables

* Una variable es un contenedor en el cual un dato puede almacenarse en la memoria de la computadora.
* El valor almacenado puede luego ser referido usando el nombre de la variable.

mosqueteros = 3
pi = 3.14
nombres = "Fulano y Mengano"
hoyLlueve = True

print(mosqueteros, pi, nombres, hoyLlueve, sep="\n")

## Tipos de datos básicos

Hay cuatro tipos básicos de datos
* `int` enteros
* `float` punto flotantes (números decimales)
* `bool` boolean (True o False)
* `str` texto

type(mosqueteros)

type(nombres)

type(pi)

type(hoyLlueve)

```{warning} Cuidado con float:
Los floats en general representan **aproximaciones** de los números reales. No siempre son los números exactos porque hay errores de redondeo al almacenar un número en binario con un tamaño finito.
```

Por ejemplo,

(1e-18 + 1) - 1

1e-18 + (1 - 1)

z = 0.1
print(f"A 24 decimales, z = 0.1 queda almacenado como {z:.24f}")

## Tipos de colecciones

Los tipos de colecciones más utilizados son
* `list` una lista ordenada y mutable de valores
* `tuple` una lista ordenada e inmutable de valores
* `set` una lista mutable pero no ordenada de valores
* `dict` un diccionario no ordenado

Aquí vemos cómo se crean, {ref}`más adelante<py-sec-colecciones>` estudiaremos su utilidad.

colores = ['azul', 'rojo', 'verde']   # list
primos = (2,3,5,7)  # tuple
inflacion = {'CRI': 2.0, 'SLV': 0.8, 'GTM': 4.0,
             'HND': 4.0, 'NIC': 5.2, 'DOM': 4.5}  # dict
cuadrados = {1,1,1,4,4,9,9,16}  # set

## Definiendo múltiples variables
En Python es posible definir varias variables en una sola instrucción:

n, a, b = 12, -2.0, 2.0

x = y = z = 1

y

## Cambiando tipos de datos: *casting*

'8' + '4'

'8' * 4

### ```int(x)``` Convierte ```x``` a un número entero

int('8') + int('4')

### ```float(x)``` Convierte ```x``` a un número de punto flotante

float('8') + float('4')

### ```str(x)``` Convierte ```x``` a una representación de texto

str(8) + str(4)

## Operaciones aritméticos


### Suma:  `+`

2 + 3

### Resta:  `-`

5 - 1.0

### Multiplicación:  `*`

4 * 4

### División:   `/`

9 / 3

### Módulo:  `%`

10 % 3

### División entera:  `//`

10 // 3

### Exponente:  `**`

5 ** 2

## Asignando valores por medio de operadores

### a `=` b    $\qquad\Rightarrow\qquad$ a = b

x = 2 + 1
x

### a `+=` b    $\qquad\Rightarrow\qquad$ a = a + b

x += 1
x

### a `-=` b    $\qquad\Rightarrow\qquad$ a = a - b

x -= 2
x

### a `*=` b    $\qquad\Rightarrow\qquad$ a = a \* b

x *= 3
x

### a `/=` b    $\qquad\Rightarrow\qquad$ a = a / b

x /= 0.25
x

### a `%=` b    $\qquad\Rightarrow\qquad$ a = a % b

x %=  5
x

### a `//=` b    $\qquad\Rightarrow\qquad$ a = a // b

x //= 1.25
x

### a `**`= b    $\qquad\Rightarrow\qquad$ a = a \*\* b

x **= 2
x

## Comparando valores


### Igualdad    `==`

5 == 5.0

### Desigualdad  `!=`

4 != 4.0

### Mayor que `> `

5 > 4

### Menor que `<`

5 < 4

### Mayor o igual que `>=`

4 >=4

### Menor o igual que `<=`

5 <= 5

## Operaciones lógicas


###  AND lógico:  `and`

1 > 2 and 1 < 4

### OR lógico:  `or`

1 > 2 or 1 < 4

### NOT lógico   `not`

not 5 > 4