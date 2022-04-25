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


# Solución por sustituciones recursivas


## Solución de la ecuación de primer orden

Dado un valor inicial $y_{-1}$ y la secuencia
\begin{equation*}
\left\{w_0, w_1, \dots, w_t\right\}
\end{equation*}

la ecuación puede resolverse de manera recursiva como:
\begin{equation*}
y_t = \phi^{t+1}y_{-1} + \phi^{t}w_{0} + \phi^{t-1}w_{1} + \dots +\phi w_{t-1} + w_{t}
\end{equation*}





## Multiplicador dinámico: shock transitorio

La solución es similar si se desea expresar  $y_{t+j}$ a partir de $y_t$
\begin{equation*}
y_{t+j} = \phi^{j+1}y_{t-1} + \phi^{j}w_{t} + \phi^{j-1}w_{t+1} + \dots +\phi w_{t+j-1} + w_{t+j}
\end{equation*}

El multiplicador dinámico se obtiene simplemente como:
\begin{equation*}
\marginal{y_{t+j}}{w_t} = \phi^j
\end{equation*}

El proceso es estable si y sólo si $|\phi| < 1$.




## Valor presente

Sea $\beta$ el factor de descuento. Se define el valor presente:
\begin{equation*}
\text{VP} = \sum_{j=0}^{\infty}\beta^j y_{t+j}
\end{equation*}

¿Cuál es el efecto de un cambio en $w_t$ sobre el VP de $y$?
\begin{equation*}
\marginal{\text{VP}}{w_t} = \sum_{j=0}^{\infty}\beta^j \marginal{y_{t+j}}{w_t} = \sum_{j=0}^{\infty}\beta^j \phi^j = \frac{1}{1-\beta\phi}
\end{equation*}

siempre y cuando $|\beta\phi| < 1$.



## Efecto de un shock permanente

Supóngase que el cambio en $w_t$ es permanente.

¿Qué efecto tiene sobre $y$ en el largo plazo?
\begin{equation*}
\lim\limits_{j\to\infty}\sum_{k=0}^{j} \marginal{y_{t+j}}{w_{t+k}} = \lim\limits_{j\to\infty}\sum_{k=0}^{j}\phi^{j-k} = \frac{1}{1-\phi}
\end{equation*}

siempre y cuando $|\phi| < 1$.



## Efecto acumulado de un shock transitorio

Se desea la suma de los cambios en $y$ como consecuencia de un único cambio en $w_t$. * Esto corresponde al ejemplo del VP cuando $\beta=1$:
\begin{equation*}
\text{EA} = \sum_{j=0}^{\infty}1^j \marginal{y_{t+j}}{w_t} = \sum_{j=0}^{\infty} \phi^j = \frac{1}{1-\phi}, \qquad |\phi|<1.
\end{equation*}

Nótese que el efecto acumulado de un shock transitorio es igual al efecto de un shock permanente en el largo plazo.



## Ecuación en diferencia de orden $p$

La variable $y_t$ evoluciona como un ecuación en diferencia de primer orden cuando depende de sus últimos $p$ valores
\begin{equation*}
y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + w_t
\end{equation*}

Es muy complicado analizar por sustitución recursiva la dinámica de una ecuación de orden $p$.

Afortunadamente es muy simple expresarla como una ecuación vectorial en diferencia de orden 1, que se resuelve de manera similar a la ecuación escalar.



## Solución de la ecuación de orden $p$
Para resolverla se definen:

\begin{align*}
\xi_t &\equiv \MAT{y_t\\y_{t-1}\\ \vdots \\ y_{t-p+1}}, & F&\equiv \MAT{\phi_1 & \phi_2 & \phi_3 & \dots & \phi_{p-1} & \phi_p \\ 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 1 & 0}, & v_t &\equiv \MAT{w_t\\ 0 \\ \vdots \\ 0}.
\end{align*}

con lo que la ecuación de orden $p$ que puede escribirse:
\begin{equation*}
\xi_t = F\xi_{t-1}  + v_t
\end{equation*}

y resolverse como:
\begin{equation*}
\xi_{t+j} = F^{j+1}\xi_{t-1} + F^{j}v_{t} + F^{j-1}v_{t+1} + \dots +F v_{t+j-1} + v_{t+j}
\end{equation*}




{{ empieza_ejemplo }} Resolviendo $y_t = 0.9y_{t-1} - 0.2y_{t-2}+3$ {{ fin_titulo_ejemplo }}
<!-- %Enders, p.16 -->

