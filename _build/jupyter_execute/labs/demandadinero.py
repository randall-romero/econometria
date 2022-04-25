#!/usr/bin/env python
# coding: utf-8

# # Estimación de la demanda de dinero

# **Nota** Para ejecutar este cuaderno se requiere el paquete `bccr`. Si no lo tiene, ejecute la siguiente celda

# In[1]:


try:
    import bccr
except ImportError:
    print('Module bccr missing. Installing it now')
    get_ipython().system('pip install bccr')


# In[2]:


from bccr import SW
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import matplotlib.gridspec as gridspec

import statsmodels.api as sm
from statsmodels.formula.api import ols


# In[3]:


plt.style.use('seaborn')

# Cambiar tamaño de las fuentes
rcParams['axes.titlesize'] = 20
rcParams['axes.labelsize'] = 16
rcParams['xtick.labelsize'] = 14
rcParams['ytick.labelsize'] = 14


# In[4]:


SW.buscar('medio circulante')


# In[5]:


SW.buscar('tasa básica pasiva', frecuencia='D')


# In[6]:


variables = dict(IMAE=35449,IPC=25482,M1=1445,Tbasica=423)
datos = SW(**variables, func='mean', FechaInicio='1991m01', FechaFinal='2020m11').dropna()
datos


# In[7]:


res = ols('M1 ~ IMAE + IPC + Tbasica', data=np.log(datos)).fit()


# In[8]:


fig = plt.figure(figsize=[10,5], tight_layout=True)
gs = gridspec.GridSpec(2, 2)
ax = fig.add_subplot(gs[0, :])
axs0 = fig.add_subplot(gs[1,0])
axs1 = fig.add_subplot(gs[1,1], sharey=axs0)

res.resid.plot(title='Residuos de la regresión', ax=ax)

OPCIONES = dict(lags=48, alpha=0.05, )
sm.graphics.tsa.plot_acf(res.resid, ax=axs0, title='Autocorrelación',**OPCIONES);
sm.graphics.tsa.plot_pacf(res.resid, ax=axs1, title='Autocorrelación parcial', **OPCIONES);
axs0.set_xticks([0,12,24,36,48])
axs1.set_xticks([0,12,24,36,48])

fig.savefig('residuos-demanda-dinero.pdf', bbox_inches='tight')


# In[9]:


sss = res.summary()
sss


# In[10]:


sss.tables[2]


# In[11]:


sss = res.summary()

with open('regresion-M1.tex','w') as file:
    file.write(sss.tables[1].as_latex_tabular())
    file.write(sss.tables[2].as_latex_tabular())

