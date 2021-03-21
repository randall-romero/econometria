---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
substitutions:
  empieza_ejemplo: |
    <div class="ejemplo">
    <div class="ejemplo-titulo"><b>Ejemplo: &nbsp;
  fin_titulo_ejemplo: "</b></div>"
  termina_ejemplo: "</div>"
---


```{include} ../math-definitions.md
```

```{code-cell} ipython3
:tags: ["hide-input",]
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from macrodemos.demo_ARMA import ARMA
from macrodemos.common_components import merge_plots
```



# Proceso autorregresivo de media móvil ARMA(p,q)

## Procesos ARMA
```{important} Definición: proceso ARMA

Sea $\left\{\epsilon_t\right\}$ un proceso ruido blanco; el proceso estocástico
\begin{equation*}
y_t = c + \phi_1y_{t-1} + \dots + \phi_py_{t-p} + \epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}
\end{equation*}

con $\phi_p, \theta_q \neq 0$ es llamado un proceso ARMA(p,q).
```


ARMA  = **A**uto**R**egressive **M**oving **A**verage, (autorregresivo media móvil)

Los procesos ARMA son importantes porque todo proceso estacionario puede ser aproximado por un proceso ARMA.



Similar a lo que encontramos con los procesos AR(p), si asumimos que es estacionario su media satisface la relación
\begin{equation*}
\mu = c + \phi_1\mu + \dots + \phi_p\mu
\end{equation*}

Por lo que el proceso puede escribirse sin el intercepto, si expresamos la variable $y$ como desviación de su media
\begin{equation*}
\tilde{y}_t = \phi_1\tilde{y}_{t-1} + \dots + \phi_p\tilde{y}_{t-p} + \epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}
\end{equation*}

Las fórmulas para la varianza y la autocovarianza se obtienen aplicando las definiciones del caso, pero tienden a ser más complicadas.




## Estabilidad e invertibilidad de un proceso ARMA

El proceso  $\tilde{y}_t = \phi_1\tilde{y}_{t-1} + \dots + \phi_p\tilde{y}_{t-p} + \epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}$ puede expresarse en términos de polinomios de rezagos:
\begin{align*}
\tilde{y}_t - \phi_1\tilde{y}_{t-1} - \dots - \phi_p\tilde{y}_{t-p} &= \epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}\\
\left(1 - \phi_1\Lag - \dots - \phi_p\Lag^p\right)\tilde{y}_t &= \left(1 + \theta_1\Lag + \dots + \theta_q\Lag^q\right)\epsilon_t\\
\Phi(\Lag)\tilde{y}_t &= \Theta(\Lag)\epsilon_t
\end{align*}


```{panels}
Estabilidad
^^^
Si las raíces del polinomio $\Phi(z)$ están todas fuera del círculo unitario, el proceso es **estable**.
\begin{equation*}
\tilde{y}_t = \Phi(\Lag)^{-1}\Theta(\Lag)\epsilon_t
\end{equation*}


---
Invertibilidad
^^^
Si las raíces del polinomio $\Theta(z)$ están todas fuera del círculo unitario, el proceso es **invertible**.
\begin{equation*}
\epsilon_t = \Theta(\Lag)^{-1}\Phi(\Lag)\tilde{y}_t
\end{equation*}

```


## Sobreparametrización de un proceso ARMA

Supongamos que tenemos un proceso ARMA(p, q) $\Phi(\Lag)y_t = \Theta(\Lag)\epsilon_t$, en el cual los polinomios $\Theta(\Lag)$ tiene una raíz en común. En este caso podemos
\begin{align*}
\Phi(\Lag)y_t &= \Theta(\Lag)\epsilon_t\\
(1-r\Lag)\Phi^*(\Lag)y_t &= (1-r\Lag)\Theta^*(\Lag)\epsilon_t\\
\Phi^*(\Lag)y_t &= \Theta^*(\Lag)\epsilon_t
\end{align*}


Es decir, podemos representar el mismo proceso con un modelo ARMA(p-1, q-1).

Decimos que:

* el modelo ARMA(p,q) está **sobreparametrizado**.
* el modelo ARMA(p-1, q-1) es una representación más **parsimoniosa** del proceso generador de datos.



{{ empieza_ejemplo }} Sobreparametrización {{ fin_titulo_ejemplo }}

Consideremos estos dos procesos ARMA
\begin{align*}
y_t &= 1.3y_{t-1}-0.4y_{t-2}+\epsilon_t+0.1\epsilon_{t-1} -0.3\epsilon_{t-2} \tag{ARMA(2,2)}\\
y_t &= 0.8y_{t-1} +\epsilon_t+0.6\epsilon_{t-1} \tag{ARMA(1,1)}
\end{align*}

```{code-cell} ipython3
:tags: ["hide-input",]
arma22 = ARMA(phi=[1.3, -0.4], theta=[0.1, -0.3])
arma11 = ARMA(phi=[0.8], theta=[0.6])


merge_plots(
   [arma22.plot_correlogram(18), arma11.plot_correlogram(18), arma22.plot_partial_correlogram(18), arma11.plot_partial_correlogram(18)],
   cols=2,
   subplot_titles=[str(arma22), str(arma11)],
   title_text='Autocorrelación (arriba) y autocorrelación parcial (abajo)',
)
```

¡Sus funciones ACF y PACF son idénticas!


Las raíces de los polinomios de rezagos del proceso ARMA(2,2)


```{code-cell} ipython3
:tags: ["hide-input",]
arma22.plot_ar_roots()
```

```{code-cell} ipython3
:tags: ["hide-input",]
arma22.plot_ma_roots()
```


Vemos que ambas tienen a $z=0.5$ como una raíz.

Al “eliminarla” de ambos polinomios, terminamos con el mismo proceso pero con menos parámetros.

Esta representación ARMA(1, 1) es una versión más **parsimoniosa** del mismo proceso.
{{ termina_ejemplo }}
