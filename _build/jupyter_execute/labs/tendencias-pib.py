#!/usr/bin/env python
# coding: utf-8

# # Pruebas de raíz unitaria para el PIB en Costa Rica

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm


# In[2]:


from statsmodels.tsa.stattools import adfuller, kpss


# In[3]:


plt.style.use('seaborn')
plt.rc('figure', figsize=(15,4))
plt.rc('axes', titlesize=20, labelsize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)

figpath = "../figures/"


# ## Descargar los datos

# In[4]:


import bccr


# In[5]:


pib = bccr.SW(PIB=33783)
pib['lPIB'] = np.log(pib['PIB'])

temp = pib.copy()
temp.index = pib.index.to_series().astype(str)
temp.reset_index().to_stata('pib-costa-rica.dta')
del temp


# ## Gráfico de la serie

# In[6]:


fig, ax = plt.subplots()
pib['PIB'].plot(ax=ax, legend=False)
ax.set(yscale='log', title='Producto interno bruto de Costa Rica', ylabel='escala logarítmica')
fig.savefig(figpath + 'pib-costa-rica-I(1).pdf', bbox_inches='tight')


# ## Correlograma del (logaritmo) del PIB y su primer diferencia

# In[7]:


fig,axs = plt.subplots(2,1, figsize=[15,8], sharex=True)
sm.graphics.tsa.plot_acf(pib['lPIB'],ax=axs[0]);
axs[0].set(ylim=[-0.1,1.1], title='$\log(PIB_t)$')

sm.graphics.tsa.plot_acf(pib['lPIB'].diff().dropna(),ax=axs[1]);
axs[1].set(ylim=[-0.5,1.1], title='$\Delta\log(PIB_t)$')

fig.suptitle('Autocorrelación del PIB trimestral de Costa Rica', fontsize=20)
fig.savefig(figpath + 'pib-costa-rica-rho.pdf',bbox_inches='tight')


# ## Ajustando una tendencia lineal

# ### Estimando la tendencia y los residuos

# In[8]:


pib['t'] = np.arange(pib.shape[0])

pib['tendencia'] = smf.ols('lPIB ~ t', pib).fit().fittedvalues
pib['residuos'] = pib['lPIB'] - pib['tendencia']


# In[9]:


fig, axs = plt.subplots(2,1, figsize=[15,6], sharex=True)
pib[['lPIB','tendencia']].plot(ax=axs[0], legend=False)
axs[0].set(title='PIB con tendencia lineal ajustada', ylabel='logaritmos')

pib[['residuos']].plot(ax=axs[1], legend=False)
axs[1].set(title='Residuos')
fig.savefig(figpath + 'pib-tendencia-lineal.pdf', bbox_inches='tight')


# ### Correlograma de los residuos

# In[10]:


sm.graphics.tsa.plot_acf(pib['residuos']);


# ## Pruebas de DickeyFuller

# ### Implementando la prueba DF con regresión lineal

# In[11]:


dy  = pib['lPIB'].diff()[1:]
ly = pib['lPIB'].shift(1)[1:]
tt = np.arange(dy.size)

X = sm.add_constant(ly)
Z = np.c_[X,tt]


# In[12]:


tnc = sm.OLS(dy,ly, hasconst=False).fit().tvalues[0]
tc = sm.OLS(dy, X, hasconst=True).fit().tvalues[1]
tct = sm.OLS(dy, Z, hasconst=True).fit().tvalues[1]


# In[13]:


tnc, tc, tct


# In[14]:


tbl = sm.OLS(dy, X, hasconst=True).fit().summary().tables[1]

with open(figpath + 'df-lpib-regresion.tex','w') as cuadro:
    cuadro.write(tbl.as_latex_tabular())


# ### Implementando el código para hacer las tablas

# In[15]:


specs = ['nc', 'c', 'ct']
indice = ['sin constante', 'con constante', 'con constante y tendencia']

def DF(datos, spec):
    res = adfuller(datos, maxlag=0,regression=spec)
    resultado = {
        'z':res[0], 
        '1%': res[4]['1%'], 
        '5%': res[4]['5%'], 
        '10%': res[4]['10%']}
    return resultado

def ADF(datos, spec):
    res = adfuller(datos, regression=spec, autolag='t-stat')
    resultado = {
        'z':res[0], 
        '1%': res[4]['1%'], 
        '5%': res[4]['5%'], 
        '10%': res[4]['10%'],
        'p': res[2]}
    return resultado

pruebas = {'df':DF, 'adf':ADF}

def tabla_dickey_fuller(serie, test, diff=0):
    datos = pib[serie].diff(diff) if diff else pib[serie]
    resultados = pd.DataFrame([pruebas[test](datos.dropna(), ss) for ss in specs], index=indice).round(3)
    nombre = '_'.join([test,serie,str(diff)])
    resultados.to_latex(figpath + nombre + '.tex')
    return resultados


# ### Pruebas para serie en nivel

# In[16]:


tabla_dickey_fuller('lPIB','df')


# ### Pruebas para serie en primer diferencia

# In[17]:


tabla_dickey_fuller('lPIB', 'df', diff=1)


# ### Serie de los residuos alrededor de tendencia

# In[18]:


tabla_dickey_fuller('residuos', 'df', diff=0)


# ## Prueba aumentada de Dickey-Fuller

# ### Serie en nivel

# In[19]:


tabla_dickey_fuller('lPIB', 'adf', diff=0)


# ### Serie en primer diferencia

# In[20]:


tabla_dickey_fuller('lPIB', 'adf', diff=1)


# ### Serie de los residuos alrededor de tendencia

# In[21]:


tabla_dickey_fuller('residuos', 'adf', diff=0)


# ## Pruebas KPSS

# In[22]:


def KPSS_una_serie(datos, tipo):
    return [kpss(datos.dropna(), regression=tipo, lags=k)[0] for k in range(7)]   


# In[23]:


critical = pd.DataFrame(
    {'c': np.array([0.347, 0.463, 0.574, 0.739]),
     'ct':np.array([0.119, 0.146, 0.176, 0.216])},
    index=['10%', '5%', '2.5%', '1%'])


# In[24]:


def tabla_KPSS(diff=0):
    datos = pib['lPIB'].diff(diff) if diff else pib['lPIB']
    resultados = pd.DataFrame([KPSS_una_serie(datos, ss) for ss in ['c','ct']], index=['c','ct']).round(3)
    #nombre = '_'.join([test,serie,str(diff)])
    #resultados.to_latex(figpath + nombre + '.tex')
    return resultados.T


# In[25]:


get_ipython().run_cell_magic('capture', '', "tab = pd.concat([tabla_KPSS(diff=r) for r in range(2)], axis=1,keys=['nivel','diferencia'])")


# In[26]:


tab.to_latex(figpath + 'kpss_lPIB.tex')
tab


# In[27]:


critical.to_latex(figpath + 'kpss_critical.tex')

