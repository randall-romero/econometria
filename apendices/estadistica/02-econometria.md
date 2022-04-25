# Resultados de econometría

```{include} ../math-definitions.md
```


(appendix:sesgo-simultaneidad)=
##  Sesgo de simultaneidad

Considere el modelo
\begin{align*}
  C_t &= \alpha + \beta Y_t + \epsilon \\
  Y_t &= C_t + I_t
\end{align*}

Esto implica que $Y_t = \frac{\alpha + I_t}{1-\beta} + \frac{\epsilon_t}{1-\beta}$.

Si se estima la primera ecuación por OLS, la estimación será **inconsistente** porque
\begin{equation*}
\Cov\left(Y_t, \epsilon_t\right) = \Cov\left(\frac{\epsilon_t}{1-\beta}, \epsilon_t\right) = \frac{1}{1-\beta}\Var\left(\epsilon_t\right) \neq 0
\end{equation*}
