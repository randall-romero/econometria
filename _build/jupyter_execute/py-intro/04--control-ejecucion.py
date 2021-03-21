# Control de ejecución



* Los programas usualmente se ejecutan corriendo cada instrucción en el orden en que aparecen
* Pero en ocasiones, necesitamos ejecutar las  instrucciones de otra manera.
* Para ello, usamos instrucciones de control de ejecución:
- ```if, elif, else``` ejecuta algunas instrucciones una vez, pero solo si cierta condición es verdadera
- ```while``` ejecuta algunas instrucciones varias veces, solo mientras que cierta condición sea verdadera
- ```for``` ejecuta algunas instrucciones varias veces, iterando sobre un iterable
- ```continue``` brinca a la siguiente iteraciónde un bucle  `while` o `for`
- ```break``` detiene la ejecución de un bucle `while` o `for`

<div class = "video-w">
    <div class = "video-container">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/yd2nGfknE4k" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
</div>

## Ejecución condicional con `if`

* La palabra clave ```if``` evalua una expresión para obtener un valor `True` o `False`.
* Esto permite que un programa proceda en diferentes direcciones de acuerdo con el resultado del test.
* La expresión evaluada debe ser seguida de dos puntos ```:```, luego las instrucciones que se evaluan si el test es verdadero deben escribirse en líneas separadas e indentadas respecto a la línea que contiene el ```if```.
* El tamaño de la indentación no es importante, pero debe ser el mismo en cada línea.
* Por tanto, la sintaxis se ve así:
```
if test-expression:
   statements-to-execute-when-test-expression-is-True
   statements-to-execute-when-test-expression-is-True
```   



Por ejemplo, para determinar si un número ```m``` es par o impar:

m = 7
if m % 2 == 0:
    print('m es par')
else:
    print('m es impar')

El test no necesariamente tiene que ser un boolean. El número `0`, el valor `None`, y un texto vacío `''`, lista vacía `[]`, tupla vacía `()` o conjunto vacío `{}`, todos son interpretados como  `False`.

if m % 5:
    print('m is not divisible by 5')
else:
    print('m is divisible by 5')

horas = 10

if horas < 12:
    ampm = 'a.m.'
else:
    ampm = 'p.m.'

ampm

ampm1 = 'a.m.' if horas < 12 else 'p.m.'
ampm1

## Examinando condiciones
Algunas veces necesitamos asignar un valor dependiendo de una condición, como así
```
if testExpression:
    x = ifTrueThis
else:
    x = ifFalseThis
```
Esto es equivalente a :
```
x = ifTrueThis if testExpression else ifFalseThis
```
Por ejemplo

n = 17
z = "n is odd" if n % 2 else "n is even"

z

## Iterando `while` true i

* Un bucle es una pieza de código que automáticamente se repite.
* Una ejecución completa de todas las instrucciones dentro de un bucle se llama una “iteración”.
* El tamaño del buche se controla con un test condicional que se ejecuta dentro del bucle.
* Mientras que la expresión evaluada sea  ```True``` el bucle continuará –-- hasta que la expresión sea ```False```, punto en el cual el bucle termina.
* En programas de Python, la palabra clave ```while``` crea un bucle. Es seguida por la expresion a evaluar y dos puntos ```:```.
* Las instrucciones que se deben evaluar cuando el test pasa (sea ```True```) deben seguir abajo en líneas separadas, y cada línea debe estar indentada con el mismo espacio respecto a la línea que tiene el ```while```.
* Este bloque de instrucciones debe incluir una instrucción que en algún momento cambie el resultado del test a ```False``` --- de lo contrario el bucle será infinito.
* Por tanto, la sintaxis se ve así:

```
while test-expression :
    statements-to-execute-when-test-expression-is-True
    statements-to-execute-when-test-expression-is-True
```    



Por ejemplo, para obtener la serie de Fibonacci hasta 100

a, b = 0, 1

while b < 100:
    print(b, end=', ')
    a, b = b, a + b

Un enfoque distinto, pero que incluye el primer elemnto que se pasa de 100

fib = [1, 1]

while fib[-1]<100:
    fib.append(fib[-2] + fib[-1])
else:
    fib.pop()


fib

## La función ```range```
Algunas veces necesitamos iterar sobre los enteros. Podemos generarlos con la función ```range```.

range(6)

Para ahorrar memoria, ```range``` retorna sus elementos uno a la vez, solo cuando se necesita, para evitar usar demasiada memoria. En los ejemplos que siguen convertimos objetos ```range``` en listas para poder imprimir sus elementos.



`range(n)` retorna enteros de ```0``` a ```n-1```

list(range(6))

`range(m, n)` retorna enteros de ```m``` a ```n-1```

list(range(2,8))

`range(m, n, s)` retorna enteros de ```m``` a ```n-1```, de ```s``` en ```s```

list(range(2,9,3))

