# Acerca de este capítulo


Este tema constituye el primer paso para el estudio de la econometría de series de tiempo.

En esta presentación, se asumirá que todas las variables son determinísticas (no estocásticas).

El interés de esta presentación es el estudio de las consecuencias **dinámicas** de eventos a través del **tiempo**.

Se limita la exposición a ecuaciones en diferencia lineales.




## Ecuación en diferencia lineal de orden $p$

La variable $y_t$ evoluciona como un ecuación en diferencia de orden $p$ cuando depende de sus últimos $p$ valores
\begin{equation*}
y_t = \phi_1 y_{t-1} + \phi_2 y_{t-2} + \dots + \phi_p y_{t-p} + w_t
\end{equation*}

 Si $w_t=0$ en todo período $t$, obtenemos la ecuación en diferencia lineal homogénea
\begin{equation*}
y_t - \phi_1 y_{t-1} - \phi_2 y_{t-2} - \dots - \phi_p y_{t-p} = 0
\end{equation*}

Nuestra meta es responder a: **¿cuál es el efecto sobre la trayectoria de $y$ de un cambio en $w$?**




## Ecuación en diferencia de primer orden

Si $p=1$, la variable $y_t$ evoluciona como un ecuación en diferencia de primer orden 
\begin{equation*}
y_t = \phi y_{t-1} + w_t
\end{equation*}

En este caso, la ecuación homogénea correspondiente es
\begin{equation*}
y_t - \phi y_{t-1} = 0
\end{equation*}