La ecuación puede escribirse como
\begin{equation*}
\notation{\MAT{y_{t}\\y_{t-1}}}{$\xi_t$} =
\notation{\MAT{0.9 & -0.2\\1 & 0}}{$F$}
\notation{\MAT{y_{t-1}\\y_{t-2}}}{$\xi_{t-1}$} +
\notation{\MAT{3\\0}}{$v$}
\end{equation*}

Por sustitución recursiva encontramos
\begin{align*}
\xi_t &= \left(I+F+F^2+\dots+F^{t-2}\right)v + F^{t-1}\xi_1\\
&=\left(I-F\right)^{-1}\left(I-F\right)\left(I+F+F^2+\dots+F^{t-2}\right)v + F^{t-1}\xi_1\\
&=\left(I-F\right)^{-1}\left(I-F^{t-1}\right)v + F^{t-1}\xi_1\\
\end{align*}

Necesitamos una expresión para $F^{t-1}$. Para ello, buscamos la [descomposición espectral](appendix:descomp-espectral) de $F$.

Encontramos los eigenvalores de $F$:
\begin{equation*}
\left|\begin{matrix}
0.9-\lambda & -0.2\\ 1& -\lambda
\end{matrix}\right| = \lambda^2-0.9\lambda+0.2 =(\lambda-0.5)(\lambda-0.4)=0
\end{equation*}

es decir, $\lambda_1=0.5, \lambda_2=0.4$.

Es fácil mostrar que los eigenvectores son $\MAT{\lambda_1 \\ 1}$ y $\MAT{\lambda_2 \\ 1}$.



Entonces
\begin{align*}
F  &= \MAT{\lambda_1 & \lambda_2\\ 1 & 1}
\MAT{\lambda_1 & 0 \\ 0 & \lambda_2}
\MAT{\lambda_1 & \lambda_2\\ 1 & 1}^{-1}  \Rightarrow  \\
F^{t-1} &= \MAT{\lambda_1 & \lambda_2\\ 1 & 1}
\MAT{\lambda_1^{t-1} & 0 \\ 0 & \lambda_2^{t-1}}
\MAT{\lambda_1 & \lambda_2\\ 1 & 1}^{-1} \Rightarrow  \\
&= \tfrac{1}{\lambda_1-\lambda_2}\MAT{\lambda_1 & \lambda_2\\ 1 & 1}
\MAT{\lambda_1^{t-1} & 0 \\ 0 & \lambda_2^{t-1}}
\MAT{1 & -\lambda_2\\ -1 & \lambda_1} \\
&= \tfrac{1}{\lambda_1-\lambda_2}
\MAT{\lambda_1^{t} - \lambda_2^{t} & \quad-\lambda_1\lambda_2\left(\lambda_1^{t-1} - \lambda_2^{t-1}\right) \\
\lambda_1^{t-1} - \lambda_2^{t-1} & \quad-\lambda_1\lambda_2\left(\lambda_1^{t-2} - \lambda_2^{t-2}\right)}
\end{align*}

Recuerde que es fácil calcular [la potencia de la matriz](appendix:potencia-matriz)  $F$ a partir de su descomposición espectral.


Sustituyendo los valores de $\lambda_1$ y $\lambda_2$
\begin{align*}
F^{t-1} &=
\MAT{10\left(0.5^{t} - 0.4^{t}\right) & \quad -2\left(0.5^{t-1} - 0.4^{t-1}\right) \\
10\left(0.5^{t-1} - 0.4^{t-1}\right) & \quad-2\left(0.5^{t-2} - 0.4^{t-2}\right)}
\end{align*}

Por otra parte:
\begin{equation*}
\left(I-F\right)^{-1} = \tfrac{10}{3}\mat{1& -0.2\\1 & \phantom{-}0.1} = \tfrac{1}{3}\mat{10& -2\\10 & \phantom{-}1}
\end{equation*}

Sustituyendo lo anterior en la ecuación vectorial:
\begin{multline*}
\mat{y_t\\y_{t-1}} = \tfrac{1}{3}
\mat{10 & -2\\ 10 & \phantom{-}1}
\mat{1-10\left(0.5^{t} - 0.4^{t}\right) & \quad 2\left(0.5^{t-1} - 0.4^{t-1}\right) \\
-10\left(0.5^{t-1} - 0.4^{t-1}\right) & \quad1-2\left(0.5^{t-2} - 0.4^{t-2}\right)}
\mat{3\\ 0} + \\
\mat{10\left(0.5^{t} - 0.4^{t}\right) & \quad -2\left(0.5^{t-1} - 0.4^{t-1}\right) \\
10\left(0.5^{t-1} - 0.4^{t-1}\right) & \quad-2\left(0.5^{t-2} - 0.4^{t-2}\right)}
\mat{y_1\\y_0} = \\
\mat{10 & -2\\ 10 & \phantom{-}1}
\mat{1-10\left(0.5^{t} - 0.4^{t}\right) \\ -10\left(0.5^{t-1} - 0.4^{t-1}\right) } +
\mat{10\left(0.5^{t} - 0.4^{t}\right) & \quad -2\left(0.5^{t-1} - 0.4^{t-1}\right) \\
10\left(0.5^{t-1} - 0.4^{t-1}\right) & \quad-2\left(0.5^{t-2} - 0.4^{t-2}\right)}
\mat{y_1\\y_0}
\end{multline*}


