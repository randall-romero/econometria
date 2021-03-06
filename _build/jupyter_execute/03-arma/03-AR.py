```{include} ../math-definitions.md
```

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from macrodemos.demo_ARMA import ARMA
from macrodemos.common_components import merge_plots

# Proceso autorregresivo AR(p)


## Proceso autorregresivo de primer orden: AR(1)

Sea $\left\{\epsilon_t\right\}_{t=-\infty}^\infty$ un proceso ruido blanco. Se define el proceso AR(1) como:
\begin{align*}
y_t  &= c + \phi y_{t-1} +  \epsilon_t \\
y_t - \phi y_{t-1} &= c + \epsilon_t \\
(1 - \phi\Lag)y_t &= c + \epsilon_t
\end{align*}

Siempre que $|\phi|<1$ podemos invertir el término $(1 - \phi\Lag)$
\begin{align*}
y_t  &= (1 - \phi\Lag)^{-1}\left(c + \epsilon_t\right) \\
     &= (1 - \phi\Lag)^{-1}c + (1 - \phi\Lag)^{-1}\epsilon_t \\
     &= \frac{c}{1-\phi} + \left(1 + \phi\Lag + \phi^2\Lag^2+\dots\right)\epsilon_{t}  \\
     &= \frac{c}{1-\phi} + \epsilon_{t} + \phi\epsilon_{t-1} + \phi^2\epsilon_{t-2} + \dots
\end{align*}


Vemos por tanto que si $|\phi|<1$ el proceso AR(1) puede escribirse como el proceso MA($\infty$)
\begin{equation*}
y_t  = \frac{c}{1-\phi} + \epsilon_{t} + \phi\epsilon_{t-1} + \phi^2\epsilon_{t-2} + \dots
\end{equation*}

Por lo que su valor esperado es:
\begin{equation*}
\E[y_t]  \equiv \mu = \frac{c}{1-\phi}
\end{equation*}

y su varianza es
\begin{align*}
\Var[y_t] \equiv \gamma_0 &= \left(1 + \phi^2 + \phi^4 + \phi^6 + \dots\right)\sigma^2\\
                          &= \frac{\sigma^2}{1-\phi^2}
\end{align*}

La representación MA($\infty$) nos muestra que $y_t$ depende de la perturbación presente $\epsilon_{t}$ y de **todas las pasadas** $\epsilon_{t-1}, \epsilon_{t-2}, \dots$, pero no depende de **ninguna de las perturbaciones futuras** $\epsilon_{t+1}, \epsilon_{t+2}, \dots$.

Por ello, la covarianza de $y_t$ con cualquier perturbación posterior $\epsilon_{t+k}$ (con $k>0$) es cero.


Sabiendo que un proceso AR(1) es estacionario si $|\phi|<1$, es fácil obtener sus momentos sin necesidad de obtener su representación MA($\infty$).

En el caso de la media:
\begin{align*}
	y_t             & = c + \phi y_{t-1} +  \epsilon_t         \\
	\E[y_t]         & = c + \phi \E[y_{t-1}] +  \E[\epsilon_t] \\
	\mu             & = c + \phi\mu + 0                        \\
	\Rightarrow \mu & = \frac{c}{1-\phi}
\end{align*}

Restando la tercera línea de la primera, vemos que el proceso puede escribirse como un AR(1) para la **desviación respecto a la media** sin la constante:
\begin{equation*}
\notation{y_t - \mu}{$\tilde{y}_t$}  = \phi ( \notation{y_{t-1} - \mu}{$\tilde{y}_{t-1}$} ) +  \epsilon_t
\end{equation*}

Por ello, en adelante ocasionalmente asumiremos que $c=0$ para simplificar el álgebra.


Para obtener su varianza elevamos al cuadrado la expresión anterior y tomamos su valor esperado
\begin{align*}
	\E\left(\tilde{y}_t^2\right) & = \E\left[\left(\phi \tilde{y}_{t-1} +  \epsilon_t\right)^2\right]                        \\
