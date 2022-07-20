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
  empieza_test: |
    <div class="test">
    <div class="test-titulo">
  fin_titulo_test: "</div>"
  termina_test: "</div>"
  test_inquietud: |
    <i class="fas fa-question test-simbolo"></i>
  test_hipotesis: |
    <br><hr><i class="fas fa-heading test-simbolo"></i>
  test_estadistico: |
    <br><hr><i class="fas fa-calculator test-simbolo"></i>
  test_interpretacion: |
    <br><hr><i class="far fa-lightbulb test-simbolo"></i>
---

# Tipo de contenido

## Tests estadísticos

Para facilitar la explicación de pruebas estadísticas, estas se presentarán en este formato


{{ empieza_test }} NOMBRE DE LA PRUEBA/TEST {{ fin_titulo_test }}
::::{grid} 
:gutter: 1

:::{grid-item}
:outline: 
:columns: 4
{fas}`question;test-simbolo`
¿Qué pregunta buscamos responder con este test?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`bullseye;test-simbolo`
¿Cuál es la hipótesis nula del test? Es decir, ¿qué afirma el test en términos de parámetros, que sea conducente a responder la interrogante planteada anteriormente?
:::

:::{grid-item} 
:outline: 
:columns: 8
{fas}`calculator;test-simbolo`
¿Cómo se calcula el estadístico del test? En general, en un test se calcula un estadístico y se determina su distribución.
:::

:::{grid-item} 
:outline: 
:columns: 4
{fas}`lightbulb;test-simbolo` 
¿Cómo interpreto el estadístico? Es decir, ¿cuándo debo rechazar la hipótesis nula?
:::
::::
{{ termina_test }}




## Ejemplos
Por su parte, los ejemplos se presentan así


{{ empieza_ejemplo }} TITULO DEL EJEMPLO {{ fin_titulo_ejemplo }}
Contenido del ejemplo acá.

```{code-cell} ipython3
:tags: [hide-input]
import matplotlib.pyplot as plt
plt.style.use("seaborn")

plt.plot([1,9,2,8,3,7,4,6,5,5,5]);
```
Mismo gráfico de antes, pero ahora en un ejemplo y con mejor formato
{{ termina_ejemplo }}
