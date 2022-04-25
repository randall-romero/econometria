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

# Identificación


El problema de **identificación** en ecuaciones simultáneas se refiere a cómo obtener los parámetros **estructurales** $\alert{B,\Gamma, \Sigma}$ a partir de los parámetros **reducidos $\alert{\Pi, \Omega}$.
\begin{equation*}
\left.\begin{aligned}
\Pi &= -B\Gamma^{-1} \\ \\
\Omega &=\left(\Gamma^{-1}\right)'\Sigma\Gamma^{-1}
\end{aligned} \right\} \Rightarrow
\left\{\begin{aligned}
B &= ?\\
\Gamma &= ?\\
\Sigma &= ?\\
\end{aligned} \right.
\end{equation*}

```{warning}
No es un problema de estimación, sino de resolución de un sistema de ecuaciones no lineales.
```

Considere la matriz $F\neq I$, y defina $\tilde{\Gamma} = \Gamma F$ y $\tilde{B} = B F$. Entonces
\begin{align*}
Y\Gamma + XB &= E \tag{estructura verdadera} \\
Y\tilde{\Gamma} + X\tilde{B} &= \tilde{E} \tag{estructura falsa}
\end{align*}

Pero ambas tienen la misma forma reducida!:

\begin{equation*}
\begin{aligned}
\tilde{\Pi} &= -\tilde{B}\tilde{\Gamma}^{-1} \\
&= - BFF^{-1}\Gamma^{-1} \\
&= -B\Gamma^{-1}\\
&= \Pi
\end{aligned}
\end{equation*}

Decimos que las estructuras son **observacionalmente equivalentes**.


##   Identificación: contando parámetros

```{panels}
:header: bg-dark text-center text-white

parámetros estructurales
^^^
| Matriz    | # de parámetros         |
| :-------: | :---------------------: |
| $\Gamma$  | $M^2$                   |
| $B$       | $KM$                    |
| $\Sigma$  | $\frac{M(M+1)}{2}$      |
| **Total** | $\tfrac{M}{2}(1+2K+3M)$ |

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

Para identificar los parámetros $\alert{B,\Gamma, \Sigma}$ a partir de $\alert{\Pi, \Omega}$ tenemos:
\begin{equation*}
\notation{\tfrac{M}{2}(1+2K+3M)}{# de incógnitas} \;-\;
\notation{\tfrac{M}{2}(1+2K+M)}{# de ecuaciones} =
\notation{M^2}{exceso de parámetros}
\end{equation*}


##   Identificación de la ecuación $j$
Dado que tenemos más parámetros estructurales que reducidos, es necesario tener información no muestral:

- normalizaciones
- identidades
- exclusiones
- restricciones lineales
- restricciones en varianza


##   Identificación via restricciones lineales por ecuación
La forma estructural puede escribirse como ${\color{DarkGreen}A }{\color{FireBrick}z_t} = \epsilon_t$:

\begin{equation*}
{\color{DarkGreen}
\MAT{%
\gamma_{11} & \dots & \gamma_{M1} & \beta_{11} & \dots & \beta_{K1} \\
\gamma_{12} & \dots & \gamma_{M2} & \beta_{12} & \dots & \beta_{K2} \\
& & &\vdots & & \\
\gamma_{1M} & \dots & \gamma_{MM} & \beta_{1M} & \dots & \beta_{KM}
}} {\color{FireBrick}
\MAT{%
y_{t1} \\ \vdots \\ y_{tM} \\ x_{t1} \\ \vdots \\ x_{tK}
}} =
\MAT{%
\epsilon_{t1} \\ \epsilon_{t2} \\ \vdots \\ \epsilon_{tM}
}
\end{equation*}


Algunos de los parámetros de la fila $j$:
\begin{equation*}
\MAT{\gamma_{1j} & \dots & \gamma_{Mj} & \beta_{1j} & \dots & \beta_{Kj} }
\end{equation*}

están restringidos porque:

- una variable endógena está normalizada, ej: $\gamma_{jj}=1$
- alguna variable está excluida, ej: $\gamma_{3j} = 0$ o bien $\beta_{2j} = 0$
- dos variables tienen el mismo coeficiente, ej: $\beta_{2j} = \beta_{3j}$



##   Restricción de normalización
La más sencilla de las restricciones es la **normalización**: en cada ecuación, el parámetro de una variable (usualmente endógena) es uno.

Ejemplos:

```{panels}
:header: bg-dark text-center text-white

Un modelo de oferta y demanda
^^^
\begin{align*}
\alert{1q_t^d} &= \alpha_0 + \alpha_1 p_t + \alpha_2 x_t + \epsilon_t^d \\
\alert{1q_t^s} &= \beta_0 + \beta_1 p_t + \epsilon_t^s \\
q_t^d &=q_t^s
\end{align*}

---
Un modelo de demanda agregada
^^^
\begin{align*}
\alert{1C_t} &= \alpha_0 + \alpha_1 Y_t + \epsilon_{1t} \\
\alert{1I_t} &= \beta_0 + \beta_1\left(Y_t - Y_{t-1}\right) + \epsilon_{2t} \\
       Y_t &= C_t + I_t + G_t
\end{align*}
```

##   Restricción de exclusión
La **exclusión** se refiere a que alguna variable del modelo no aparece en cierta ecuación (es decir, su coeficiente es cero en esa ecuación).

Ejemplos:

```{panels}
:header: bg-dark text-center text-white

Un modelo de oferta y demanda
^^^
\begin{align*}
q_t^d &= \alpha_0 + \alpha_1 p_t + \alpha_2 x_t + \epsilon_t^d \\
q_t^s &= \beta_0 + \beta_1 p_t + \alert{0x_t} + \epsilon_t^s \\
q_t^d &=q_t^s
\end{align*}

---
Un modelo de demanda agregada
^^^
\begin{align*}
C_t &= \alpha_0 + \alpha_1 Y_t + \alert{0Y_{t-1}} + \alert{0G_t} + \alert{0I_t} + \epsilon_{1t} \\
I_t &= \beta_0 + \beta_1\left(Y_t - Y_{t-1}\right) + \alert{0G_t} + \alert{0C_t} + \epsilon_{2t} \\
Y_t &= C_t + I_t + G_t
\end{align*}
```

%-----------------------------------------------------------------------
##   Restricción de combinación lineal de parámetros
En este caso, una \alert{combinación lineal de parámetros} es conocida. El caso más sencillo es cuando dos parámetros son iguales.

Ejemplo:
```{panels}
:header: bg-dark text-center text-white

Un modelo de demanda agregada
^^^
\begin{align*}
C_t &= \alpha_0 + \alpha_1 Y_t + \epsilon_{1t} \\
I_t &= \beta_0 + \alert{\beta_1}Y_t + \alert{(-\beta_1)}Y_{t-1} + \epsilon_{2t} \\
Y_t &= C_t + I_t + G_t
\end{align*}
+++
es decir, en la ecuación de inversión la suma de los parámetros de $Y_t$ y de $Y_{t-1}$ debe ser igual a cero.
```



##   La condición de rango
Sea $\tilde{A}_j$ la matriz formada por aquellas columnas de $A$ en las que la ecuación $j$ tiene restricciones.

```{panels}
:header: bg-dark text-center text-white

Condición de rango
^^^
La ecuación $j$ está idenficada si y solo si la matriz $\tilde{A}_j$ tiene {ref}`rango fila completo<appendix:rango-matriz>`; es decir
\begin{equation*}
\text{rango}\left[\tilde{A}_j\right] = M
\end{equation*}
+++
Esta condición es necesaria y suficiente.
```


##   La condición de orden
Note que para que se cumpla la condición de rango, es necesario que $\tilde{A}_j$ tenga al menos $M$ columnas.

```{panels}
:header: bg-dark text-center text-white

Condición de orden
^^^
Para que la ecuación $j$ esté identificada, es necesario que el número de restricciones en tal ecuación sea mayor o igual al número de variables endógenas del sistema ($=$ al número de ecuaciones).
+++
Esta condición es necesaria **pero no suficiente**.
```



##   Clasificación de ecuaciones
| Tipo de ecuación         | Condición de orden        | Condición de rango |
| :----------------------- | :------------------------ | :----------------- |
| Sobre-identificada       | Se cumple con desigualdad | Se cumple          |
| Exactamente identificada | Se cumple con igualdad    | Se cumple          |
| Sub-identificada         | No se cumple              | Puede no cumplirse |

Se dice que está **identificada** sólo si está “sobre-identificada” o “exactamente-identificada”

```{tip}
Solo las ecuaciones identificadas pueden ser estimadas
```



{{ empieza_ejemplo }} Identificación en el modelo de oferta y la demanda {{ fin_titulo_ejemplo }}

En {ref}`un ejemplo anterior<ex-oferta-demanda-estructural-reducida>` encontramos esta forma estructural para el modelo de oferta y demanda
\begin{equation*}
\notation{\MAT{q_t & p_t}}{$y'_t$}
\notation{\MAT{1 & 1 \\ -\alpha_1 & -\beta_1} }{$\Gamma$} +
\notation{\MAT{1 & x_t}}{$x'_t$}
\notation{\MAT{-\alpha_0 & -\beta_0 \\ -\alpha_2 & 0}}{$B$} =
\notation{\MAT{\epsilon_t^d & \epsilon_t^s}}{$\epsilon'_t$}
\end{equation*}

que puede escribirse también como
\begin{equation*}
\alert{Az_t =}
\MAT{
\notation{\begin{matrix}  1 & -\alpha_1 \\  1 & -\beta_1 \end{matrix}}{$\Gamma'$}
& \color{orange} \Bigg|\Bigg. &
\notation{\begin{matrix} -\alpha_0 & -\alpha_2 \\  -\beta_0  & 0 \end{matrix}}{$B'$}
}
\notation{\MAT{q_t \\ p_t \\ 1 \\ x_t} }{$z_t$} =
\notation{\MAT{\epsilon^d_t \\ \epsilon^s_t}}{$\epsilon_t$}
\end{equation*}

Entonces
\begin{equation*}
\tilde{A}_1 =
\MAT{1 \\ 1} \qquad
\tilde{A}_2 =
\MAT{1 & -\alpha_2\\1 & 0}
\end{equation*}


Demanda
:   $\tilde{A}_1 = \MAT{1 \\ 1}$ no cumple condición de orden, por lo tanto es no-identificada.

Oferta
:   $\tilde{A}_2 = \MAT{1 & -\alpha_2\\1 & 0}$ cumple condición de rango si y solo si $\alpha_2\neq 0$.


En conclusión, podemos estimar la oferta siempre y cuando la demanda efectivamente dependa de $x_t$. La demanda no puede ser estimada.
{{ termina_ejemplo }}



{{ empieza_ejemplo }} Identificación de un modelo de demanda agregada {{ fin_titulo_ejemplo }}

En {ref}`este otro ejemplo<ex-demanda-agregada-estructural-reducida>` encontramos esta forma estructural para el modelo de oferta y demanda

\begin{equation*}
\alert{Az_t =}
\MAT{
\notation{\begin{matrix}     1 & 0 & -\alpha_1 \\  0 & 1 & -\beta_1 \\ -1 & -1 & 1\end{matrix}}{$\Gamma'$}
& \color{orange} \Bigg|\Bigg. &
\notation{\begin{matrix}    -\alpha_0 & 0 & 0\\ -\beta_0 &\beta_1 & 0 \\ 0 & 0 & -1 \end{matrix}}{$B'$}
}
\notation{\MAT{C_t \\ I_t \\ Y_t \\ 1 \\ Y_{t-1} \\ G_t} }{$z_t$} =
\notation{\MAT{\epsilon_{1t} \\ \epsilon_{2t} \\ 0}}{$\epsilon_t$}
\end{equation*}


En este caso las matrices de restricciones de las ecuaciones 1 y 2 son idénticas:
\begin{equation*}
\tilde{A}_1 = \tilde{A}_2 =
\MAT{%
1 & 0 & 0 &  0\\
0 & 1 & \beta_1 & 0 \\
-1 & -1 & 0 & -1
}
\end{equation*}


Ecuación de consumo
:  Tenemos que
  - $\text{rango}\left[\tilde{A}_1\right] = 3 \quad\Rightarrow$ identificada.
  - $\tilde{A}_1$ tiene 4 columnas pero 3 filas $\Rightarrow$ sobre-identificada.

Ecuación de inversión
:  Dado que $\tilde{A}_2 = \tilde{A}_1$, sabemos que esta ecuación también está sobre-identificada.

Ecuación de ingreso
:  Es una identidad $\Rightarrow$ no hay nada que estimar.

{{ termina_ejemplo }}
