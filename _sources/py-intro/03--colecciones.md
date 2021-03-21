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

(py-sec-colecciones)=
# Colecciones

Los tipos de colecciones más utilizados son

* `list` una lista ordenada y mutable de valores
* `tuple` una lista ordenada e inmutable de valores
* `set` una lista mutable pero no ordenada de valores
* `dict` un diccionario no ordenado

## Listas

### Haciendo listas
Para hacer una lista, enumeramos sus elemento entre un par de ```[ ]```

```{code-cell} ipython3
seasons = ['Spring', 'Summer','Autumn','Winter']
seasons
```
![seasons](figures/list-diagram.png)


Las listas pueden tener elementos heterogéneos

```{code-cell} ipython3
mylist = [4, 3.0, 'abc', 5, 8, -3, 0 , 2]
mylist
```

### Para obtener los datos:

```{code-cell} ipython3
seasons[2]
```

```{code-cell} ipython3
seasons[-3]
```

### Para modificar los datos:

```{code-cell} ipython3
seasons[2] = 'Fall'
seasons
```

### *Slicing*

Para obtener una franja de datos:

```{code-cell} ipython3
mylist
```

```{code-cell} ipython3
mylist[2:4]
```

```{code-cell} ipython3
mylist[:3]
```

```{code-cell} ipython3
mylist[5:]
```

```{code-cell} ipython3
mylist[-2:]
```

```{code-cell} ipython3
mylist[3:4] # a pesar de que es un solo elemento, retorna una lista
```

```{code-cell} ipython3
mylist[3]
```

```{code-cell} ipython3
mylist[3:3]
```

```{code-cell} ipython3
mylist[::2]
```

```{code-cell} ipython3
mylist[1::2]
```

### Copiando una lista

- `nueva_lista = vieja_lista` hace una variable nueva que apunta a la misma lista que la lista anterior:

```{code-cell} ipython3
otralista = mylist
otralista
```

```{code-cell} ipython3
otralista[0] = 99999
otralista
```

```{code-cell} ipython3
mylist
```

Vemos que es la misma lista al comparar sus `id`:

```{code-cell} ipython3
print(id(otralista), id(mylist),sep='\n')
```

```{code-cell} ipython3
otralista is mylist
```

- `nueva_lista = vieja_lista.copy()` hace una copia *independiente* de la original:

```{code-cell} ipython3
copialista = mylist.copy()
copialista[-1] = 'copia independiente de la original'
print('copialista = ', copialista)
print('mylist     = ', mylist)
print('otralista  = ', mylist)
print(f'copialista es {id(copialista)}',  f'mylist     es {id(mylist)}', f'otralista  es {id(otralista)}',  sep='\n')
```

### Manipulando listas

```{code-cell} ipython3
fruit = ['apple','orange','grape','kiwi']
```

#### ```list.append(x)``` Agrega el elemento ```x``` al final de la lista

```{code-cell} ipython3
fruit.append('apple')
fruit
```

#### ```list.extend(L)``` Agrega todos los elementos de la lista ```L``` al final de la lista

```{code-cell} ipython3
fruit.extend(['mango','banana','kiwi'])
fruit
```



#### ```list.insert(i,x)``` Inserta el elemento ```x``` en la posición de índice ```i```

```{code-cell} ipython3
fruit.insert(2,'guava')
fruit
```



#### ```len(list)``` cuenta el número de elementos de la lista

```{code-cell} ipython3
len(fruit)
```



#### ```list.remove(x)``` Elimina el primer elemento ```x``` de la lista

```{code-cell} ipython3
fruit.remove('kiwi')
fruit
```



#### ```list.pop(i)``` Eliminina el elemento en la posición ```i``` y lo retorna

```{code-cell} ipython3
fruit.pop()
fruit
```



#### ```list.index(x)``` Retorna el índice del primer elemento ```x``` de la lista

```{code-cell} ipython3
fruit.index('grape')
```



#### ```list.count(x)``` Retorna el número de veces que aparece ```x``` en la lista

```{code-cell} ipython3
fruit.count('apple')
```



#### ```list.sort()``` Ordena todos los elementos de la lista, in situ

```{code-cell} ipython3
fruit.sort()
fruit
```


#### ```list.reverse()``` Revierte el orden de todos los elementos de la lista, in situ

```{code-cell} ipython3
fruit.reverse()
fruit
```

