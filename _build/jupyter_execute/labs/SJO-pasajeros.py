#!/usr/bin/env python
# coding: utf-8

# # Estacionalidad del número de pasajeros del aeropuerto Juan Santamaría

# ## Importando y limpiando los datos

# Los datos fueron obtenidos de la [ARESEP](https://aresep.go.cr/transparencia/datos-abiertos/pasajeros-movilizados-aeropuerto-internacional)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-talk')
figpath = "../figures/"

plt.rc('figure', figsize=[8.0,4.0])


# In[2]:


from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.x13 import x13_arima_select_order, x13_arima_analysis
from statsmodels.tsa.statespace.sarimax import SARIMAX

GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'

x13path = DATAPATH


# In[3]:


meses = ['Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre', 'Noviembre','Diciembre']
mesescorto = [x[:3] for x in meses]
meses2 = {mes: i for i, mes in enumerate(meses, start=1)}


# In[4]:


FILENAME = "Datos-ARESEP-Pasajeros-por-aeropuerto.csv"
SJO = pd.read_csv(DATAPATH + FILENAME)


# In[5]:


SJO.query('Aeropuerto =="Aeropuerto Internacional Juan Santamaría"', inplace=True)
SJO


# In[6]:


SJO.replace(meses2, None,inplace=True)
SJO


# In[7]:


SJO.sort_values(['Año','Mes'], inplace=True)
SJO


# In[8]:


SJO.index = pd.period_range(start=f"{SJO['Año'].iloc[0]}-{SJO['Mes'].iloc[0]}", periods=SJO.shape[0], freq='M')
SJO


# In[9]:


SJO.drop(['Aeropuerto', 'Mes', 'Año', 'Cantidad En Tránsito', 'Cantidad Exentos','Total Pasajeros'], axis=1,inplace=True)
SJO.rename(columns={'Cantidad Nacionales':'nacionales', 'Cantidad Extrajeros':'extranjeros'}, inplace=True)
SJO                    


# ## Gráficos de estacionalidad

# ### Serie de tiempo original contra el tiempo

# In[10]:


sjodatos = SJO/1000

fig, ax = plt.subplots()
sjodatos.plot(ax=ax)
ax.set(xlabel='', ylabel='miles de pasajeros', title='Cantidad de pasajeros del aeropuerto Juan Santamaría, por mes y residencia')
fig.savefig(figpath+'SJO-pasajeros.pdf', bbox_inches='tight')


# ### Cada mes en su propio gráfico

# In[11]:


sjodatos.index = pd.MultiIndex.from_arrays([sjodatos.index.year, sjodatos.index.month])
sjodatos


# In[12]:


sjodatoscuadro = sjodatos.unstack()
sjodatoscuadro


# In[13]:


sjodatoscuadro['nacionales']


# In[14]:


promediomensual = sjodatoscuadro.mean().unstack().T


# In[15]:


promediomensual


# In[16]:


plt.style.use('seaborn')
fig, axs= plt.subplots(2,12, figsize=[10,4], sharex=True, sharey='row')

sjodatoscuadro['nacionales'].plot(subplots=True, ax=axs[0],legend=False);
for ax, (mes, mean) in zip(axs[0], promediomensual['nacionales'].iteritems()):
    ax.set_title(mesescorto[mes-1])
    color = ax.lines[0].get_color()
    ax.axhline(mean, color=color, ls=':')
    ax.grid(False)
    

sjodatoscuadro['extranjeros'].plot(subplots=True, ax=axs[1],legend=False);
for ax, (mes, mean) in zip(axs[1], promediomensual['extranjeros'].iteritems()):
    color = ax.lines[0].get_color()
    ax.axhline(mean, color=color, ls=':')
    ax.grid(False)    
    ax.set_xlabel('')
    
axs[0,0].set_xticks([2010,2014,2018])
axs[0,0].set_xticklabels(['10','14','18'])


axs[0,0].set_ylabel('nacionales', size=14)
axs[1,0].set_ylabel('extranjeros', size=14)

fig.suptitle('Miles de pasajeros del aeropuerto Juan Santamaría, por mes y residencia', size=16)
fig.savefig(figpath+'SJO-pasajeros-por-mes.pdf', bbox_inches='tight')


# ### Cada año como serie individual, meses en el eje horizontal

# In[17]:


fig, axs= plt.subplots(1,2, figsize=[10,3.5], sharex=True)

sjodatoscuadro['nacionales'].T.plot(ax=axs[0], cmap = 'Blues', marker='o', legend=False);
sjodatoscuadro['extranjeros'].T.plot(ax=axs[1], cmap = 'Blues', marker='o', legend=False);


