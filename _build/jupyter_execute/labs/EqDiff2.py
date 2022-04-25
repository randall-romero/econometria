#!/usr/bin/env python
# coding: utf-8

# # Resolviendo una ecuación en diferencia con `sympy`

# Este cuaderno resuelve la ecuación en diferencia
# \begin{equation*}
# y_t = 0.9y_{t-1} -0.2y_{t-2} + 3
# \end{equation*}
# 
# que está incluida en el tema "2. Ecuaciones en diferencia".

# In[1]:


import numpy as np
from sympy import Function, rsolve
from sympy.abc import t
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

y = Function('y')


# ## Solución analítica

# ### Solución ecuación homogénea

# In[2]:


rsolve(y(t) - 0.9*y(t-1) + 0.2*y(t-2), y(t))


# ### Solución general

# In[3]:


rsolve(y(t) - 0.9*y(t-1) + 0.2*y(t-2) - 3, y(t))


# ### Solución general con condiciones iniciales

# In[4]:


z = rsolve(y(t) - 0.9*y(t-1) + 0.2*y(t-2) - 3, y(t), {y(0):13, y(1): 11.3})
z


# In[5]:


tt = np.arange(13)
plt.plot(tt, 2*0.4**tt+0.5**tt+10, 'ro-', markersize=12)


# ## Solución recursiva a partir de condiciones iniciales

# In[6]:


T = 13
Y = np.zeros(T)
Y[:2] = 13, 11.3


for t in range(2, T):
    Y[t] = 0.9*Y[t-1]-0.2*Y[t-2] + 3

plt.plot(Y,'ro-', markersize=12)