```{code-cell} ipython3
fruit.sort(reverse=True)
```

## Tuplas

Una tupla es similar a una lista, pero una vez que se define **sus elementos no pueden cambiarse**. Se define enumerando sus elementos entre un par de  ```( )```

```{code-cell} ipython3
seasons = ('Spring', 'Summer','Autumn','Winter')
```

![seasons](figures/tuple-diagram.png)

Para obtener datos:

```{code-cell} ipython3
seasons[2]
```

```{code-cell} ipython3
seasons[-3]
```



Sin embargo, los datos no se pueden modificar

```{code-cell} ipython3
:tags: ["raises-exception"]
seasons[2] = 'Fall'
```

Las tuplas también entienden de franjas

```{code-cell} ipython3
M = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', \
'Jul','Aug','Sep','Oct','Nov','Dec')
M
```

```{code-cell} ipython3
# To split the months into quarters:
Q1, Q2, Q3, Q4 = M[:3], M[3:6], M[6:9], M[9:]
Q2
```

Para hacer una tupla de un único elemento:

```{code-cell} ipython3
solo = (55, )
```

```{code-cell} ipython3
type(solo)
```

## Conjuntos
Para hacer un conjunto, enumeramos sus elementos entre ```{ }```. Alternativamento, transformamos una lista en un conjunto usando la función ```set```.

### Operaciones con conjuntos

```{code-cell} ipython3
M2 = {2, 4, 6, 8, 10, 12, 14}
M3 = set([3, 6, 9, 12, 15])
```

#### ```set.add(x)``` Agrega un elemento ```x``` al conjunto

```{code-cell} ipython3
M2.add(16)
M2
```

#### ```set.update([x,y,z])``` Agrega varios elementos al conjunto

```{code-cell} ipython3
M3.update([18, 21])
M3
```

#### ```set.copy()``` Retorna una copia del conjunto

```{code-cell} ipython3
M2c = M2.copy()
M2c
```


#### ```set.pop()``` Elimina al azar un elemento del conjunto

```{code-cell} ipython3
M2c.pop()
```

```{code-cell} ipython3
M2c
```

#### ```set.discard(x)``` Elimina el elemnto ```x``` del conjunto (si es miembro)

```{code-cell} ipython3
M2c.discard(10)
M2c
```

#### ```set1.union(set2)``` Retorna elementos que aparecen en cualquiera de los conjuntos

```{code-cell} ipython3
M2.union(M3)
```



#### ```set1.intersection(set2)``` Retorna elementos que aparecen en los dos conjuntos

```{code-cell} ipython3
M3.intersection(M2)
```

#### ```set1.difference(set2)``` Retorna elementos del conjunto ```set1``` que no estén en ```set2```

```{code-cell} ipython3
M2.difference(M3)
```

#### ```set1.isdisjoint(set2)``` True si los conjuntos no tienen elementos en común

```{code-cell} ipython3
M2.isdisjoint(M3)
```

## Diccionarios
* En Python un “diccionario” es un contenedor de datos que puede almacenar múltiples elementos de datos como una lista de pares `llave:valor`.
* A diferencia de las listas y tuplas, cuyos datos se obtienen por referencia a su índice, los valores almacenados en un diccionario se obtienen por referencia a su llave.
* La llave debe ser única en el diccionario, usualmente se una un texto aunque también puede usarse números.

```{code-cell} ipython3
king = {'name': 'John Snow',
        'age': 24,
        'home': 'Winterfell'}

king
```



Los diccionarios se pueden crear con la función ```dict```:

```{code-cell} ipython3
friend = dict(name='Samwell Tarly', age=22)
friend
```

Obteniendo datos

```{code-cell} ipython3
king['age']
```

Modificando datos:

```{code-cell} ipython3
king['home'] = 'Castle Black'
king
```

Agregando datos:

```{code-cell} ipython3
king['lover'] = 'Ygritte'
king['knows'] = None
king
```

Borrando datos:

```{code-cell} ipython3
del king['lover'] # killed by Olly!
king
```

Para almacenar un texto muy largo, podemos encerrarlo en triples comillas dobles:

```{code-cell} ipython3
king['lover'] = """Daenerys Stormborn of the House Targaryen, First of Her Name,
The Unburnt, Queen of the Andals and the First Men, Khaleesi of the Great Grass Sea,
Breaker of Chains, and Mother of Dragons"""

print(king['lover'])
```
