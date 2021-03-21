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


```{include} ../math-definitions.md
```


%# Cambio estructural


%==========================================================================================================================
%==========================================================================================================================
# Introducción

 %Levendis p.171
## La crítica de Lucas

-  En 1976 Lucas publicó una de las críticas más fuertes al enfoque de modelación económica de gran escala de la Comisión Cowles.
-  Lucas criticó el supuesto de que muchos fenómenos económicos son estructurales.
-  En esencia, argumentaba que cambios en las leyes y regulaciones afectaban el comportamiento humano, y que esto se reflejaría en los datos.
-  Por ejemplo, en una estimación de consumo
\begin{equation*}
c_t = \alpha + \beta y_t + \epsilon_{t}
\end{equation*}
la propensión marginal a consumir $\beta$ podría cambiar con el tiempo.




## Cambio estructural en una serie de tiempo
%\framesubtitle{subtitle}
```{figure} figures/ labs/cambios-estructurales.png  ```




# La prueba de Chow

 % Greene p191--
## Determinando si hay un cambio estructural

-  Recordemos que podemos expresar una regresión lineal como
\begin{align*}
y_t &= \beta_{1}x_{t,1} + \dots + \beta_{k}x_{t,k} + \epsilon \\
\uncover<+->{&=\MAT{x_{t,1} & \dots & x_{t,k}}\MAT{\beta_{1} \\ \vdots \\ \beta_{k}} + \epsilon_{t} \\}
\uncover<+->{&=x'_t\beta + \epsilon_{t}}
\end{align*}
-  Cuando apilamos todas $T$ las observaciones
\begin{equation*}
\uncover<+->{Y = \MAT{y_1 \\ \vdots \\ y_T} = \MAT{x'_1\beta + \epsilon_{1} \\ \vdots \\ x'_T\beta + \epsilon_{T}} } \uncover<+->{= \MAT{x'_1\\ \vdots \\ x'_T}\beta   + \MAT{\epsilon_{1} \\ \vdots \\ \epsilon_{T}} } \uncover<+->{= X\beta + \epsilon}
\end{equation*}





-  La regresión $Y=X\beta+\epsilon$ asume que el vector de coeficientes $\beta$ es el mismo para toda la muestra.
-  Supongamos que pensamos que durante el período conocido hubo un cambio estructural en la economía, por lo que el vector de parámetros fue $\beta_0$ antes del cambio pero $\beta_{1}$ después. \uncover<+->{Entonces:}
\begin{align*}
\uncover<+->{&\begin{cases}
Y_1 = X_1\beta_1 + \epsilon_{1},& \text{ antes del cambio}\\
Y_2 = X_2\beta_2 + \epsilon_{2},& \text{ después}\\
\end{cases}\\}
\uncover<+->{\MAT{Y_1\\ Y_2} &=\MAT{X_1 & 0 \\ 0 & X_2}\MAT{\beta_1\\ \beta_2} + \MAT{\epsilon_{1}\\ \epsilon_{2}}}
\end{align*}
-  Por lo que el estimador de mínimos cuadrados ordinarios
\begin{equation*}
\widehat{\MAT{\beta_1\\ \beta_2}}= \MAT{X'_1X_1 & 0 \\ 0 & X'_2X_2}^{-1}\MAT{X'_1Y_1 \\ X_2Y_2} \uncover<+->{= \MAT{\hat\beta_1\\ \hat\beta_2}}
\end{equation*}





-  Esto nos dice que los parámetros $\beta_{1}$ y $\beta_2$ pueden estimarse por MCO separadamente.
-  Planteamos la hipótesis nula de que no hay cambio estructural: $\beta_{1}=\beta_2$. \uncover<+->{Entonces}
\begin{align*}
\uncover<+->{&\begin{cases}
Y_1 = X_1\beta + \epsilon_{1},& \text{ antes del cambio}\\
Y_2 = X_2\beta + \epsilon_{2},& \text{ todo sigue igual}\\
\end{cases}\\}
\uncover<+->{\MAT{Y_1\\ Y_2} &=\MAT{X_1 \\ X_2}\beta + \MAT{\epsilon_{1}\\ \epsilon_{2}}}
\end{align*}
-  Esto corresponde a la regresión con todas las observaciones.
-  La hipótesis $\beta_{1}=\beta_2$ puede comprobarse con un test de Wald.




## La prueba de Chow

-  Sea $S$ la suma de los cuadrados de los residuos de la regresión restringida, y $S_i$ la suma de los cuadrados de los residuos de la regresión de la muestra $i$.


\TEST{Prueba de cambio estructural de Chow}{¿Son los coeficientes $\beta_1$ y $\beta_2$ distintos?}{$\beta_{1} = \beta_2$}{$\frac{\frac{S - S_1 - S_2}{k}}{\frac{S_1+S_2}{T-2k}} \sim F(k, T-2k)$}{Si el estadístico es grande (mayor que el valor crítico), los modelos son distintos, por lo que sí hay cambio estructural.}




\begin{EXAMPLE}[TableF2-2.txt \\ \midrule Greene-gas-market.ipynb]{Cambio en la demanda por combustible}



```{figure} figures/ labs/mercado-gasolina.png  ```




El mercado del petróleo tuvo un cambio significativo en 1973:

\begin{tabu} to \linewidth {X[c,m]X[4p,m]}
\uncover<2->{\includegraphics[width=\linewidth]{figures/seven-sisters.jpg} & Antes de 1973, el comercio de petróleo estaba dominado por las “Siete Hermanas”, que controlaba $\approx 85\%$ de la reservas de petróleo \\ \\}
\uncover<3->{\includegraphics[width=\linewidth]{figures/OPEC-flag} & Desde la guerra de Yom Kippur (oct-1973), la OPEP ha dominado activamente en la fijación del precio. \\}
\end{tabu}


```{figure} figures/ labs/precio-petroleo.png  ```



\textcite{Greene:2012} estima el modelo el consumo per capita de combustible $G$ 
\begin{equation*}
G_t = \beta_1 + \beta_2 I_t + \beta_3 PG_t + \beta_4 PNC_t + \beta_5 PUC_t + \beta_6 t + \epsilon_{t}
\end{equation*}
(todas las variables en logaritmo, excepto $t$) \uncover<2->{y comprueba si hay un cambio estructural en 1974.\\ }\vspace{1.5em}
\uncover<3->{
\begin{table}
\centering
\begin{scriptsize}
\input{labs/gas-results-break.tex}
\end{scriptsize}\\
\tiny{* significativo al 5\%}
\end{table}
}



La prueba de Chow confirma que hay un cambio estructural en 1974: los parámetros de 1953-1973 son significativamente distintos a los de 1974-2004. \vspace{0.5em}

```{figure} figures/ labs/mercado-gasolina-cambio-estructural.png  ```



\end{EXAMPLE}


## Limitaciones de la prueba de Chow
La prueba de Chow tiene algunas limitaciones importantes

-  Asume que el analista sabe la fecha en que ocurre el cambio estructural
-  Asume que la varianza de los errores es la misma antes y después del cambio estructural.






# Cambio estructural y raíces unitarias: fecha conocida


## Cambio estructural y raíces unitarias

-  Cuando se realizan pruebas de raíz unitaria, debe tenerse cuidado si se sospecha que ha ocurrido un cambio estructural.
-  Cuando hay cambios estructurales, los estadísticos Dickey-Fuller están sesgados hacia no rechazar la hipótesis de que hay raíz unitaria.





## Ejemplos de cambios estructurales
%\framesubtitle{subtitle}
```{figure} figures/ labs/cambios-estructurales-enders.png  ```





-  Los datos de la figura \textcolor{red}{A} fueron generados por 
\begin{align*}
y_t &= 0.5y_{t-1} + \epsilon_{t} + 3D_L(50)_t \tag{AR(1) + cambio $\mu$}\\
D_L(50)_t &= \mathrm{I}(t\geq 50) \tag{dummy de nivel}
\end{align*}
-  La serie simulada parece tener una tendencia lineal.
-  La manera apropiada de estimar este modelo es 
\begin{align*}
y_t &= \beta_0 + \beta_1y_{t-1} + \delta D_L(50) + \epsilon_{t} 
\uncover<+->{\intertext{pero si estimamos}
y_t &= \alpha_0 + \alpha_1 t + \epsilon_{t} }
\end{align*}
\uncover<+->{el coeficiente $\alpha_1$ tendería a ser positivo para capturar el salto en la serie.}





-  Suponga que por equivocación estimamos
\begin{equation*}
y_t - y_{t-1} = c + \gamma y_{t-1} + \epsilon_{t} 
\end{equation*}
lo que sería una caminata aleatoria con deriva si $\gamma = 0$. \uncover<+->{Entonces:
\begin{equation*}
y_t = y_0 + ct + \sum_{i=i}^{t}\epsilon_{i}
\end{equation*}}
-  Esta ecuación describe los datos de manera similar a como lo hace $y_t = \alpha_0 + \alpha_1 t + \epsilon_{t}$, lo cual nos dice que la regresión Dickey-Fuller sesgaría los resultados hacia $\gamma = 0$, es decir, hacia no rechazar la presencia de una raíz unitaria.
-  Perron (1989) demostró este sesgo con simulaciones de Monte Carlo.






-  Ahora bien, una serie con raíz unitaria también puede presentar un cambio estructural, como en la figura \textcolor{red}{B}, generada por
\begin{align*}
y_t &= y_{t-1} + \epsilon_{t} + 5D_P(50)_t \tag{RW + cambio $\mu$}\\
D_P(50)_t &= \mathrm{I}(t = 50) \tag{dummy de impulso}
\end{align*}
-  Note que $D_P(t)$ es igual a 1 solo en el período $t$: cualquier cambio aditivo a una caminata aleatoria tiene un efecto permanente sobre el nivel de la serie.
-  La serie simulada parece tener una tendencia lineal.
-  De hecho, no es sencillo distinguirla de la figura \textcolor{red}{A} a simple vista.





-  ¿Cómo saber entonces si una serie con cambio estructural tiene raíz unitaria?
-  Una opción, similar a lo que hace la prueba de Chow, es partir la muestra de datos en dos partes, y realizar pruebas de raíz unitaria en cada una por separado
-  Lo malo de este procedimiento es que pierde muchos grados de libertad.
-  Sería preferible tener un test que utilice toda la muestra





## ¿Caminata aleatoria o serie estacionaria alrededor de tendencia?

-  \textcite{Perron1989} desarrolla un procedimiento formal para detectar raíces unitarias en presencia de un cambio estructural ocurrido en $t=\tau$.
-  Las hipótesis nula y alternativa son
\begin{align*}
y_t &= \alpha_0 + y_{t-1} + \mu_1 D^P_t(\tau) + \epsilon_{t} \tag{nula}\\
y_t &= \alpha_0 + \alpha_2 t + \mu_2 D^L_t(\tau) + \epsilon_{t} \tag{alternativa}
\end{align*}
-  Es decir, la hipótesis nula es que hay un solo salto en una caminata aleatoria en el período $\tau$, la alternativa es que en esa misma fecha hay un solo salto en el intercepto de una serie estacionaria alrededor de tendencia.








-  Observemos que \\
\begin{minipage}{0.4\linewidth}
\begin{equation*}
\sum_{k=1}^{t}D_p(\tau)_k = D_L(\tau)_t
\end{equation*}
\end{minipage}
\begin{flushright}
```{figure} figures/ labs/perron-breaks.png  ```
\end{flushright}
-  Integrando la hipótesis nula
\begin{equation*}
y_t = y_0 + \alpha_0 t + \mu_1D_L(\tau)_t + \sum_{k=0}^{t}\epsilon_{k}
\end{equation*}
vemos que es equivalente a la alternativa excepto por las perturbaciones.




## Las pruebas de cambio estructural de Perron
\begin{RESALTADO}{Modelo A: cambio de intercepto (crash)}
\begin{align*}
y_t &= \notationbrace{\alpha_0 + \mu_1 D^P_t}{intercepto} +  y_{t-1}  + \epsilon_{t} \tag{nula}\\
y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \alpha_2 t  + \epsilon_{t} \tag{alternativa}
\end{align*}
\end{RESALTADO}



\begin{RESALTADO}{Modelo B: cambio de tendencia (changing growth)}
\begin{align*}
y_t &= \notationbrace{\alpha_0 + \mu_2 D^L_t}{intercepto} +  y_{t-1}  + \epsilon_{t} \tag{nula}\\
y_t &= \alpha_0 + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa}
\end{align*}
\end{RESALTADO}
donde $D^T_t(\tau) = \max(t-\tau, 0)$




\begin{RESALTADO}{Modelo C: cambio de intercepto y de tendencia}
\begin{align*}
y_t &= \notationbrace{\alpha_0 + \mu_1 D^P_t + \mu_2 D^L_t}{intercepto} +  y_{t-1}  + \epsilon_{t} \tag{nula}\\
y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa}
\end{align*}
\end{RESALTADO}





