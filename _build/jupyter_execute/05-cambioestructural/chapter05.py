import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Cambio estructural

 %Levendis p.171


En 1976 Lucas publicó una de las críticas más fuertes al enfoque de modelación económica de gran escala de la Comisión Cowles.
Lucas criticó el supuesto de que muchos fenómenos económicos son estructurales.

En esencia, argumentaba que cambios en las leyes y regulaciones afectaban el comportamiento humano, y que esto se reflejaría en los datos.

Por ejemplo, en una estimación de consumo
\begin{equation*}
c_t = \alpha + \beta y_t + \epsilon_{t}
\end{equation*}
la propensión marginal a consumir $\beta$ podría cambiar con el tiempo.

np.random.seed(1234)

T = 200
data = pd.DataFrame({'t':np.arange(T), 'e':np.random.randn(T),'y0':0})
data['D'] = (data['t']>T/2).astype(int)
for t in range(1,T):
    data.loc[t,'y0'] = 0.5 * data.loc[t-1,'y0'] + data.loc[t,'e']

data['y1'] = data['y0'] + 20 * data['D']
data['y2'] = data['y0'] + 10 * data['D'] + 0.12*data['t']
data['y3'] = data['y0'] - 25 * data['D'] + 0.05*data['t'] + 0.25*data['t']*data['D']
data['y4'] = data['y0']  + 0.05*data['t'] + 0.25*data['t']*data['D']


fig = make_subplots(2,2, horizontal_spacing=0.05, shared_xaxes=True)

fig.append_trace(go.Scatter(y = data['y1']), row=1, col=1)
fig.append_trace(go.Scatter(y = data['y2']), row=1, col=2)
fig.append_trace(go.Scatter(y = data['y3']), row=2, col=1)
fig.append_trace(go.Scatter(y = data['y4']), row=2, col=2)
fig.add_vline(x=T/2, line_width=3, line_dash="dash", line_color="green")
fig.update_layout(showlegend=False, title_text="Ejemplos de cambio estructural en una serie de tiempo")

```{toctree}
:hidden:
:titlesonly:


01-chow
02-conocido
03-desconocido
refs
```