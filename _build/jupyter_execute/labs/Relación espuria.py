#!/usr/bin/env python
# coding: utf-8

# # Regresión espuria

# Estos apuntes tienen por objetivo ilustrar el problema que surge de estimar modelos de regresión lineal con series de tiempo no estacionarias (regresión espuria).
# 
# En primer lugar, se estima una regresión en la que el PIB per capita de Costa Rica depende del de Malta (a priori, no esperaríamos que el PIB per capita de Malta tenga impacto en el de Costa Rica).  Más adelante, realizamos experimentos de Monte Carlo para analizar las consecuencias de estimar regresiones con datos no estacionarios.

# ## Preparación

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.api import OLS
from statsmodels.formula.api import ols

pd.set_option('display.float_format',lambda x: '%.2f' % x)
plt.style.use('seaborn')


# In[2]:


GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'


# Necesitamos importar una clase de un módulo local. Para ello, usualmente es suficiente con tener el módulo (archivo py) en la misma carpeta que este cuaderno, pero eso no funcionaría cuando se corre en Colab. Por ello, añadimos explícitamente la carpeta que contiene ese módulo en el path de Python.

# In[3]:


import sys
sys.path.insert(1, DATAPATH)
from mackinnon import MacKinnon  # este módulo contiene herramientas para calcular valores críticos de MacKinnon


# La función AEG acá definida realizará la prueba (aún no Aumentada) de Engle y Granger a partir de los residuos de una regresión

# In[4]:


mk = MacKinnon()

def AEG(residuals, N, summary=True):
    '''Prueba de cointegración de Engle y Granger'''
    aux = OLS(residuals.diff(), residuals.shift(1), missing='drop').fit()
    t = aux.tvalues[0]
    nobs = aux.nobs
    
    crit = mk('c', N, T=nobs)
    
    if summary:
        print('Prueba de cointegración de Engle y Granger')
        print('ADF stat = %.3f\nCritical values:' % t)
        for k, v in crit.items():
            print('\t%5s: %.3f' % (k,v))
        if t < crit['1%']:
            print('Series están cointegradas (al 1% significancia)')
        elif t < crit['5%']:
            print('Series están cointegradas (al 5% significancia)')
        elif t < crit['10%']:
            print('Series están cointegradas (al 10% significancia)')
        else:
            print('Series no están cointegradas')
    return t
       


# ## Regresión con datos de Costa Rica y de Malta
# 
# Los datos los obtenemos directamente del Banco Mundial, usando el paquete `wbdata`. Las líneas importantes son:
# 
#     import wbdata
#     df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)
# 
# El resto del código da la opción de abrir datos previamente guardados en el directorio.

# In[5]:


data_file_name = 'datos-CRI-MLT.pickle'
update_data = False

if update_data:
    try:
        import wbdata
        countries = ["MLT", "CRI"]
        indicators = {'NY.GDP.PCAP.KD':'GDP per capita (constant 2010 US$)'}
        df = wbdata.get_dataframe(indicators, country=countries, convert_date=False)
        data = df.unstack(level=0)['GDP per capita (constant 2010 US$)']
        data.rename(columns={'Costa Rica':'CRI', 'Malta':'MLT'}, inplace=True)
        data.to_pickle(data_file_name)
        print('Downloaded data from World DataBank\nData saved to %s.' % data_file_name)
    except:
        data = pd.read_pickle(DATAPATH + data_file_name)
        print('Could not download data from World DataBank\nData read from %s.' % data_file_name)
else:
    data = pd.read_pickle(DATAPATH + data_file_name)
    print('Reading data from %s.' % data_file_name)


# Cargados los datos, los graficamos y mostramos las últimas 8 observaciones en una tabla.

# In[6]:


data.plot()
data.tail(8)


# Los datos originales están en niveles. Para la regresión
# $$ \log(CRI) = c + \log(MLT) + \epsilon $$ 
# 
# se necesita calcular el logaritmo de cada serie. Acá simplemente hacemos una base nueva `ldata` a partir de la original.

# In[7]:


ldata = np.log(data)


# Ahora sí, estimamos la regresión con el función `ols`. Nótese que según los resultados, un aumento de un punto porcentual en el PIB de Malta está asociado con una disminución de 0.4494 pp en Costa Rica; el resultado es estadísticamente significativo. 

# In[8]:


model = ols('CRI ~ MLT',ldata)
resultados = model.fit()
resultados.summary()


# In[9]:


print(resultados.summary())


# Ahora bien, observe que los residuos no parecen ser ruido blanco.

# In[10]:


resultados.resid.plot()


# Esto lo podemos confirmar con la prueba de Dickey y Fuller. Dado que al parecer los residuos tienen raíz unitaria, podemos inferir que el PIB de Costa Rica **no está cointegrado** con el de Malta.

