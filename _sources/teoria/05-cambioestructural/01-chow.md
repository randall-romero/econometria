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

```{code-cell} ipython3
:tags: ["hide-input",]
import numpy as np
import pandas as pd
pd.options.plotting.backend = "plotly"

from statsmodels.formula.api import ols
import pandas_datareader as pdr
import plotly.express as px
```





# La prueba de Chow

 % Greene p191--
## Determinando si hay un cambio estructural

Recordemos que podemos expresar una regresión lineal como
\begin{align*}
y_t &= \beta_{1}x_{t,1} + \dots + \beta_{k}x_{t,k} + \epsilon \\
    &=\MAT{x_{t,1} & \dots & x_{t,k}}\MAT{\beta_{1} \\ \vdots \\ \beta_{k}} + \epsilon_{t} \\
    &=x'_t\beta + \epsilon_{t}
\end{align*}

Cuando apilamos todas $T$ las observaciones
\begin{equation*}
Y = \simbolo{\MAT{y_1 \\ \vdots \\ y_T}}{Y} = \MAT{x'_1\beta + \epsilon_{1} \\ \vdots \\ x'_T\beta + \epsilon_{T}}
= \simbolo{\MAT{x'_1\\ \vdots \\ x'_T}}{X}\beta   + \simbolo{\MAT{\epsilon_{1} \\ \vdots \\ \epsilon_{T}}}{\epsilon}
= X\beta + \epsilon
\end{equation*}


La regresión $Y=X\beta+\epsilon$ asume que el vector de coeficientes $\beta$ es el mismo para toda la muestra.

Supongamos que pensamos que durante el período conocido hubo un cambio estructural en la economía, por lo que el vector de parámetros fue $\beta_0$ antes del cambio pero $\beta_{1}$ después. Entonces:
\begin{align*}
&\begin{cases}
Y_1 = X_1\beta_1 + \epsilon_{1},& \text{ antes del cambio}\\
Y_2 = X_2\beta_2 + \epsilon_{2},& \text{ después}\\
\end{cases}\\
\MAT{Y_1\\ Y_2} &=\MAT{X_1 & 0 \\ 0 & X_2}\MAT{\beta_1\\ \beta_2} + \MAT{\epsilon_{1}\\ \epsilon_{2}}
\end{align*}