También podemos crear un ```range``` con el orden invertido:

list(range(4, 0,-1))

### Comparando la cantidad de memoria necesaria

from sys import getsizeof

getsizeof(list(range(1_000_000)))

getsizeof(range(1_000_000))

## Iterando sobre los elementos de un iterable: `for`

En Python la palabra clave ```for``` itera sobre todos los elementos de cualquier iterable que aparezca luego de la palabra clave ```in```.

La sintaxis se ve así:

```
for item in iterable :
    statements-to-execute-on-each-iteration
    statements-to-execute-on-each-iteration
```    

Ejemplos de iterables:
* rangos
* listas, tuplas, conjutos, diccionarios
* textos
* archivos de texto
* arreglos de números



### Iterando sobre textos

for letra in 'abcd':
    print(letra.upper())

### Iterando sobre enteros

for k in range(1, 6):
    print(k**2)

### Iterando líneas de un archivo de texto

for linea in open("mi_estilo.css", 'r'):
    print(linea)

### Iterando los elemetos de un diccionario

king = {'name': 'John Snow',
        'age': 24,
        'home': 'Castle Black',
        'lover': 'Ygritte',
        'knows': None}

for llave, valor in king.items():
    print(f'king["{llave}"] = {valor}')

## enumerate



Para llevar cuenta del número de iteración usamos ```enumerate```

eltexto = 'abcde'

for i in range(len(eltexto)):
    letra = eltexto[i]
    print(f'iteración {i} da por resultado  {letra}')


eltexto = 'abcde'

for i, letra in enumerate(eltexto):
    print(f'iteración {i} da por resultado  {letra}')


for i, letter in enumerate('abcd'):
    print(f'{i} = {letter}')

for i, letter in enumerate('abcd'):
    print(f'Estoy en la iteración {i:d} = {letter}')

## zip



Para iterar dos iterables en paralelo, usamos `zip`

quantities = [3, 2, 4]
fruits = ('apple','banana','coconut')

for i in range(len(quantities)):  # muy complicado
    n = quantities[i]
    fruit = fruits[i]
    print(f'{n} {fruit}s')

for n, fruit in zip(quantities,fruits): # más elegante
    print(f'{n} {fruit}s')

Una ventaja de trabajar con `zip` es que no genera un error si una lista es más corta que la que medimos con `len`, simplemente itera mientras haya elementos en ambas listas. Por ejemplo

quantities.append(8)  # ahora quantities tiene 4 elementos, pero fruits sigue con 3

for i in range(len(quantities)):  
    n = quantities[i]
    fruit = fruits[i]
    print(f'{n} {fruit}s')

mientras con `zip`:

for n, fruit in zip(quantities,fruits): # más elegante
    print(f'{n} {fruit}s')

## *List comprehensions*

* *List comprehension* es una manera elegante de definir una lista basado en otra lista (un iterable).
* Generalmente son más compactas y rápidas que los bucles tradicionales.
* No obstante, debemos evitar *list comprenhension* demasiado largas para que el código sea claro.




### Caso más sencillo



A veces necesitamos hacer una lista de elementos a partir de otro iterable, como con este código

```
lst = list()
for item in iterable:
    lst.append(expression)
```

Esto puede hacer más sucintamente con

```
lst = [expression for item in iterable]
```



Por ejemplo, para obtener una lista de los cuadrados de los números del 1 al 14:

miscuadrados = []

for k in range(1,15):
    miscuadrados.append(k**2)

miscuadrados

miscuadrados2 = [k**2 for k in range(1,15)]
miscuadrados2

[k**2 for k in range(1,15) if k%2==1]

miscuadradosimpares = []

for k in range(1,15):
    if k%2==1:
        miscuadradosimpares.append(k**2)

miscuadradosimpares

Para contar las letras en una lista de palabras

frutas = ['apple','banana','carrot','grape','kiwi']

[len(palabra) for palabra in frutas]

### Caso con un condicional



A veces necesitamos además que se satisfaga alguna condición en la iteración, como con este código
```
lst = list()
for item in iterable:
    if conditional:
        lst.append(expression)
```

Esto puede hacer más sucintamente con

```
lst = [expression for item in iterable if conditional]
```



Por ejemplo, para generar los cuadrados de los números pares menores que 12

lista1 = list()

for k in range(1,12):
    if k % 2 == 0:
        lista1.append(k**2)

lista1

lista2 = [k**2 for k in range(1, 12) if not k%2]
lista2

## Operaciones con textos

diasemana = 'lunes'
dia = 30
mes = 'febrero'
año = 2020

"Hoy es %s %d de %s de %d" % (diasemana, dia, mes, año)

"Hoy es {0} {1} de {2} de {3}".format(diasemana, dia, mes, año)

f"Hoy es {diasemana.upper()} {dia-1} de {mes.title()} de {año}"

x = 1/7
x

f"x es igual a {x:15.5f}"