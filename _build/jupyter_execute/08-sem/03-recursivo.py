```{include} ../math-definitions.md
```

#   El modelo recursivo

##   Un sistema de ecuaciones no simultáneas
El modelo recursivo tiene la forma

\begin{align*}
y_1 &=x'\beta_1 + \epsilon_1\\
y_2 &=x'\beta_2 + \gamma_{12}y_1  + \epsilon_2\\
&\vdots \\
y_M &=x'\beta_M + \gamma_{1M}y_1+\dots+\gamma_{M-1,M}y_{M-1}+ \epsilon_M
\end{align*}

o bien, en versión matricial


\begin{equation*}
\notation{\MAT{1 & 0 & \dots & 0 \\ -\gamma_{12} & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ -\gamma_{1M} & -\gamma_{2M} & \dots & 1} }{$\Gamma'$ es triangular}
\notation{\MAT{y_1 \\ y_2 \\ \vdots \\ y_M}}{$y_t$}
+
\notation{\MAT{-\beta_1 \\ -\beta_2 \\ \vdots \\ -\beta_M}}{$B'$}
\notation{x'}{$x_t$}
=
\notation{\MAT{\epsilon_{1} \\ \epsilon_{2} \\ \vdots \\  \epsilon_{M}}}{$\epsilon_t$}
\end{equation*}


##   El término de error
Se asume que
\begin{align*}
\E\epsilon_j &= 0\\
\E\epsilon^2_j &= \sigma^2_j\\
\E\epsilon_i\epsilon_j &= 0 \quad(i\neq j)
\end{align*}

o escrito en términos de matrices:

\begin{equation*}
\E[\epsilon_t\epsilon'_t] = \notation{\MAT{\sigma^2_1 & 0 & \dots & 0 \\ 0 & \sigma^2_2 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & \sigma^2_M} }{$\Sigma$ es diagonal}
\end{equation*}


##   Contando parámetros del modelo recursivo

```{panels}
parámetros estructurales
^^^
| Matriz    | # de parámetros         |
| :-------: | :---------------------: |
| $\Gamma$  | $\frac{M(M-1)}{2}$      |
| $B$       | $KM$                    |
| $\Sigma$  | $M$                     |
| **Total** | $\tfrac{M}{2}(1+2K+M)$  |

---
parámetros reducidos
^^^
| Matriz    | # de parámetros        |
| :-------: | :--------------------: |
|           |                        |
| $\Pi$     | $KM$                   |
| $\Omega$  | $\frac{M(M+1)}{2}$     |
| **Total** | $\tfrac{M}{2}(1+2K+M)$ |
```

Asi, para identificar $\alert{B,\Gamma, \Sigma}$ a partir de $\alert{\Pi, \Omega}$ tenemos:
\begin{equation*}
\notation{\tfrac{M}{2}(1+2K+M)}{# de incógnitas} \;-\;
\notation{\tfrac{M}{2}(1+2K+M)}{# de ecuaciones} =
\notation{0}{exceso de parámetros}
\end{equation*}

es decir, el sistema está exactamente identificado


{{ empieza_ejemplo }} Identificación de un SVAR(1) {{ fin_titulo_ejemplo }}

Considere el modelo
\begin{align*}
x_t &= \phi y_t + \beta_{11}x_{t-1} + \beta_{21}y_{t-1}  + \epsilon_{1t}\\
y_t &= \gamma x_t + \beta_{12}x_{t-1} + \beta_{22}y_{t-1}  + \epsilon_{2t}
\end{align*}

o bien, en forma matricial
\begin{equation*}
\notation{\MAT{1 & -\phi \\ -\gamma & 1}}{$\Gamma'$} \MAT{x_t \\ y_t} =
\notation{\MAT{\beta_{11} & \beta_{21} \\ \beta_{12} & \beta_{22}}}{$-B'$} \MAT{x_{t-1} \\ y_{t-1}} +
\MAT{\epsilon_{1t} \\ \epsilon_{2t}}
\end{equation*}

Hay 2 ecuaciones pero cada una tiene únicamente una restricción (la normalización), por lo que la condición de orden no se cumple $\Rightarrow$ ninguna ecuación está identificada.

Para poder estimar este modelo, sería necesario añadir nuevas restricciones.


Suponga que estamos dispuestos a asumir que $x_t$ no responde a $y_t$ contemporáneamente, es decir $\phi=0$. Entonces, la forma reducida del modelo sería
\begin{equation*}
\MAT{x_t \\ y_t} =
\MAT{\notation{\beta_{11}}{$\pi_{11}$} & \notation{\beta_{21}}{$\pi_{21}$} \\
\notation{\beta_{12}+\gamma\beta_{11}}{$\pi_{12}$} & \notation{\beta_{22}+\gamma\beta_{21}}{$\pi_{22}$}}
\MAT{x_{t-1} \\ y_{t-1}} +
\MAT{\epsilon_{1t} \\ \epsilon_{2t} + \gamma\epsilon_{1t}}
\end{equation*}

Entonces, si lográramos identificar $\gamma$ los demás parámetros estructurales serían:
\begin{align*}
\beta_{11} &=\pi_{11}  & \beta_{21} &=\pi_{21} \\
\beta_{12} &=\pi_{12} - \gamma\pi_{11}  & \beta_{22} &=\pi_{22} - \gamma\pi_{21}
\end{align*}

Suponga además que estamos dispuestos a asumir que los errores no están correlacionados:
\begin{equation*}
\Var[\epsilon_t] = \notation{\MAT{\sigma^2_1 & 0\\ 0 &\sigma^2_2}}{$\Sigma$}
\end{equation*}
- Entonces, la varianza de los errores reducidos $\Omega$ es:
\begin{align*}
\Omega \equiv \MAT{\sigma^2_x & \sigma_{xy}\\ \sigma_{xy} & \sigma^2_y}   &=
\notation{\MAT{1 & 0 \\ \gamma & 1}}{${\Gamma'}^{-1}$}
\notation{\MAT{\sigma^2_1 & 0\\ 0 &\sigma^2_2}}{$\Sigma$}
\notation{\MAT{1 & \gamma \\ 0 & 1}}{$\Gamma^{-1}$}\\
&= \MAT{\sigma^2_1 & \gamma\sigma^2_1\quad \\ \gamma\sigma^2_1 & \quad\gamma^2\sigma^2_1 + \sigma^2_2}
\end{align*}
- Así, conociendo $\Omega$ (estimado a partir de la forma reducida), los parámetros estructurales estarían identificados!
\begin{align*}
\sigma^2_1 &=\sigma^2_x &
\gamma &= \frac{\sigma_{xy}}{\sigma^2_x} &
\sigma^2_2 &=\sigma^2_y-\gamma^2\sigma^2_x
\end{align*}


Antes de continuar, observe que
\begin{align*}
\Omega \equiv \MAT{\sigma^2_x & \sigma_{xy}\\ \sigma_{xy} & \sigma^2_y}  &=
\notation{\MAT{1 & 0 \\ \gamma & 1}}{${\Gamma'}^{-1}$}
\notation{\MAT{\sigma^2_1 & 0\\ 0 &\sigma^2_2}}{$\Sigma$}
\notation{\MAT{1 & \gamma \\ 0 & 1}}{$\Gamma^{-1}$}\\
&= \notation{\MAT{\sigma_1 & 0 \\ \gamma\sigma_1 & \sigma_2}}{$L$}
\notation{\MAT{\sigma_1 & \gamma\sigma_1 \\ 0 & \sigma_2}}{$L'$}
\end{align*}

Es decir, hemos descompuesto $\Omega$ como el producto de una matriz triangular inferior y su transpuesta:
\begin{equation*}
\Omega = LL'
\end{equation*}

Esta es la **descomposición de Choleski**. Toda matriz simétrica semi-definida positiva puede ser descompuesta así.

La diagonal de $L$ identifica las desviaciones estándar de los errores estructurales.
{{ termina_ejemplo }}