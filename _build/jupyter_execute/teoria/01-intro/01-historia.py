#!/usr/bin/env python
# coding: utf-8

# # Una breve historia
# 
# ```{include} ../math-definitions.md
# ```

# In[1]:


try:
    import bccr
except:
    get_ipython().system('pip install bccr')

from bccr import SW
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.filters.hp_filter import hpfilter


# ## ¿Para qué estudiar series de tiempo?
# 
# El análisis de series de tiempo ayuda a detectar **regularidades** en las observaciones de una variable y derivar **leyes** a partir de ellas, o bien para explotar toda la información incluida en la variable para **predecir** mejor el futuro.
# 
# El análisis de series de tiempo ha tenido un papel importante en la ciencia desde la antigüedad.
# 
# - Por ejemplo, los astrónomos babilonios usaron series de tiempo de las posiciones relativas de las estrellas y planetas para predecir eventos astronómicos.
# - Kepler descubrió las leyes que llevan su nombre a partir de observaciones de los movimientos de los planetas.
# 
# ## Inicios 1900s ->  Evgenij E. Slutzky y George Udny Yule  
# 
# A inicios del siglo XX, Slutzky y Yule mostraron que series de tiempo con propiedades similares a series económicas pueden generarse como  sumas o restas (simples o ponderadas) de procesos puramente aleatorios.
# 
# Desarrollaron los procesos de media móvil y autorregresivos como modelos para representar series de tiempo.
# 
# 
# ## 1919 -> Warren M. Persons  
# En 1919 Persons propuso la descomposición de una serie de tiempo en componentes no observables que dependen de causas distintas. Los componentes son:
# 
# * un movimiento de largo plazo, la **tendencia**,
# * un componente cíclico con períodos de más de un año, el **ciclo económico**,
# * un componente que contiene los aumentos y disminuciones dentro del año, el ciclo **estacional**,
# * un componente que contiene todos los movimientos no atribuibles a los demás componentes, el residual o **componente irregular**.
# 
# 
# 
# 
# <table>
#     <tr>
#         <th><div class="alert alert-success">Aditiva</div></th>
#         <th>&emsp;</th>
#         <th><div class="alert alert-success">Multiplicativa</div></th>
#     </tr>
#     <tr>
#         <td>
#             \begin{equation*}
#             Y_t = T_t + C_t + S_t + I_t
#             \end{equation*}
#         </td>
#         <td></td>
#         <td>
#             \begin{equation*}
#             Y_t = T_t \times C_t \times S_t \times I_t
#             \end{equation*}
#         </td>
#     </tr>
# </table>    
# 
# 
# 
# 
# 
# <div class="ejemplo">
# <div class="ejemplo-titulo">Ejemplo 1.1: Componentes del IMAE</div>
# En el siguiente ejemplo vemos los componentes del IMAE de Costa Rica.

# In[2]:


imaes = SW.buscar('IMAE serie original', frecuencia='M', Unidad='Nivel')
imaes[imaes.descripcion.str.contains('IMAE')]


# In[3]:


imae = SW(IMAE=87703)  # descargar el imae
imae.plot(figsize=[12,5]);


# Descomposición aditiva y multiplicativa del IMAE de Costa Rica

# In[4]:


def descomponer(serie, model):
    """
    Toma una serie y separa sus componentes. Aplica el filtro Hodrick-Prescott para 
    separar la tendencia del ciclo.

    serie: pd.Series, datos originales
    model: "additive" o "multiplicative", método para la separación.
    """
    res = seasonal_decompose(serie, model=model, period=12, extrapolate_trend='freq')
    if model == 'additive':
        ciclo, tendencia = hpfilter(res.trend, lamb=14400)
    elif model == 'multiplicative':
        ciclo, tendencia = np.exp(hpfilter(np.log(res.trend), lamb=14400))
    return pd.DataFrame({'Original':res.observed,
                         'Tendencia': tendencia, 
                         'Ciclo': ciclo, 
                         'Estacional': res.seasonal, 
                         'Irregular': res.resid})
    
# Hacer las dos descomposiciones, y unirlas en una sola tabla de pandas
descomp = pd.concat([descomponer(imae, version) for version in ('additive','multiplicative')], 
                    keys= ['Aditivo', 'Multiplicativo'], axis=1)

# Graficar los resultados
fig, axs = plt.subplots(5,2,sharex=True, figsize=(10,12))

descomp.plot(subplots=True, ax=axs.T, color='C0', legend=False, xlabel="")
for ax, version in zip(axs[0], descomp.columns.levels[0]): ax.set_title(version)
for ax, componente in zip(axs[:,0], descomp.columns.levels[1]): ax.set_ylabel(componente)


