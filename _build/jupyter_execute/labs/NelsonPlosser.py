#!/usr/bin/env python
# coding: utf-8

# # Replicando el trabajo de Nelson y Plosser (1982)

# En un artículo muy citado
# 
# * Nelson y Plosser 1982 **Trends and Random Walks in Macroeconomic Time Series: Some evidence and implications**. Journal of Monetary Economics 10, pp.139-162
# 
# los autores examinan varias series macroeconómicas de uso común.  
# 
# Usando pruebas de Dickey-Fuller, encontraron que todas las series macroeconómicas contienen raíces unitarias, o más correctamente, que no podían rechazar  la hipótesis nula de un raíz unitaria.
# 
# En esta parte del laboratorio replicamos algunos de los resultados de Nelson y Plosser.

# ## Preparación

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf, kpss
from statsmodels.formula.api import ols


# ## Leer los datos y visualizarlos

# In[2]:


GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'


# In[3]:


datos = pd.read_stata(DATAPATH + 'NelsonPlosserData.dta')
datos.set_index('year',inplace=True)
datos.index = datos.index.year


# In[4]:


titulos = [f'r{i}' for i in range(1,7)] # para rotular unas tablas abajo


# In[5]:


variables = {'lrgnp':'Real GNP',
           'lgnp':'Nominal GNP',
           'lpcrgnp':'Real per capita GNP',
           'lip':'Industrial production',
           'lemp':'Employment', 
           'lun':'Unemployment rate',
           'lprgnp':'GNP deflator',
           'lcpi':'Consumer prices',
           'lwg':'Wages',
           'lrwg':'Real wages', 
           'lm':'Money stock', 
           'lvel':'Velocity',
           'bnd':'Bond yield',
           'lsp500':'Common stock prices'}


# In[6]:


datos = datos[variables.keys()].rename(columns=variables)
datos.plot(subplots=True, figsize=[15,15], layout=[-1,3]);


# ## Calculando autocorrelaciones
# 
# ![Nelson Plosser 1982 tabla 2](../imgs/NelsonPlosser-table2.png)
# * Fuente: Nelson y Plosser 1982 Trends and Random Walks in Macroeconomic Time Series: Some evidence and implications. Journal of Monetary Economics 10, pp.139-162

# In[7]:


def acf6lags(nombre_variable, d):
    """
    Calcula los primeros 6 coeficientes de autocorrelación
    
    Args:
        nombre_variable: str, el nombre de una columna de la tabla "datos"
        d: número de veces que hay que diferenciar la serie (0 o 1 en la práctica)

    Returns:
        np.array, los 6 coeficientes de autocorrelación, redondeados a dos decimales
    """
    serie = datos[nombre_variable].diff(d) if d>0 else datos[nombre_variable]
    return acf(serie.dropna(), nlags=6, fft=False)[1:].round(2)


# In[8]:


def tabla_acf(d):
    """
    Crea una tabla con las primeras 6 autocorrelaciones de todas las series en "datos"

    Args:
        d:  int, número de veces que hay que diferenciar la serie (0 o 1 en la práctica)

    Returns:
        una tabla de pandas, series en las filas, número de rezagos en las columnas
    """
    return pd.DataFrame([acf6lags(serie,d) for serie in datos], index=variables.values(), columns=titulos)


# ### Serie en nivel

# In[9]:


tabla2 = tabla_acf(0)
tabla2


# In[10]:


def rango_datos(ser):
    """
    Determina el rango de los datos disponibles de una serie
    Args:
        ser: una serie de pandas

    Returns:
        str, primera observación -- última observación
    """
    return f'{ser.first_valid_index()} -- {ser.last_valid_index()}'


# In[11]:


datos.apply(rango_datos)


# In[12]:


tabla2.insert(0,'Period', datos.apply(rango_datos))
tabla2.insert(1, 'T', datos.apply(lambda ser: ser.dropna().count()))
tabla2


# ### Serie en primera diferencia
# 
# ![Nelson Plosser 1982 tabla 3](../imgs/NelsonPlosser-table3.png)
# * Fuente: Nelson y Plosser 1982 Trends and Random Walks in Macroeconomic Time Series: Some evidence and implications. Journal of Monetary Economics 10, pp.139-162

# In[13]:


tabla3 = tabla_acf(1)
tabla3.insert(0,'Period', datos.apply(rango_datos))
tabla3.insert(1, 'T', datos.apply(lambda ser: ser.dropna().count()))
tabla3


# ### Desviaciones respecto a una tendencia lineal
# 
# ![Nelson Plosser 1982 tabla 4](../imgs/NelsonPlosser-table4.png)
# * Fuente: Nelson y Plosser 1982 Trends and Random Walks in Macroeconomic Time Series: Some evidence and implications. Journal of Monetary Economics 10, pp.139-162

# In[14]:


