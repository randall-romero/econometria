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


# La función de impulso respuesta

## Impulso respuesta

\begin{equation*}
\hat{Y}_{t+s} = \xi_{t+s} + \Phi\xi_{t+s-1} +\dots+ \alert{\Phi^s\xi_{t}} + \Phi^{s+1}\hat{Y}_{t-1}
\end{equation*}

La función de **impulso-respueta** mide la respuesta observada en la variable $m$-ésima $s$ períodos después ($\hat{Y}_{t+s,m}$) de que se presenta un impulso en la $k$-ésima variable ($\xi_{t,k}$)

Viene dada por
\begin{equation*}
\marginal{\hat{Y}_{t+s,m}}{\xi_{t,k}} = \left(\Phi^s\right)_{km}
\end{equation*}

es decir, por el elemento en la fila $k$, columna $m$, de la matriz $\Phi$ elevada al número de períodos $s$.



## Interpretando la función de impulso-respuesta
Suponga que

-  el sistema estaba en equilibrio en $t-1$, es decir $\alert{\hat{Y}_{t-1}=0}$
-  hay un shock $v' = \MAT{v_1&\dots&v_n}$ a las variables en $t$, $\alert{\xi_t = v}$
-  el shock es transitorio: $\alert{0=\xi_{t+1} = \xi_{t+2}=\dots}$

En este caso, la desviación del sistema respecto a su equilibrio $s$ períodos después del shock es
\begin{equation*}
\hat{Y}_{t+s} = \Phi^sv
\end{equation*}


\begin{equation*}
\Omega = PP' = \left[\Gamma_0^{-1}\Sigma^{1/2}\right] \left[\Gamma_0^{-1}\Sigma^{1/2}\right]' = \Gamma_0^{-1}\Sigma{\Gamma'}_0^{-1}
\end{equation*}

En la práctica, estamos interesados en shocks $\varepsilon_t$ a las ecuaciones estructurales, en vez de a las ecuaciones reducidas $\epsilon_t$. Esto para tomar en cuenta los efectos contemporáneos del shock.

Para calcular las respuestas, nos valemos de $\epsilon_t = \Gamma_0^{-1}\varepsilon_t$ y de la descomposición de Cholesky de la covarianza de los errores reducidos $\Omega$:

| Tamaño del impulso | Impulso estructural          | Impulso reducido                | Respuesta                          |
|--------------------|------------------------------|---------------------------------|------------------------------------|
| unitarios          | $\varepsilon_t=I$            | $v = \Gamma_0^{-1}$             | $\Phi^s\Gamma_0^{-1}$              |
| 1 desv. estándar   | $\varepsilon_t=\Sigma^{1/2}$ | $v = \Gamma_0^{-1}\Sigma^{1/2}$ | $\Phi^s \Gamma_0^{-1}\Sigma^{1/2}$ |


{{ empieza_ejemplo }} Impulso respuesta y descomposición de Cholesky {{ fin_titulo_ejemplo }}

Siguiendo con el ejemplo anterior, si $y'_t=\MAT{m_t & r_t & k_t}$ y la matriz de covarianza reducida es

\begin{equation*}
\begin{aligned}
\Omega = \MAT{1 & 0.5 & -1 \\ 0.5 & 4.25 & 2.5\\ -1 &  2.5 & 12.25}
&=\simbolo{\MAT{1 & 0 & 0\\ 0.5 & 2 & 0\\-1 & 1.5 & 3}}{P}
\simbolo{\MAT{1 & 0.5 & -1\\ 0 & 2 & 1.5 \\0 & 0 & 3}}{P'} \\
&=\simbolo{\MAT{1 & 0 & 0\\ 0.5 & 1 & 0\\-1 & 0.75 & 1}}{\Gamma_0^{-1}}
\simbolo{\MAT{1 & 0 & 0\\ 0 & 4 & 0 \\0 & 0 & 9}}{\Sigma}
\simbolo{\MAT{1 & 0.5 & -1\\ 0 & 1 & 0.75 \\0 & 0 & 1}}{{\Gamma'}_0^{-1}}
\end{aligned}
\end{equation*}

La respuesta del sistema a un shock en $k_t$ se calcula a partir de...

-  $v'=\MAT{0 & 2 & 1.5}$ si el shock es de una desviación estándar.
-  $v'=\MAT{0 & 1 & 0.75}$ si el shock es unitario.
{{ termina_ejemplo }}
