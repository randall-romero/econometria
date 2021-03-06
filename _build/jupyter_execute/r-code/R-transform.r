(Rcode-transform)=
# Transformaciones con R

**Cálculo de transformaciones de la serie del PIB de Costa Rica**

Importar las librerías necesarias

library(readr)
library(fpp3)
library(slider)
#library(ggplot2)

Leer datos del PIB trimestral de Costa Rica e indexar datos como serie de tiempo

datos <- read_csv("../data/CR-PIB.csv") %>%
  mutate(trimestre = yearquarter(periodo)) %>%
  as_tsibble(index=trimestre) %>%
  select(trimestre, pib)

Datos originales

datos %>% autoplot(pib) +
  labs(title = "Producto Interno Bruto de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")

Primera diferencia

datos %>% mutate(Dpib=difference(pib)) %>%
  autoplot(Dpib) +
  labs(title = "Cambio trimestral en el PIB de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")

Tasa de variación

datos %>% mutate(growth=100* difference(pib) / lag(pib)) %>%
  autoplot(growth) +
  labs(title = "Tasa de crecimiento trimestral del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")

Tasa de variación continua

datos %>% mutate(growth=100* difference(log(pib))) %>%
  autoplot(growth) +
  labs(title = "Tasa de crecimiento trimestral del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")

Cambio interanual

datos %>% mutate(growth=100* difference(pib, lag=4) / lag(pib)) %>%
  autoplot(growth) +
  labs(title = "Cambio interanual en el PIB de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")

Tasa de variación interanual

datos %>% mutate(growth=100* difference(log(pib), lag=4)) %>%
  autoplot(growth) +
  labs(title = " de crecimiento interanual del PIB de Costa Rica") +
  ylab("por ciento") + xlab(" ")

Serie suavizada

datos %>% mutate(suave=slide_dbl(pib, mean, .before=4, .complete=TRUE)) %>%
  select(trimestre, pib, suave) %>%
  gather() %>%
  autoplot() + geom_line() +
  labs(title = "Producto Interno Bruto de Costa Rica") +
  ylab("billones de colones constantes") + xlab(" ")

{ref}`Volver al texto principal.<subsec-nivel-serie>`