
```{include} ../math-definitions.md
```


# Raíces unitarias estacionales


## Diferenciación estacional y raíces unitarias

Si para modelar una serie estacional es necesario aplicar el operador $\Delta_s=(1-\Lag^s)$, entonces la serie original tiene una raíz unitaria estacional: $1-1^s = 0$.

Pero 1 no es la única raíz de $1-\Lag^s$: al ser este un polinomio de grado $s$, tiene exactamente $s$ raíces (no necesariamente todas reales):

\begin{equation*}
z_k = e^{\frac{2k\pi}{n}i}, \qquad k=0,1,\dots, s\\
\end{equation*}

o bien, usando la fórmula de Euler

\begin{equation*}
z_k = \cos\left(\frac{2k\pi}{n}\right) + i\sin\left(\frac{2k\pi}{n}\right)
\end{equation*}

Todas estas raíces están equidistanciadas en la circunferencia unitaria.

```{panels}
Mensuales
^^^
![](figures/diff12roots.png)

$\cos\left(\frac{k\pi}{6}\right) + i\sin\left(\frac{k\pi}{6}\right)$
---

Trimestrales
^^^
![](figures/diff4roots.png)

$\cos\left(\frac{k\pi}{2}\right) + i\sin\left(\frac{k\pi}{2}\right)$
```



## Pruebas de raíz unitaria estacional

La literatura provee varias pruebas para detectar raíces unitarias.
Una de ellas es la prueba de Dickey, Hasza y Fuller (DHF, 1984), la cual es una extensión de la prueba Dickey Fuller:
\begin{align*}
y_{t} &= \rho y_{t-s} + \epsilon_{t}\\
y_{t} - y_{t-s} &= (\rho-1) y_{t-s} + \epsilon_{t}\\
\Delta_s y_t &= \gamma y_{t-s} + \epsilon_{t}
\end{align*}

Al igual que en la prueba DF, la hipótesis nula es $\gamma=0$ contra la alternativa $\gamma <0$, aunque los valores críticos son distintos.

Una limitación de esta prueba es que no es apropiada para diagnosticar la presencia de las otras raíces unitarias estacionales.


Existen otras pruebas de raíces unitarias estacionales

- La prueba HEGY de Hylleberg, Engle, Granger, y Yoo (1990)
- La prueba de Kunst (1997)
- La prueba OCSB, de Osborn, Chui, Smith y Birchenhall (1988)
- La prueba CH, de Canova y Hansen (1995)

Sin embargo, no estudiaremos estas pruebas en este curso.