\gamma_0                     & = \E\left[\phi^2 \tilde{y}_{t-1}^2 + 2\phi\tilde{y}_{t-1}\epsilon_t + \epsilon_t^2\right] \\
                             & = \phi^2\gamma_0 + 2\times 0 + \sigma^2                                                   \\
\Rightarrow \gamma_0         & = \frac{\sigma^2}{1-\phi^2}
\end{align*}


Para obtener su autocovarianza $\gamma_j$, para $j\geq 1$, escribimos
\begin{align*}
	\tilde{y}_{t}                               & = \phi\tilde{y}_{t-1} +  \epsilon_t                                              \\
\end{align*}

multiplicamos ambos lados por $\tilde{y}_{t-j}$ y tomamos esperanza
\begin{align*}
\E\left[\tilde{y}_{t}\tilde{y}_{t-j}\right] & = \E\left[\phi\tilde{y}_{t-1}\tilde{y}_{t-j} +  \tilde{y}_{t-j}\epsilon_t\right] \\
\gamma_j                                    & =\phi\gamma_{j-1}
\end{align*}

Vemos que la función de autocorrelación es la solución de una ecuación en diferencia homogénea de primer orden, cuya solución es
\begin{equation*}
\gamma_j =\phi^j\gamma_0
\end{equation*}


Resumiendo los resultados que hemos obtenido
\begin{align*}
\E[y_t]   &= \mu = \frac{c}{1-\phi} \\
\Var[y_t] &= \gamma_0 = \frac{\sigma^2}{1 - \phi^2} \\
\Cov[y_t, y_{t-j}] &= \gamma_j = \phi^j \gamma_0 \\
&\phantom{= } \rho_j = \phi^j
\end{align*}

vemos que ninguno de estos momentos depende del tiempo $t$, por lo que el proceso AR(1) es covarianza-estacionario siempre y cuando $|\phi|<1$.



A partir de la representación MA($\infty$) del proceso AR(1) con $|\phi|<1$
\begin{equation*}
y_t  = \mu + \epsilon_{t} + \phi\epsilon_{t-1} + \phi^2\epsilon_{t-2} + \dots
\end{equation*}

es fácil observar que su función de impulso respuesta
\begin{equation*}
\Psi(j) = \marginal{y_{t+j}}{\epsilon_{t}} = \marginal{y_{t}}{\epsilon_{t-j}} = \phi^j
\end{equation*}
es idéntica a su función de autocorrelaciones.




{{ empieza_ejemplo }} AR(1) con $\phi>0$ {{ fin_titulo_ejemplo }}
$y_t  = 0.9y_{t-1} + \epsilon_t $

modelo_ar1p = ARMA(phi=[0.9])
modelo_ar1p.sample(120)

merge_plots(
   [modelo_ar1p.plot_process(), modelo_ar1p.plot_correlogram(18)],
   cols=2,
   subplot_titles=['Realización', 'Autocorrelación'] ,
   title_text=str(modelo_ar1p),
   shared_yaxes=False
)

{{ termina_ejemplo }}

{{ empieza_ejemplo }} AR(1) con $\phi<0$ {{ fin_titulo_ejemplo }}
$y_t  = -0.9y_{t-1} + \epsilon_t $

modelo_ar1n = ARMA(phi=[-0.9])
modelo_ar1n.sample(120)

merge_plots(
   [modelo_ar1n.plot_process(), modelo_ar1n.plot_correlogram(18)],
   cols=2,
   subplot_titles=['Realización', 'Autocorrelación'] ,
   title_text=str(modelo_ar1n),
   shared_yaxes=False
)

{{ termina_ejemplo }}



## El proceso AR(p)

Es fácil extender el proceso AR(1) para incluir más rezagos. El proceso AR(p) es
\begin{align*}
	y_t                                                      & = c + \phi_1 y_{t-1} +\dots + \phi_p y_{t-p} +  \epsilon_t \\
y_t - \phi_1 y_{t-1} -\dots - \phi_p y_{t-p}             & = c +  \epsilon_t \\
\left(1 - \phi_1\Lag^1 -\dots - \phi_p\Lag^p\right)y_{t} & = c +  \epsilon_t \\
\Phi(\Lag)y_{t}                                          & = c +  \epsilon_t
\end{align*}

