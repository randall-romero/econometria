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




# Estacionariedad

\begin{equation*}
\hat{Y}_{t+s} = \xi_{t+s} + \Phi\xi_{t+s-1} +\dots+\Phi^s\xi_{t} + \Phi^{s+1}\hat{Y}_{t-1}
\end{equation*}

Recuerde que la respuesta del VAR $s$ períodos después a un impulso $\xi_{t}$ es $\Phi^s\xi_{t}$.

Si el VAR es estacionario, toda respuesta a cualquier impulso en $t$ debe ser transitoria:
\begin{equation*}
\lim\limits_{s\to\infty}\Phi^s\xi_{t} = 0.
\end{equation*}

De lo contrario, la media $\mu$ del proceso no sería constante.

Es decir, el VAR es estacionario si y sólo si
\begin{equation*}
\lim\limits_{s\to\infty}\Phi^s = 0
\end{equation*}



## Condiciones para la estacionariedad

$Y$ es estacionario si y solo si todos los eigenvalores de $\Phi$ están dentro {ref}`del círculo unitario<appendix:mult-complex>`.

Los eigenvalores $\lambda$ de $\Phi$ satisfacen:
\begin{equation*}
\left|I\lambda^p - \Phi_1\lambda^{p-1} - \dots -\Phi_p\right| = 0
\end{equation*}

{{ empieza_ejemplo }}  Estacionariedad de un VAR(2) {{ fin_titulo_ejemplo }}

Para el VAR(2) del ejemplo anterior:

\begin{align*}
0 &=\left|\MAT{1 & 0 \\ 0 & 1}\lambda^2 - \MAT{.5 & .1\\.4 & .5}\lambda - \MAT{0 & 0\\.25 & 0} \right| \\
 &=\left|\MAT{\lambda^2 -.5\lambda & -.1\lambda \\ -.4\lambda -.25 & \lambda^2 - .5\lambda} \right|\\
&=\left(\lambda^2 -.5\lambda\right)\left(\lambda^2 - .5\lambda\right)-\left(-.4\lambda -.25\right)\left(-.1\lambda \right) \\
&= \lambda^4 -\lambda^3+0.21\lambda^2-0.025\lambda
\end{align*}

Las raíces de este polinomio son
\begin{align*}
\lambda_1 &= 0                &\rightarrow |\lambda_1| &= 0      \\
\lambda_2 &= 0.7693           &\rightarrow |\lambda_2| &= 0.7693      \\
\lambda_3 &= 0.1154+0.1385i   &\rightarrow |\lambda_3| &= \sqrt{0.1154^2+0.1385^2} \approx 0.1803  \\
\lambda_4 &= 0.1154-0.1385i   &\rightarrow |\lambda_4| &= \sqrt{0.1154^2+0.1385^2} \approx 0.1803   
\end{align*}

todas ellas dentro del círculo unitario. Por lo tanto, el VAR es estacionario.
{{ termina_ejemplo }}








{{ empieza_ejemplo }}  {Dinámica de un VAR} {{ fin_titulo_ejemplo }}



-  Hasta el momento hemos estudiado

-  cómo determinar si un VAR es estacionario
-  la función de impulso respuesta

-  En el cuaderno de Jupyter \texttt{02 Simulacion de un VAR.ipynb} se introduce un ejemplo para analizar un VAR.
-  En el cuaderno de Jupyter \texttt{03 VAR(1) clase.ipynb} se presentan 5 modelos VAR reducidos. Acá definimos una \alert{clase} para representar un VAR.


{{ termina_ejemplo }}
