#!/usr/bin/env python
# coding: utf-8

# # Replicando el trabajo de KPSS (1992)

# El test KPSS fue propuesto en
# 
# * Kwiatkowski, Phillips, Schmidt y Shin 1992 **Testing the null hypothesis of stationarity against the alternative of a unit root**. Journal of Econometrics 54, pp.159-178.
# 
# La idea del test es que las pruebas de Dickey-Fuller, al tener muy poca potencia para series persistentes pero sin raíz unitaria, terminan diagnosticando que muchas más series tienen raíz unitaria de las que efectivamente las tienen.
# 
# KPSS proponen una prueba en la que la hipótesis nula es que *la serie es estacionaria*.
# 
# Los autores estudian las mismas series que Nelson y Plosser, y llegan a resultados distintos.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import kpss


# ## Leer los datos y visualizarlos

# ### Definir ubicación de archivos de datos

# In[2]:


GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'


# In[3]:


datos = pd.read_stata(DATAPATH + 'NelsonPlosserData.dta')
datos.set_index('year',inplace=True)


# In[4]:


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


# In[5]:


datos = datos[variables.keys()].rename(columns=variables)
datos.plot(subplots=True, figsize=[15,15], layout=[-1,3]);


# ![KPSS tabla 5](KPSS-table5.png)

# ## Calculando los resultados de las pruebas

# In[6]:


def KPSS_una_serie(nombre_variable, tipo):
    """
    Calcula los estadísticos LM de la prueba de estacionariedad KPSS, con rezagos de 0 a 8
     
    Args:
        nombre_variable: str, el nombre de una columna de la tabla "datos"
        tipo: str, tipo de prueba a realizar, "c" o "ct"

    Returns:
        np.array, los 9 estadísticos LM estimados
    """
    return [kpss(datos[nombre_variable].dropna(), regression=tipo, lags=k)[0] for k in range(9)]   


# In[7]:


KPSS_una_serie('Real GNP', 'c')


# In[8]:


def KPSS(tipo):
    """
    Calcula los estadísticos LM de la prueba de estacionariedad KPSS, con rezagos de 0 a 8, para
    todas las series de la tabla "datos"
     
    Args:
        tipo: str, tipo de prueba a realizar, "c" o "ct"

    Returns:
        pd.DataFrame, series en filas, número de rezagos en columnas
    """    
    return pd.DataFrame([KPSS_una_serie(ser, tipo=tipo) for ser in variables.values()], index=variables.values())


# In[9]:


get_ipython().run_cell_magic('capture', '', "tabla5_kpss = pd.concat([KPSS('c'), KPSS('ct')], keys=['c', 'ct']).round(3)")


# In[10]:


tabla5_kpss


# ## Añadiendo asteriscos para indicar significancia de la prueba

# In[11]:


critical = pd.DataFrame(
    {'c': np.array([0.347, 0.463, 0.574, 0.739]),
     'ct':np.array([0.119, 0.146, 0.176, 0.216])},
    index=['10%', '5%', '2.5%', '1%'])

formatos = {'c':'%.2f', 'ct':'%.3f'}


# In[12]:


critical


# In[13]:


def significancia(v, tipo):
    """
    Contar cuántos valores críticos KPSS fueron superados por un estimado 
    Args:
        v: float, el estadístico LM estimado de una prueba KPSS
        tipo: str, tipo de prueba realizada, "c" o "ct"

    Returns:
        int: 4 (signficativa al 1%), 3 (signficativa al 2.5%), 2 (signficativa al 5%), 
             1 (signficativa al 10%), 0 (no signficativa al 10%)
    """
    return (v > critical[tipo]).sum()


# In[14]:


