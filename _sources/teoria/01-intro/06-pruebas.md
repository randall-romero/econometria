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
  empieza_test: |
    <div class="test">
    <div class="test-titulo">
  fin_titulo_test: "</div>"
  termina_test: "</div>"
  test_inquietud: |
    <i class="fas fa-question test-simbolo"></i>
  test_hipotesis: |
    <br><hr><i class="fas fa-heading test-simbolo"></i>
  test_estadistico: |
    <br><hr><i class="fas fa-calculator test-simbolo"></i>
  test_interpretacion: |
    <br><hr><i class="far fa-lightbulb test-simbolo"></i>
---


```{include} ../math-definitions.md
```

```{code-cell} ipython3
:tags: ["hide-input",]
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
import pandas as pd
import statsmodels.api as sm
```



# Pruebas de series de tiempo



## Determinando si una serie de tiempo es ruido blanco

Cuando se estiman modelos de series de tiempo, es importante evaluar si los residuos de la estimación corresponden a una realización de un proceso de ruido blanco.

Recordando que un proceso ruido blanco $\left\{\epsilon_t\right\}$ es tal que
\begin{align*}
		\E\left(\epsilon_t\right) &=0 \tag{media cero}\\
		\E\left(\epsilon^2_t\right) &= \sigma^2 \tag{varianza constante}\\
		\E\left(\epsilon_t\epsilon_\tau\right) &= 0 \quad\text{for }t\neq\tau \tag{términos no correlacionados}
		\end{align*}

una forma natural de evaluar si los residuos son ruido blanco es determinar si las autocorrelaciones
\begin{equation*}
\rho_1 = \rho_2 = \dots =\rho_\tau = 0
\end{equation*}
para todo $\tau\geq 1$


## Test de Box-Pierce

{{ empieza_test }} Test de Box-Pierce (1970)  {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
¿Es esta serie  un caso de ruido blanco?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
$\rho_1 = \rho_2 = \dots =\rho_m = 0$ (sí es ruido blanco)
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`calculator;test-simbolo`
\begin{equation*}
Q^{*} = T\sum_{j=1}^{m}\hat{\rho}_j^2 \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
\end{equation*}
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`lightbulb;test-simbolo` 
Si $Q^{*} > \chi_{m-k}(1-\alpha)$, rechazar $H_0$ con $100\alpha\%$ de significancia: la serie no es ruido blanco.

La intuición es que si la serie no es ruido blanco, algunos $\hat{\rho}_j$ serán “muy grandes”, y entonces $Q^*$ también lo será.
:::
::::
{{ termina_test }}








## Test de Ljung-Box

{{ empieza_test }} Test de Ljung-Box (1978) {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
¿Es esta serie  un caso de ruido blanco?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
$\rho_1 = \rho_2 = \dots =\rho_m = 0$ (sí es ruido blanco)
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`calculator;test-simbolo`
\begin{equation*}
Q = T(T+2)\sum_{j=1}^{m}\frac{\hat{\rho}_j^2}{T-j} \; \overset{\text{asy}}{\sim} \; \chi^2_{m-k}
\end{equation*}

$k$ es número de parámetros estimados
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`lightbulb;test-simbolo` 
Si $Q^{*} > \chi_{m-k}(1-\alpha)$, rechazar $H_0$ con $100\alpha\%$ de significancia: la serie no es ruido blanco.

Este test es similar al de Box-Pierce, pero ajustada para muestras pequeñas.
:::
::::
{{ termina_test }}




## Test de Durbin-Watson
<!-- %Greene 2018, p1001-1003 -->

{{ empieza_test }} Test de Durbin-Watson (1950/1) {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
Inquietud:** ¿Hay autocorrelación de primer orden en esta serie?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
$\rho_1 = 0$ (no hay autocorrelación)
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`calculator;test-simbolo`
\begin{equation*}
d = \frac{\sum_{t=2}^{T}(e_t-e_{t-1})^2}{\sum_{t=1}^{T}e_t^2} \approx 2\left(1-\hat{\rho}_1 \right)\qquad \text{(si T es grande)}
\end{equation*}
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`lightbulb;test-simbolo` 
Si $d$ está “lejos” de 2 según los valores críticos de DW, rechazar $H_0$: la serie sí presenta autocorrelación.

Esta prueba no es válida para residuos de una ecuación donde haya rezagos de la variable dependiente.
:::
::::
{{ termina_test }}


## Ventajas de Box-Pierce / Ljung-Box sobre Durbin-Watson

1.  Box-Pierce / Ljung-Box evalúan la existencia de autocorrelación de cualquir orden, no solo de primer orden.
2.  Sus resultados también son válidos para evaluar residuos de regresiones que contienen rezagos de la variable dependiente.



{{ empieza_ejemplo }} Pruebas de ruido blanco {{ fin_titulo_ejemplo }}

```{margin} Archivos
* log_imae.csv
* euro.csv
* wntest.ipynb
* wntest.do
```

**Crecimiento del IMAE**

Los resultados de las pruebas Ljung-Box son consistentes con lo que obtuvimos a partir de un autocorrelograma: el crecimiento mensual del IMAE no es ruido blanco.
```{image} ../../imgs/wntest-imae-corrgram.PNG
:scale: 30%
```
```{image} ../../imgs/wntest-imae-plot.PNG
:scale: 30%
```
```{image} ../../imgs/wntest-imae-rho.PNG
:scale: 30%
```

**Cambios en el tipo EUR/USD**

Las pruebas Ljung-Box **no rechazan** que esta serie sea ruido blanco. Pero en la gráfica parece que la varianza no es constante, por lo que posiblemente la serie tampoco sería ruido blanco.
```{image} ../../imgs/wntest-euro-corrgram.PNG
:scale: 30%
```
```{image} ../../imgs/wntest-euro-plot.PNG
:scale: 30%
```
```{image} ../../imgs/wntest-euro-rho.PNG
:scale: 30%
```
{{ termina_ejemplo }}

## De no-correlación a independencia y normalidad

El hecho de que una serie no esté autocorrelacionada no implica que sus elementos sean independientes o que estén normalmente distribuidos.

Ausencia de autocorrelación implica independencia solamente si las variables están normalmente distribuidas.

Usualmente se asume normalidad del proceso estocástico, porque muchos tests dependen de este supuesto.

Para evaluar si este supuesto es apropiado, analizamos los momentos tercero (asimetría) y cuarto (kurtosis).



## Test de normalidad

{{ empieza_test }} Test de Jarque-Bera (1980) {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
¿Es esta serie  normal?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
$S\equiv\E\left(\frac{y-\mu}{\sigma}\right)^3 = 0,\; K\equiv\E\left(\frac{y-\mu}{\sigma}\right)^4 = 3$ (sí es)
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`calculator;test-simbolo`
\begin{equation*}
JB = \frac{T}{6}\left(\hat{S}^2 + \tfrac{1}{4}\left(\hat{K}-3\right)^2\right) \;\sim\chi^2_2
\end{equation*}
:::

:::{grid-item} 
:outline: 
:columns: 6
{fas}`lightbulb;test-simbolo` 
Si $JB > \chi^2_{2}(1-\alpha)$, rechazar $H_0$ con $100\alpha\%$ de significancia: la serie no es normal.
:::
::::
{{ termina_test }}



## Referencias {-}

```{bibliography}
:filter: docname in docnames
```
