# Tipo de contenido

## Tests estadísticos

Para facilitar la explicación de pruebas estadísticas, estas se presentarán en este formato

{{ empieza_test }} NOMBRE DE LA PRUEBA/TEST {{ fin_titulo_test }}
{{ test_inquietud }} ¿Qué pregunta buscamos responder con este test?
{{ test_hipotesis }} ¿Cuál es la hipótesis nula del test? Es decir, ¿qué afirma el test en términos de parámetros, que sea conducente a responder la interrogante planteada anteriormente?
{{ test_estadistico }} ¿Cómo se calcula el estadístico del test? En general, en un test se calcula un estadístico y se determina su distribución.
{{ test_interpretacion }} ¿Cómo interpreto el estadístico? Es decir, ¿cuándo debo rechazar la hipótesis nula?
{{ termina_test }}

## Ejemplos
Por su parte, los ejemplos se presentan así


{{ empieza_ejemplo }} TITULO DEL EJEMPLO {{ fin_titulo_ejemplo }}
Contenido del ejemplo acá.

import matplotlib.pyplot as plt
plt.style.use("seaborn")

plt.plot([1,9,2,8,3,7,4,6,5,5,5]);

Mismo gráfico de antes, pero ahora en un ejemplo y con mejor formato
{{ termina_ejemplo }}