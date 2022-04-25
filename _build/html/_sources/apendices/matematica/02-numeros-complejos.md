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
---

# Números complejos


```{include} ../../teoria/math-definitions.md
```

```{code-cell} ipython3
:tags: ["hide-input",]
import plotly.express as px
import numpy as np
```

(appendix:polar-complex)=
## Representación de números complejos
```{image} ../../imgs/polar-complex.png
```

(appendix:mult-complex)=
## Multiplicación de números complejos

Si {math}`z = Re^{i\theta}` y {math}`w = Se^{i\varphi}`, entonces su producto es
\begin{equation*}
zw = RS e^{i(\theta+\varphi)}
\end{equation*}


Así, si elevamos {math}`z` a la {math}`n`-ésima potencia:
\begin{equation*}
  z^n = \left(Re^{i\theta}\right)^n = R^ne^{in\theta}
\end{equation*}

Es decir
\begin{equation*}
\lim\limits_{n\to\infty}z^n = 0 \Leftrightarrow | R | < 1
\end{equation*}


### Ejemplos de potencia de números complejos

Cuando el módulo o valor absoluto {math}`R` de un número complejo está por debajo de 1, su potencia tiende a cero conforme el exponente tiende a infinito:

```{code-cell} ipython3
:tags: ["hide-input",]
𝜃 = 30
t = np.arange(48)

px.scatter_polar(r=0.95**t, theta=t*𝜃,
  animation_frame=t,
  start_angle=0,
  range_r=[0, 1.1],
  direction='counterclockwise')
```

Por el contrario, si {math}`R > 1`, la potencia tenderá alejarse cada vez más del origen:
```{code-cell} ipython3
:tags: ["hide-input",]
px.scatter_polar(r=1.03**t, theta=t*𝜃,
  animation_frame=t,
  start_angle=0,
  range_r=[0, 4.5],
  direction='counterclockwise')
```

En el caso intermedio en que {math}`R = 1`, la potencia se mantendrá orbitando en la circunferencia unitaria:
```{code-cell} ipython3
:tags: ["hide-input",]
px.scatter_polar(r=1.0**t, theta=t*𝜃,
  animation_frame=t,
  start_angle=0,
  range_r=[0, 1.5],
  direction='counterclockwise')
```