El proceso AR(p) es una ecuación en diferencia de orden $p$. Esta ecuación es estable si y solo si las raíces del polinomio $1 - \phi_1z^1 -\dots - \phi_pz^p$ están todas **fuera** del círculo unitario.


Si el proceso es estable, resolvemos para $y_t$
\begin{align*}
y_{t} &= \Phi^{-1}(\Lag)\left(c +  \epsilon_t\right) \\
      &= \Phi^{-1}(1)c  + \Phi^{-1}(\Lag)\epsilon_t \\
      &= \frac{c}{1 - \phi_1 -\dots - \phi_p}  + \Phi^{-1}(\Lag)\epsilon_t
\end{align*}

Su valor esperado es
\begin{equation*}
	\E\left(y_t\right) = \frac{c}{1 - \phi_1 -\dots - \phi_p} =\mu
\end{equation*}

Similar a lo que obtuvimos para el proceso AR(1), podemos escribir el proceso AR(p) en términos de desviación de la media $\tilde{y}\equiv y-\mu$.
\begin{equation*}
\tilde{y}_t = \phi_1\tilde{y}_{t-1} +\dots + \phi_p\tilde{y}_{t-p} +  \epsilon_t
\end{equation*}

Para obtener su varianza y autocovarianzas multiplicamos la expresión anterior por $\tilde{y}_{t-j}$, con $j\geq0$, y calculamos el valor esperado
\begin{align*}
\E\left[\tilde{y}_t\tilde{y}_{t-j}\right] &= \E\left[\phi_1\tilde{y}_{t-1}\tilde{y}_{t-j} +\dots + \phi_p\tilde{y}_{t-p}\tilde{y}_{t-j} +  \epsilon_t\tilde{y}_{t-j}\right] \\
\gamma_j &=\begin{cases}
\phi_1\gamma_{1} +\dots + \phi_p\gamma_{p} + \sigma^2 & \text{ si } j=0 \\
\phi_1\gamma_{j-1} +\dots + \phi_p\gamma_{j-p}        & \text{ si } j>0
\end{cases}
\end{align*}


Si dividimos la última línea entre la varianza $\gamma_0$ obtenemos las

```{important} Ecuaciones Yule-Walker
\begin{equation*}
\rho_j = \phi_1\rho_{j-1} +\dots + \phi_p\rho_{j-p}, \text{ con } j>0
\end{equation*}
```

Esta es la misma ecuación en diferencia que el proceso original, por lo que en principio se puede resolver con los métodos convencionales, una vez que tengamos $p$ valores iniciales $\rho_0, \rho_1, \dots,\rho_{p-1}$.

En general, no es tan sencillo obtener despejar los valores de las autocorrelaciones $\rho_j$.


Para obtener la función de impulso respuesta, podríamos partir de la forma
\begin{equation*}
y_t = \mu + \Phi^{-1}(\Lag)\epsilon
\end{equation*}

pero esto requiere que obtengamos la forma explícita del polinomio de rezagos
\begin{equation*}
\Phi^{-1}(\Lag) = 1 + \psi_1\Lag + \psi_2\Lag^2+\dots
\end{equation*}


Ahora bien, reconociendo que un proceso AR(p) es una ecuación en diferencia de orden $p$, encontramos que
\begin{equation*}
\marginal{y_{t+j}}{\epsilon_t} = c_1\lambda_1^j + c_2\lambda_2^j +\dots + c_p\lambda_p^j
\end{equation*}
donde $\lambda_j$ son las raíces del polinomio característico $\lambda^p - \phi_1 \lambda^{p-1} -\dots - \phi_p$ **_(ver tema 2, p.19-20)._**



Para un proceso AR(p) estacionario, sabemos que todas las raíces $\lambda_j$ están dentro del círculo unitario.

Por ello, a partir de
\begin{equation*}
\marginal{y_{t+j}}{\epsilon_t} = c_1\lambda_1^j + c_2\lambda_2^j +\dots + c_p\lambda_p^j
\end{equation*}