for ax,tlt in zip(axs, ['Nacionales', 'Extranjeros']):
    ax.set(xlabel='', 
           xticks=[3,6,9,12], 
           xticklabels = mesescorto[2::3], 
           xlim=[0.5,13.25],
           ylabel='miles de pasajeros')
    ax.grid(False, axis='y')
    ax.set_title(tlt, size=14)
    colores = [aa.get_color() for aa in ax.lines]
    for (a,v), cc in zip(sjodatoscuadro[tlt.lower()].T.loc[12].iteritems(), colores):
        ax.annotate(str(a), [12, v], color=cc)
        
fig.savefig(figpath+'SJO-pasajeros-por-mes2.pdf', bbox_inches='tight')        


# ## Estudiando la autocorrelación

# In[18]:


def correlogramas4(serie, residencia, func):
    fig, axs= plt.subplots(2,2, figsize=[15,4], sharex=True, sharey=True)
    opts = dict(lags=24)
    if func is plot_pacf:
        opts['method'] = 'ols'
    
    func(serie, **opts,ax=axs[0,0], title='$y_t$');
    func(serie.diff(1).dropna(), **opts, ax=axs[0,1],title='$\Delta y_t$');
    func(serie.diff(12).dropna(), **opts, ax=axs[1,0],title='$\Delta_{12}y_t$');
    func(serie.diff(1).diff(12).dropna(), **opts, ax=axs[1,1],title='$\Delta\Delta_{12}y_t$');
    
    for ax in axs.flat:
        ax.set(xlim=[-0.5,24.5], xticks=np.arange(0,25,6))
    
    pp = 'parcial' if (func is plot_pacf) else ''
    fig.suptitle(f'Correlogramas {pp} de cantidad de pasajeros {residencia} en SJO', size=18)
    return fig


# In[19]:


nacionales = pd.DataFrame(np.log(sjodatos['nacionales'].values), index=pd.period_range('2011-01', '2019-12', freq='M'))
correlogramas4(nacionales, 'nacionales', plot_acf);


# In[20]:


correlogramas4(nacionales, 'nacionales', plot_pacf);


# In[21]:


extranjeros = pd.DataFrame(np.log(sjodatos['extranjeros'].values), index=pd.period_range('2011-01', '2019-12', freq='M'))
fig = correlogramas4(extranjeros, 'extranjeros', plot_acf);
fig.savefig(figpath+'sjo-ACF-extranjeros.pdf', bbox_inches='tight')


# In[22]:


correlogramas4(extranjeros, 'extranjeros', plot_pacf);


# ## Estimación de un modelo SARIMA

# ### Selección de orden usando X13

# #### Pasajeros nacionales

# In[23]:


resultado = x13_arima_select_order(nacionales, x12path=x13path, log=False)
print(f"Modelo escogido: SARIMA{resultado['order']}X{resultado['sorder']}")


# #### Pasajeros extranjeros

# In[24]:


resultado = x13_arima_select_order(extranjeros, x12path=x13path, log=False)
print(f"Modelo escogido: SARIMA{resultado['order']}X{resultado['sorder']}")


# ### Estimación del modelo

# #### Pasajeros nacionales

# In[25]:


mod_nacionales = SARIMAX(nacionales, order=(0,1,2), seasonal_order=(0,1,1,12)).fit()
mod_nacionales.summary()


# #### Pasajeros extranjeros

# In[26]:


mod_extranjeros = SARIMAX(extranjeros, order=(0,1,1), seasonal_order=(0,1,1,12)).fit()

with open(figpath+'SJO-extranjeros-SARIMA.tex','w') as archivo:
    archivo.write(mod_extranjeros.summary().as_latex())
    
mod_extranjeros.summary()


# ### Pronósticos

# In[27]:


def plot_forecast(modelo, serie, residencia, ax):
    fcast = modelo.get_forecast('2020-12')
    ci = np.exp(fcast.conf_int())
    np.exp(fcast.predicted_mean).plot(ax=ax)
    ax.fill_between(ci.index,'lower y', 'upper y', data=ci, alpha=0.5)    
    np.exp(serie).plot(ax=ax, legend=False)
    ax.set(title=f'Pronóstico de pasajeros {residencia} en aeropuerto SJO')
    return ax


# In[28]:


fig, ax = plt.subplots(1,1, figsize=[8,3])
plot_forecast(mod_extranjeros, extranjeros['2015':], 'extranjeros', ax)
ax.set(ylabel='miles de pasajeros')
fig.savefig(figpath+'SJO-sarima-extranjeros-forecast.pdf', bbox_inches='tight')


# In[29]:


