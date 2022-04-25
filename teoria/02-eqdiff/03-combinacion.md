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



# Solución por combinación de soluciones homogéneas y particulares

## La estrategia de solución

Para resolver la ecuación lineal en diferencia
\begin{equation*}
   y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + w_t
\end{equation*}
seguimos estos pasos


{badge}`Paso 1,badge-secondary`
~   Formamos la ecuación homogénea $y_t - \phi_1 y_{t-1} - \phi_2 y_{t-2} - \dots - \phi_p y_{t-p} = 0$ y encontramos sus $p$ soluciones;

{badge}`Paso 2,badge-secondary`
~   Encontramos una solución particular;

{badge}`Paso 3,badge-secondary`
~   Obtenemos la solución general como la suma de la solución particular  y una combinación lineal de todas las soluciones homogéneas;

{badge}`Paso 4,badge-secondary`
~   Eliminamos las constantes arbitrarias imponiendo $p$ condiciones iniciales en el problema.



## Ecuación homogénea de primer orden

Para la ecuación
\begin{equation*}
y_t = \phi y_{t-1}\quad\Rightarrow y_t - \phi y_{t-1} = 0
\end{equation*}

Solución trivial: $y_t = y_{t-1} = \dots = 0$, pero no es única.


La expresión $y^h_t = \phi^t$ también es una solución:
\begin{equation*}
\notation{\phi^t}{$y^h_t$} - \phi \notation{\left(\phi^{t-1}\right)}{$y^h_{t-1}$} = 0
\end{equation*}

Pero si $y^h_t$ es una solución, entonces $Ay^h_t$ también lo es, para cualquier escalar $A$:
\begin{equation*}
Ay^h_t - \phi\left(Ay^h_{t-1}\right) = A\left(y^h_t - \phi y^h_{t-1}\right) = 0
\end{equation*}



## Condición inicial para la ecuación homogénea de primer orden

Hemos obtenido que $y_t = A\phi^t$ resuelve $y_t - \phi y_{t-1} = 0$ Para determinar una valor específico de $A$, necesitamos una condición inicial.

Por ejemplo, supongamos que el valor de $y_t$ en $t=0$ es conocido. Entonces:
\begin{equation*}
y_0 = A\phi^0 \quad\Rightarrow A = y_0
\end{equation*}

Por lo que en ese caso la solución de la ecuación sería
\begin{equation*}
y_t = \phi^t y_0
\end{equation*}




## Ecuación homogénea de orden $p$

Para la ecuación
\begin{equation*}
y_t - \phi_1 y_{t-1} - \phi_2 y_{t-2} - \dots -  \phi_{p-1} y_{t-p+1} - \phi_p y_{t-p} = 0
\end{equation*}

Solución trivial es de nuevo: $y_t = y_{t-1} = \dots = 0$.


Supongamos que la expresión $y^h_t = z^t$ también es una solución. Sustituyendo en la ecuación:
\begin{align*}
z^t - \phi_1 z^{t-1} - \phi_2 z^{t-2} - \dots - \phi_{p-1} z^{t-p+1} - \phi_p z^{t-p} &= 0 \\
z^{t-p}\left[z^{p} - \phi_1 z^{p-1} - \phi_2 z^{p-2} - \dots - \phi_{p-1} z^{1} - \phi_p z^{0}\right] &= 0
\end{align*}

Hemos logrado cambiar el problema original por el de encontrar los ceros de un polinomio de grado $p$:
\begin{equation*}
z^{p} - \phi_1 z^{p-1} - \phi_2 z^{p-2} - \dots - \phi_{p-1} z - \phi_p = 0
\end{equation*}

Esta es la misma ecuación característica que encontramos en la sección anterior.





## Resolviendo la ecuación característica

Todo polinomio de grado $p$ tiene exactamente $p$ raíces, no necesariamente distintas o reales.

Supongamos que $z_1, z_2, \dots, z_p$ son las raíces del polinomio. Las soluciones homogéneas son entonces
\begin{equation*}
y^h_t \in \left\{z^t_1, z^t_2, \dots, z^t_p \right\}
\end{equation*}

