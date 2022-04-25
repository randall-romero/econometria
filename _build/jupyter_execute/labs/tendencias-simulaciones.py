#!/usr/bin/env python
# coding: utf-8

# # Series integradas

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm


# In[2]:


plt.style.use('seaborn')
plt.rc('figure', figsize=(15,4))
plt.rc('axes', titlesize=20, labelsize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('savefig', bbox='tight')

figpath = "../figures/"


# ## Simulaciones de caminatas aleatorias

# In[3]:


plt.style.use('seaborn-dark')
pd.options.plotting.backend = "matplotlib"

np.random.seed(2021)

T = 60 # horizonte
n = 100 # cantidad de simulaciones

𝜖 = pd.DataFrame(np.random.randn(T+1, n)) # ruido blanco
y = 𝜖.cumsum(axis=0)  # caminatas aleatorias


fig = plt.figure(figsize=(14, 8))
gs = fig.add_gridspec(5, 2,  width_ratios=(6, 2),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)

# -----------Graficar las simulaciones
ax = fig.add_subplot(gs[:, 0])
y.plot(color='RoyalBlue', alpha=0.1, legend=False, ax=ax)
ax.axhline(0, color='white');
ax.set(title=f'{n} caminatas aleatorias',ylim=[-25,25])

# -----------Histogramas
ax_last = None
for i in range(5):
    ax_last = fig.add_subplot(gs[i, 1], sharex= ax_last)
    y.loc[15*i].hist(ax=ax_last, color='RoyalBlue', alpha=0.8)
    if i==0:
        ax_last.set(title='Histogramas',xlim=[-25,25])

    ax_last.set_yticks([])
    ax_last.annotate(f't ={15*i}', (0.1, 0.8), xycoords='axes fraction')
    
fig.savefig(figpath + 'Simulaciones-caminata-aleatoria.pdf')    


# ## Simulaciones de caminatas aleatorias con deriva

# In[4]:


pd.options.plotting.backend = "matplotlib"
a = 0.5 # deriva
y = (𝜖+a).cumsum(axis=0)  # caminatas aleatorias con deriva


fig = plt.figure(figsize=(14, 8))
gs = fig.add_gridspec(5, 2,  width_ratios=(6, 2),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)

ax = fig.add_subplot(gs[:, 0])
y.plot(color='RoyalBlue', alpha=0.1, legend=False, ax=ax)
ax.plot(a*np.arange(T), color='white');
ax.set(title=f'{n} caminatas aleatorias con deriva',ylim=[-10,50])

ax_last = None
for i in range(5):
    ax_last = fig.add_subplot(gs[i, 1], sharex= ax_last)
    y.loc[15*i].hist(ax=ax_last, color='RoyalBlue', alpha=0.8)
    if i==0:
        ax_last.set(title='Histogramas',xlim=[-10,50])

    ax_last.set_yticks([])
    ax_last.annotate(f't ={15*i}', (0.05, 0.8), xycoords='axes fraction')
    
fig.savefig(figpath + 'Simulaciones-caminata-aleatoria-con-deriva.pdf')        


# ## Autocorrelación de una caminata aleatoria

# In[5]:


def rw_rho(t, smax=20):
    """
    Calcula las primera autocorrelaciones de una serie con raiz unitaria
    
    Ver pagina 56 de los apuntes del tema 4 del curso
    """
    return np.sqrt(1 - np.arange(smax+1) /t)

rw_rho_data = pd.DataFrame({f't={t}':rw_rho(t) for t in [20,40,60,80]})
     
fig, ax = plt.subplots()
rw_rho_data.plot(ax=ax)
ax.set(ylim=[0,1], xticks=np.arange(0,21,4), xlabel='rezagos', title='Autocorrelaciones')
plt.savefig(figpath + 'rw-rho.pdf', bbox_inches='tight')


# ## Estacionario en diferencia vs estacionario en tendencia
# 
# Ejemplo basado en Levendis 2019, pp. 109-113. Muestra que no es tan fácil distinguir a simple vista un proceso estacionario en diferencia de uno estacionario alrededor de una tendencia.

# In[6]:


T = 100
np.random.seed(12345)
tt = np.arange(T)
e = np.random.randn(T)


# In[7]:


datos = pd.DataFrame({'t':tt, 'e':e}, index=tt)
datos['DS'] = (1+e).cumsum()
datos['TS'] = 1*tt + e
datos


# In[8]:


get_ipython().run_cell_magic('timeit', '', "lento = pd.DataFrame({'t':tt, 'e':e}, index=tt)\n\n# caminata aleatoria\ny = np.zeros(T)\ny[0] = 1 + e[0]\nfor t in range(1, T):\n    y[t] = 1 + y[t-1] + e[t]\n\n# estacionario alrededor de tendencia    \nx = np.zeros(T)\nx[0] = e[0]\nfor t in range(1, T):\n    x[t] = 1 * tt[t] + e[t]\n\nlento['y'] = y\nlento['x'] = x\n#lento")


# In[9]:


detrended = pd.DataFrame(
    {'DS':smf.ols('DS ~ t', datos).fit().resid,
     'TS':smf.ols('TS ~ t', datos).fit().resid
    }, index=tt)


# In[10]:


def ols_ala_stata(formula):
    return smf.ols(formula, datos).fit().summary()


# In[11]:


ols_ala_stata('DS ~ t + TS -1')


# In[12]:


fig, axs = plt.subplots(3,1, figsize=[15,9], sharex=True)
series = ['DS', 'TS']
datos[series].plot(ax=axs[0], title='Series en nivel')
datos[series].diff().plot(ax=axs[1], title='Series en primera diferencia')
detrended[series].plot(ax=axs[2], title='Series menos tendencia lineal')


# In[13]:


np.random.seed(1)
T = 121
e = np.random.randn(T)
e[0] = 0

x0 = y0 = a = 1
t = np.arange(T)

y = y0 + a*t + e.cumsum()
x = x0 + a*t + e

ejemplo = pd.DataFrame({'DS':y,'TS':x})    

fig, ax = plt.subplots()
ejemplo.plot(ax=ax)
ax.set_title('Tendencia determinística (TS) versus estocástica (DS)', fontsize=16)
fig.suptitle('Series no estacionarias',fontsize=24, y=1.05)
fig.savefig(figpath + 'TS-DS-sample.pdf')


# Repetimos el ejercicio, pero con un millón de observaciones

# In[14]:


T = 1_000_000
np.random.seed(12345)
tt = np.arange(T)
e = np.random.randn(T)


# In[15]:


big = pd.DataFrame({'t':tt, 'e':e}, index=tt)
big['DS'] = (1+e).cumsum()
big['TS'] = tt + e

bigdetrended = pd.DataFrame(
    {'DS':smf.ols('DS~t', big).fit().resid,
     'TS':smf.ols('TS~t', big).fit().resid
    }, index=tt)

resumen = pd.concat([
    big[series].diff().describe().T,
    bigdetrended[series].describe().T
], keys=['1-diff', '- tend'])

resumen