%
%Para implementar la prueba de Perron se siguen 4 pasos:
%\begin{description}
%- [Paso 1] Eliminar la tendencia: se estima la hipótesis alternativa del modelo, y se generan los residuos $\tilde{y}_t$
%- [Paso 2] ¿Tiene $\tilde{y}$ una raíz unitaria? Se estima la regresión \vspace{-0.5em}
%\begin{equation*}
%\tilde{y}_t = \alpha\tilde{y}_{t-1} + \varepsilon_t 
%\end{equation*}
%y se evalúa si los residuos $\hat{\epsilon}$ tienen autocorrelación.
%- [Paso 3] ¿Están autocorrelacionados los residuos $\hat{\epsilon}$? De ser así se estima la regresión\vspace{-0.5em}
%\begin{equation*}
%\tilde{y}_t = \alpha\tilde{y}_{t-1} + \sum_{i=1}^{p}\gamma_i\Delta\tilde{y}_{t-i} +  \varepsilon_t 
%\end{equation*}
%- [Paso 4] Se evalúa la hipótesis nula $\alpha_1=1$, utilizando los valores críticos de Perron. Si el estadístico estimado es mayor que el valor crítico, se rechaza la hipótesis nula.
%\end{description}
%





Para implementar la prueba de Perron se siguen 3 pasos:
\begin{description}
- [Paso 1] Se estima la regresión correspondiente al modelo
\end{description}
\begin{align*}
\uncover<+->{y_t &= \alpha_0 + \alpha_1y_{t-1} + \alpha_2 t + \mu_1 D_t^P + \mu_2 D_t^L  +\epsilon_{t} \tag{A} \\}
\uncover<+->{y_t &= \alpha_0 + \alpha_2 t + \mu_3 D_t^T  + \tilde{y}_{t} \qquad\Rightarrow
\tilde{y}_t = \alpha_1\tilde{y}_{t-1} + \epsilon_{t}  \tag{B}  \\}
\uncover<+->{y_t &= \alpha_0 + \alpha_1y_{t-1} + \alpha_2 t + \mu_1 D_t^P + \mu_2 D_t^L + \mu_3 D_t^L  +\epsilon_{t} \tag{C}\\}
\end{align*}\vspace{-2em}
\begin{description}
- [Paso 2] Si los residuos de la regresión están autocorrelacionados, se estima la regresión ampliada, agregando $p$ rezagos del cambio en la variable:
\begin{align*}
\uncover<+->{\text{A y C} &:\sum_{i=1}^{p}\beta_i\Delta y_{t-1}  &}
\uncover<+->{\text{B} &:\sum_{i=1}^{p}\beta_i\Delta \tilde{y}_{t-1}}
\end{align*}
\end{description}