sabemos que la función de impulso respuesta converge a cero en el largo plazo.

La forma de la función depende especialmente del valor $\lambda_j$ más grande:

* Si es positivo, decae geométricamente,
* Si es negativo, decae alternando de signo,
* Si es complejo, decae oscilando periódicamente **_(ver tema 2, p.25)._**


{{ empieza_ejemplo }} Ejemplo: AR(2) {{ fin_titulo_ejemplo }}
$y_t  = 0.9y_{t-1} - 0.625y_{t-2} +  \epsilon_t$

modelo_ar2 = ARMA(phi=[0.9, -0.625])
modelo_ar2.sample(120)

merge_plots(
   [modelo_ar2.plot_process(), modelo_ar2.plot_correlogram(18)],
   cols=2,
   subplot_titles=['Realización', 'Autocorrelación'] ,
   title_text=str(modelo_ar2),
   shared_yaxes=False
)

Con las ecuaciones Yule-Walker
\begin{align*}
\phi_1 + \phi_2\rho_1 &=\rho_1 \\
\phi_1\rho_1 + \phi_2 &=\rho_2
\end{align*}

encontramos
\begin{align*}
\rho_1 &= \frac{\phi_1}{1-\phi_2} \approx 0.5538\\
\rho_2 &= \phi_1\rho_1 + \phi_2 \approx -0.1265
\end{align*}

Las demás autocorrelaciones las encontramos con
\begin{equation*}
\rho_j = 0.9\rho_{j-1} - 0.625\rho_{j-2}
\end{equation*}


La ecuación característica es
\begin{equation*}
\lambda^2 - 0.9\lambda + 0.625=0
\end{equation*}

con raíces
\begin{align*}
\lambda &= 0.45 \pm 0.65i\\
       &\approx 0.79\left(\cos0.97 \pm i\sin0.97 \right)
\end{align*}

por lo que el proceso es estacionario:

modelo_ar2.plot_ar_roots()

Usando las [fórmulas de dinámica del ajuste](sec:dinamica-ajuste), encontramos su función impulso respuesta

\begin{equation*}
0.79^j\left[\cos(0.97j) - \tfrac{9}{13}\sin(0.97j) \right]
\end{equation*}

la cual converge a cero, oscilando periódicamente conforme $j\to\infty$.

modelo_ar2.plot_irf(24)

{{ termina_ejemplo }}


{{ empieza_ejemplo }} Ejemplo: AR(1) vs AR(2) {{ fin_titulo_ejemplo }}
Consideremos estos dos procesos autorregresivos:

y = ARMA(phi=[0.9])
z = ARMA(phi=[0.5, 0.4])


merge_plots(
   [y.plot_correlogram(18), z.plot_correlogram(18)],
   cols=2,
   subplot_titles=[str(y), str(z)],
   title_text='Autocorrelaciones',
)

Este caso ilustra que es sumamente difícil identificar el orden $p$ de un proceso AR(p) a partir de su autocorrelograma.


Para resolver este problema, a continuación estudiaremos la **autocorrelación parcial**.
{{ termina_ejemplo }}



## Autocorrelación parcial
<!-- %Hamilton 1994, p.111-112, KWH 2013, p52-55 -->

La autocorrelación parcial mide la correlación **restante** entre $y_t$ y $y_{t-k}$ una vez que se han eliminado la influencia de $y_{t-1}, y_{t-2},\dots, y_{t-k+1}$.
\begin{equation*}
y_t = \notationbrace{a_1^{(k)}y_{t-1} + a_2^{(k)}y_{t-2} + \dots + a_{k-1}^{(k)}y_{t-k+1}}{“eliminamos” este efecto} + a_k^{(k)}y_{t-k}
\end{equation*}

