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
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
pd.options.plotting.backend = "plotly"
```


# Cambio estructural y raíces unitarias: fecha desconocida


## ¿Cómo saber cuándo se produjo un cambio estructural?

Un supuesto importante en la prueba de \textcite{Perron1989} es que el analista conoce la fecha en que se produjo el (único) cambio estructural. No obstante, esto no siempre es factible.

\textcite{Zivot1992} proponen una prueba de raíz unitaria similar a la de Perron, pero que asume que el momento del cambio estructural es desconocido.









## Las pruebas de cambio estructural de Zivot y Andrews

{{ empieza_test }} Las pruebas de cambio estructural de Zivot y Andrews {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
¿Hay raíces unitarias en presencia de un cambio estructural en $t=\tau$?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
\begin{align*}
y_t &= \mu +  y_{t-1}  + \epsilon_{t} \tag{nula}\\
y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \alpha_2 t  + \epsilon_{t} \tag{alternativa A}\\
y_t &= \alpha_0 + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa B} \\
y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa C}
\end{align*}
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`calculator;test-simbolo`
Para implementar la prueba de Zivot y Andrews se siguen estos pasos:

{bdg-dark}`Paso 1:` Se estima la regresión correspondiente al modelo
\begin{align*}
\textcolor{Chartreuse4}{A: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \mu_2 D_t^L \phantom{+ \mu_3 D^T_t}  &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t} \\
\textcolor{Chartreuse4}{B: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \phantom{\mu_2 D_t^L +} \mu_3 D^T_t  &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t}  \\
\textcolor{Chartreuse4}{C: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \mu_2 D_t^L + \mu_3 D^T_t &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t}
\end{align*}
donde los términos $D_t^L$ y $D_t^T$ dependen de la proporción de datos $\lambda$ anteriores al cambio estructural:
\begin{align*}
D_t^L(\lambda) &= I(t>\lambda T)  &  D_t^T &=\max(t-\lambda T, 0)
\end{align*}

{bdg-dark}`Paso 2:` Se calcula el estadístico $t$ de la hipótesis $a_1=1$:
\begin{equation*}
t_{\alpha_1} = \frac{\hat{\alpha_1}-1}{s.e.(\alpha_1)}
\end{equation*}
Observemos que el valor estimado $\hat{\alpha}$ dependerá de $\lambda$; por ello, escribimos $t_{\alpha_1}(\lambda)$

{bdg-dark}`Paso 3:` Se define el punte de quiebre $\hat{\lambda}$ como aquel valor $\lambda$ que hace más plausible la hipótesis alternativa
\begin{equation*}
\hat{\lambda} \equiv \argmin{\lambda\in(0, 1)}\left\{ t_{\alpha_1}(\lambda) \right\}
\end{equation*}
:::

:::{grid-item} 
:outline: 
:columns: 4
{fas}`lightbulb;test-simbolo` 
Se compara el valor mínimo $t_{\alpha_1}(\hat\lambda)$ con el valor crítico de Zivot y Andrews. Si el estadístico estimado es menor que el valor crítico, se rechaza la hipótesis nula.
:::
::::

**Valores críticos de Zivot y Andrews**
| Modelo   |    1% |    5% |   10% |
|:---------|------:|------:|------:|
| A        | -5.34 | -4.80 | -4.58 |
| B        | -4.93 | -4.42 | -4.11 |
| C        | -5.57 | -5.08 | -4.82 |

Fuente: \textcite{Zivot1992}

{{ termina_test }}



{{ empieza_ejemplo }} Pruebas de cambio estructural {{ fin_titulo_ejemplo }}

\textcite{Zivot1992} también analizan los datos de Nelson y Plosser. Al estimar el modelo A encuentran

\input{labs/zivot-andrews-nelson-plosser.tex}


Recordemos los valores críticos del modelo A
**Valores críticos de Zivot y Andrews**
| Modelo   |    1% |    5% |   10% |
|:---------|------:|------:|------:|
| A        | -5.34 | -4.80 | -4.58 |


A continuación vemos cómo replicar los resultados del modelo A de Zivot y Andrews, escribiendo un programa de Python.

\begin{equation*}
y_t = \alpha_0 + \alpha_1 y_{t-1} + \alpha_2 t  + \mu_2 D_t^L  + \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t}
\end{equation*}


```{code-cell} ipython3
:tags: ["hide-input",]
NP = pd.read_stata('../../data/NelsonPlosserData.dta', index_col='year')
NP.index = NP.index.year

def ZivotAndrewsA(serie, k=8):
    dta = NP[[serie]].dropna()
    dta.rename(columns={serie:'y'}, inplace=True)
    dta['t'] = np.arange(dta.shape[0])
    dta['Ly'] = dta['y'].shift(1)
    dta['Dy'] = dta['y'].diff(1)
    for j in range(1, k+1):
        dta[f'D{j}y'] = dta['Dy'].shift(j)    

    lags = '+'.join(dta.columns[-k:])

    alpha1values = pd.Series(0.0, index=dta.index[12:-12])

    for tau in alpha1values.index:
        dta['DL'] = (dta.index>tau).astype(int)
        modelo = ols('y ~ Ly + t + DL + ' + lags, dta).fit()
        alpha1values[tau] = ((modelo.params - 1)/modelo.bse)['Ly']

    tauhat, tval = alpha1values.idxmin(), alpha1values.min()
    dta['DL'] = (dta.index>tauhat).astype(int)
    modelo = ols('y ~ Ly + t + DL + ' + lags, dta).fit()

    return {r'$\hat{T}_B$':tauhat, r'$\alpha_1$': np.round(modelo.params['Ly'],3), r'$t$': np.round(tval,2)}



seriesA = ['lrgnp', 'lgnp', 'lpcrgnp', 'lip', 'lemp', 'lprgnp', 'lcpi', 'lwg', 'lm']
lags = [8,8,7,8,7,5,2,7,6]
variables = {'lrgnp':'Real GNP',
           'lgnp':'Nominal GNP',
           'lpcrgnp':'Real per capita GNP',
           'lip':'Industrial production',
           'lemp':'Employment',
           'lun':'Unemployment rate',
           'lprgnp':'GNP deflator',
           'lcpi':'Consumer prices',
           'lwg':'Wages',
           'lrwg':'Real wages',
           'lm':'Money stock',
           'lvel':'Velocity',
           'bnd':'Bond yield',
           'lsp500':'Common stock prices'}


temp = pd.DataFrame([ZivotAndrewsA(ser, k) for ser, k in zip(seriesA, lags)], index=seriesA)
temp.rename(index=variables)
```



{{ termina_ejemplo }}
