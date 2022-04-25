#!/usr/bin/env python
# coding: utf-8

# # Importando y manipulando datos con Python

# ## Ejemplo 1: Importando datos de Internet

# A menudo necesitamos darle seguimiento a algunos indicadores económicos. Este trabajo usualmente requiere:
# * visitar el sitio de Internet del proveedor de datos, 
# * buscar los indicadores requeridos, 
# * descargar los datos (posiblemente en varios archivos separados), 
# * copiar los datos a un solo archivo, 
# * acomodar los datos de manera apropiada, 
# * y solo después de que se hayan completado estas engorrosas tareas, graficarlos. 
# 
# Si este trabajo debe realizarse periódicamente entonces también se hace necesario documentar exhaustivamente cada uno de estos pasos, de manera que podamos replicarlos de manera exacta en un futuro. Sobra decir que, si estas tareas hay que realizarlas para múltiples indicadores, el trabajo termina demandando una cantidad de tiempo considerable y además es muy susceptible a errores.

# Para facilitar este trabajo, podemos utilizar Python para descargar datos disponibles en Internet directamente, gracias a paquetes como [pandas-datareader](https://pandas-datareader.readthedocs.io/en/latest/index.html). Esto se hace fácilmente cuando los proveedores de datos proporcionan una API (interfaz de programa de aplicación) que especifica cómo un lenguaje como Python puede encontrar los datos deseados.

# Vamos a ilustrar esto con un ejemplo. Supongamos que queremos datos recientes sobre el crecimiento económico para los países miembros de la CMCA. El Banco Mundial proporciona los datos pertinentes en su "World Database", que podemos leer con el módulo `wb` de `pandas_datareader`.

# In[1]:


import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt

pd.set_option('display.precision',2)
get_ipython().run_line_magic('matplotlib', 'inline')


# Para poder descargar datos del Banco Mundial, primero necesitamos saber el código exacto del indicador que queremos leer. La primera vez que hagamos esta tarea no conoceremos este código, pero podemos buscarlo en el sitio web del Banco Mundial o más fácilmente desde python. Por ejemplo, para encontrar datos sobre el PIB real per cápita, ejecutamos la función `.search()`:

# In[2]:


wb.search('gdp.*capita.*const')


# In[3]:


wb.search('gdp.*capita.*const').iloc[:,:2]


# donde el punto seguido de un asterisco `.*` indica que cualquier texto en esa posición es una coincidencia. Esta función devuelve una tabla de datos con información sobre indicadores que coinciden con los criterios de búsqueda. En la línea anterior, usamos el código `.iloc[:,:2]` para que Python solo imprima las dos primeras columnas de esa tabla.
# 
# Después de ejecutar esa búsqueda, elegimos el `'NY.GDP.PCAP.KD'`, cuya descripción es "GDP per capita (constant 2010 US\$)". Definimos una variable con una lista de códigos de país de los países del CMCA:

# In[4]:


paises = ['CR', 'DO', 'GT', 'HN', 'NI', 'SV']


# y procedemos a leer datos desde 1991:

# In[5]:


datos = wb.download(indicator='NY.GDP.PCAP.KD',
                    country=paises,start=1991, end=2019)

datos.head(7)


# In[6]:


datos


# También es posible leer datos de más de un indicador en una sola llamada a la función `wb.download()`, escribiendo sus códigos en una lista (tal como lo hicimos para leer datos de los seis países a la vez). En cualquier caso, obtenemos una tabla de datos en formato de panel, donde cada columna corresponde a uno de los indicadores.
# 
# Para nuestro ejemplo en particular, donde solo leemos un indicador, sería útil si la tabla estuviera organizada de manera que cada fila corresponda a un año y cada columna a un país. Podemos lograrlo con esta instrucción:

# In[7]:


paises2 = {'Costa Rica':'CR', 
           'Dominican Republic':'DO',
           'El Salvador':'SV',
           'Guatemala':'GT',
           'Honduras':'HN',
           'Nicaragua':'NI'}


# In[8]:


datos.unstack('country')


# In[9]:


datos.unstack('country').columns


# In[10]:


datos.unstack('country')


# In[11]:


GDP = datos.unstack('country')['NY.GDP.PCAP.KD']
GDP


