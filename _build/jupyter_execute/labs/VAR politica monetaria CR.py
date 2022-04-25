#!/usr/bin/env python
# coding: utf-8

# # Estimación de un VAR de la política monetaria de Costa Rica

# ## Primeros pasos

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
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

from statsmodels.tsa.api import VAR


# In[3]:


plt.rc('font', serif=['Computer Modern'])


# ### Descargar datos

# In[4]:


SW.buscar('desempleo abierto', periodo='Trimestral')


# In[5]:


datos = SW(Desempleo=22796, Inflación=25485, TPM=3541, FechaInicio=2010, func=np.mean, fillna='ffill').dropna()


# In[6]:


datos.plot(figsize=[15,5])


# **Importante** Por fines didácticos, ahora restringimos la muestra a datos hasta el primer trimestre de 2020. El gran aumento en la tasa de desempleo que siguió al impacto de la pandemia del COVID no se ve reflejado en las otras variables del modelo. Como ejercicio, estime y analice este mismo VAR con datos hasta el segundo trimestre del 2020 (cambiando la siguiente celda); verá que en ese caso el VAR estimado resulta inestable!!

# In[7]:


datos = datos[:'2020Q1']


# ### Graficar los datos utilizados

# In[8]:


fig, ax = plt.subplots(figsize=[9,3])
datos.plot(ax=ax)
ax.set(title='Desempleo, inflación y tasa de política monetaria', ylabel='puntos porcentuales');
#fig.savefig('VAR-variables.pdf', bbox_inches='tight')


# ## Estimar un VAR

# In[9]:


model = VAR(datos)
res = model.fit(4, ic='bic')
res.summary()


# **Autocorrelograma de los residuos**

# In[10]:


res.plot_acorr();


# ### Número óptimo de rezagos para el VAR

# In[11]:


temp = model.select_order(4).summary()
temp


# Exportar esta tabla a LaTeX

# In[12]:


with open('VAR-ic.tex','w') as archivo:
    archivo.write(temp.as_latex_tabular())


# ## Pronosticar las variables

# In[13]:


fig = res.plot_forecast(12);
#fig.savefig('VAR-forecast.pdf', bbox_inches='tight')


# ## Analizar las funciones de impulso respuesta

# In[14]:


fig = res.irf(10).plot(subplot_params={'figsize':[12,4]});
#fig.savefig('VAR-irf-1.pdf', bbox_inches='tight')


# ## Analizar la descomposición de varianza

# In[15]:


fig=res.fevd(20).plot(figsize=[9,6]);
fig.axes[0].set(xticks=[])
fig.axes[1].set(xticks=[])
fig.axes[2].set(xticks=np.arange(0,21,2))
for ax in fig.axes:
    ax.set(yticks=[0,0.25,0.5,0.75,1.0])
    
#fig.savefig('VAR-fevd.pdf', bbox_inches='tight')    


# ## Estudiar la causalidad de Granger

# In[16]:


granger = pd.DataFrame(np.zeros([3,3]), index = datos.columns.values, columns=datos.columns.values)

for i in datos.columns:
    for j in datos.columns:
        temp = res.test_causality(i, j)
        print(temp.summary())
        granger.loc[j, i] = np.round(temp.pvalue,3)


# In[17]:


granger.index.name = 'Explicativa'
granger.columns.name = 'Dependiente'
granger


# In[18]:


granger.to_latex('VAR-Granger-causality.tex', escape=False)


# ## ¿Qué tan sensibles son los resultados al ordenamiento de las variables? Estimando todas las combinaciones 

# In[19]:


from itertools import permutations


# In[20]:


ordenamientos = [x for x in permutations(datos.columns)]


# In[21]:


def chol_irf(orden, h=10):
    res = VAR(datos[[*orden]]).fit(1)
    irf = res.irf(h).orth_irfs.flatten()
    idx = pd.MultiIndex.from_product([np.arange(h+1),orden, orden])
    return pd.DataFrame({'→'.join(orden): irf}, index=idx)


# In[22]:


irfs = pd.concat([chol_irf(A) for A in ordenamientos], axis=1)


# In[23]:


irfs = irfs.stack().unstack(level=[2,1,3])


# In[24]:


irfs


# In[25]:


fig, axs = plt.subplots(3,3, figsize=[12,6], sharex=True, sharey='row')

for i, impulso in enumerate(datos.columns):
    for j, respuesta in enumerate(datos.columns):
        irfs[impulso][respuesta].plot(ax=axs[i,j], legend=False)
        axs[j,i].set_title(impulso + '→' + respuesta )

for ax in axs[-1]:
    ax.set_xlabel('horizonte')
        
fig.suptitle('Impulso respuesta, todos los posibles ordenamientos de Choleski')   
#fig.savefig('VAR-irf-all-orderings.pdf', bbox_inches='tight')

