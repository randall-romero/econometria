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
import pandas as pd
```



# El operador de rezagos

## Definición de operador de series de tiempo

Un operador de serie de tiempo es un “proceso” que transforma una o más series de tiempo en nuevas series de tiempo.

Ejemplos:

*  Multiplicación escalar: $y_t = \beta x_t$
*  Suma: $y_t = x_t + w_t$
*  Identidad: $y_t = 1y_t$

Nótese que:
\begin{equation*}
y_t = \beta(x_t + w_t) = \beta x_t + \beta w_t
\end{equation*}




## Operador de rezago

El operador de rezago se denota por $\Lag$ y se define como:

\begin{equation*}
\Lag x_t \equiv x_{t-1}
\end{equation*}

En general, se tiene que:

\begin{equation*}
\Lag^k x_t = x_{t-k}
\end{equation*}


{{ empieza_ejemplo }} Operador de rezagos y transformación de series {{ fin_titulo_ejemplo }}
Algunas de las transformaciones de la serie $y_t$ de la sección anterior pueden expresarse con el operador de rezagos:

| Serie original                   | $y_t$ |
| :------------------------------- | :-------------------------------------------------------------------------------------- |
| Primera diferencia               | $\Delta y_t \equiv y_t - y_{t-1} = y_t - \Lag y_t = (1-\Lag)y_t$                        |
| Tasa de crecimiento              | $\Delta\% y_t \approx 100\left(\ln y_t - \ln y_{t-1}\right) = 100 (1-\Lag)\ln y_t$      |
| Diferencia interanual            | $\Delta_4 y_t \equiv y_t - y_{t-4} = y_t - \Lag^4 y_t = (1-\Lag^4)y_t$                  |
| Tasa de crecimiento interanual   | $\Delta_4\% y_t \approx 100\left(\ln y_t - \ln y_{t-4}\right) = 100 (1-\Lag^4)\ln y_t$                                              |
| Suavizada por media móvil        | $y^s_t \equiv \tfrac{1}{4}\left(y_t + y_{t-1} + y_{t-2} + y_{t-3}\right) = \tfrac{1}{4}\left(1 + \Lag + \Lag^2 +  \Lag^3\right)y_t$ |
{{ termina_ejemplo }}


(example-lags-and-diffs)=
{{ empieza_ejemplo }} Operador de rezagos {{ fin_titulo_ejemplo }}
El archivo `data/LandD.csv` tiene los siguientes datos ficticios
```{code-cell} ipython3
:tags: ["hide-input",]
datos = pd.read_csv('data/LandD.csv', index_col=0, parse_dates=True)
y = datos['y']
datos
```

```{margin} Otras implementaciones
* {ref}`R<Rcode-lags>`
```
Para calcular sus rezagos, diferencias, y diferencias estacionales con **Python**:
```{code-cell} ipython3
datos['L_y'] = y.shift(1)        # primer rezago
datos['L2_y'] = y.shift(2)       # segundo rezago
datos['D_y'] = y.diff()          # primera diferencia
datos['D2_y'] = y.diff().diff()  # segunda diferencia
datos['S_y'] = y.diff(4)         # diferencia estacional
datos
```
{{ termina_ejemplo }}


## Propiedades del operador de rezago
Sean $x_t, w_t$ dos series de tiempo. Entonces:

*  $\Lag(\beta x_t) = \beta\Lag x_t$
*  $\Lag(x_t + w_t) = \Lag x_t + \Lag w_t$
*  $\Lag(c) = c$
*  $\Lag^{-h} x_t = x_{t+h}$
*  $\Lag^{0} x_t = x_t$
*  $(\alpha \Lag^{h} + \beta\Lag^k) x_t = \alpha x_{t-h} + \beta x_{t-k}$

donde $\alpha, \beta, c$ son constantes.

El operador tiene propiedades conmutativa, asociativa y distributiva.



## Polinomio de rezagos

El operador de rezagos sigue las reglas usuales de operaciones algebraicas. Por ejemplo:
\begin{align*}
(a + b \Lag)(c + d \Lag)x_t &= (a + b \Lag)(c x_t + d x_{t-1}) \\
                            &= a c x_t + a d x_{t-1} + bc x_{t-1} + bd x_{t-2} \\
                            &= \left[ac + (ad+bc)\Lag + bd \Lag^2\right]x_t
\end{align*}

Así, definimos un polinomio de rezagos de orden $p$:
\begin{equation*}
\left(1 + \phi_1 \Lag + \phi_2 \Lag^2 + \dots + \phi_p \Lag^p\right)x_t =
x_{t} + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \dots + \phi_p x_{t-p}
\end{equation*}


## Inverso de un polinomio de rezagos de grado 1  

Considere la operación
\begin{align*}
(1 - \phi \Lag)\left(1 + \phi \Lag +\dots + \phi^k \Lag^k\right)x_t &= \left(1 -  \phi^{k+1} \Lag^{k+1}\right)x_t\\
                                                                    &= x_t - \phi^{k+1}x_{t-k-1}
\end{align*}

Si $|\phi| < 1$,
\begin{equation*}
\lim\limits_{k\to\infty} \phi^{k+1}x_{t-k-1}  = 0
\end{equation*}

con lo que
\begin{equation*}
(1 - \phi \Lag)\left(1 + \phi \Lag + \phi^2 \Lag^2 + \dots\right)x_t =  x_t
\end{equation*}

En este caso, escribimos
\begin{equation*}
(1 - \phi \Lag)^{-1} = 1 + \phi \Lag + \phi^2 \Lag^2 + \dots
\end{equation*}




## Inverso de un polinomio de rezagos de grado $p$

Consideremos el polinomio
\begin{equation*}
\Phi(L) \equiv 1 - \phi_1 \Lag - \dots - \phi_p \Lag^p
\end{equation*}

Si factorizamos el polinomio como
\begin{equation*}
\Phi(L) = (1-\lambda_1\Lag)(1-\lambda_2\Lag)\cdots(1-\lambda_p\Lag)
\end{equation*}

Encontramos su inverso como
\begin{align*}
\Phi^{-1}(L) &= (1-\lambda_1\Lag)^{-1}\cdots(1-\lambda_p\Lag)^{-1} \\
             &=\left(1 + \lambda_1 \Lag + \lambda_1^2 \Lag^2 + \dots\right)\cdots\left(1 + \lambda_p \Lag + \lambda_p^2 \Lag^2 + \dots\right)
\end{align*}
