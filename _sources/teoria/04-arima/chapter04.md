# Modelos de tendencia


```{tableofcontents}
```

**Series con tendencia**

Hasta ahora, para cada uno de los procesos que hemos estudiado su valor esperado es constante.

Sin embargo, muchas de las series que estudiamos en la práctica tienen una tendencia.

En tales casos, un modelo de proceso estacionario (como ARMA) no es apropiado para describir la serie.

Por ejemplo:

%```{figure} labs/pib-costa-rica-I(1).pdf
%```



**Componentes (no observados) de una serie**
Para este capítulo, es útil imaginar que una serie de tiempo consiste de dos componentes distintos:
\begin{equation*}
y_t = \text{tendencia}_t + \text{componente_estacionario}_t
\end{equation*}

En el tema 3 del curso aprendimos que una serie estacionaria puede modelarse como un proceso ARMA. Ahora en este tema aprenderemos:

- cómo se modela una tendencia,
- cómo se determina si una serie tiene tendencia,
- cómo extraer una tendencia.


