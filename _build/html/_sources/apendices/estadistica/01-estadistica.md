# Resultados de teoría estadística

```{include} ../math-definitions.md
```


(appendix:grandes-numeros)=
## Ley de los grandes números
La ley débil de los grandes números establece que si $X_1, X_2, X_3, \dots$ es una sucesión infinita de variables aleatorias **independientes** que tienen el mismo valor esperado $\mu$ y varianza $\sigma^2$, entonces el promedio
\begin{equation*}
\overline{X}_n = \frac{X_1+\cdots+X_n}{n}
\end{equation*}
converge en probabilidad a $\mu$. En otras palabras, para cualquier número positivo $\epsilon$ se tiene
\begin{equation*}
\lim _{n\rightarrow \infty } \Prob\left(\left|{\overline {X}}_{n}-\mu \right|<\varepsilon \right)=1.
\end{equation*}


**Prueba (muy) informal**: Note que:

*  $\E[{\overline{X}}_n] = \mu$
*  $\Var[{\overline{X}}_n] = \frac{\sigma^2}{n} \to 0$ conforme $n\to\infty$.




(appendix:plim)=
## Convergencia en probabilidad

Una secuencia $\left\{X_n\right\}$ de variables aleatorias **converge en probabilidad** hacia la variable aleatoria $X$ si para todo $\epsilon>0$
\begin{equation*}
\lim\limits_{n\to\infty}\Pr\left(\left|X_n - X\right| > \epsilon\right) = 0
\end{equation*}

Para denotar que $\left\{X_n\right\}$ converge en probabilidad hacia $X$ escribimos
\begin{equation*}
\PLIM{X_n}{X} \qquad\text{ o bien }\quad \plim X_n = X
\end{equation*}


##  Propiedades de la convergencia en probabilidad
Sean $c$ una constante, $g()$ una función continua, y $X_n, Y_n$ dos secuencias de variables aleatorias. Entonces:

- $\plim c = c$
- $\plim cX_n = c\plim X_n$
- $\plim\left(X_n + Y_n\right) = \plim X_n + \plim Y_n$
- $\plim\left(X_n Y_n\right) = \left(\plim X_n\right) \left(\plim Y_n\right)$
- $\plim g(X_n) = g\left(\plim X_n\right)$