\begin{description}
- [Paso 3] Se calcula el estadístico $t$ de la hipótesis $a_1=1$:
\begin{equation*}
t_{\alpha_1} = \frac{\hat{\alpha_1}-1}{s.e.(\alpha_1)}
\end{equation*}
 y se compara con el valor crítico de Perron. 
\end{description}


-  Si el estadístico estimado es menor que el valor crítico, se rechaza la hipótesis nula.
-  El valor crítico depende de la proporción $\lambda$ de observaciones que corresponden al periodo anterior al quiebre estructural.







\begin{table}
\captionof{table}{Valores críticos de Perron}
\begin{small}
\input{labs/PerronModelABC.tex}
\end{small}
\begin{flushleft}
{\tiny Fuente: \textcite{Perron1989}}
\end{flushleft}
\end{table}






\begin{EXAMPLE}[NelsonPlosserData.dta \\ \midrule Perron1989.py]{Pruebas de cambio estructural}


Perron analiza los datos de Nelson y Plosser.

```{figure} figures/ labs/perron-ejemplo-salarios-paso1.png  ```



Al estimar el modelo A encuentran

\begin{center}
\input{labs/perron-nelson-plosser.tex}
\end{center}


[fragile]
A continuación vemos cómo replicar los resultados del modelo A de Perron, escribiendo un programa de Python.