Es decir, las primeros $m$ autocorrelaciones parciales vienen de
\begin{align*}
	y_t & = a_1^{(1)}y_{t-1}                                                                       \\
	y_t & = a_1^{(2)}y_{t-1} + a_2^{(2)}y_{t-2}                                                    \\
	    & \vdots                                                                                   \\
	y_t & = a_1^{(m-1)}y_{t-1} + a_2^{(m-1)}y_{t-2} + \dots + a_{m-1}^{(m-1)}y_{t-m+1}             \\
	y_t & = a_1^{(m)}y_{t-1} + a_2^{(m)}y_{t-2} + \dots + a_{m-1}^{(m)}y_{t-m+1} + a_m^{(m)}y_{t-m}
\end{align*}


Para encontrar el valor de $a^{(k)}_k$ basta con resolver
\begin{equation*}
\MAT{1          & \rho_1     &\rho_2      & \dots  & \rho_{k-1} \\
     \rho_1     & 1          & \rho_1     & \dots  & \rho_{k-2} \\
     \rho_2     & \rho_1     & 1          & \dots  & \rho_{k-3} \\
     \vdots     & \vdots     & \vdots     & \ddots & \vdots     \\
     \rho_{k-1} & \rho_{k-2} & \rho_{k-3} &\dots & 1
}
\MAT{a_1^{(k)} \\
a_2^{(k)} \\
a_3^{(k)} \\
\vdots \\
a_{k}^{(k)}
} =
\MAT{\rho_1 \\ \rho_2 \\ \rho_3 \\ \vdots \\ \rho_k}
\end{equation*}

En adelante, denotaremos la $k$-ésima correlación parcial por $\varphi(k) \equiv a_k^{(k)}$



Comparando las ecuaciones del proceso AR(p) y de la autocorrelación parcial $k$:
\begin{align*}
  y_t &= \phi_1 y_{t-1} +\phi_2 y_{t-2} +\dots + \phi_p y_{t-p} +  \epsilon_t\\
      &= a_1^{(k)}y_{t-1} + a_2^{(k)}y_{t-2} + \dots + a_{k-1}^{(k)}y_{t-k+1} + a_k^{(k)}y_{t-k}
\end{align*}

vemos que

* si $k=p$, entonces $\varphi_k = \phi_p$
* si $k>p$, entonces $\varphi_k = 0$
* si $k=1$, entonces $\varphi_1 = \rho_1$




{{ empieza_ejemplo }} AR(1) vs AR(2), con autocorrelación parcial {{ fin_titulo_ejemplo }}

Consideremos de nuevo estos procesos autorregresivos:

merge_plots(
   [y.plot_partial_correlogram(18), z.plot_partial_correlogram(18)],
   cols=2,
   subplot_titles=[str(y), str(z)],
   title_text='Autocorrelación Parcial',
)

Ahora es muy sencillo identificar el orden $p$ de los proceso AR.


Para encontrar la segunda autocorrelación parcial, resolvemos
\begin{equation*}
\MAT{a_1 \\ \varphi_2} = \MAT{1 & \rho_1 \\ \rho_1 & 1}^{-1}\MAT{\rho_1 \\ \rho_2} = \frac{1}{1-\rho_1^2}\MAT{1 & -\rho_1 \\ -\rho_1 & 1}\MAT{\rho_1 \\ \rho_2}
\end{equation*}
de donde $\varphi_2 = \frac{\rho_2 - \rho_1^2}{1-\rho_1^2}$.


Para el proceso AR(1) sabemos que $\rho_k = \phi^k$, con lo que comprobamos que $\varphi_2 = \frac{\phi^2 - \phi^2}{1-\phi^2} = 0$.

En un ejemplo anterior encontramos que para un proceso AR(2) se cumple
\begin{align*}
\rho_1 &= \frac{\phi_1}{1-\phi_2} =\frac{5}{6} &
\rho_2 &= \phi_1\rho_1 + \phi_2 =\frac{49}{60}
\end{align*}

Al sustituir en la expresión para $\varphi_2$ comprobamos que
\begin{equation*}
\varphi_2 = \frac{\frac{49}{60} - \frac{25}{36}}{1-\frac{25}{36}} = 0.4 = \phi_2.
\end{equation*}
{{ termina_ejemplo }}