# In[11]:


t=AEG(resultados.resid, 2)


# Ahora bien, nótese que el problema de regresión espuria (casi) desaparece una vez corremos la regresión con series estacionarias (en este caso, el crecimiento en cada país).

# In[12]:


modeldiff = ols('CRI ~ MLT',ldata.diff())
modeldiff.fit().summary()


# In[13]:


print(modeldiff.fit().summary())


# ## Simulación de datos
# 
# Ahora, vamos a definir una función para simular dos caminatas aleatorias con intercepto, calibradas con la media y la desviación estándar del crecimiento en ambos países.

# In[14]:


growth = ldata.diff().mean() 
print('El crecimiento medio es:')
print(growth)

sigma = ldata.diff().std()
print('\ny las respectivas volatilidades son:')
print(sigma)


# Para las simulaciones, fijamos el tamaño de muestra en `T=48`. Observe que las dos series que se crean son independientes.

# In[15]:


T = 48
calendario = pd.date_range(start='1970',freq='A',periods=T)

def generate_series():
    X = np.ones((T,2))
    
    for t in range(1, T):
        X[t] = X[t-1] + growth + sigma * np.random.randn(2)
    
    return pd.DataFrame(X,index=calendario, columns=['MLT','CRI'])


# Aquí simulamos el proceso una vez para ver que parezca razonable.

# In[16]:


datos_simulados = generate_series()
datos_simulados.plot(figsize=[12,6])


# In[17]:


resultados_simulados = ols('CRI ~ MLT',datos_simulados).fit().summary()
resultados_simulados


# ## Monte Carlo

# In[18]:


from joblib import Parallel, delayed

def Monte_Carlo(funcion, repeticiones, columnas, *args, **kwargs):
    """
    Ejecuta simulaciones de Montecarlo en paralelo, aprovechando todos los núcleos del procesador

    Argumentos:
        funcion: una función que dé por resultado una única realización de las cantidades que se desean simular
        repeticiones: un entero que indica cuántas muestras se desean simular
        columnas: una lista (o tupla) de strings, que identifiquen a las cantidades individuales retornadas por funcion
        *args, **kwargs: otros parámetros requeridos por funcion

    Retorna:
         Un data frame de pandas, con tantas filas como `repeticiones` y columnas como textos en `columnas`.
    """
    datos = Parallel(n_jobs=-1)(delayed(funcion)(*args, **kwargs) for _ in range(repeticiones))
    return pd.DataFrame(datos, columns=columnas)


# Para la simulación de Monte Carlo, veremos el parámetro asociado con MLT, así como su estadístico *t* y el valor *p*. Para facilitar la labor, definimos una función que extrae estos tres estadísticos de los resultados de una regresión y los retorna como una lista. Añadimos ademas el *p-value* de la prueba aumentada de Dickey-Fuller respecto a si los residuos de la regresión presentan raices unitarias.

# In[19]:


def give_me_the_summary(res):
    statistics = ['params', 'tvalues', 'pvalues']
    tval = AEG(res.resid, 2,False)
    return [getattr(res, k)['MLT'] for k in statistics] + [tval]


# Para cada iteración del experimento de Monte Carlo, generamos una nueva muestra con `generate_series()`, luego estimamos el modelo con los datos en niveles (resultados en `rl`) y en primeras diferencias (`rd`). Retornamos los seis estadísticos correspondientes.
# 
# Recuerde que, por construcción, las series en primera diferencia sí son estacionarias.

# In[20]:


def simulate_regression():
    data = generate_series()
    rl = ols('CRI ~ MLT', data).fit()
    rd = ols('CRI ~ MLT', data.diff()).fit()
    return give_me_the_summary(rl) + give_me_the_summary(rd)


# Fijamos el número de repeticiones en `nrep=1000` y creamos una tabla (`pd.DataFrame`) con los resultados de todas las simulaciones.

# In[21]:


get_ipython().run_cell_magic('time', '', "\nnrep = 10000 # number of repetitions\nmontecarlo = Monte_Carlo(simulate_regression, nrep, columnas=pd.MultiIndex.from_product([['LEVEL','DIFF'], ['coeff','t-stat', 'p-value', 'tvalue-res']]))")


# Finalmente, analizamos la distribución de cada uno de los estadísticos bajo consideración.

# In[22]:


ax = montecarlo.swaplevel(axis=1).hist(layout=(4,2), figsize=[12,12],bins=20)
mk('c', 2, T)


# Puede verse para las regresiones en niveles, siempre encontramos una asociación positiva y estadísticamente significativa entre las dos series, a pesar de que son independientes! En contraste, cuando las regresiones se realizan con datos estacionarios (primeras diferencias), rutinariamente rechazaríamos la hipótesis de que el PIB de Malta está correlacionado con el de Costa Rica.
