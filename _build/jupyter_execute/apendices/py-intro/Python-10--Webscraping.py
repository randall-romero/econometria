#!/usr/bin/env python
# coding: utf-8

# # Web scraping con BeautifulSoup
# 
# En este script hacemos una pequeña introducción al uso de BeautifulSoup para extraer datos de una página HTML.
# 
# 
# En ocasiones deseamos trabajar con datos que están dispersos en páginas HTML.
# 
# En este ejemplo mostramos cómo obtener datos de precios de libros del sitio web de una librería ficticia
# 
#     http://books.toscrape.com/
# 
# Para cada uno de los libros en venta en este sitio, deseamos saber lo siguiente:
#     - título
#     - precio
#     - disponibilidad
#     - rating
# 

# In[1]:


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

URL_LIBROS = 'http://books.toscrape.com/catalogue/'


# Esta funciones nos ayudará a convertir los datos a pandas

# In[2]:


def extraer_info(articulo):
    """
    La información de cada libro viene contenida en una etiqueta "article", como en este ejemplo

    <article class="product_pod">
      <div class="image_container">
        <a href="a-light-in-the-attic_1000/index.html"><img alt="A Light in the Attic" class="thumbnail" src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/>
        </a>
         <p class="star-rating Three">
           <i class="icon-star"/>
           <i class="icon-star"/>
           <i class="icon-star"/>
           <i class="icon-star"/>
           <i class="icon-star"/>
         </p>
         <h3>
           <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
         </h3>
         <div class="product_price">
           <p class="price_color">£51.77</p>
           <p class="instock availability">
           <i class="icon-ok"/>

                        In stock

           </p>
           <form>
             <button class="btn btn-primary btn-block" data-loading-text="Adding..." type="submit">Add to basket</button>
           </form>
         </div>
       </div>
    </article>


    Esta función extrae el título, precio, disponibilidad y rating y lo devuelve como una tupla.

    """
    titulo = articulo.h3.a['title']
    precio = articulo.find('p', attrs=['price_color']).get_text()[1:]
    disponible = articulo.find('p', attrs=['instock availability']).get_text().strip()
    rating = articulo.find('p', attrs=[re.compile('star-rating ([A-Za-z]+)')])['class']
    return (titulo, precio, disponible, rating.split()[1])

def procesar_pagina(n):
    """
    Procesa la página número "n" del sitio http://books.toscrape.com/

    Devuelve un dataframe de pandas con columnas título, precio, disponibilidad y rating,
    donde cada fila corresponde a un libro.
    """

    with urlopen(URL_LIBROS + f'page-{n}.html') as archivo:
        soup = BeautifulSoup(archivo, 'xml', from_encoding='UTF-8')
        datos_crudos = [extraer_info(articulo) for articulo in soup.findAll('article')]
        return pd.DataFrame(datos_crudos, columns=('Título', 'Precio', 'Disponibilidad', 'Rating'))


# ## Procesar toda la librería

# In[3]:


datos = pd.concat([procesar_pagina(n) for n in range(1, 51)], ignore_index=True)


# Convertir datos de precio a tipo numérico

# In[4]:


datos['Precio'] = datos['Precio'].astype(float)


# Información de la tabla de datos

# In[5]:


datos.info()


# Descripción de las columnas numéricas

# In[6]:


datos.describe()


# ¿Son más caros los libros mejor calificados?

# In[7]:


print("Precio por rating", datos.groupby('Rating')['Precio'].mean(), sep='\n\n')


# Convirtamos los datos de Rating a Categorías

# In[8]:


datos['Rating'] = pd.Categorical(datos['Rating'], categories=('One', 'Two', 'Three', 'Four', 'Five'), ordered=True)

print("Precio por rating, ya ordenados", datos.groupby('Rating')['Precio'].mean(), sep='\n\n')