def acf_deviation_from_trend(nombre_variable):
    """
    Calcular las primeras 6 autocorrelaciones de la desviación de una serie respecto a 
    su tendencia lineal.
    
    Se estima por mínimos cuadrados ordinarios una regresión de la forma
        y = intercepto + time
    
    y se calcula la autocorrelación de los residuos.
    Args:
        nombre_variable: str, nombre de una variable de la tabla "datos" 

    Returns:
        np.array, los 6 coeficientes de autocorrelación, redondeados a dos decimales
    """
    temp = datos[[nombre_variable]].dropna()
    temp.columns = ['y']
    temp['t'] = np.arange(temp.shape[0]) 
    resid = ols('y ~ t', temp).fit().resid
    return acf(resid, nlags=6, fft=False)[1:].round(2)


# In[15]:


tabla4 = pd.DataFrame([acf_deviation_from_trend(ser) for ser in datos], index=variables.values(), columns=titulos)
tabla4.insert(0,'Period', datos.apply(rango_datos))
tabla4.insert(1, 'T', datos.apply(lambda ser: ser.dropna().count()))
tabla4


# ### Mostrar las tablas 2 a 4 en una sola

# In[16]:


pd.concat([tabla2, tabla3, tabla4], axis=1)


# In[17]:


pd.concat([tabla2, tabla3.iloc[:,-6:], tabla4.iloc[:,-6:]], axis=1, keys=['Niveles','Diferencias','Desviación de tendencia'])


# ## Estimar la regresión Dickey-Fuller, "a pie"
# 
# ![Nelson Plosser 1982 tabla 5](../imgs/NelsonPlosser-table5.png)
# * Fuente: Nelson y Plosser 1982 Trends and Random Walks in Macroeconomic Time Series: Some evidence and implications. Journal of Monetary Economics 10, pp.139-162

# ![Levendis tabla 7.5](../imgs/Levendis-table7-5.png)
# * Fuente: Levendis 2018 Time Series Econometrics: Learning Through Replication. Springer

# In[18]:


def ADFregression(nombre_variable, k):
    """
    Estima la regresión necesaria para la prueba aumentada de Dickey-Fuller
    Args:
        nombre_variable: str, nombre de una variable de la tabla "datos"
        k: Número de rezagos del proceso AR subyacente (1 + rezagos en regresión)

    Returns:
        Un objeto de resultados estimados de statsmodels
    """
    temp = datos[[nombre_variable]].dropna()
    temp.columns=['Y']
    temp['DY'] = temp['Y'].diff()
    temp['LY'] = temp['Y'].shift()
    temp['t'] = np.arange(temp.shape[0])    
    for j in range(1, k):
        temp[f'D{j}Y'] = temp['DY'].shift(j)
        regresores = ' + '.join(temp.columns[2:])
    print(regresores)
    frml = 'DY ~ ' + regresores
    return ols(frml, temp).fit()
    


# In[19]:


ADFregression('Real GNP', 4).summary()


# In[20]:


def NelsonPlosser(ser, k):
    """
    Calcula varios estadísticos de la regresión de la prueba aumentada de Dickey-Fuller, 
    para reproducir los resultados reportados en la tabla 5 de Nelson y Plosser (1982)
    
    Args:
        ser: str, nombre abreviado de una variable de la tabla "datos"
        k: Número de rezagos del proceso AR subyacente (1 + rezagos en regresión)

    Returns:
        dict, estadísticos calculados        
    """
    nombre_variable = variables[ser]
    fuller5pct = -3.45
    model = ADFregression(nombre_variable, k)
    
    estadisticos = {
        'mu': np.round(model.params['Intercept'], 3),
        't(mu)': np.round(model.tvalues['Intercept'], 2),
        'gamma': np.round(model.params['t'], 3),
        't(gamma)': np.round(model.tvalues['t'], 2),
        'rho': np.round(model.params['LY'] + 1, 3),
        't(rho)': np.round(model.tvalues['LY'], 2),
        's(u)': np.round(np.sqrt(model.mse_resid),3),
        'r1': acf(model.resid, nlags=1, fft=False)[1].round(2),
        'resultado': '* estacionaria' if model.tvalues['LY'] < fuller5pct else 'raiz unitaria'
    }
    
    return estadisticos
    


# In[21]:


NelsonPlosser('lrgnp', 3)


# In[22]:


rezagos = {'lrgnp':2, 'lgnp':2, 'lpcrgnp':2,'lip':6, 'lemp':3, 'lun':4, 'lprgnp':2, 'lcpi':4, 'lwg':3, 'lrwg':2, 'lm':2, 'lvel':4,'bnd':3,'lsp500':3}


# In[23]:


tabla5 = pd.DataFrame([NelsonPlosser(ser, lags) for ser, lags in rezagos.items()], index=rezagos.keys())
tabla5


# **NOTA:** Una versión anterior de este archivo tenía la réplica del trabajo de KPSS. Ese código ahora está en el cuaderno KPSS.ipynb.
