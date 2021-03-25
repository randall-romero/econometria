```{include} ../math-definitions.md
```

# Motivación


## ¿Cómo afecta el dinero al producto? Keynesianos vs Clásicos

Basado en \textcite[ch.1]{Walsh:2010}


Cuando la oferta de dinero aumenta, el empleo y el producto real...

```{panels}
Clásicos
^^^
no se ven afectados.

---
Keynesianos
^^^
también aumentan.
```

En palabras de \textcite{Lucas:1996}:

>   Esta tensión entre dos ideas incompatibles ---que cambios en dinero son cambios neutrales de unidades, y que inducen movimientos en empleo y producción de la misma direción--- ha estado en el centro de la teoría monetaria al menos desde Hume (1752).


## Un econometrista al rescate

Para resolver este problema, un econometrista estima el modelo
\begin{equation*}
y_t = \bar{y} + \alpha_0 m_t + \alpha_1 m_{t-1} + c_0 z_t + c_1 z_{t-1} + u_t
\end{equation*}
donde $m$ es dinero, $y$ es producto, $z$ una variable de control.

-  Si $\alpha_0=\alpha_1=0$, los keynesianos estarían en problemas.
-  Si $\alpha_0>0$ o $\alpha_1>0$, los clásicos estarían en problemas.

## Una regla de política monetaria

Suponga que el banco central desea estabilizar el producto alrededor de $\bar{y}$.

Para ello fija la oferta de dinero así:
\begin{align*}
m^*_t &= \argmin{m_t}\E\left(y_t-\bar{y}\right)^2 \\
      &= \argmin{m_t}\E\left(\alpha_0 m_t + \alpha_1 m_{t-1} + c_0 z_t + c_1 z_{t-1} + u_t\right)^2 \\
      &= -\frac{\alpha_1}{\alpha_0}m_{t-1} - \frac{c_1}{\alpha_0} z_{t-1}
\end{align*}
donde se supone que el banco central espera $\E z_t=0$.

La regla de política sería
\begin{equation*}
  m^*_t = \pi_1 m_{t-1} +\pi_2 z_{t-1} + \nu_t
\end{equation*}  }


## Otra versión de los hechos

Ahora suponga que el producto real depende solo de cambios **sorpresivos** en la oferta de dinero $\nu_t$:
\begin{equation*}
y_t = \bar{y} + d_0 v_t + d_1 z_t + d_2 z_{t-1} + u_t
\end{equation*}

Pero la regla de política implica $\alert{v_t = m_t - \pi_1 m_{t-1}  - \pi_2 z_{t-1}}$

Entonces:
\begin{align*}
y_t &= \bar{y} + d_0[m_t - \pi_1 m_{t-1}  - \pi_2 z_{t-1}] + d_1 z_t + d_2 z_{t-1} + u_t \\
    &= \bar{y} + d_0 m_t - \alert{d_0\pi_1} m_{t-1} + d_1 z_t + \alert{(d_2 - d_0\pi_2)} z_{t-1} + u_t
\end{align*}

## Un econometrista en problemas
El econometrista compara los dos modelos:


\begin{align*}
\text{keynes}\qquad  & y_t = \bar{y} + \alpha_0 m_t + \alpha_1 m_{t-1} + c_0 z_t + c_1 z_{t-1} + u_t \\
\text{clásico}\qquad & y_t = \bar{y} + d_0 m_t - d_0\pi_1 m_{t-1} + d_1 z_t + (d_2 - d_0\pi_2) z_{t-1} + u_t
\end{align*}

La estimación de la regresión no puede distinguir entre las dos hipótesis propuestas: los modelos resultan en regresiones **observacionalmente equivalentes**.

Los parámetros estimados pueden depender de la regla de política.

Así, el ejercicio estaría sujeto a la crítica de \textcite{Lucas:1976}: **no podemos predecir qué pasaría si cambia la política, porque el modelo podría no ser invariante a la política misma**.



## Un econometrista con más problemas

Suponga que el econometrista se conforma con estimar el modelo
\begin{equation*}
  y_t = \bar{y} + \alpha_0 m_t + \alpha_1 m_{t-1} + c_0 z_t + c_1 z_{t-1} + u_t
\end{equation*}

y que $z_t$ es el déficit fiscal.

Si $\tau$ es la tasa impositiva media y el gasto público $\bar{g}$ es constante, entonces:
\begin{equation*}
  z_t = \bar{g} - \tau y_t
\end{equation*}

En este caso, estimar el modelo por OLS resulta en **{ref}`estimadores sesgados e inconsistentes!<appendix:sesgo-simultaneidad>`**


## Un modelo de ecuaciones simultáneas (VAR estructural)


Dado que en modelos macro las variables son endógenas, es necesario considerar un **sistema de  ecuaciones**.
\begin{equation*}
  \MAT{1 & -\alpha_0 & -c_0 \\ 0 & 1 & 0 \\ \tau & 0 & 1} \MAT{y_t \\ m_t \\ z_t} =
  \MAT{\bar{y} \\ 0 \\ \bar{g}} +    \MAT{0 & \alpha_1 & c_1 \\ 0 & \pi_1 & \pi_2 \\ 0 & 0 & 0} \MAT{y_{t-1} \\ m_{t-1} \\z_{t-1}} +
  \MAT{u_t \\ \nu_t \\ 0}
\end{equation*}

Su estimación exige imponer (muchas) restricciones. Por ejemplo, acá imponemos la restricción de que $z_t$ no afecta a $m_t$ en el mismo período.



## Resolviendo el sesgo de simulateidad
Según \textcite[pp.14-15]{Sims:1980}

>  Debido a que los grandes modelos existentes contienen demasiadas restricciones increíbles, la investigación empírica dedicada a probar teorías macroeconómicas alternativas con demasiada frecuencia procede en un marco de una o pocas ecuaciones.
>
>  Esta razón es suficiente para que valga la pena investigar la posibilidad de crear grandes modelos en un estilo que no tienda a acumular restricciones tan caprichosamente...
>
> **Debe ser factible estimar modelos macro de gran escala como formas reducidas sin restricciones, tratando todas las variable como endógenas.**

## Un vector autor-regresivo (VAR)
````{margin}
```{warning}
El modelo original de Sims es de 6 ecuaciones; acá solo ilustramos la propuesta.
```
````

Así, lo que \textcite{Sims:1980} propone es estimar
\begin{align*}
y_t &= \bar{y} + \alpha_{11}y_{t-1} + \alpha_{12}m_{t-1} + \alpha_{13}z_{t-1} + u^y_t\\
m_t &= \bar{m} + \alpha_{21}y_{t-1} + \alpha_{22}m_{t-1} + \alpha_{23}z_{t-1} + u^m_t\\
z_t &= \bar{z} + \alpha_{31}y_{t-1} + \alpha_{32}m_{t-1} + \alpha_{33}z_{t-1} + u^z_t
\end{align*}

Este es un **modelo reducido**: Las variables $y_t, m_t, z_t$ no interactuan contemporáneamente.

También es un **modelo SUR** con regresores idénticos: todas las ecuaciones tienen los mismos regresores; los errores están correlacionados.

Al ser un modelo SUR con regresores idénticos, **puede estimarse con OLS ecuación por ecuación**. En la siguiente sección estudiamos por qué esto es así.
