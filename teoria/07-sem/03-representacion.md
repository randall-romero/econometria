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


# Representación de ecuaciones simultáneas

```{math}
\newcommand{\yregressors}[1]{\gamma_{1 #1}y_{t1} + \dots + \gamma_{M #1}y_{tM}}
\newcommand{\xregressors}[1]{\beta_{1#1}x_{t1} + \dots + \beta_{K#1}x_{tK}}
\newcommand{\yxequation}[1]{\yregressors{#1} + \xregressors{#1} &=\epsilon_{t#1}}
```



En Economía, muchas de las teorías se construyen como modelos de ecuaciones simultáneas.

Ejemplos:

```{panels}

Un modelo de oferta y demanda
^^^
\begin{align*}
q_t^d &= \alpha_0 + \alpha_1 p_t + \alpha_2 x_t + \epsilon_t^d \\
q_t^s &= \beta_0 + \beta_1 p_t + \epsilon_t^s \\
q_t^d &= q_t^s = q
\end{align*}

---
Un modelo de demanda agregada
^^^
\begin{align*}
    C_t &= \alpha_0 + \alpha_1 Y_t + \epsilon_{1t} \\
    I_t &= \beta_0 + \beta_1\left(Y_t - Y_{t-1}\right) + \epsilon_{2t} \\
    Y_t &= C_t + I_t + G_t
\end{align*}
```

En estos modelos se presentan un grupo de variables dependientes que se determinan simultáneamente en un sistema de ecuaciones.

Se asume que existen tantas ecuaciones como variables dependientes en el sistema.


## Modelo en forma estructural

Hay $\alert{K}$ variables exógenas, $\alert{M}$ endógenas, y $\alert{M}$ ecuaciones.

Se cuenta con $\alert{T}$ observaciones de cada variable.


