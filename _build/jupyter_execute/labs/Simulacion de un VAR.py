#!/usr/bin/env python
# coding: utf-8

# # Simulación de un VAR(1)

# Suponga el siguiente modelo dinámico
# 
# \begin{align*}
# x_t &= 4 + 0.8x_{t-1} + y_{t-1} + \epsilon_{x,t} \\
# y_t &= 1 + 0.1x_{t-1} + 0.5y_{t-1} + \epsilon_{y,t}
# \end{align*}
# 
# que puede escribirse
# \begin{equation*}
# \underset{X_t}{\begin{pmatrix}x_t \\ y_t\end{pmatrix}} = 
# \underset{c}{\begin{pmatrix}0.9 \\ 1.8\end{pmatrix}} +
# \underset{A}{\begin{pmatrix}0.8 & 0.7 \\ -0.2 & 0.8\end{pmatrix}}
# \underset{X_{t-1}}{\begin{pmatrix}x_{t-1} \\ y_{t-1}\end{pmatrix}} +
# \underset{\epsilon_t}{\begin{pmatrix}\epsilon_{x,t} \\ \epsilon_{y,t}\end{pmatrix}}
# \end{equation*}
# 
# con matriz de correlaciones de los errores reducidos
# \begin{equation*}
# \Omega = E\left[\underset{\epsilon_t}{\begin{pmatrix}\epsilon_{x,t} \\ \epsilon_{y,t}\end{pmatrix}}\underset{\epsilon'_t}{\begin{pmatrix}\epsilon_{x,t} & \epsilon_{y,t}\end{pmatrix}}\right] =
# E\begin{pmatrix}\epsilon^2_{x,t} & \epsilon_{x,t}\epsilon_{y,t} \\ \epsilon_{y,t}\epsilon_{x,t} & \epsilon^2_{y,t}\end{pmatrix} =
# \begin{pmatrix}0.0400 & 0.0280 \\ 0.0280 & 0.0596\end{pmatrix}
# \end{equation*}
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pandas as pd
from statsmodels.tsa.api import VAR


# ## Simulando los datos 

# Vamos a simular una muestra de 100 observaciones de un VAR(1). Empezamos por ingresar los valores de los parámetros

# In[2]:


T = 100

A = np.array([[0.8, 0.7], [-0.2, 0.8]])
c = np.array([[0.9], [1.8]])


# In[3]:


Ω = 0.04*np.array([[1, 0.7],[0.7,1.49]])


# Calculamos la descomposición de Cholesky para poder simular la correlación de los errores

# In[4]:


P = np.linalg.cholesky(Ω)
P


# Fijamos una semilla para el generador de números aleatorios, para obtener resultados replicables.

# In[5]:


np.random.seed(16)


# Calculamos la media del proceso $\mu = (I-A)^{1}c$ y lo usamos como valor inicial de la simulación.

# In[6]:


𝜇 = (np.linalg.inv(np.eye(2) - A) @ c)

X = np.zeros((T,2))
X[0] = 𝜇.T

for t in range(1, T):
    X[t] = c.T + X[t-1] @ A.T + np.random.randn(2) @ P.T


# Guardamos los datos simulados como un DataFrame de pandas y los graficamos

# In[7]:


trimestres = pd.date_range(start='1992q1', freq='Q', periods=T)
data = pd.DataFrame(X, columns=['cantidad', 'precio'], index=trimestres)

fig, axs = plt.subplots(1,2,figsize=[12,4])
data.plot(subplots=True, ax=axs);


# ## Determinando si el VAR es estable
# 
# Para ello calculamos los valores propios de la matriz A, y comprobamos si estan en el círculo unitario

# In[8]:


eigenvalues = np.linalg.eigvals(A)
print('Los eigenvalores son ', eigenvalues)
print('y sus modulos son', abs(eigenvalues))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, polar=True)

ax.plot(np.angle(eigenvalues), abs(eigenvalues),marker='o',linewidth=0)
ax.set(ylim=[0,1], yticks=[1], yticklabels=[''], xticks=np.arange(4)*np.pi/2)

ax.annotate('$\lambda_1$',[0.5,1.0], fontsize=16)
ax.annotate('$\lambda_2$',[-0.5,1.0], fontsize=16);


# ## Estimación del VAR a partir de los datos simulados

# In[9]:


model = VAR(data)


# Determinamos el rezago óptimo

# In[10]:


model.select_order(5).summary()


# Estimamos el VAR con un único rezago

# In[11]:


results = model.fit(maxlags=1)
results.summary()


# ## Pruebas de causalidad de Granger
# 
# En ambos casos, las pruebas confirman que una variable tiene capacidad predictiva sobre la otra variable.

# In[12]:


results.test_causality('precio', 'cantidad').summary()


# In[13]:


results.test_causality('cantidad', 'precio').summary()


# ## Funciones de impulso respuesta
# 
# Simulamos impulsos unitarios. A la izquierda, el impulso es $\begin{pmatrix}1 \\ 0\end{pmatrix}$ (un choque de una unidad en la cantidad); a la derecha el impulso es $\begin{pmatrix}0 \\ 1\end{pmatrix}$ (un choque de una unidad en el precio).

# In[14]:


results.irf(24).plot();


# ## Pronosticando los siguientes datos
# 
# Vemos que después de un tiempo los pronósticos convergen a la media estimada del proceso (en rojo).

# In[15]:


fig = results.plot_forecast(36)

for i in range(2):
    fig.axes[i].axhline(𝜇[i], ls=':')
    fig.axes[i].axhline(results.mean()[i], color='r')

