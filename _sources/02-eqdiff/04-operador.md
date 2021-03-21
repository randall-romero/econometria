```{include} ../math-definitions.md
```


# Solución por medio del operador de rezagos  


## Introducción

Este tema constituye una herramienta para simplificar el análisis de ecuaciones en diferencia

Se asumirá que todas las variables son determinísticas (no estocásticas).

Se limita la exposición a ecuaciones en diferencia lineales.



## Ecuación en diferencia de primer orden

En este caso
\begin{equation*}
y_t = \phi y_{t-1} + w_t
\end{equation*} 

Utilizando el operador de rezagos se resuelve así:
\begin{align*}
              y_t &= \phi\Lag y_{t} + w_t \\
(1 - \phi\Lag)y_t &=  w_t \\
\left(1 + \phi \Lag +\dots + \phi^t \Lag^t\right)(1 - \phi\Lag)y_t &=  \left(1 + \phi \Lag +\dots + \phi^t \Lag^t\right)w_t \\
\left(1 - \phi^{t+1} \Lag^{t+1}\right)y_t &=  w_{t} + \phi w_{t-1} +\dots + \phi^t w_{0}
\end{align*} 

Así
\begin{equation*}
y_t =  \phi^{t+1} y_{-1} + w_{t} + \phi w_{t-1} +\dots + \phi^t w_{0} 
\end{equation*}




## Solución de “largo plazo”

En este caso
\begin{align*}
(1 - \phi\Lag)y_t &=  w_t \\
\left(1 - \phi \Lag\right)^{-1}(1 - \phi\Lag)y_t &=  \left(1 + \phi \Lag + \phi^2 \Lag^2 + \dots\right)w_t \\
y_t &=  w_{t} + \phi w_{t-1} + \phi^2 w_{t-2}  + \dots
\end{align*} 
siempre y cuando $|\phi|< 1$.

## Ecuación en diferencia de orden $p$ 


La variable $y_t$ evoluciona como
\begin{equation*}
y_{t} = \phi_1y_{t-1} + \phi_2y_{t-2} + \dots + \phi_py_{t-p} + w_t
\end{equation*}

Con operador de rezagos:
\begin{equation*}
\left(1 - \phi_1 \Lag - \phi_2 \Lag^2 - \dots - \phi_p \Lag^p\right)y_t = w_t 
\end{equation*}

Para factorizar el polinomio es necesario resolver 
\begin{equation*}
f(z) \equiv 1 - \phi_1 z  - \phi_2 z^2 - \dots - \phi_p z^p = 0
\end{equation*}

Con el  cambio de variable $z=\frac{1}{\lambda}$ obtenemos
\begin{align*}
1 - \phi_1 \left(\tfrac{1}{\lambda}\right) - \phi_2 \left(\tfrac{1}{\lambda}\right)^2 - \dots - \phi_p  \left(\tfrac{1}{\lambda}\right)^p &= 0 \\
\lambda^p - \phi_1\lambda^{p-1} - \phi_2\lambda^{p-2} - \dots - \phi_{p-1}\lambda - \phi_p &= 0
\end{align*}

Esta es la misma expresión que se obtuvo con álgebra de matrices: por lo tanto las raíces de $f(z)$ son los **recíprocos** de las raíces anteriores.


## Estabilidad

Dada la relación existente entre las ecuaciones
\begin{align*}
1 - \phi_1 z  - \phi_2 z^2 - \dots - \phi_p z^p &= 0 \\
\lambda^p - \phi_1\lambda^{p-1} - \phi_2\lambda^{p-2} - \dots - - \phi_{p-1}\lambda - \phi_p &= 0
\end{align*}

está claro que para que el proceso sea estable es necesario que las raíces de 
\begin{equation*}
1 - \phi_1 z  - \phi_2 z^2 - \dots - \phi_p z^p = 0
\end{equation*}

estén **fuera** del círculo unitario, esto es, si $z_i$ es raíz, entonces $|z_i|>1$.