Cualquier combinación lineal de estas soluciones $y^h_t = A_1z^t_1 + \dots + A_pz^t_p$ también es una solución:
\begin{multline*}
y_t - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p} = \left(A_1z^t_1 + \dots + A_pz^t_p\right) - \\ \phi_1\left(A_1z^{t-1}_1 + \dots + A_pz^{t-1}_p\right) - \dots - \phi_p \left(A_1z^{t-p}_1 + \dots + A_1z^{t-p}_p\right) = \\
A_1\left(z^t_1- \phi_1z^{t-1}_1 - \dots - \phi_p z^{t-p}_1 \right) +\dots + A_p\left(z^t_p- \phi_1z^{t-1}_p - \dots - \phi_p z^{t-p}_p \right) = \\
A_1z_1^{t-p}\left(z^p_1- \phi_1z^{p-1}_1 - \dots - \phi_p\right) +\dots + A_pz_p^{t-p}\left(z^p_p- \phi_1z^{p-1}_p - \dots - \phi_p\right) = 0
\end{multline*}


{{ empieza_ejemplo }} Resolviendo una ecuación por combinación {{ fin_titulo_ejemplo }}
<!-- %Enders, p.16 -->

\begin{equation*}
y_t = 0.9y_{t-1} - 0.2y_{t-2}+3
\end{equation*}

{badge}`Paso 1,badge-secondary`
:   Resolvemos la ecuación homogénea $y_t - 0.9y_{t-1} + 0.2y_{t-2} = 0$:
\begin{align*}
z^2 - 0.9z + 0.2 &= (z-0.4)(z-0.5) = 0\\
z\in\left\{0.4,0.5\right\} \quad&\Rightarrow\quad y_{1,t}^h = 0.4^t,\; y_{2,t}^h = 0.5^t
\end{align*}

Es fácil verificar que son las soluciones:

\begin{align*}
0.4^t - 0.9\left(0.4\right)^{t-1} + 0.2\left(0.4\right)^{t-2} &= \left(0.4\right)^{t-2}\left[(0.4)^2 - 0.9(0.4) + 0.2\right] = 0\\
0.5^t - 0.9\left(0.5\right)^{t-1} + 0.2\left(0.5\right)^{t-2} &= \left(0.5\right)^{t-2}\left[(0.5)^2 - 0.9(0.5) + 0.2\right] = 0
\end{align*}

{badge}`Paso 2,badge-secondary`
:   Supongamos que $y^p_t=c$, una constante, es una solución particular:
\begin{equation*}
c = 0.9c - 0.2c + 3 \quad\Rightarrow c= 10 \quad\Rightarrow y^p_t=10
\end{equation*}


{badge}`Paso 3,badge-secondary`
:   Obtenemos la solución general como la suma de la solución particular  y una combinación lineal de todas las soluciones homogéneas:
\begin{equation*}
y_t = A_1(0.4)^t + A_2(0.5)^t + 10
\end{equation*}

{badge}`Paso 4,badge-secondary`
:   Eliminamos $A_1, A_2$ imponiendo 2 condiciones iniciales: $y_0=13, y_1=11.3$.
\begin{equation*}
\begin{cases}
13 &=A_1+ A_2 +10 \\ 11.3 &=0.4A_1 + 0.5A_2 +10
\end{cases} \Rightarrow
\begin{cases}
A_1+ A_2 &= 3 \\ 0.4A_1 + 0.5A_2 &=1.3
\end{cases}
\end{equation*}

entonces $A_1 = 2, A_2 = 1$ y la solución general de la ecuación es:
\begin{equation*}
y_t = 2(0.4)^t + (0.5)^t + 10
\end{equation*}
{{ termina_ejemplo }}


{{ empieza_ejemplo }} Resolviendo la ecuación con `sympy`{{ fin_titulo_ejemplo }}
Podemos también resolver este sistema utilizando el paquete `sympy` de Python:

```{code-cell} ipython3
from sympy import Function, rsolve
from sympy.abc import t

y = Function('y')
rsolve(y(t) - 0.9*y(t-1) + 0.2*y(t-2) - 3, y(t), {y(0):13, y(1): 11.3})
```
{{ termina_ejemplo }}