Tomando la primera fila
\begin{multline*}
y_t = 10 -100\left(0.5^{t} - 0.4^{t}\right) + 20\left(0.5^{t-1} - 0.4^{t-1}\right) + \\
10y_1\left(0.5^{t} - 0.4^{t}\right) - 2y_0\left(0.5^{t-1} - 0.4^{t-1}\right) \Rightarrow
\end{multline*}

\begin{align*}
y_t &= 10 + 10\left(y_1-10\right)\left(0.5^{t} - 0.4^{t}\right) - 2\left(y_0 - 10\right)\left(0.5^{t-1} - 0.4^{t-1}\right)\\
    &= 10 + \left(10y_1-100\right)\left(0.5^{t} - 0.4^{t}\right) + \left(20 -2y_0\right)\left(2\times 0.5^{t} - 2.5\times 0.4^{t}\right)\\
    &= 10 + \left(10y_1 - 4y_0 - 60\right)0.5^{t} - \left(10y_1-5y_0 -50\right)0.4^{t}
\end{align*}

Si imponemos las 2 condiciones iniciales: $y_0=13, y_1=11.3$, la solución de la ecuación es:
\begin{equation*}
y_t = 10 + 0.5^{t} +2\times 0.4^{t}
\end{equation*}
{{ termina_ejemplo }}


## Multiplicador dinámico: caso orden $p$

