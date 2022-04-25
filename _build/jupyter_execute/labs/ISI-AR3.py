#!/usr/bin/env python
# coding: utf-8

# # Estimación de un modelo ARMA de inflación para Costa Rica

# **Nota** Para ejecutar este cuaderno se requiere el paquete `bccr`. Si no lo tiene, ejecute la siguiente celda

# In[1]:


try:
    import bccr
except ImportError:
    print('Module bccr missing. Installing it now')
    get_ipython().system('pip install bccr')


# ## Descarga de datos

# In[2]:


from bccr import SW
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


# In[3]:


SW.buscar(todos='inflación subyacente')


# In[4]:


isi = SW(isi=25725).dropna()
isi


# ## Graficar la serie original y estudiar su autocorrelograma

# In[5]:


fig, axs = plt.subplot_mosaic(
    """
    AA
    BC
    """, figsize=[10,5], tight_layout=True)#, sharey='row')

isi.plot(ax=axs['A'], title='Inflación subyacente, mensual', legend=None)
plot_acf(isi, ax=axs['B'], title='Autocorrelación')
plot_pacf(isi, ax=axs['C'], title='Autocorrelación parcial');
axs['B'].set_xticks(range(0,30,6))
axs['C'].set_xticks(range(0,30,6))
axs['C'].sharey(axs['B'])
fig.savefig('ISI-AR3.pdf', bbox_inches='tight')


# ## Estimar un modelo AR(3)

# In[6]:


res = ARIMA(isi, order=[3,0,0]).fit()
res.summary()


# #### Exportar la tabla de coeficientes a LaTeX

# In[7]:


sss = res.summary()

with open('AR3-ISI.tex','w') as file:
    file.write(sss.tables[1].as_latex_tabular())


# #### Analizar los residuos

# In[8]:


fig, axs = plt.subplot_mosaic(
    """
    AA
    BC
    """, figsize=[10,5], tight_layout=True)#, sharey='row')

res.resid.plot(ax=axs['A'], title='Residuos del modelo AR(3)', legend=None)
plot_acf(res.resid, ax=axs['B'], title='Autocorrelación')
plot_pacf(res.resid, ax=axs['C'], title='Autocorrelación parcial')
axs['B'].set_xticks(range(0,30,6))
axs['C'].set_xticks(range(0,30,6))
axs['C'].sharey(axs['B'])
fig.savefig('ISI-AR3resid.pdf', bbox_inches='tight')


# ### Raíces del polinomio característico (recíprocos de las raíces del polinomio de rezagos)

# In[9]:


1 / res.arroots


# In[10]:


arroots = 1/res.arroots

plt.polar(np.angle(arroots), np.abs(arroots), '.', ms=20)
fig = plt.gcf()
ax = fig.gca()
ax.set_rlim([0,1])
ax.set_title('Raíces inversas del polinomio autorregresivo')
fig.savefig('ISI-AR3roots.pdf', bbox_inches='tight')


# ## Usar criterios de selección para determinar el grado p, q del modelo ARMA

# In[11]:


pmax = 4
qmax = 2
P = np.arange(pmax+1)
Q = np.arange(qmax+1)


# ### Akaike

# In[12]:


aic = [[ARIMA(isi, order=[p,0,q]).fit().aic for q in Q ] for p in P ]
AIC = pd.DataFrame(aic, index=[f'p={p}' for p in P], columns=[f'q={q}' for q in Q])
AIC.style.highlight_min()


# Exportar a LATEX

# In[13]:


AIC.round(2).to_latex('ISI-AR3aic.tex')


# ### Bayesiano

# In[14]:


bic = [[ARIMA(isi, order=[p,0,q]).fit().bic for q in Q ] for p in P ]
BIC = pd.DataFrame(bic, index=[f'p={p}' for p in P], columns=[f'q={q}' for q in Q])
BIC.style.highlight_min()


# Exportar a LATEX

# In[15]:


BIC.round(2).to_latex('ISI-AR3bic.tex')


# ## Pronóstico

# In[16]:


horizon = 36

temp = res.get_prediction(start=isi.index[-1] + pd.offsets.MonthEnd(), end='2023-12', dynamic=False, index=None, exog=None, extend_model=None, extend_kwargs=None)

ff, std, conf = temp.predicted_mean, temp.se_mean, temp.conf_int(0.05)

#ff, std, conf = res.forecast(steps=horizon, alpha=0.05) # version anterior, no funciona con el nuevo módulo de ARIMA


# #### Valores críticos de la distribución normal

# In[17]:


from scipy.stats import norm


# In[18]:


alpha = np.arange(1,6)/10
zvalues = norm(0, 1).isf(np.array(alpha)/2)


# #### Graficar el pronóstico

# In[19]:



# Datos pronosticados
fcast = pd.DataFrame({'isi':ff,'std':std}, index=pd.period_range(isi.index[-1]+1, periods=horizon, freq='M'))

# Concatenar los datos observados con los pronosticados
fcast2 = pd.concat([isi,fcast], sort=False)
fcast2['$\mu$'] = isi.values.mean()

# Graficar la serie y el pronóstico
fig, ax =plt.subplots(figsize=[12,4])
fcast2[['isi','$\mu$']].plot(ax=ax)



def intervalo(z):
    """
    Para calcular los límites superior e inferior del intervalo de confianza,
    dado el valor crítico de la distribución normal
    """
    return fcast2['isi']+z*fcast2['std'],  fcast2['isi']-z*fcast2['std']

# fechas para graficar los intervalos
d = fcast2.index.values

# Graficar los intervalos de confianza
for z in zvalues:
    ax.fill_between(d, *intervalo(z), facecolor='red', alpha=0.12, interpolate=True)

fig.savefig('ISI-AR3forecast.pdf', bbox_inches='tight')


# ## Exportar datos a STATA

# In[20]:


isi.index = isi.index.to_series().astype(str)
isi.to_stata('isi.dta')

