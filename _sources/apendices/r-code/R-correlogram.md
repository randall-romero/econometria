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

(Rcode-correlogram)=
# Correlogramas con R

**Cálculando el autocorrelograma del IMAE de Costa Rica**

Importar las librerías necesarias

```{code-cell} r
library(readr)
library(fpp3)
library(patchwork)
```

Leemos datos del IMAE de Costa Rica (original y tendencia-ciclo), indexamos datos como series de tiempo


```{code-cell} r
datos <- read.csv("../data/log-imae.csv", stringsAsFactors=FALSE) %>%
  mutate(mes = yearmonth(seq(as.Date("1991-01-01"), as.Date("2019-12-01"), by = "1 month"))) %>%
  as_tsibble(index=`mes`) %>%
  select(mes, Original, Tendencia.ciclo)
```

Las primeras dos líneas del código anterior serían mejores como

```r
datos <- read.csv("../data/log-imae.csv", stringsAsFactors=FALSE) %>%
  mutate(mes = yearmonth(X) %>%
```
pero por alguna extraña razón `yearmonth` está convirtiendo los meses 11 como enero y 12 como febrero! (al menos en mi instalación con Linux).



## Graficamos las dos series
```{code-cell} r
datos %>% gather() %>% autoplot()
```

## Autocorrelogramas
```{code-cell} r
datos %>% ACF(Original) %>% autoplot() + xlab(" ") -> fig1a
datos %>% ACF(Tendencia.ciclo) %>% autoplot() + xlab(" ") -> fig1b

datos %>% mutate(temp = difference(Original)) %>% ACF(temp) %>% autoplot() + xlab(" ") -> fig2a
datos %>% mutate(temp = difference(Tendencia.ciclo)) %>% ACF(temp) %>% autoplot() + xlab(" ") -> fig2b

datos %>% mutate(temp = difference(Original, lag=12)) %>% ACF(temp) %>% autoplot() + xlab(" ") -> fig3a
datos %>% mutate(temp = difference(Tendencia.ciclo, lag=12)) %>% ACF(temp) %>% autoplot() + xlab(" ") -> fig3b

(fig1a | fig1b) / (fig2a | fig2b) / (fig3a | fig3b)
```


## Autocorrelogramas parciales
```{code-cell} r
datos %>% ACF(Original, type="partial") %>% autoplot() + xlab(" ") -> figP1a
datos %>% ACF(Tendencia.ciclo, type="partial") %>% autoplot() + xlab(" ")-> figP1b

datos %>% mutate(temp = difference(Original)) %>% ACF(temp, type="partial") %>% autoplot() + xlab(" ") -> figP2a
datos %>% mutate(temp = difference(Tendencia.ciclo)) %>% ACF(temp, type="partial") %>% autoplot() + xlab(" ")-> figP2b

datos %>% mutate(temp = difference(Original, lag=12)) %>% ACF(temp, type="partial") %>% autoplot() + xlab(" ") -> figP3a
datos %>% mutate(temp = difference(Tendencia.ciclo, lag=12)) %>% ACF(temp, type="partial") %>% autoplot() + xlab(" ") -> figP3b

(figP1a | figP1b) / (figP2a | figP2b) / (figP3a | figP3b)
```