# In[12]:


GDP.rename(columns=paises2, inplace=True)
GDP


# In[13]:


GDP.index = pd.period_range(start=GDP.index[0], periods=len(GDP.index),freq='A')


# Una vez que los datos se organizan de esta manera, es muy fácil calcular el crecimiento para todos los países en un solo paso:

# In[14]:


GDP.tail(6)


# In[15]:


GROWTH = 100 * GDP.dropna().pct_change()
GROWTH.tail()


# o para generar una tabla de datos formateada para ser incluida en un documento $\LaTeX$

# In[16]:


GROWTH.tail(6).round(2).to_latex('micuadro.tex')


# En la última instrucción, la parte `.tail(6)` indica que solo queremos las últimas seis observaciones, mientras que la parte `.to_latex('micuadro.tex')` exporta esa tabla a un archivo llamado *micuadro.tex*, que luego puede incluirse en un documento. El resultado de este código es

# In[17]:


print(open('micuadro.tex').read())


# Finalmente, graficamos los resultados. Es posible mejorar el aspecto estético de esta figura, por ejemplo, cambiando la posición de la leyenda. Tales mejoras no se presentan aquí por consideraciones de espacio.

# In[18]:


GROWTH.head()


# In[19]:


paises


# In[20]:


plt.style.use('seaborn');
GROWTH = GROWTH[paises]


# In[21]:


GROWTH[['GT','HN']]['2013':].plot(subplots=True)
plt.savefig('growth.pdf', bbox_inches='tight')


# In[22]:


plt.style.use('fivethirtyeight');
GROWTH.columns = paises
GROWTH[['GT','HN']]['2013':].plot(subplots=True)


# También es posible trazar cada una de las series de tiempo en un subgráfico separado, con la instrucción

# In[23]:


GROWTH.plot(subplots=True, layout=[2,3], sharey=True);
#plt.savefig('growth-subplots.pdf', bbox_inches='tight')


# donde hemos especificado que cada serie de tiempo debe trazarse por separado (`subplots=True`), organizarse en dos filas y tres columnas (`layout=[2,3]`), y todos los subgráficos deben tener el mismo eje "y" (`sharey=True`, para facilitar las comparaciones de países).

# Para ver cuáles estilos de gráficos están disponibles

# In[24]:


plt.style.available


# ## Ejemplo 2: Estimaciones econométricas

# El paquete `statsmodels` de Python permite la estimación de muchos tipos de modelos econométricos, aunque no tantos como se pueden estimar usando R. Una ilustración simple es la estimación de una función de consumo keynesiana,
# \begin{equation*}
# \ln(c_t) = \beta_0 + \beta_1 \ln(y_t) + \epsilon_t
# \end{equation*}
# 
# donde $c_t$ representa consumo, $y_t$ ingreso, $\epsilon$ un shock estocástico. En este caso $\beta_1$ corresponde a la elasticidad ingreso del consumo.
# 
# Al igual que en el ejemplo anterior, usaremos `pandas-datareader` para importar datos de Internet. En este ejemplo, también importamos la función `log()` del paquete `numpy` para calcular el logaritmo de los datos, así como el módulo `formula.api` de `statsmodels` para estimar el modelo.

# In[25]:


import pandas_datareader.data as web
from numpy import log
import statsmodels.formula.api as smf


# Una vez hecho esto, estamos listos para importar datos. En este ejemplo, utilizamos datos trimestrales sobre consumo y producción en los Estados Unidos, disponibles en [FRED](https://fred.stlouisfed.org/), una base de datos del Banco de la Reserva Federal de Saint Louis. Para “consumo” usamos la serie “PCEC” (Personal Consumption Expenditures), y para “ingreso” usamos “GDP” (Gross Domestic Product).

# In[26]:


usdata = web.DataReader(['PCEC','GDP'],'fred', 1947, 2018)


# In[27]:


usdata.tail()


# Después de ejecutar esta instrucción, la variable `usdata` apunta a una tabla de datos `pandas`, en la que cada columna corresponde a una variable y cada fila a un cuarto.
# 
# Ahora estimamos el modelo por mínimos cuadrados ordinarios (`.ols()`) e imprimimos un resumen de los resultados

# In[28]:


log(usdata).plot()


