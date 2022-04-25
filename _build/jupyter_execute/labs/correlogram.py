#!/usr/bin/env python
# coding: utf-8

# # Autocorrelograma y pruebas de ruido blanco para el IMAE de Costa Rica
# 
# Ejemplo numérico para ilustrar el uso del autocorrelograma y el autocorrelograma parcial.

# **Nota** Para ejecutar este cuaderno se requiere el paquete `bccr`. Si no lo tiene, ejecute la siguiente celda

# In[1]:


try:
    import bccr
except ImportError:
    print('Module bccr missing. Installing it now')
    get_ipython().system('pip install bccr')


# In[2]:


from bccr import SW
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats.distributions import chi2
import os

figpath = "../figures/"


# ## Importamos los datos
# La clase `ServicioWeb` permite obtener datos directamente del Banco Central de Costa Rica
# 
# Buscamos series que tenga "IMAE" en su DESCRIPCION, frecuencia mensual. Filtramos los resultados para ver solo las series en nivel, y dejamos solo aquellos qe tengan la palabra "IMAE" en su descripción

# In[3]:


imaes = SW.buscar(todos='IMAE', frecuencia='M')
imaes = imaes[imaes.Unidad == 'Nivel']
imaes[imaes.descripcion.str.contains('IMAE')]


# De esta lista, escogemos los indicadores <strike>35449 (serie original) y 35553 (tendencia-ciclo)</strike> (éstas están discontinuadas, usarememos entonces las series 87703 y 87764, que de momentos no pueden encontrarse con bccr, pero sí descargarse). Descargamos los datos y cambiamos los nombres de las series.

# In[4]:


imae = SW(Original=87703, Tendencia_ciclo=87764)


# Graficamos las dos series para ver su dinamica.

# In[5]:


imae.plot(figsize=[12,5])


# ## Autocorrelograma
# 
# Obtenemos autocorrelogramas (48 rezagos, con intervalos de 95% de significancia (Bartlett)) para las series en nivel, primera diferencia, y diferencia estacional.

# In[6]:


OPCIONES = dict(lags=48, alpha=0.05, title='')
plot_acf = sm.graphics.tsa.plot_acf
plot_pacf = sm.graphics.tsa.plot_pacf
log_imae = np.log(imae)


# In[7]:


fig, axs = plt.subplots(3,2, figsize=[16,9], sharex=True, sharey=True)

for indic, ax in zip(imae, axs.T):
    plot_acf(log_imae[indic].dropna(), ax=ax[0], **OPCIONES);
    plot_acf(log_imae[indic].diff().dropna(), ax=ax[1], **OPCIONES);
    plot_acf(log_imae[indic].diff(12).dropna(), ax=ax[2], **OPCIONES);

for indic, ax in zip(imae, axs[0]):
    ax.set_title(indic)

for ax in axs[-1]:
    ax.set_xlabel(r'Rezago $\tau$')
    ax.set_xticks(np.arange(0,49,12));

axs[0,0].set_ylabel(r'$\log(IMAE)$')
axs[1,0].set_ylabel(r'$\Delta log(IMAE)$')
axs[2,0].set_ylabel(r'$\Delta_{12} log(IMAE)$')

fig.suptitle('Autocorrelograma del IMAE (original y tendencia-ciclo) en Costa Rica', size=16)
fig.savefig(figpath + 'IMAE-acf.pdf', bbox_inches='tight')    


# ## Autocorrelograma parcial
# 
# Repetimos el ejercicio, pero esta vez obtenemos autocorrelogramas parciales (48 rezagos, con intervalos de 95% de significancia) para las series en nivel, primera diferencia, y diferencia estacional.

# In[8]:


OPCIONES = dict(lags=48, alpha=0.05, title='', method='ols')

fig, axs = plt.subplots(3,2, figsize=[16,9], sharex=True, sharey=True)

for indic, ax in zip(imae, axs.T):
    plot_pacf(log_imae[indic].dropna(), ax=ax[0], **OPCIONES);
    plot_pacf(log_imae[indic].diff().dropna(), ax=ax[1], **OPCIONES);
    plot_pacf(log_imae[indic].diff(12).dropna(), ax=ax[2], **OPCIONES);

for indic, ax in zip(imae, axs[0]):
    ax.set_title(indic)

for ax in axs[-1]:
    ax.set_xlabel(r'Rezago $\tau$')
    ax.set_xticks(np.arange(0,49,12));

axs[0,0].set_ylabel(r'$\log(IMAE)$')
axs[1,0].set_ylabel(r'$\Delta log(IMAE)$')
axs[2,0].set_ylabel(r'$\Delta_{12} log(IMAE)$')

fig.suptitle('Autocorrelograma parcial del IMAE (original y tendencia-ciclo) en Costa Rica', size=16)
fig.savefig(figpath + 'IMAE-pacf.pdf', bbox_inches='tight')    


# ## Pruebas de ruido blanco
# 
# ¿Es es crecimiento mensual del IMAE tendencia-ciclo un proceso ruido blanco?

# In[9]:


growth = log_imae['Tendencia_ciclo'].diff().dropna()
T = growth.size  # número de datos
M = 7   # máximo número de rezagos
rezagos = np.arange(1, M+1)
alpha = 0.05  # significancia de los test


# Calculamos las autocovarianzas, a partir de un rezago

# In[10]:


rho = sm.tsa.acf(growth, fft=True, nlags=M)[1:] 


# Calculamos el estadístico de Box-Pierce, para todos los rezagos desde el 1 hasta el 7
# 
# \begin{equation}
# Q^{*} = T\sum_{j=1}^{m}\hat{\rho}_j^2 \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation}

# In[11]:


Qstar = T * (rho ** 2).cumsum()


# Calculamos el estadístico de Ljung-Box
# 
# \begin{equation}
# Q = T(T+2)\sum_{j=1}^{m}\frac{\hat{\rho}_j^2}{T-j} \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation}

# In[12]:


Q = T * (T+2) * ((rho ** 2)/(T-rezagos)).cumsum()


# Calculamos los valores críticos, tomando en cuenta que $k=0$ porque los datos que estamos usando no son residuos

# In[13]:


vcrits = np.array([chi2(k).ppf(1-alpha) for k in rezagos])


# Con carácter informativo nada más, calculamos la autocorrelación parcial

# In[14]:


rhop = sm.tsa.pacf(growth, nlags=M, method='ols')[1:]


# Juntamos todos los resultados en una tabla de resumen.

# In[15]:


resumen = pd.DataFrame({'AC':rho, 'PAC': rhop, 'Box-Pierce':Qstar, 'Ljung-Box':Q, f'$\chi^2(m-k)$': vcrits}, index=rezagos)
resumen.index.name = 'Rezagos'

resumen.round(3)


# ### Exportar datos
# Finalmente, exportamos los datos para poder replicar este ejercicio con otros programas (Stata, EViews, R).

# In[16]:


log_imae.to_csv('log_imae.csv')