\begin{lstlisting}[language=python, basicstyle=\scriptsize,numbers=none, showstringspaces=false]
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols

NP = pd.read_stata('NelsonPlosserData.dta')
NP.set_index('year',inplace=True)
NP.index = NP.index.year
\end{lstlisting}


[fragile]
\begin{equation*}
y_t = \alpha_0 + \alpha_1y_{t-1} + \alpha_2 t + \mu_1 D_t^P + \mu_2 D_t^L +\sum_{i=1}^{p}\beta_i\Delta y_{t-1}  +\epsilon_{t} 
\end{equation*}

\begin{lstlisting}[language=python, basicstyle=\scriptsize,numbers=none, showstringspaces=false]
def Perron_testA(serie, k=8):
    dta = NP[[serie]].dropna()
    dta.rename(columns={serie:'y'}, inplace=True)
    dta['DL'] = (dta.index>1929)
    dta['DP'] = (dta.index==1930)
    dta['t'] = np.arange(dta.shape[0])
    dta['Ly'] = dta['y'].shift(1)
    dta['Dy'] = dta['y'].diff(1)
    for j in range(1, k+1):
        dta[f'D{j}y'] = dta['Dy'].shift(j)
    
    lags = '+'.join(dta.columns[-k:])
    
    modelo = ols('y ~ DL + DP + t + Ly +' + lags,dta).fit()
    tval = ((modelo.params - 1)/modelo.bse).round(2)['Ly']
    lda = 1-dta['DL'].mean()
    crit = perron['Modelo A'].loc[np.round(lda,1)]
    
    return {'$t$':tval, '$\lambda$':np.round(lda,2), '1\%':crit['1\%'],'5\%':crit['5\%'],'10\%':crit['10\%']}
