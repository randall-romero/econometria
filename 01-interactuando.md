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

# Cómo interactuar con este libro

Este libro fue creado con [Jupyter Book](https://jupyterbook.org/intro.html), un proyecto de código abierto para diseñar libros interactivos en línea, que contienen el código y otros material computacional.

A continuación se explican las herramientas interactivas de este libro. La mayoría de estas heramientas están en la barra de herramientas en la parte superior de la página

## <i class="fa fa-rocket" aria-hidden="true"></i> Abrir el cuaderno de Jupyter en la nube

Usted puede abrir la mayoría de las páginas de este libro en la nube y correr allí el código. Coloque el puntero del *mouse* sobre el icono <i class="fa fa-rocket" aria-hidden="true"></i>  en la parte superior de la página y haga clic en "Binder" para abrir una versión de esta página en la nube.


[Binder](https://mybinder.org/) es un servicio que permite ejecutar cuadernos de Jupyter sin necesidad de una instalación o configuración previa. Puede tomar varios minutos abrir un archivo en Binder.

## <i class="fa fa-download" aria-hidden="true"></i> Descargue el cuaderno de Jupyter

Usted puede descargar cualquier página que contenga código en este libro como un cuaderno de Jupyter (archivo con extensión .ipynb). Coloque el puntero del *mouse* sobre el icono <i class="fa fa-download" aria-hidden="true"></i> y haga clic en ".ipynb"


```{attention}
Para trabajar con este archivo .ipynb, usted necesitará tener Jupyter en su computardora.

Además, para algunos de los ejemplos requerirá haber instalado los paquetes de python `bccr` y `macrodemos`.
```

Algunos de los cuadernos de Jupyter desarrollan ejemplos a partir de datos almacenados en este libro. En tales casos, puede descargarlos desde [el repositorio en GitHub de este libro](https://github.com/randall-romero/econometria/tree/master/data). En esta página, seleccione el archivo necesario, y descárguelo presionando el botón "Raw".


## <i class="fa fa-download" aria-hidden="true"></i> Download PDF

Usted puede descargar cualquier página de este libro como un archivo PDF. Coloque el puntero del *mouse* sobre el icono <i class="fa fa-download" aria-hidden="true"></i> y haga clic en ".pdf"


## <i class="fas fa-expand" aria-hidden="true"></i> Modo de pantalla completa

Para ver cualquier página de este cuaderno en pantalla completa, haga clic en el icono <i class="fas fa-expand" aria-hidden="true"></i> en la parte superior de la página.

<!--
## <i class="fab fa-github" aria-hidden="true"></i> Open Issue on GitHub

Si tuviese algún problema utilizando este libro, o si quisiera hacerme una sugerencia, puede enviarme un correo a randall.romero@ucr.ac.cr .
-->

## Clic para mostrar el código

Para facilitar la lectura del material, la mayoría de las páginas de este libro ocultan el código que genera los resultados obtenidos. Para ver ese código, haga clic en "Click to Show" a la derecha de la celda de código.

```{code-cell} ipython3
:tags: [hide-input]
import matplotlib.pyplot as plt

print("Este es un resultado obtenido con Python!\n\nClic en 'Click to Show' para ver el código que lo generó!")

plt.plot([1,9,2,8,3,7,4,6,5,5,5]);
```
