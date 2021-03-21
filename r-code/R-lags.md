---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: R
  language: R
  name: ir
---

(Rcode-lags)=
# Rezagos con R

**Ejemplo numérico para ilustrar el uso de los operadores de rezago, diferencia, y diferencia estacional.**

+++

Basado en Levendis 2018 Time Series Econometrics, pp4-5

+++

Importar las librerías necesarias

```{code-cell} r
library(readr)
library(fpp3)
```

Leer una serie de tiempo ficticia de data\LandD.csv, declarar los datos como serie de tiempo

```{code-cell} r
datos <- read_csv("../data/LandD.csv") %>%
  mutate(trimestre = yearquarter(trimestre)) %>%
  as_tsibble(index=trimestre) %>%
  select(trimestre, y)

datos
```

Operador de rezagos

```{code-cell} r
datos <- datos %>% mutate(
  Lag_y = lag(y),
  Lag2_y = lag(y, 2)
)
```

Operador de diferencias

```{code-cell} r
datos <- datos %>% mutate(
  D_y = difference(y),
  D2_y = difference(y, differences = 2)
)
```

Operador de diferencia estacional

```{code-cell} r
datos <- datos %>% mutate(
  S_y = difference(y, lag = 4)
)
```

Mostrar los resultados

```{code-cell} r
show(datos)
```

{ref}`Volver al texto principal.<example-lags-and-diffs>`