\end{lstlisting}


\end{EXAMPLE}




# Cambio estructural y raíces unitarias: fecha desconocida


## ¿Cómo saber cuándo se produjo un cambio estructural?

-  Un supuesto importante en la prueba de \textcite{Perron1989} es que el analista conoce la fecha en que se produjo el (único) cambio estructural.
-  No obstante, esto no siempre es factible.
-  \textcite{Zivot1992} proponen una prueba de raíz unitaria similar a la de Perron, pero que asume que el momento del cambio estructural es desconocido.









## Las pruebas de cambio estructural de Zivot y Andrews
\begin{RESALTADO}{Una hipótesis nula, tres alternativas}
\begin{align*}
\uncover<+->{y_t &= \mu +  y_{t-1}  + \epsilon_{t} \tag{nula}\\}
\uncover<+->{y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \alpha_2 t  + \epsilon_{t} \tag{alternativa A}\\}
\uncover<+->{y_t &= \alpha_0 + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa B} \\}
\uncover<+->{y_t &= \notationbrace{\alpha_0 + \mu_2 D_t^L}{intercepto} + \notationbrace{\alpha_2 t + \mu_3 D^T_t}{tendencia} +  \epsilon_{t} \tag{alternativa C}\\}\vspace{-1em}
\end{align*}
\end{RESALTADO}





Para implementar la prueba de Zivot y Andrews se siguen estos pasos:
\begin{description}[<+->]
- [Paso 1] Se estima la regresión correspondiente al modelo
\end{description}
\begin{align*}
\uncover<+->{\textcolor{Chartreuse4}{A: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \mu_2 D_t^L \phantom{+ \mu_3 D^T_t}  &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t} \\}
\uncover<+->{\textcolor{Chartreuse4}{B: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \phantom{\mu_2 D_t^L +} \mu_3 D^T_t  &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t}  \\}
\uncover<+->{\textcolor{Chartreuse4}{C: } y_t &= \alpha_0 + \alert{\alpha_1 y_{t-1}} + \alpha_2 t  &+& \mu_2 D_t^L + \mu_3 D^T_t &+& \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t} }
\end{align*}
\uncover<+->{donde los términos $D_t^L$ y $D_t^T$ dependen de la proporción de datos $\lambda$ anteriores al cambio estructural:
\begin{align*}
D_t^L(\lambda) &= I(t>\lambda T)  &  D_t^T &=\max(t-\lambda T, 0)
\end{align*}}