De nuevo el multiplicador dinámico se obtiene por derivación:
\begin{equation*}
\marginal{\xi_{t+j}}{v'_t} = F^j
\end{equation*}

El primer elemento de $\xi_{t+j}$ es $y_{t+j}$ y el primer elemento de $v_t$ es $w_t$, por lo tanto:
\begin{equation*}
\marginal{y_{t+j}}{w_t} = F^j_{(11)}
\end{equation*}

Ahora la estabilidad depende de $F^j$.


## Estabilidad

Que $F^j$ tienda a 0 cuando $j$ crece al infinito depende de los eigenvalores de $F$.

Si todos son distintos, entonces $F^j = T\Lambda^jT^{-1}$, donde:
\begin{equation*}
F^j = \MAT{t_{11} & t_{12} & \dots & t_{1p}\\ t_{21} & t_{22} & \dots & t_{2p}\\ \vdots & \vdots & \ddots  & \vdots \\ t_{p1} & t_{p2} & \dots & t_{pp}}
\MAT{\lambda_1^j & 0 & \dots & 0 \\ 0 & \lambda_2^j & \dots & 0 \\ \vdots & \vdots & \ddots  & \vdots \\ 0 & 0 & \dots & \lambda_p^j}
\MAT{t^{11} & t^{12} & \dots & t^{1p}\\ t^{21} & t^{22} & \dots & t^{2p}\\ \vdots & \vdots & \ddots  & \vdots \\ t^{p1} & t^{p2} & \dots & t^{pp}}
\end{equation*}

por tanto
\begin{align*}
\marginal{y_{t+j}}{w_t} = F^j_{(11)} &= \left(t_{11}t^{11}\right)\lambda_1^j + \left(t_{12}t^{21}\right)\lambda_2^j + \dots +\left(t_{1p}t^{p1}\right)\lambda_p^j \\
&= c_1\lambda_1^j + c_2\lambda_2^j +\dots + c_p\lambda_p^j
\end{align*}



## Obteniendo los eigenvalores y los ponderadores

Los eigenvalores de $F$ se obtienen de resolver:

```{admonition} Ecuación característica
\begin{equation*}
|F - \lambda I_p| = \lambda^p - \phi_1\lambda^{p-1} - \phi_2\lambda^{p-2} - \dots - \phi_{p-1}\lambda - \phi_p = 0
\end{equation*}
```

Mientras que $c_i$ se obtiene de:
\begin{equation*}
c_i = \frac{\lambda_i^{p-1}}{\prod\limits_{\stackrel{k=1}{k\neq i}}^{p}(\lambda_i - \lambda_k)}
\end{equation*}

Nótese que:
\begin{equation*}
c_1 + c_2 +\dots + c_p = \left(t_{11}t^{11}\right) + \left(t_{12}t^{21}\right) + \dots +\left(t_{1p}t^{p1}\right) = 1
\end{equation*}




(sec:dinamica-ajuste)=
## Dinámica de ajuste

Dado que
\begin{align*}
\marginal{y_{t+j}}{w_t} &= c_1\lambda_1^j + c_2\lambda_2^j +\dots + c_p\lambda_p^j\\
1 &= c_1 + c_2 +\dots + c_p
\end{align*}

el multiplicador dinámico es un promedio ponderado de las potencias de los eigenvalores.

La forma del ajuste dependerá del eigenvalor de mayor valor absoluto $\lambda_{max}$

* Si $0 < \lambda_{max} < 1$, el MD decae geométricamente.
* Si $-1< \lambda_{max} < 0$, el MD decae alternando
* Si $|\lambda_{max}| > 1$, la serie explota (no converge)  



## ¿Cómo se da el ajuste si $\lambda_{max}$ es complejo?

Se sabe que si $\lambda_1 = a+bi$, entonces $\lambda_2 = a - bi$

Si expresamos $\lambda_j$ en [coordenadas polares](appendix:polar-complex):


```{margin} Cambio de coordenas
\begin{align*}
R &= \sqrt{a^2+b^2} \\
a &= R\cos\theta \\
b &= R\sin\theta
\end{align*}
```

\begin{align*}
\lambda_1 &= R[\cos\theta + i\sin\theta] = Re^{i\theta} \\
\lambda_2 &= R[\cos\theta - i\sin\theta] = Re^{-i\theta}
\end{align*}


Entonces [la potencia de los eigenvalores](appendix:mult-complex) es:
\begin{align*}
\lambda_1^j &= R^je^{ij\theta} = R^j[\cos j\theta + i\sin j\theta]  \\
\lambda_2^j &= R^je^{-ij\theta} = R^j[\cos j\theta - i\sin j\theta]
\end{align*}


El promedio de estos dos eigenvalores es:
\begin{align*}
 c_1\lambda_1^j + c_2\lambda_2^j & = c_1R^j[\cos j\theta + i\sin j\theta] + c_2R^j[\cos j\theta - i\sin j\theta] \\
                                 &=R^j\left[ (c_1+c_2) \cos j\theta + i(c1-c_2) \sin j\theta\right]\\
\end{align*}

Pero $c_1$ y $c_2$ son conjugados: $c_1, c_2 = \alpha \pm \beta i$
\begin{align*}
 c_1\lambda_1^j + c_2\lambda_2^j &=R^j\left[ 2\alpha \cos j\theta - 2\beta \sin j\theta\right]
\end{align*}



que en función de $j$ es periódica, con frecuencia $\theta$ y período $\frac{2\pi}{\theta}$



{{ empieza_ejemplo }} Dinámica de ajuste cuando $p=2$ {{ fin_titulo_ejemplo }}

```{code-cell} ipython3
:tags: ["hide-input",]
y1 = ARMA(phi=[0.9, -0.9])
y2 = ARMA(phi=[0.2, 0.35])
y3 = ARMA(phi=[1.6, -0.64])
y4 = ARMA(phi=[0.5, 0.5])

merge_plots(
   [y1.plot_irf(50), y2.plot_irf(50), y3.plot_irf(50), y4.plot_irf(50)],
   cols=2,
   subplot_titles=[str(y1), str(y2), str(y3), str(y4)] ,
   title_text="Funciones de impulso respuesta",
   shared_yaxes=False
)
```
{{ termina_ejemplo}}



## Valor presente

Recordando que
\begin{equation*}
   \marginal{\xi_{t+j}}{v'_t} = F^j
\end{equation*}

Se tiene que:
\begin{equation*}
  \sum_{j=0}^{\infty}\beta^j\marginal{\xi_{t+j}}{v'_t} = \sum_{j=0}^{\infty}\beta^j F^j = \left(I_p - \beta F\right)^{-1}
\end{equation*}

En este caso su elemento 1,1 es
\begin{equation*}
  \frac{1}{1-\phi_1\beta - \phi_2\beta^2 - \dots - \phi_p\beta^p}
\end{equation*}



## Efecto acumulado y multiplicador de largo plazo

Se obtiene del VP en el caso particular en que $\beta = 1$:
\begin{equation*}
   \frac{1}{1-\phi_1 - \phi_2 - \dots - \phi_p}
\end{equation*}
