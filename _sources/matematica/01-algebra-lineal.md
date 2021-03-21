# Álgebra lineal



```{include} ../math-definitions.md
```



(appendix:descomp-espectral)=
## Descomposición espectral de una matriz

Si los eigenvectores de la matriz cuadrada $A$ son linealmente independientes, entonces

\begin{equation*}
A = C\Lambda C^{-1}
\end{equation*}

donde $\Lambda$ es la matriz diagonal formada por los eigenvalores de $A$:
\begin{equation*}
   \Lambda = \MAT{\lambda_1 & 0 & \dots & 0\\ 0 &\lambda_2 & \dots & 0\\ & & \ddots & \\ 0 & 0 & \dots &\lambda_n}
\end{equation*}
y las columnas de $C$ son los correspondientes eigenvectores de $A$.


(appendix:potencia-matriz)=
## Potencia de una matriz

Si $A$ tiene la descomposición espectral $A = C\Lambda C^{-1}$ es fácil calcular su $t$-ésima potencia:
\begin{equation*}
A^t = C\Lambda^t C^{-1}
\end{equation*}

ya que
\begin{equation*}
\Lambda^t = \MAT{\lambda^t_1 & 0 & \dots & 0\\ 0 &\lambda^t_2 & \dots & 0\\ & & \ddots & \\ 0 & 0 & \dots &\lambda^t_n}
\end{equation*}
