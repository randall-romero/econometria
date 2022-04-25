#!/usr/bin/env python
# coding: utf-8

# # El operador de rezagos
# 
# Ejemplo numérico para ilustrar el uso de los operadores de rezago, diferencia, y diferencia estacional.

# ## Cargar paquetes necesarios

# In[1]:


import pandas as pd


# ## Importar los datos

# * Leer una serie de tiempo ficticia de data\LandD.csv y mostrarlos

# In[2]:


GITHUB_REPO = "https://raw.githubusercontent.com/randall-romero/econometria/master/data/"
DATAPATH = GITHUB_REPO if 'google.colab' in str(get_ipython()) else '../data/'

datos = pd.read_csv(DATAPATH + 'LandD.csv', index_col=0, parse_dates=True)
datos.columns


# ## Obtener las series transformadas

# * Operador de rezagos

# In[3]:


datos['Lag_y'] = datos['y'].shift(1)
datos['Lag2_y'] = datos['y'].shift(2)


# * Operador de diferencias
# \begin{align*}
# \Delta y_t &= (1-L)y_t = y_t - y_{t-1} \\
# \Delta^2 y_t &= (1-L)^2y_t = y_t - 2y_{t-1} + y_{t-2}
# \end{align*}

# In[4]:


datos['D_y'] = datos.y.diff()
datos['D2_y'] = datos.y.diff(1).diff(1)


# * Operador de diferencia estacional
# 
# \begin{equation*}
# \Delta_4 y_t = (1-L^4)y_t = y_t - y_{t-4}
# \end{equation*}

# In[5]:


datos['S_y'] = datos.y.diff(4)


# * Mostrar los resultados

# In[6]:


datos


# Nótese que a pesar de que la serie original está en números enteros, las demás están en floats (dependiendo de su versión de pandas). Esto se debe a que versiones de Pandas anteriores a la 1.0 no tienen un valor para datos faltantes (NaN) para números enteros.
