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

(Rcode-transform)=
# Transformaciones con R

**Cálculo de transformaciones de la serie del PIB de Costa Rica**

Importar las librerías necesarias

```{code-cell} r
library(readr)
library(fpp3)
library(slider)
#library(ggplot2)
```

Leer datos del PIB trimestral de Costa Rica e indexar datos como serie de tiempo

```{code-cell} r
datos <- read_csv("../data/CR-PIB.csv") %>%
  mutate(trimestre = yearquarter(periodo)) %>%
  as_tsibble(index=trimestre) %>%
  select(trimestre, pib)
```

Datos originales

```{code-cell} r
datos %>% autoplot(pib) +
  labs(title = "Producto Interno Bruto de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")
```

Primera diferencia

```{code-cell} r
datos %>% mutate(Dpib=difference(pib)) %>%
  autoplot(Dpib) +
  labs(title = "Cambio trimestral en el PIB de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")
```

Tasa de variación

```{code-cell} r
datos %>% mutate(growth=100* difference(pib) / lag(pib)) %>%
  autoplot(growth) +
  labs(title = "Tasa de crecimiento trimestral del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")
```

Tasa de variación continua

```{code-cell} r
datos %>% mutate(growth=100* difference(log(pib))) %>%
  autoplot(growth) +
  labs(title = "Tasa de crecimiento trimestral del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")
```

Cambio interanual

```{code-cell} r
datos %>% mutate(growth=100* difference(pib, lag=4) / lag(pib)) %>%
  autoplot(growth) +
  labs(title = "Cambio interanual en el PIB de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")
```

Tasa de variación interanual

```{code-cell} r
datos %>% mutate(growth=100* difference(log(pib), lag=4)) %>%
  autoplot(growth) +
  labs(title = " de crecimiento interanual del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")
```

Serie suavizada

```{code-cell} r
datos %>% mutate(suave=slide_dbl(pib, mean, .before=4, .complete=TRUE)) %>%
  select(trimestre, pib, suave) %>%
  gather() %>%
  autoplot() + geom_line() +
  labs(title = "Producto Interno Bruto de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")
```
{ref}`Volver al texto principal.<subsec-nivel-serie>`