\begin{description}[<+->]
- [Paso 2] Se calcula el estadístico $t$ de la hipótesis $a_1=1$:
\begin{equation*}
t_{\alpha_1} = \frac{\hat{\alpha_1}-1}{s.e.(\alpha_1)}
\end{equation*}
\uncover<+->{Observemos que el valor estimado $\hat{\alpha}$ dependerá de $\lambda$; por ello, escribimos $t_{\alpha_1}(\lambda)$}
- [Paso 3] Se define el punte de quiebre $\hat{\lambda}$ como aquel valor $\lambda$ que hace más plausible la hipótesis alternativa
\begin{equation*}
\hat{\lambda} \equiv \argmin{\lambda\in(0, 1)}\left\{ t_{\alpha_1}(\lambda) \right\}
\end{equation*}
\end{description}




%\frametitle{}
\begin{description}[<+->]
- [Paso 4]  Se compara el valor mínimo $t_{\alpha_1}(\hat\lambda)$ con el valor crítico de Zivot y Andrews. \uncover<+->{Si el estadístico estimado es menor que el valor crítico, se rechaza la hipótesis nula.}
\end{description}

\centering
\uncover<+->{
\begin{table}
\captionof{table}{Valores críticos de Zivot y Andrews}
\begin{tabu} to 0.7\linewidth {X[2c]X[l]X[l]X[l]}
\toprule
Modelo & 1\% & 5\% & 10\% \\ \midrule
A  & -5.34 & -4.80 & -4.58 \\
B  & -4.93 & -4.42 & -4.11 \\
C  & -5.57 & -5.08 & -4.82 \\
\bottomrule
\multicolumn{4}{l}{\tiny Fuente: \textcite{Zivot1992}}
\end{tabu}
\end{table}
}




\begin{EXAMPLE}[NelsonPlosserData.dta \\ \midrule Perron1989.py]{Pruebas de cambio estructural (continuación)}


\textcite{Zivot1992} también analizan los datos de Nelson y Plosser. Al estimar el modelo A encuentran

\begin{center}
\input{labs/zivot-andrews-nelson-plosser.tex}
\end{center}

Recordemos los valores críticos 
\begin{scriptsize}
\begin{tabular}{ccc}
\toprule
 1\% & 5\% & 10\% \\ \midrule
-5.34 & -4.80 & -4.58 \\
\bottomrule
\end{tabular}
\end{scriptsize}


[fragile]
A continuación vemos cómo replicar los resultados del modelo A de Zivot y Andrews, escribiendo un programa de Python.

\begin{equation*}
y_t = \alpha_0 + \alpha_1 y_{t-1} + \alpha_2 t  + \mu_2 D_t^L  + \sum_{i=1}^{p}\beta_i\Delta y_{t-1} + \epsilon_{t} 
\end{equation*}


[fragile]


\begin{lstlisting}[language=python, basicstyle=\scriptsize,numbers=none, showstringspaces=false]
def ZivotAndrewsA(serie, k=8):
    dta = NP[[serie]].dropna()
    dta.rename(columns={serie:'y'}, inplace=True)
    dta['t'] = np.arange(dta.shape[0])
    dta['Ly'] = dta['y'].shift(1)
    dta['Dy'] = dta['y'].diff(1)
    for j in range(1, k+1):
        dta[f'D{j}y'] = dta['Dy'].shift(j)    
    
    lags = '+'.join(dta.columns[-k:])

    a1vals = pd.Series(0.0, index=dta.index[12:-12])
    for tau in a1vals.index:
        dta['DL'] = (dta.index>tau)
        reg = ols('y ~ Ly + t + DL + ' + lags, dta).fit()
        a1vals[tau] = ((reg.params - 1)/reg.bse)['Ly']

    tauhat, tval = a1vals.idxmin(), a1vals.min()
    dta['DL'] = (dta.index>tauhat)
    reg = ols('y ~ Ly + t + DL + ' + lags, dta).fit()
        
    return {r'$\hat{T}_B$':tauhat, r'$\alpha_1$': reg.params['Ly'], r'$t$':tval}
\end{lstlisting}


\end{EXAMPLE}

%==========================================================================================================================
%==========================================================================================================================
\makeReferencesFrame{Enders:2015, Levendis2018}
\end{document}




