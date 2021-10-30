```{include} ../math-definitions.md
```
# El modelo SUR

Basado en \textcite[capítulo 10]{Greene:2012}

## Introducción

Hay modelos uniecuacionales que aplican a un grupo de variables relacionadas.

Ejemplos:

```{panels}
Modelo CAPM
^^^
\begin{equation*}
r_{it} - r_{ft} = \alpha_i + \beta_i\left(r_{Mt} - r_{ft}\right) + \epsilon_{it}
\end{equation*}

---
Modelos de inversión
^^^
\begin{equation*}
I_{it} = \beta_{1i} + \beta_{2i}F_{it} + \beta_{3i}C_{it} + \epsilon_{it}
\end{equation*}
```

Como los errores $\epsilon_{it}$ de las distintas ecuaciones pueden estar correlacionados, es preferible considerar los modelos de manera conjunta.

## Modelo de regresiones aparentemente no relacionadas (SUR)

En este modelo se presentan un grupo de variables dependientes, pero **NO simultáneas**.

Cada ecuación puede tener sus propias variables explicativas o éstas pueden ser las mismas para todas las ecuaciones.

Las ecuaciones del sistema son
\begin{equation*}
\left\{
\begin{aligned}
\y_1 &= \X_1\beta_1 + \e_1 \\
\y_2 &= \X_2\beta_2 + \e_2 \\
&\qquad\vdots \\
\y_M &= \X_M\beta_M + \e_M
\end{aligned}
\right.
\end{equation*}

que se pueden expresar como
\begin{equation*}
\simbolo{\stackEq{\y}}{\Y} =
\simbolo{\MAT{\X_1 & 0 & \dots & 0 \\
0 & \X_2 & \dots & 0 \\
& & \ddots \\
0 & 0 & \dots & \X_M} }{\X}
\simbolo{\stackEq{\beta}}{\beta} +
\simbolo{\stackEq{\e}}{\e}
\end{equation*}



## El modelo SUR: errores correlacionados

Se asume que perturbaciones de distintas observaciones no están correlacionadas, aunque las perturbaciones de distintas ecuaciones sí pueden estar correlacionados:
\begin{equation*}
\E\left[\e_i\e'_j | \X \right] = \sigma_{ij}I
\end{equation*}

o bien

\begin{equation*}
\simbolo{\E\left[\e \e' | \X\right]}{\Omega} =
\simbolo{\MAT{\sigma_{11}I & \sigma_{12}I & \dots & \sigma_{1M}I \\
        \sigma_{21}I & \sigma_{22}I & \dots & \sigma_{2M}I \\
        & & \ddots \\
        \sigma_{M1}I & \sigma_{M2}I & \dots & \sigma_{MM}I} }{\Sigma \otimes I}
\end{equation*}

{ref}`$\otimes$: el producto kronecker<appendix:kronecker>`


## Estimación de un modelo SUR
El modelo SUR

\begin{equation*}
\left.
\begin{aligned}
\Y&= \X\beta + \e \\
\E\left[\e | \X \right] &=0 \\
\Var\left[\e | \X \right] &=\Omega = \Sigma \otimes I
\end{aligned}
\right\}
\alert{\text{supuestos del modelo generalizado de regresión lineal!}}
\end{equation*}

puede ser estimado por FGLS:
\begin{align*}
\estimator{\beta}{GLS} &= \left[\X'\Omega^{-1}\X\right]^{-1}\X'\Omega^{-1}\Y \\
&= \left[\X'(\Sigma \otimes I)^{-1}\X\right]^{-1}\X'(\Sigma \otimes I)^{-1}\Y
\end{align*}



## Caso especial del modelo SUR

Si todas las regresiones tienen los mismos regresores, estimar el sistema SUR por GLS es equivalente a estimar ecuación por ecuación con OLS.

En el caso especial $\X_1 =\dots = \X_M = \mathbb{X}$ tenemos
\begin{equation*}
\X =
\MAT{\X_1 & 0 & \dots & 0 \\
    0 & \X_2 & \dots & 0 \\
    & & \ddots \\
    0 & 0 & \dots & \X_M}
=
\MAT{\mathbb{X} & 0 & \dots & 0 \\
    0 & \mathbb{X} & \dots & 0 \\
    & & \ddots \\
    0 & 0 & \dots & \mathbb{X}}
= I \otimes \mathbb{X}
\end{equation*}
y el estimador GLS es
\begin{align*}
\estimator{\beta}{GLS} &=\left[\X'(\Sigma \otimes I)^{-1}\X\right]^{-1}\X'(\Sigma \otimes I)^{-1}\Y \\
   &= \left[(I \otimes \mathbb{X})'(\Sigma \otimes I)^{-1}(I \otimes \mathbb{X})\right]^{-1}(I \otimes \mathbb{X})'(\Sigma \otimes I)^{-1}\Y \\
   &= \left[(I \otimes \mathbb{X}')(\Sigma^{-1} \otimes I)(I \otimes \mathbb{X})\right]^{-1}(I \otimes \mathbb{X}')(\Sigma^{-1} \otimes I)\Y \\
   &= \left[\Sigma^{-1} \otimes (\mathbb{X'X})\right]^{-1}\left[\Sigma^{-1} \otimes \mathbb{X}'\right]\Y \\
   &= \left[\Sigma \otimes (\mathbb{X'X})^{-1}\right]\left[\Sigma^{-1} \otimes \mathbb{X}'\right]\Y \\
   &= \left[I \otimes (\mathbb{X'X})^{-1}\mathbb{X}'\right]\Y \\
   &= \left[I \otimes (\mathbb{X'X})^{-1}\mathbb{X}'\right]\Y \\
   &= \MAT{(\mathbb{X'X})^{-1}\mathbb{X}' & 0 & \dots & 0 \\
   0 & (\mathbb{X'X})^{-1}\mathbb{X}' & \dots & 0 \\
& & \ddots \\
0 & 0 & \dots & (\mathbb{X'X})^{-1}\mathbb{X}'} \stackEq{\y} \\
&=   \stackEq{(\mathbb{X'X})^{-1}\mathbb{X}'\y} =   \stackEq{\estimator{\beta}{OLS}}
\end{align*}


## <presentation>
\begin{align*}
\estimator{\beta}{GLS}
&= \left[I \otimes (\mathbb{X'X})^{-1}\mathbb{X}'\right]\Y \\
&= \MAT{(\mathbb{X'X})^{-1}\mathbb{X}' & 0 & \dots & 0 \\
0 & (\mathbb{X'X})^{-1}\mathbb{X}' & \dots & 0 \\
& & \ddots \\
0 & 0 & \dots & (\mathbb{X'X})^{-1}\mathbb{X}'} \stackEq{\y} \\
&=   \stackEq{(\mathbb{X'X})^{-1}\mathbb{X}'\y} =   \stackEq{\estimator{\beta}{OLS}}
\end{align*}

```{tip}
Este resultado justifica que **un VAR sin restricciones se estima ecuación por ecuación con OLS**.
```