# Esta es una descomposición “ingenua”. Más adelante en el curso estudiaremos métodos más sofisticados.
# </div>
# 
# 
# 
# 
# ## Enfoques clásico vs moderno de descomposición de series
# 
# Como los componentes **no son observables**, es necesario hacer supuestos acerca de su naturaleza para estudiar el proceso generador de la serie.
# 
# <div class="container">
#   <div class="row">
#     <div class="col-sm-5 border border-3 border-success p-0">
#       <h3 class="alert alert-success">Enfoque clásico</h3>
#       \begin{equation*}Y_t = \underbrace{T_t + C_t + S_t}_{\text{determinísticos}}+\underbrace{I_t}_{\text{estocástico}}\end{equation*}
#       <p  class="p-2">Los componentes sistemáticos son funciones <strong>determinísticas</strong> del tiempo, el componente residual es estocástico pero <strong>no contiene movimientos sistemáticos</strong>.</p>
# 
#     </div>
#       <div class="col-sm-1"> </div>
#     <div class="col-sm-5 border border-3 border-success p-0">
#       <h3 class="alert alert-success">Enfoque clásico</h3>
#         \begin{equation*}Y_t = \underbrace{T_t + C_t + S_t + I_t}_{\text{estocásticos}}\end{equation*}
#       <p class="p-2">La “ley de movimiento” de la serie es vista como un <strong>proceso estocástico</strong>, y los datos de la serie como <strong>una realización</strong> del proceso generador de datos.</p>
#     </div>
#   </div>
# </div>
# 
# 
# 
# ## 1930s -> Jan Tinbergen
# 
# En 1936, Tinbergen construyó el primer modelo econométrico: un modelo macroeconométrico de la economía holandesa, empezando así el desarrollo de la econometría aplicada.
# 
# En 1939, presentó su metodología para el análisis estadístico de teorías de ciclo económico, así como un modelo macroeconométrico de Estados Unidos.
# 
# Sus métodos fueron controversiales:
# 
# > “Nadie podría ser más franco, más meticuloso, más libre de prejuicios subjetivos o partidistas que el profesor Tinbergen. No hay nadie, por lo tanto, en lo que respecta a las cualidades humanas, a quien sería más seguro confiar con magia negra. Todavía no estoy convencido de que haya alguien en quien confiaría en la etapa actual o que esta marca de alquimia estadística está madura para convertirse en una rama de la ciencia. Pero Newton, Boyle y Locke jugaron con la alquimia. Así que déjenle continuar.”
# >
# > --- Keynes, 1940 (citado por Boumans2015)
# 
# ## 1938 -> Herman Wold  
# Wold sistematizó y generalizó el trabajo de Slutzky y Yule.
# 
# Demostró que para proceso covarianza-estacionario, puramente no-determinístico, existe una descomposición de la serie como combinación lineal de una serie de variables aleatorias no correlacionadas con media cero y varianza constante.
# 
# ## 1949 -> Donald Cochrane y Guy H. Orcutt
# Tinbergen utilizó los supuestos del modelo clásico de regresión lineal, sin prestar atención a la dependencia cronológica de los residuos.
# 
# En 1949 Cochrane y Orcutt notaron que esta práctica era problemática.
# 
# Demostraron que si los residuos de una regresión están positivamente correlacionados, entonces la varianza de los parámetros de regresión está subestimada y los estadísticos t y F sobrestimados.
# 
# El problema se podía resolver transformando los datos adecuadamente.
# 
# ## 1950 -> James Durbin y Geoffrey S. Watson
# 
# En 1950/51 Durbin y Watson desarrollaron un test para identificar autocorrelación de primer orden en los residuos.
# 
# ## 1970 -> George E.P. Box y Gwilym M. Jenkins
# En 1970 Box y Jenkins publican un libro de texto de análisis de series de tiempo.
# 
# Introducen modelos univariados para series de tiempo, que usan sistemáticamente la información contenida en los valores de la serie.
# 
# Manera sencilla de producir pronósticos.
# 
# Hoy en día conocida como **metodología Box-Jenkins**.
# 
# ```{figure} ../../imgs/box-jenkins.png
# :scale: 45%
# 
# La metología Box-Jenkins
# ```
# 
# ## 1975 -> Clive W.J. Granger y Paul Newbold
# En 1975 Granger y Newbold mostraron que los pronósticos sencillos de métodos univariados a menudo eran mejores que los pronósticos basados en modelos econométricos grandes (cientos de ecuaciones).
# 
# Esto impulsó la enorme popularidad de la metodología Box-Jenkins.
