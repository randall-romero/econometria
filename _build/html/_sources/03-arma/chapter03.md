
# Modelos AutoRegresivos de Media Móvil (ARMA)


```{include} ../math-definitions.md
```



## En esta clase 

* En esta clase aprenderemos a modelar series de tiempo en función de:

* sus valores rezagados (procesos autorregresivos)
* valores rezagados de un ruido blanco (procesos de media móvil)

* Primero estudiamos las propiedades teóricas de procesos estocásticos.
* Luego tratamos de identificar el PGD de nuestra serie a partir de sus estadísticos muestrales, comparándolos con los estadísticos de los procesos del punto anterior.
* Finalmente, utilizamos nuestro modelo estimado para

* análisis de escenarios: ¿qué pasaría con la serie de tiempo si recibe una perturbación estocástica de cierta magnitud (función impulso respuesta)
* pronósticos: ¿qué valores esperamos ver en el futuro para esta serie de tiempo?





## Modelos que estudiaremos 

```{panels}
Ruido blanco
^^^
Es una secuencia  $\left\{\epsilon_t\right\}$ cuyos elementos satisfacen,
\begin{align*}
		\E\left(\epsilon_t\right) &=0\\
		\E\left(\epsilon^2_t\right) &= \sigma^2 \\
		\E\left(\epsilon_t\epsilon_\tau\right) &= 0 \quad\text{for }t\neq\tau 
\end{align*}

---
Proceso media móvil
^^^
Sea $\left\{\epsilon_t\right\}$ ruido blanco; el proceso estocástico 
\begin{equation*}
y_t = \epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}
\end{equation*}
con $\theta_q \neq 0$ es llamado un proceso MA(q).

---
Proceso autorregresivo
^^^
Sea $\left\{\epsilon_t\right\}$ ruido blanco; el proceso estocástico 
\begin{equation*}
y_t = \phi_1y_{t-1} + \dots + \phi_py_{t-p} + \epsilon_t 
\end{equation*}
con $\phi_p \neq 0$ es llamado un proceso AR(p).

---
Autorregresivo media móvil
^^^
Sea $\left\{\epsilon_t\right\}$ ruido blanco; el proceso estocástico
\begin{multline*}
y_t = \phi_1y_{t-1} + \dots + \phi_py_{t-p} + \dots\\
+\epsilon_t + \theta_1\epsilon_{t-1} + \dots + \theta_q\epsilon_{t-q}
\end{multline*}
es llamado proceso ARMA(p,q).
```

## La metodología Box-Jenkins 

```{image} ./figures/box-jenkins.png
```

## Acerca de los ejemplos 

En esta clase veremos ilustraciones de distintos proceso AR, MA, y ARMA.

Usted puede reproducirlas (y estudiar más casos específicos de estos procesos) con el paquete [macrodemos](http://randall-romero.com/code/macrodemos/) que escribí en Python para este tema.

Para instalarlo, en una ventana de sistema:
    
```
pip install macrodemos
```

Para ejecutarlo:
```python
from macrodemos import ARMA_demo
ARMA_demo()
```

```{figure} ./figures/ARMAdemo.png
```


