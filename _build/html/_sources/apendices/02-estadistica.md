# Apuntes de teoría estadística

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