def cuadro(residencia):
    temp = sjodatoscuadro[residencia]
    temp.columns = mesescorto
    temp.index.name = ''
    temp.columns.name= ''
    temp.round(0).astype(int).reset_index().to_latex(figpath + f'cuadro-SJO-{residencia}.tex', index=False)
    return temp


# In[30]:


ilustrado = cuadro('extranjeros').round(1).astype(str).iloc[5:,4:8]

v2019 = ilustrado.iloc[-1].values.copy()
rezagos = ['-36', '-24', '-12',r'\phantom{-00}']

ilustrado['May'] = ['']*4
ilustrado['Jun'] = ['']*4
ilustrado['Ago'] = [f'$y_{{t{lag}}}={v}$' for lag, v in zip(rezagos, ilustrado['Ago'])]
ilustrado['Jul'] = [f'$y_{{t{lag}-1}}$' for lag in rezagos]
ilustrado.iloc[-1,:3] = [f'$y_{{t{lag}}}={v}$' for lag, v in zip(['-3','-2','-1'], v2019[:-1])]
ilustrado.reset_index().to_latex(figpath + 'cuadro-SJO-ilustrado.tex',escape=False, index=False)
ilustrado


# ## Descomposición de una serie usando X13

# In[31]:


def X13ARIMA(serie, show=False):
    
    res = x13_arima_analysis(serie, x12path=x13path, log=False)
    if show:
        print(res.results)
    temp = pd.concat([res.__getattribute__(componente) for componente in ['observed','seasadj','trend','irregular']], axis=1)
    temp.columns = ['Serie original','Serie ajustada por estacionalidad','Serie tendencia ciclo','Componente irregular']
    return temp


# In[32]:


componentes = X13ARIMA(extranjeros, False)


# In[33]:


componentes


# In[34]:


fig = plt.figure(figsize=[12,6])
gs = plt.GridSpec(3,1,figure=fig, height_ratios=[4,1,1])
ax0 = fig.add_subplot(gs[0])
np.exp(componentes.iloc[:,:3]).plot(ax=ax0)

ax1 = fig.add_subplot(gs[1],sharex=ax0)
sfact = componentes['Serie original'] - componentes['Serie ajustada por estacionalidad']
np.exp(sfact).plot(ax=ax1)


ax2 = fig.add_subplot(gs[2],sharex=ax0, sharey=ax1)
np.exp(componentes['Componente irregular']).plot(ax=ax2)

ax0.set(title='Series original, ajustada por estacionalidad, y tendencia-ciclo')
ax1.set(title='Factor estacional')
ax2.set(title='Componente irregular')
fig.suptitle('Descomposición multiplicativa de la serie de pasajeros extranjeros en SJO, X13as', size=18)

fig.savefig(figpath+'SJO-extranjeros-descomposición.pdf', bbox_inches='tight')


# ### Graficando los factores

# In[35]:


factores2019 = np.exp(sfact['2019':'2019'])
etiq = [f'{ff:.2f}' for ff in factores2019]
fig, ax = plt.subplots(figsize=[9,3])

ax.bar(mesescorto, factores2019-1)
ax.set(yticks=np.array([0.6,0.8,1.0,1.2,1.4])-1, 
       yticklabels = ['0.6','0.8','1.0','1.2','1.4'], 
       ylim=[-0.45,0.45])

ax.grid(False)
ax.axhline(0, color='red')

for mes, ff, tx in zip(range(12), factores2019.values, etiq):
    offs = -1.025 if ff<1 else -0.975
    ax.annotate(tx, (mes,ff+offs),ha='center', va='center')

ax.set(title='Factores estacionales de 2019')
fig.savefig(figpath+'SJO-extranjeros-seasonal-factor.pdf', bbox_inches='tight')


# In[36]:


factores2019


# ## Comparando la tasa de crecimiento obtenida a partir de series ajustadas

# In[37]:


fig, axs = plt.subplots(3,1,figsize=[12,6], sharex=True)

(100 * componentes[['Serie original','Serie tendencia ciclo']].diff(12)).plot(ax=axs[0])

(100 * componentes[['Serie original','Serie tendencia ciclo']].diff()).plot(ax=axs[1])

(100*((componentes[['Serie tendencia ciclo']].diff())*12)).plot(ax=axs[2])
(100 * componentes[['Serie tendencia ciclo']].diff(12)).plot(ax=axs[2])


axs[0].set(title='Tasa de crecimiento interanual')
axs[1].set(title='Tasa de crecimiento mensual')
axs[2].set(title='Tasa de crecimiento de la serie tendencia-ciclo')
axs[2].legend(['Mensual, anualizada', 'Interanual'])

for ax in axs:
    ax.grid(False)
    
fig.savefig(figpath+'SJO-extranjeros-tasa-crecimiento.pdf', bbox_inches='tight')    