\begin{equation*}
\left\{
\begin{aligned}
\yxequation{1} \\
\yxequation{2} \\
&\vdots \\
\yxequation{M}
\end{aligned}
\right.
\end{equation*}


##   Ecuaciones en forma estructural: Matrices
Escribimos las ecuaciones como $\alert{y'_t\Gamma + x'_tB = \epsilon'_t}$:
\begin{equation*}
\notation{\MAT{y_1 & \dots& y_M}_t}{$y'_t$}
\notation{\MAT{\gamma_{11} &\dots &\gamma_{1M}\\ &\ddots& \\ \gamma_{M1}&\dots &\gamma_{MM} }}{$\Gamma$}
+
\notation{\MAT{x_1 & \dots& x_K}_t}{$x'_t$}
\notation{\MAT{\beta_{11} &\dots &\beta_{1M}\\ &\ddots& \\ \beta_{K1}&\dots &\beta_{KM} }}{$B$}
=
\notation{\MAT{\epsilon_1&\dots&\epsilon_M}_t}{$\epsilon'_t$}
\end{equation*}

En las matrices $\Gamma$ y $B$, cada columna corresponde a una ecuación, y cada fila a una variable.


Juntando todas las observaciones $\alert{y'_t\Gamma + x'_tB = \epsilon'_t}$ obtenemos

\begin{equation*}
\begin{aligned}
y'_1\Gamma + x'_1B &= \epsilon'_1 \\
y'_2\Gamma + x'_2B &= \epsilon'_2 \\
 & \vdots \\
y'_T\Gamma + x'_TB &= \epsilon'_T
\end{aligned}
\Rightarrow
\MAT{y'_1\Gamma\\ y'_2\Gamma\\ \vdots \\ y'_T\Gamma }
+
\MAT{x'_1B\\ x'_2B\\ \vdots \\ x'_TB }
=
\MAT{\epsilon'_1 \\ \epsilon'_2 \\ \vdots \\ \epsilon'_T }
\Rightarrow
\MAT{y'_1 \\ y'_2 \\ \vdots \\ y'_T}\Gamma
+
\MAT{x'_1 \\ x'_2 \\ \vdots \\ x'_T}B
=
\MAT{\epsilon'_1 \\ \epsilon'_2 \\ \vdots \\ \epsilon'_T }
\end{equation*}

##   Modelo en forma reducida
Postmultiplicando la forma estructural por $\Gamma^{-1}$ tenemos

\begin{align*}
y'_t\Gamma + x'_tB &= \epsilon'_t \\
y'_t\Gamma\Gamma^{-1} + x'_tB\Gamma^{-1} &= \epsilon'_t\Gamma^{-1} \\
y'_t - x'_t\Pi &= \nu'_t \\
y'_t  &= x'_t\Pi + \nu'_t
\end{align*}

o bien
\begin{align*}
Y\Gamma + XB &= E \\
Y\Gamma\Gamma^{-1} + XB\Gamma^{-1} &= E\Gamma^{-1} \\
Y - X\Pi &= V \\
Y  &= X\Pi + V
\end{align*}

donde hemos definido $\Pi\equiv -B\Gamma^{-1}$ como los parámetros reducidos del sistema, y $v'_t \equiv \epsilon'_t\Gamma^{-1}$.

```{panels}

Forma Estructural
^^^
\begin{equation*}
	Y\Gamma + X B = E
\end{equation*}

---
Forma Reducida
^^^
\begin{equation*}
 Y = X\Pi + V
\end{equation*}
```

(ex-oferta-demanda-estructural-reducida)=
{{ empieza_ejemplo }} Forma estructural y reducida del modelo de oferta y demanda {{ fin_titulo_ejemplo }}

\begin{equation*}
\left\{\begin{aligned}
q_t^d &= \alpha_0 + \alpha_1 p_t + \alpha_2 x_t + \epsilon_t^d \\
q_t^s &= \beta_0 + \beta_1 p_t + \epsilon_t^s \\
q_t^d &= q_t^s = q
\end{aligned}  \right.
\end{equation*}

Su forma estructural es
\begin{equation*}
\notation{\MAT{q_t & p_t}}{$y'_t$}\notation{\MAT{1 & 1 \\ -\alpha_1 & -\beta_1} }{$\Gamma$} +
\notation{\MAT{1 & x_t}}{$x'_t$}\notation{\MAT{-\alpha_0 & -\beta_0 \\ -\alpha_2 & 0}}{$B$} =
\notation{\MAT{\epsilon_t^d & \epsilon_t^s}}{$\epsilon'_t$}
\end{equation*}

Note que **cada columna** de $\Gamma$ y de $B$ corresponden a una ecuación del modelo.

Así,
\begin{equation*}
\Gamma = \MAT{1 & 1 \\ -\alpha_1 & -\beta_1} \Rightarrow \Gamma^{-1} = \frac{1}{\beta_1-\alpha_1}\MAT{\beta_1 & 1 \\ -\alpha_1 & - 1}
\end{equation*}

Los parámetros reducidos son:
\begin{equation*}
\Pi = -B\Gamma^{-1} = \tfrac{1}{\beta_1-\alpha_1}\MAT{\alpha_0 & \beta_0 \\ \alpha_2 & 0}\MAT{\beta_1 & 1 \\ -\alpha_1 & - 1}
=\tfrac{1}{\beta_1-\alpha_1}\MAT{\alpha_0\beta_1-\alpha_1\beta_0 & \alpha_0 - \beta_0 \\ \alpha_2\beta_1 & \alpha_2}
\end{equation*}

y los shocks reducidos son:
\begin{equation*}
\nu'_t = \epsilon'_t\Gamma^{-1}= \tfrac{1}{\beta_1-\alpha_1}\MAT{\epsilon^d_t & \epsilon^s_t}\MAT{\beta_1 & 1 \\ -\alpha_1 & - 1}
=\tfrac{1}{\beta_1-\alpha_1}\MAT{\beta_1\epsilon^d_t-\alpha_1\epsilon^s_t & \epsilon^d_t - \epsilon^s_t}
\end{equation*}

por lo que la forma reducida es:
\begin{equation*}
\notation{\MAT{q_t & p_t}}{$y'_t$}
=
\notation{\MAT{1 & x_t}}{$x'_t$}
\notation{\MAT{\tfrac{\alpha_0\beta_1-\alpha_1\beta_0}{\beta_1-\alpha_1} & \tfrac{\alpha_0 - \beta_0}{\beta_1-\alpha_1}  \\  \tfrac{\alpha_2\beta_1}{\beta_1-\alpha_1} & \tfrac{\alpha_2}{\beta_1-\alpha_1}}}{$\Pi$}
+
\notation{\MAT{\tfrac{\beta_1\epsilon^d_t-\alpha_1\epsilon^s_t}{\beta_1-\alpha_1} & \tfrac{\epsilon^d_t - \epsilon^s_t}{\beta_1-\alpha_1}}}{$\nu'_t$}
\end{equation*}

La forma reducida corresponde a la cantidad y precio de equilibrio:

\begin{equation*}
\left\{\begin{aligned}
q_t^* &= \notation{\tfrac{\alpha_0\beta_1-\alpha_1\beta_0}{\beta_1-\alpha_1}}{$\pi_{11}$} + \notation{\tfrac{\alpha_2\beta_1}{\beta_1-\alpha_1}}{$\pi_{21}$}x_t +
\notation{\tfrac{\beta_1\epsilon_t^d - \alpha_1\epsilon_t^s}{\beta_1-\alpha_1}}{$\nu_1$} \\
p_t^* &=  \notation{\tfrac{\alpha_0-\beta_0}{\beta_1-\alpha_1}}{$\pi_{12}$} + \notation{\tfrac{\alpha_2}{\beta_1-\alpha_1}}{$\pi_{22}$}x_t +
\notation{\tfrac{\epsilon_t^d - \epsilon_t^s}{\beta_1-\alpha_1} }{$\nu_2$}
\end{aligned}  \right.
\end{equation*}

A partir de la forma reducida, es fácil calcular el efecto de shocks o de cambios en variables exógenas sobre las endógenas. Por ejemplo:
\begin{equation*}
\marginal{q^*_t}{x_t} = \pi_{21} = \tfrac{\alpha_2\beta_1}{\beta_1-\alpha_1} \qquad\qquad
\marginal{p^*_t}{\epsilon^s_t} = \tfrac{-1}{\beta_1-\alpha_1}
\end{equation*}

Nótese que a partir de la forma reducida, el efecto de una variable exógena es observable (es un parámetro reducido), no así el efecto de un shock estructural (está combinado con los demás shocks estructurales en el shock reducido).
{{ termina_ejemplo }}




(ex-demanda-agregada-estructural-reducida)=
{{ empieza_ejemplo }} Forma estructural y reducida del modelo de demanda agregada {{ fin_titulo_ejemplo }}

\begin{equation*}
\left\{\begin{aligned}
    C_t &= \alpha_0 + \alpha_1 Y_t + \epsilon_{1t} \\
    I_t &= \beta_0 + \beta_1\left(Y_t - Y_{t-1}\right) + \epsilon_{2t} \\
    Y_t &= C_t + I_t + G_t
\end{aligned}  \right.
\end{equation*}


Su forma estructural es
\begin{equation*}
\notation{\MAT{1 & 0 & -\alpha_1 \\ 0 & 1 & -\beta_1 \\ -1 & -1 & 1} }{$\Gamma'$}\notation{\MAT{C_t \\ I_t \\ Y_t}}{$y_t$}  +
\notation{\MAT{-\alpha_0 & 0 & 0 \\ -\beta_0 & \beta_1 & 0 \\ 0 & 0 &-1}}{$B'$}\notation{\MAT{1 \\ Y_{t-1} \\ G_t}}{$x_t$} =
\notation{\MAT{\epsilon_{1t} \\ \epsilon_{2t} \\ 0}}{$\epsilon_t$}
\end{equation*}

Como tomamos la transpuesta, note que **cada fila** de $\Gamma'$ y de $B'$ corresponden a una ecuación del modelo.

Así,
\begin{equation*}
\Gamma' = \MAT{1 & 0 &-\alpha_1 \\ 0 & 1 & - \beta_1 \\ -1 & -1 & 1} \Rightarrow {\Gamma'}^{-1} = \frac{1}{1-\alpha_1-\beta_1}\MAT{1-\beta_1 & \alpha_1 & \alpha_1 \\ \beta_1 & 1-\alpha_1 & \beta_1 \\ 1 & 1 & 1}
\end{equation*}

Los parámetros reducidos son:
\begin{align*}
\Pi' = -{\Gamma'}^{-1}B' &= \tfrac{1}{1-\alpha_1-\beta_1}\MAT{1-\beta_1 & \alpha_1 & \alpha_1 \\ \beta_1 & 1-\alpha_1 & \beta_1 \\ 1 & 1 & 1}
\MAT{\alpha_0 & 0 & 0 \\ \beta_0 & -\beta_1 & 0 \\ 0 & 0 & 1} \\
&= \tfrac{1}{1-\alpha_1-\beta_1}\MAT{\alpha_0 - \alpha_0\beta_1 + \alpha_1\beta_0 & -\alpha_1\beta_1 & \alpha_1 \\ \alpha_0\beta_1 + \beta_0 - \alpha1\beta_0 & \alpha_1\beta_1 - \beta_1 & \beta_1 \\ \alpha_0+\beta_0 & -\beta_1 & 1}
\end{align*}

y los shocks reducidos son:
\begin{align*}
\nu_t = {\Gamma'}^{-1}\epsilon_t &= \tfrac{1}{1-\alpha_1-\beta_1}\MAT{1-\beta_1 & \alpha_1 & \alpha_1 \\ \beta_1 & 1-\alpha_1 & \beta_1 \\ 1 & 1 & 1}
\MAT{\epsilon_{1t} \\ \epsilon_{2t} \\ 0} \\
&=\tfrac{1}{1-\alpha_1-\beta_1}\MAT{(1-\beta_1)\epsilon_{1t} + \alpha_1\epsilon_{2t} \\ \beta_1\epsilon_{1t} + (1-\alpha_1)\epsilon_{2t}  \\  \epsilon_{1t} + \epsilon_{2t}}
\end{align*}


por lo que la forma reducida es:
\begin{equation*}
\notation{\MAT{C_t \\ I_t \\ Y_t}}{$y_t$}
=
\notation{\tfrac{1}{1-\alpha_1-\beta_1}\MAT{\alpha_0 - \alpha_0\beta_1 + \alpha_1\beta_0 & -\alpha_1\beta_1 & \alpha_1 \\ \alpha_0\beta_1 + \beta_0 - \alpha1\beta_0 & \alpha_1\beta_1 - \beta_1 & \beta_1 \\ \alpha_0+\beta_0 & -\beta_1 & 1}}{$\Pi'$}
\notation{\MAT{1 \\ Y_{t-1} \\ G_t}}{$x_t$}
+
\notation{\tfrac{1}{1-\alpha_1-\beta_1}\MAT{(1-\beta_1)\epsilon_{1t} + \alpha_1\epsilon_{2t} \\ \beta_1\epsilon_{1t} + (1-\alpha_1)\epsilon_{2t}  \\  \epsilon_{1t} + \epsilon_{2t}}}{$\nu_t$}
\end{equation*}


La forma reducida corresponde al consumo, inversión, e ingreso de equilibrio:
\begin{equation*}
\left\{\begin{aligned}
C_t^* &= \tfrac{\alpha_0 - \alpha_0\beta_1 + \alpha_1\beta_0}{1-\alpha_1-\beta_1} - \tfrac{\alpha_1\beta_1}{1-\alpha_1-\beta_1}Y_{t-1} + \tfrac{ \alpha_1 }{1-\alpha_1-\beta_1}G_t + \tfrac{(1-\beta_1)\epsilon_{1t} + \alpha_1\epsilon_{2t}}{1-\alpha_1-\beta_1} \\
I_t^* &= \tfrac{ \alpha_0\beta_1 + \beta_0 - \alpha1\beta_0}{1-\alpha_1-\beta_1} + \tfrac{\alpha_1\beta_1 - \beta_1}{1-\alpha_1-\beta_1}Y_{t-1} + \tfrac{\beta_1}{1-\alpha_1-\beta_1}G_t + \tfrac{\beta_1\epsilon_{1t} + (1-\alpha_1)\epsilon_{2t} }{1-\alpha_1-\beta_1} \\
Y_t^* &= \tfrac{ \alpha_0+\beta_0 }{1-\alpha_1-\beta_1} - \tfrac{\beta_1 }{1-\alpha_1-\beta_1}Y_{t-1} + \tfrac{1}{1-\alpha_1-\beta_1}G_t + \tfrac{\epsilon_{1t} + \epsilon_{2t}}{1-\alpha_1-\beta_1}
\end{aligned}  \right.
\end{equation*}

Así, el multiplicador del gasto público es:
\begin{equation*}
\marginal{Y^*_t}{G_t} = \pi_{33} = \tfrac{1}{1-\alpha_1-\beta_1}
\end{equation*}

De nuevo, observe que los shocks reducidos son combinaciones lineales de los shocks estructurales.
{{ termina_ejemplo }}
