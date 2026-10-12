# Verificaciones de la sección 3.4.2

## 1. Las columnas de $Z$ suman cero

Esta verificación se pide justo después de (3.8): se debe probar que $Z^T\mathbf{1}=\mathbf{1}^TZ=\mathbf{0}$. Sean $\bar x_j=n^{-1}\sum_{i=1}^n x_{ij}$, $s_j>0$ y $z_{ij}=(x_{ij}-\bar x_j)/s_j$. La componente $j$ de $Z^T\mathbf{1}$, con $j=1,\dots,p$, es la suma de la columna $j$ de $Z$:

$$
(Z^T\mathbf{1})_j=\sum_{i=1}^n z_{ij}=\frac{1}{s_j}\sum_{i=1}^n\left(x_{ij}-\bar x_j\right)=\frac{1}{s_j}\left(n\bar x_j-n\bar x_j\right)=0 .
$$

Por tanto $Z^T\mathbf{1}=\mathbf{0}$ y, al transponer, $\mathbf{1}^TZ=(Z^T\mathbf{1})^T=\mathbf{0}$. $\blacksquare$

Esto elimina el término cruzado $2\beta_0^\star\,\mathbf{1}^TZ\boldsymbol{\beta}_s$ del desarrollo de $S_\lambda(\beta_0^\star,\boldsymbol{\beta}_s)$ (el que aparece en rojo en la página). Por eso, al derivar respecto a $\beta_0^\star$ y usar $\mathbf{1}^T\mathbf{1}=n$ y $\mathbf{1}^T\boldsymbol{y}=n\bar y$, solo queda

$$
\frac{\partial S_\lambda}{\partial\beta_0^\star}=-2n\bar y+2n\beta_0^\star=0 .
$$

En el desarrollo de la página aparece "$2\beta_0$"; debe ser $2\beta_0^\star$.

## 2. Verificación de las igualdades (3.11)

Se centra la respuesta, $y_i\leftarrow y_i-\bar y$, y se estandarizan los predictores, $x_{ij}\leftarrow z_{ij}$. En (3.11) la página usa $x_{ij}$ para los datos ya estandarizados. Hay que verificar tres igualdades.

**(a) $\sum_{i=1}^n y_i=0$.**

$$
\sum_{i=1}^n(y_i-\bar y)=n\bar y-n\bar y=0 .
$$

**(b) $\sum_{i=1}^n x_{ij}=0$.** Es el cálculo de la sección 1:

$$
\sum_{i=1}^n z_{ij}=0,\qquad j=1,\dots,p .
$$

**(c) $\sum_{i=1}^n x_{ij}^2=n$.** Se usa $s_j^2=n^{-1}\sum_{i=1}^n(x_{ij}-\bar x_j)^2$, la definición de varianza de la página:

$$
\sum_{i=1}^n z_{ij}^2=\frac{1}{s_j^2}\sum_{i=1}^n\left(x_{ij}-\bar x_j\right)^2=\frac{n\,s_j^2}{s_j^2}=n .\qquad\blacksquare
$$

La igualdad (c) vale exactamente porque $s_j^2$ divide entre $n$; con el divisor $n-1$ se obtendría $n-1$.

## 3. Consecuencias

Como $\hat\beta_0^\star=\bar y$ y la respuesta ya está centrada, $\bar y=0$ y por tanto $\hat\beta_0^\star=0$. Se puede trabajar sin intercepto con $\boldsymbol{y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, que es lo que usa la página a continuación. Además, la igualdad (c) da

$$
\operatorname{diag}(X^TX)=n\,\mathbf{1},
$$

que se usa en el caso ortogonal y en el descenso por coordenadas de lasso ({doc}`capítulo 3 <03_lasso_lars>`).