# In[29]:


mod = smf.ols('PCEC ~ GDP', log(usdata)).fit()
mod.summary()


# Observe que la función `.ols()` toma dos argumentos, la fórmula que especifica el modelo y el nombre de la tabla de datos que contiene las variables. En este bloque de código, especificamos los datos como `log(usdata)`, que le dice a Python que queremos el logaritmo de los datos, lo que nos ahorra la tarea de generar otra tabla de datos con los datos transformados de antemano (como sería necesario en, para ejemplo, Stata).
# 
# Alternativamente, esa línea también se puede escribir como
# ```
# mod = smf.ols('log(PCEC) ~ log(GDP)', usdata).fit()
# ```
# lo cual es conveniente en casos donde no todas las variables deben ser transformadas.

# Como se espera en una regresión de series de tiempo de tendencia, el estadístico $R^2$ es muy cercano a uno, y el estadístico de Durbin-Watson apunta a la alta posibilidad de autocorrelación en los residuos. Este documento no pretende ser una guía de mejores prácticas en econometría, pero consideremos un último modelo en el que el crecimiento del consumo depende del crecimiento del ingreso:
# 
# \begin{equation*}
# \Delta\ln(c_t) = \beta_0 + \beta_1 \Delta \ln(y_t) + \epsilon_t
# \end{equation*}
# 
# que estimamos en Python con

# In[30]:


smf.ols('PCEC ~ GDP', log(usdata).diff()).fit().summary()


# Notamos que ahora el $R^2$ ya no está cerca de uno, y que la estadística de Durbin-Watson está más cerca de 2.0, lo que indica falta de autocorrelación.
# 
# Con los resultados disponibles, podríamos predecir que un aumento de un punto porcentual (p.p.) en el crecimiento del PIB conduciría a un 0.618 p.p. aumento en el crecimiento del consumo. Sin embargo, dado que la muestra de datos cubre un período tan largo (casi 70 años de observación trimestral), es razonable preguntarse si los parámetros en este modelo son constantes, dado que podrían haber ocurrido varios cambios estructurales a lo largo de estos años. Una forma de evaluar dicha posibilidad es estimar el modelo con una muestra continua. En particular, vamos a estimar este modelo con 24 ventanas trimestrales de ventana móvil, cambiando la muestra en un cuarto en cada paso.
# 
# En este caso, dado que vamos a necesitar datos de crecimiento muchas veces, es más eficiente calcular los datos de crecimiento solo una vez y almacenarlos en una variable de 'crecimiento'. Con el código `[1:]` estamos eliminando la primera observación, que perdemos cuando calculamos la diferencia de primer orden `.diff()`. Además, usamos la propiedad `.shape` de la tabla para averiguar cuántas observaciones tenemos` T`, y luego establecemos el rango de ventana en observaciones `h = 24`:

# In[31]:


growth = (100*log(usdata).diff())[1:]
T, nvar = growth.shape
h = 40


# In[32]:


T /4


# Para facilitar el siguiente paso, definimos la función `window_beta1`, que toma como único argumento el número de la última observación que se incluirá en la estimación, y devuelve el valor del coeficiente estimado del PIB

# In[33]:


def window_beta1(k):
    submuestra = growth[k-h:k]
    return smf.ols('PCEC~GDP', submuestra).fit().params['GDP']


# In[34]:


window_beta1(81)


# Con esto, estamos listos para estimar el modelo muchas veces, agregando los resultados a la tabla de `growth` como el “indicador” `beta1`. Al graficar los resultados, obtenemos la siguiente figura, donde vemos claramente que el efecto del crecimiento del PIB en el crecimiento del consumo es bastante inestable y, por lo tanto, las predicciones hechas con el modelo simple podrían ser muy pobres.

# In[35]:


growth.loc[h-1:,'beta1'] = [window_beta1(k) for k in range(h,T+1)]
growth[['beta1']].plot()
#plt.savefig('dynamic-beta.pdf', bbox_inches='tight')


# ## Referencias
# 
# * Romero-Aguilar, Randall (2017). **[Python para economistas](http://www.secmca.org/NOTAS_ECONOMICAS/articulo93NOV2017.pdf)**. Nota Económica Regionales N0.93, diciembre. SECMCA. 
