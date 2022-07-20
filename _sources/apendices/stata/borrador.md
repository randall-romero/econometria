---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Stata
  language: stata
  name: stata
---

(Rcode-correlogram)=
# Correlogramas con Stata

**Cálculando el autocorrelograma del IMAE de Costa Rica**

Importar las librerías necesarias

```{code-cell} stata
%set graph_format png
set autotabgraphs on

clear *
```

Leemos datos del IMAE de Costa Rica (original y tendencia-ciclo), indexamos datos como series de tiempo


```{code-cell} stata
python
# Read data with bccr

from bccr import SW

imae = SW(Original=87703, Tendencia_ciclo=87764)
imae['mes'] = imae.index.astype(str)


# Export data to Stata
from sfi import Data

Data.setObsTotal(len(imae))
Data.addVarDouble("Original")
Data.addVarDouble("Tendencia_ciclo")
Data.addVarStr("mes", 7)

Data.store(imae.columns, None, imae.values)
end
```

Las primeras dos líneas del código anterior serían mejores como

```{code-cell} stata
generate date = monthly(mes, "YM")
tsset date, monthly
```
pero por alguna extraña razón `yearmonth` está convirtiendo los meses 11 como enero y 12 como febrero! (al menos en mi instalación con Linux).



## Graficamos las dos series
```{code-cell} stata 
graph twoway (tsline Original)
```


```{code-cell} stata
* Series en logaritmo
generate Y = log(Original)
generate TC = log(Tendencia_ciclo)
graph twoway (tsline Y) (tsline TC), name(nivel) title("Niveles") 

* Crecimiento mensual
generate DY = D.Y
generate DTC = D.TC
graph twoway (tsline DY) (tsline DTC), name(dnivel) title("Crecimiento mensual") 

* Crecimiento interanual
generate GY = S12.Y
generate GTC = S12.Y
graph twoway (tsline GY) (tsline GTC), name(s12nivel) title("Crecimiento interanual") 
```








