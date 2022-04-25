#!/usr/bin/env python
# coding: utf-8

# # Números complejos

# ```{include} ../../teoria/math-definitions.md
# ```

# In[1]:


import plotly.express as px
import numpy as np

import plotly.io as pio
pio.renderers.default = "colab" if 'google.colab' in str(get_ipython()) else 'iframe'


# ## Representación de números complejos
# ![](../../imgs/polar-complex.png)
# 
# 
# ## Multiplicación de números complejos
# 
# Si $ z = Re^{i\theta} $  y $ w = Se^{i\varphi} $ , entonces su producto es
# \begin{equation*}
# zw = RS e^{i(\theta+\varphi)}
# \end{equation*}
# 
# 
# Así, si elevamos $ z $  a la $ n $ -ésima potencia:
# \begin{equation*}
# z^n = \left(Re^{i\theta}\right)^n = R^ne^{in\theta}
# \end{equation*}
# 
# Es decir
# \begin{equation*}
# \lim\limits_{n\to\infty}z^n = 0 \Leftrightarrow | R | < 1
# \end{equation*}

# ## Ejemplos de potencia de números complejos
# 
# Cuando el módulo o valor absoluto $ R $  de un número complejo está por debajo de 1, su potencia tiende a cero conforme el exponente tiende a infinito:

# In[2]:


𝜃 = 30
t = np.arange(48)

px.scatter_polar(r=0.95**t, theta=t*𝜃,
                 animation_frame=t,
                 start_angle=0,
                 range_r=[0, 1.1],
                 direction='counterclockwise')


# Por el contrario, si $ R > 1 $ , la potencia tenderá alejarse cada vez más del origen:

# In[3]:


px.scatter_polar(r=1.03**t, theta=t*𝜃,
                 animation_frame=t,
                 start_angle=0,
                 range_r=[0, 4.5],
                 direction='counterclockwise')


# En el caso intermedio en que $ R = 1 $ , la potencia se mantendrá orbitando en la circunferencia unitaria:

# In[4]:


px.scatter_polar(r=1.0**t, theta=t*𝜃,
                 animation_frame=t,
                 start_angle=0,
                 range_r=[0, 1.5],
                 direction='counterclockwise')

