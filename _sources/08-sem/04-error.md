
```{include} ../math-definitions.md
```


# El término de error


##   Supuestos acerca del término de error: esperanza

```{panels}
Forma estructural
^^^
\begin{align*}
\E\left[\epsilon_t | x_t\right] &= 0 \\
\E\left[\epsilon_t\epsilon'_t | x_t\right] &= \Sigma \\
\E\left[\epsilon_t\epsilon'_s | x_t,x_s\right] &= 0
\end{align*}

---
Forma reducida
^^^
\begin{align*}
\E\left[\nu_t | x_t\right] &= \left(\Gamma^{-1}\right)'0 = 0 \\
\E\left[\nu_t\nu'_t | x_t\right] &= \left(\Gamma^{-1}\right)'\Sigma\Gamma^{-1} = \Omega \\
\E\left[\nu_t\nu'_s | x_t,x_s\right] &= \left(\Gamma^{-1}\right)'0\Gamma^{-1} = 0
\end{align*}
```


## Supuestos acerca del término de error: limíte de probabilidad
{ref}`Acerca de plim<appendix:plim>`

Si suponemos que
\begin{align*}
\plim\left(\tfrac{1}{T}E'E\right) &= \Sigma\\
\plim\left(\tfrac{1}{T}X'X\right) &= Q\\
\plim\left(\tfrac{1}{T}X'E\right) &= 0
\end{align*}

Tenemos que
\begin{equation*}
\plim\left(\frac{1}{T}\MAT{Y' \\ X' \\ V'}\MAT{Y & X & V}\right) = \MAT{\Pi'Q\Pi + \Omega & \Pi'Q & \Omega \\ Q\Pi & Q & 0'\\ \Omega & 0 &\Omega}
\end{equation*}

Entonces

```{panels}
Forma estructural
^^^
\begin{align*}
\plim\left(\tfrac{1}{T}E'E\right) &= \Sigma \\
\plim\left(\tfrac{1}{T}X'X\right) &= Q \\
\plim\left(\tfrac{1}{T}X'E\right) &= 0
\end{align*}

---
Forma reducida
^^^
\begin{align*}
\plim\left(\tfrac{1}{T}V'V\right) = \left(\Gamma^{-1}\right)'\Sigma\Gamma^{-1} &= \Omega\\
\plim\left(\tfrac{1}{T}X'X\right) &= Q \\
\plim\left(\tfrac{1}{T}X'V\right) = 0 \Gamma^{-1} &= 0
\end{align*}
```