def estrellas(v, tipo):
    """
    Escribir coeficiente LM de prueba KPSS con estrellas de significancia:
    **** (signficativa al 1%), ***_ (signficativa al 2.5%), **__ (signficativa al 5%), 
    *___ (signficativa al 10%), ____ (no signficativa al 10%)
    
    Args:
        v: float, el estadístico LM estimado de una prueba KPSS
        tipo: str, tipo de prueba realizada, "c" o "ct"

    Returns:
        str, coeficiente LM con *** (variable, según significancia)
    """
    ns = significancia(v, tipo)
    return (formatos[tipo] % v) + '*' * ns + ' '*(4-ns)


# In[15]:


estrellas(0.15, 'c')


# In[16]:


def KPSS_tabla(tipo):
    """
    Replica la tabla 5 del artículo de KPSS, mostrando resultados de pruebas de estacionariedad
    aplicadas a las series de Nelson y Plosser (1982)
    
    Args:
        tipo: str, tipo de prueba realizada, "c" o "ct"

    Returns:
        pd.DataFrame, series en filas, número de rezagos en columnas, pero resultados
        son strings anotados con asteriscos de significancia
    """
    return KPSS(tipo).applymap(lambda x: estrellas(x,tipo))


# In[17]:


get_ipython().run_cell_magic('capture', '', "tabla5_kpss_star = pd.concat([KPSS_tabla('c'), KPSS_tabla('ct')], keys=['c', 'ct']).round(3)")


# In[18]:


tabla5_kpss_star


# ## Visualizando los resultados con un mapa de calor

# In[19]:


def KPSS_heatmap(tipo, ax):
    """
    Crea un mapa de calor (heatmap) para visualizar los resultados de la tabla 5 de KPSS
     
    Args:
        tipo: str, tipo de prueba realizada, "c" o "ct"
        ax: axis de matplotlib.pyplot, eje cartesiano donde se grafican los resultados

    Returns:
        una imagen. La figura queda dibujada en el parámetro ax
    """
    tabla = KPSS(tipo).applymap(lambda x: significancia(x, tipo))
    return ax.imshow(tabla, cmap='Blues', aspect='auto')


# In[20]:


def KPSS_heatmap(tipo, ax):
    tabla = KPSS(tipo).applymap(lambda x: significancia(x, tipo))
    return ax.imshow(tabla, cmap='Blues', aspect='auto')


# In[21]:


get_ipython().run_cell_magic('capture', '', "fig, axs = plt.subplots(1,2, figsize=[16,6], sharey=True)\nim0 = KPSS_heatmap('c', axs[0])  #axs[0].imshow(tabla_kpss_c, cmap='Blues', aspect='auto')\nim1 = KPSS_heatmap('ct', axs[1]) #axs[1].imshow(tabla_kpss_ct,cmap='Blues', aspect='auto')\n\naxs[0].set(\n    title='Estacionaria alrededor de una media',\n    xlabel='rezagos', \n    yticks=np.arange(len(variables)), \n    yticklabels=[''] * len(variables));\n\naxs[1].set(\n    title='Estacionaria alrededor de una tendencia',\n    xlabel='rezagos',\n    yticks=np.arange(len(variables)), \n    yticklabels=variables.values());\n    \nfor ax in axs:\n    ax.vlines(0.5 + np.arange(8), -0.5,13.5,'gray')\n    ax.hlines(0.5 + np.arange(14), -0.5,8.5,'gray')\n    \n\naxlegend = fig.add_axes([0.495,0.4, 0.035,0.4])\naxlegend.imshow(np.arange(5).reshape(5,1), cmap='Blues', aspect='auto')\naxlegend.set(xticks=[], yticks=[], title='Leyenda')\nfor k, v in enumerate(critical.index[:-1]):\n    axlegend.annotate(v, [0, 1+k],ha='center')\n\naxlegend.annotate(critical.index[-1], [0, k+2],color='yellow',ha='center')    \naxlegend.annotate('I(0)', [0, 0],ha='center')")


# In[22]:


fig.savefig('NelsonPlosser-KPSS.pdf', bbox_inches='tight')
fig