Por lo que el estimador de mínimos cuadrados ordinarios
\begin{equation*}
\widehat{\MAT{\beta_1\\ \beta_2}}= \MAT{X'_1X_1 & 0 \\ 0 & X'_2X_2}^{-1}\MAT{X'_1Y_1 \\ X_2Y_2} = \MAT{\hat\beta_1\\ \hat\beta_2}
\end{equation*}


Esto nos dice que los parámetros $\beta_{1}$ y $\beta_2$ pueden estimarse por MCO separadamente.

Planteamos la hipótesis nula de que no hay cambio estructural: $\beta_{1}=\beta_2$. Entonces
\begin{align*}
 &\begin{cases}
Y_1 = X_1\beta + \epsilon_{1},& \text{ antes del cambio}\\
Y_2 = X_2\beta + \epsilon_{2},& \text{ todo sigue igual}\\
\end{cases}\\
\MAT{Y_1\\ Y_2} &=\MAT{X_1 \\ X_2}\beta + \MAT{\epsilon_{1}\\ \epsilon_{2}}
\end{align*}

Esto corresponde a la regresión con todas las observaciones.

La hipótesis $\beta_{1}=\beta_2$ puede comprobarse con un test de Wald.


## La prueba de Chow

Sea $S$ la suma de los cuadrados de los residuos de la regresión restringida, y $S_i$ la suma de los cuadrados de los residuos de la regresión de la muestra $i$.


\TEST{Prueba de cambio estructural de Chow}{¿Son los coeficientes $\beta_1$ y $\beta_2$ distintos?}{$\beta_{1} = \beta_2$}{$\frac{\frac{S - S_1 - S_2}{k}}{\frac{S_1+S_2}{T-2k}} \sim F(k, T-2k)$}{Si el estadístico es grande (mayor que el valor crítico), los modelos son distintos, por lo que sí hay cambio estructural.}



{{ empieza_ejemplo }} Cambio en la demanda por combustible {{ fin_titulo_ejemplo }}
El mercado del petróleo tuvo un cambio significativo en 1973:

#FIXME: ARREGLAR ESTO

::::{grid}
:gutter: 3
:img-top-cls: pl-0 pr-0

:::{grid-item-card} 
:img-top: figures/seven-sisters.jpg
^^^
Antes de 1973, el comercio de petróleo estaba dominado por las “Siete Hermanas”, que controlaba $\approx 85\%$ de la reservas de petróleo.
:::

:::{grid-item-card} 
:img-top: figures/OPEC-flag.png
^^^
Desde la guerra de Yom Kippur (oct-1973), la OPEP ha dominado activamente en la fijación del precio.
:::
::::


```{code-cell} ipython3
:tags: ["hide-input",]
oil = pdr.get_data_fred('WTISPLC', start=1946)   
fig = oil.plot()


fig.update_layout(
        title="Spot Crude Oil Price: West Texas Intermediate (WTI)",
        xaxis_title=" ",
        yaxis_title="dólares por barril",
        showlegend=False
    )

vrect_options = dict(
    annotation_position="top left",
    fillcolor="green",
    opacity=0.25,
    annotation_textangle=-90,
    line_width=0
)    

fig.add_vrect(x0="1973-10-01", x1="1974-03-30",
              annotation_text="embargo 1973", **vrect_options)    

fig.add_vrect(x0="1979-01-01", x1="1980-06-30",
              annotation_text="crisis petrolera 1979", **vrect_options)

fig.add_vrect(x0="2008-01-01", x1="2010-01-01",
              annotation_text="Crisis Financiera", **vrect_options)

```
Fuente de datos: <https://fred.stlouisfed.org/series/WTISPLC>



\textcite{Greene:2012} estima el modelo el consumo per capita de combustible $G$
\begin{equation*}
G_t = \beta_1 + \beta_2 I_t + \beta_3 PG_t + \beta_4 PNC_t + \beta_5 PUC_t + \beta_6 t + \epsilon_{t}
\end{equation*}
(todas las variables en logaritmo, excepto $t$) y comprueba si hay un cambio estructural en 1974.
```{code-cell} ipython3
:tags: ["hide-input",]
greene_file = 'http://www.stern.nyu.edu/~wgreene/Text/Edition7/TableF2-2.csv'
gasdata = pd.read_csv(greene_file, parse_dates=True, index_col=0)

gasdata.eval('G = GASEXP/GASP', inplace=True)
gasdata.eval('GPC = 1e6*G/POP', inplace=True)
gasdata['t'] = np.exp(gasdata.index.year - 1952)

series = {
    'GASEXP'    : 'Total U.S. gasoline expenditure',
    'GASP'      : 'precio combustible',
    'INCOME'    : 'ingreso per capita',
    'PNC'       : 'precio carro nuevo',
    'PUC'       : 'precio carro nuevo',
    'POP'       : 'U.S. total population in thousands',
    'GPC'       : 'Consumo per capita',
    'Intercept' : 'intercepto',
    't'         : 'tendencia'
}

params = pd.DataFrame()
signif = pd.DataFrame()
stats = pd.DataFrame(index=['S', '$R^2$', 'T', 'k'])

samples = {'1953-2004': slice('1953','2004'),
           '1953-1973': slice('1953','1973'),
           '1974-2004': slice('1974','2004')}


for periodo, ss in samples.items():
    mm = ols('GPC ~ INCOME + GASP + PNC + PUC + t', np.log(gasdata)[ss]).fit()
    params[periodo] = mm.params
    signif[periodo] = ['✓' if p < 0.05 else '' for p in mm.pvalues]
    stats[periodo] = [mm.ssr, mm.rsquared, mm.nobs, mm.params.shape[0]]

params.rename(index=series)
signif.index = params.index

pd.concat([params.round(4), signif], keys=['coef ', 'p<0.05']).unstack(0)
```

```{code-cell} ipython3
:tags: ["hide-input",]
stats
```


```{code-cell} ipython3
:tags: ["hide-input",]
gasdata['PERIODO'] = ''
gasdata.loc['1953':'1973', 'PERIODO'] = '1953-1973'
gasdata.loc['1974':'2004', 'PERIODO'] = '1974-2004'
fig = px.scatter(gasdata, x="GPC", y="GASP", color="PERIODO", trendline="ols")
fig.update_layout(
        title="Cambio estructural, test de Chow",
        xaxis_title="Consumo per capita",
        yaxis_title="ndice de precio"
    )
```

\begin{equation*}
\frac{\frac{0.1020 - 0.0020 - 0.0071}{6}}{\frac{0.0020 + 0.0071}{52 - 2\times 6}} = 67.65 > 2.34 = F(6, 40)
\end{equation*}

La prueba de Chow confirma que hay un cambio estructural en 1974: los parámetros de 1953-1973 son significativamente distintos a los de 1974-2004.

{{ termina_ejemplo }}

## Limitaciones de la prueba de Chow
La prueba de Chow tiene algunas limitaciones importantes

-  Asume que el analista sabe la fecha en que ocurre el cambio estructural
-  Asume que la varianza de los errores es la misma antes y después del cambio estructural.
