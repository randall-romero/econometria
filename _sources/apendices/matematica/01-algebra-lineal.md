# Álgebra lineal



```{include} ../../teoria/math-definitions.md
```



(appendix:descomp-espectral)=
## Descomposición espectral de una matriz

Si los eigenvectores de la matriz cuadrada \begin{math}A \end{math} son linealmente independientes, entonces

\begin{equation*}
A = C\Lambda C^{-1}
\end{equation*}

donde \begin{math}\Lambda \end{math} es la matriz diagonal formada por los eigenvalores de \begin{math}A \end{math}:

\begin{equation*}
   \Lambda = \MAT{\lambda_1 & 0 & \dots & 0\\ 0 &\lambda_2 & \dots & 0\\ & & \ddots & \\ 0 & 0 & \dots &\lambda_n}
\end{equation*}
y las columnas de \begin{math}C \end{math} son los correspondientes eigenvectores de \begin{math}A \end{math}.


(appendix:potencia-matriz)=
## Potencia de una matriz

Si \begin{math}A \end{math} tiene la descomposición espectral \begin{math}A = C\Lambda C^{-1} \end{math} es fácil calcular su \begin{math}t \end{math}-ésima potencia:
\begin{equation*}
A^t = C\Lambda^t C^{-1}
\end{equation*}

ya que
\begin{equation*}
\Lambda^t = \MAT{\lambda^t_1 & 0 & \dots & 0\\ 0 &\lambda^t_2 & \dots & 0\\ & & \ddots & \\ 0 & 0 & \dots &\lambda^t_n}
\end{equation*}



(appendix:kronecker)=
## El producto Kronecker

Si \begin{math}A=\MAT{a & b \\ c & d} \end{math} y \begin{math}B \end{math} son matrices, el producto Kronecker se define por
\begin{equation*}
A \otimes B = \MAT{aB & bB \\ cB & dB}
\end{equation*}

Algunas propiedades importantes:
\begin{align*}
(A \otimes B)' &= A' \otimes B' \\
(A \otimes B)^{-1} &= A^{-1} \otimes B^{-1} \\
(A \otimes B)(C \otimes D) &= (AC) \otimes (BD)
\end{align*}




(appendix:rango-matriz)=
## El rango de una matriz

El **rango de una matriz** \begin{math}A \end{math} de tamaño \begin{math}M \times N \end{math} se denota por \begin{math}\text{rango}[A] \end{math} y se define como el número de filas (o columnas) que son linealmente independientes.

Necesariamente, se cumple que
\begin{equation*}
\text{rango}[A] \leq \min\left\{M,N\right\}
\end{equation*}

- Si \begin{math}\text{rango}[A] = M \end{math}, decimos que \begin{math}A \end{math} tiene **rango fila** completo.
- Si \begin{math}\text{rango}[A] = N \end{math}, decimos que \begin{math}A \end{math} tiene **rango columna** completo.
