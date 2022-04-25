#!/usr/bin/env python
# coding: utf-8

# # Las pruebas de Box-Pierce y Ljung-Box.
# 
# 

# ## Cargar paquetes necesarios

# In[1]:


import matplotlib.pyplot as plt
plt.style.use('seaborn')
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.stats.distributions import chi2


# ## Definir ubicación de archivos de datos

# In[2]:


GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'


# ## EJEMPLO 1: Crecimiento del IMAE de Costa Rica, serie tendencia-ciclo
# 
# ¿Es es crecimiento mensual del IMAE tendencia-ciclo un proceso ruido blanco?

# In[3]:


log_imae = pd.read_csv(DATAPATH + 'log_imae.csv')
log_imae.index = pd.period_range(start='1991-01', freq='M', periods=log_imae.shape[0])
log_imae


# In[4]:


growth = log_imae['Tendencia_ciclo'].diff().dropna()
T = growth.size  # número de datos
M = 7   # máximo número de rezagos
rezagos = np.arange(1, M+1)
alpha = 0.05  # significancia de los test


# Calculamos las autocovarianzas, a partir de un rezago

# In[5]:


rho = sm.tsa.acf(growth, fft=True, nlags=M)[1:] 


# Calculamos el estadístico de Box-Pierce, para todos los rezagos desde el 1 hasta el 7
# 
# \begin{equation*}
# Q^{*} = T\sum_{j=1}^{m}\hat{\rho}_j^2 \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation*}

# In[6]:


Qstar = T * (rho ** 2).cumsum()


# Calculamos el estadístico de Ljung-Box
# 
# \begin{equation*}
# Q = T(T+2)\sum_{j=1}^{m}\frac{\hat{\rho}_j^2}{T-j} \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation*}

# In[7]:


Q = T * (T+2) * ((rho ** 2)/(T-rezagos)).cumsum()


# Calculamos los valores críticos, tomando en cuenta que $k=0$ porque los datos que estamos usando no son residuos

# In[8]:


vcrits = np.array([chi2(k).ppf(1-alpha) for k in rezagos])


# Con carácter informativo nada más, calculamos la autocorrelación parcial

# In[9]:


rhop = sm.tsa.pacf(growth, nlags=M, method='ols')[1:]


# Juntamos todos los resultados en una tabla de resumen.

# In[10]:


resumen = pd.DataFrame({'AC':rho, 'PAC': rhop, 'Box-Pierce':Qstar, 'Ljung-Box':Q, f'$\chi^2(m-k)$': vcrits}, index=rezagos)
resumen.index.name = 'Rezagos'

resumen.round(3)


# Graficamos los datos y el autocorrelograma

# In[11]:


fig, axs = plt.subplots(2,1, figsize=[8,6])
growth.plot(ax=axs[0], title='Evolución del crecimiento del IMAE')
sm.graphics.tsa.plot_acf(growth, ax=axs[1], lags=48, alpha=0.05, title='Autocorrelograma');


# ## EJEMPLO 2: Crecimiento del tipo de cambio Euro/USD
# 
# ¿Es es crecimiento diario del tipo de cambio euro-dólar un proceso ruido blanco?

# In[12]:


euro = pd.read_csv(DATAPATH + 'euro.csv')
#euro.index = pd.to_datetime(euro['fecha'])
euro.drop('fecha',inplace=True,axis=1)


# In[13]:


depreciacion = euro.diff().dropna()
T = depreciacion.shape[0]  # número de datos
M = 7   # máximo número de rezagos
rezagos = np.arange(1, M+1)
alpha = 0.05  # significancia de los test


# Calculamos las autocovarianzas, a partir de un rezago

# In[14]:


rho = sm.tsa.acf(depreciacion, fft=True, nlags=M)[1:] 


# Calculamos el estadístico de Box-Pierce, para todos los rezagos desde el 1 hasta el 7
# 
# \begin{equation*}
# Q^{*} = T\sum_{j=1}^{m}\hat{\rho}_j^2 \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation*}

# In[15]:


Qstar = T * (rho ** 2).cumsum()


# Calculamos el estadístico de Ljung-Box
# 
# \begin{equation*}
# Q = T(T+2)\sum_{j=1}^{m}\frac{\hat{\rho}_j^2}{T-j} \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
# \end{equation*}

# In[16]:


Q = T * (T+2) * ((rho ** 2)/(T-rezagos)).cumsum()


# Calculamos los valores críticos, tomando en cuenta que $k=0$ porque los datos que estamos usando no son residuos

# In[17]:


vcrits = np.array([chi2(k).ppf(1-alpha) for k in rezagos])


# Con carácter informativo nada más, calculamos la autocorrelación parcial

# In[18]:


rhop = sm.tsa.pacf(depreciacion, nlags=M, method='ols')[1:]


# Juntamos todos los resultados en una tabla de resumen.

# In[19]:


resumen = pd.DataFrame({'AC':rho, 'PAC': rhop, 'Box-Pierce':Qstar, 'Ljung-Box':Q, f'$\chi^2(m-k)$': vcrits}, index=rezagos)
resumen.index.name = 'Rezagos'

resumen.round(4)


# Graficamos los datos y el autocorrelograma

# In[20]:


fig, axs = plt.subplots(2,1, figsize=[8,6])
depreciacion.plot(ax=axs[0], title='Evolución del cambio porcentual en EUR/USD')
sm.graphics.tsa.plot_acf(depreciacion, zero=False, ax=axs[1], lags=48, alpha=0.05, title='Autocorrelograma');

