# Regresión ridge

Este capítulo deduce el estimador ridge a partir de datos estandarizados (sección 3.4) y demuestra sus propiedades: esperanza, covarianza, sesgo y error cuadrático medio (3.12).

## Parte I. Deducción del estimador (sección 3.4)

:::{admonition} Enunciado
Con datos estandarizados $z_{ij}=(x_{ij}-\bar x_j)/s_j$ y $\lambda>0$, el minimizador de

$$
\begin{aligned}
&S_\lambda(\beta_0^\star,\beta_s) \\
&{}= (y-\beta_0^\star\mathbf 1-Z\beta_s)^T(y-\beta_0^\star\mathbf 1-Z\beta_s)+\lambda\,\beta_s^T\beta_s
\end{aligned}
$$

es $\hat\beta_0^\star=\bar y$ y $\hat\beta_s=(Z^TZ+\lambda I_p)^{-1}Z^Ty$.
:::

### Paso 1 · Estandarización

Modelo $y_i=\beta_0+\beta_1x_{i1}+\dots+\beta_px_{ip}+\varepsilon_i$, $i=1,\dots,n$. Con

$$
\begin{aligned}
&\bar x_j=\frac1n\sum_{i=1}^n x_{ij},\qquad s_j^2=\frac1n\sum_{i=1}^n (x_{ij}-\bar x_j)^2, \\
&\qquad z_{ij}=\frac{x_{ij}-\bar x_j}{s_j}\ \Rightarrow\ x_{ij}=\bar x_j+s_j z_{ij}
\end{aligned}
$$

### Paso 2 · Reparametrización

*Se usa: propiedad distributiva.*

Se sustituye $x_{ij}=\bar x_j+s_jz_{ij}$ en el modelo y se agrupan las constantes.

$$
\begin{aligned}
&y_i=\Big(\beta_0+\sum_{j=1}^p\beta_j\bar x_j\Big)+\sum_{j=1}^p(s_j\beta_j)\,z_{ij}+\varepsilon_i \\
&{}= \beta_0^\star+\sum_{j=1}^p\beta_j^\star z_{ij}+\varepsilon_i, \\
&\qquad \beta_0^\star=\beta_0+\sum_j\beta_j\bar x_j,\ \ \beta_j^\star=s_j\beta_j
\end{aligned}
$$

$$y=\beta_0^\star\mathbf 1+Z\beta_s+\varepsilon \qquad (y:n\times1,\ Z:n\times p,\ \beta_s:p\times1)$$

### Paso 3 · Verificar $Z^T\mathbf 1=0$

*Se usa: $\sum_i x_{ij}=n\bar x_j$.*

$$
\begin{aligned}
&\sum_{i=1}^n z_{ij}=\frac1{s_j}\Big(\sum_{i=1}^n x_{ij}-n\bar x_j\Big) \\
&{}=\frac1{s_j}\big(n\bar x_j-n\bar x_j\big)=0
\end{aligned}
$$

Cada coordenada de $Z^T\mathbf 1$ es una de esas sumas, así que $Z^T\mathbf 1=0$. Al transponer, $\mathbf 1^TZ=0^T$.

### Paso 4 · Desarrollo de $S_\lambda$

*Se usa: un escalar es igual a su transpuesta.*

$$
\begin{aligned}
S_\lambda&=y^Ty-2\beta_0^\star\,y^T\mathbf 1-2y^TZ\beta_s+2\beta_0^\star\,\mathbf 1^TZ\beta_s\\
&\quad+\beta_s^TZ^TZ\beta_s+n(\beta_0^\star)^2+\lambda\beta_s^T\beta_s
\end{aligned}
$$

Se usó $\mathbf 1^T\mathbf 1=n$. Por el paso 3, $\mathbf 1^TZ=0^T$, así que el término cruzado $2\beta_0^\star\,\mathbf 1^TZ\beta_s$ se anula:

$$
\begin{aligned}
S_\lambda&=y^Ty-2\beta_0^\star\,y^T\mathbf 1-2y^TZ\beta_s\\
&\quad+\beta_s^T(Z^TZ+\lambda I)\beta_s+n(\beta_0^\star)^2
\end{aligned}
$$

### Paso 5 · Intercepto

*Se usa: derivada e igualdad a cero.*

$$
\begin{aligned}
&\frac{\partial S_\lambda}{\partial\beta_0^\star}=-2y^T\mathbf 1+2n\beta_0^\star=0\ \\
&\Rightarrow\ n\beta_0^\star=y^T\mathbf 1=\sum_i y_i=n\bar y\ \Rightarrow\ \hat\beta_0^\star=\bar y
\end{aligned}
$$

### Paso 6 · Coeficientes

*Se usa: $\partial(x^TAx)/\partial x=(A+A^T)x=2Ax$ si $A=A^T$.*

$$
\begin{aligned}
&\frac{\partial S_\lambda}{\partial\beta_s}=-2Z^Ty+2Z^TZ\beta_s+2\lambda\beta_s=0\ \\
&\Rightarrow\ (Z^TZ+\lambda I_p)\beta_s=Z^Ty\ \Rightarrow\ \hat\beta_s=(Z^TZ+\lambda I_p)^{-1}Z^Ty
\end{aligned}
$$

### Paso 7 · Volver a la escala original

De $\beta_0^\star=\beta_0+\sum_j\beta_j\bar x_j$, $\beta_j^\star=s_j\beta_j$ y $\hat\beta_0^\star=\bar y$:

$$\hat\beta_j=\frac{\hat\beta_j^\star}{s_j},\qquad \hat\beta_0=\bar y-\sum_{j=1}^p\hat\beta_j\bar x_j$$

### Paso 8 · Datos centrados: modelo sin intercepto

*Se usa: $\sum y^c_i=0,\ \sum x_{ij}=0,\ \sum x_{ij}^2=n$.*

Con $y_i^c=y_i-\bar y$ se verifica $\sum_i y_i^c=\sum_i y_i-n\bar y=0$. Con $z_{ij}$ en lugar de $x_{ij}$, $\sum_i z_{ij}=0$ (paso 3) y, como $s_j^2=\tfrac1n\sum_i(x_{ij}-\bar x_j)^2$:

$$\sum_{i=1}^n z_{ij}^2=\frac1{s_j^2}\sum_{i=1}^n(x_{ij}-\bar x_j)^2=\frac{n\,s_j^2}{s_j^2}=n$$

Como $\hat\beta_0^\star=\bar y$, el modelo para $y^c$ no lleva intercepto, y se escribe sin perder generalidad $y=X\beta+\varepsilon$ con $X$ centrada. La función objetivo es

$$
\begin{aligned}
&S_\lambda(\beta)=(y-X\beta)^T(y-X\beta)+\lambda\beta^T\beta \\
&{}=y^Ty-2\beta^TX^Ty+\beta^T(X^TX+\lambda I)\beta
\end{aligned}
$$

$$
\begin{aligned}
&\frac{\partial S_\lambda}{\partial\beta}=-2X^Ty+2X^TX\beta+2\lambda\beta \\
&{}=0\ \Rightarrow\ \hat\beta_R=(X^TX+\lambda I_p)^{-1}X^Ty \qquad\blacksquare
\end{aligned}
$$

Una consecuencia que se usa en lasso ({doc}`lasso_lars`): como $\sum_i x_{ij}^2=n$, se tiene $\operatorname{diag}(X^TX)=n\,\mathbf 1$.

### Complemento: por qué la inversa existe y el punto es el mínimo
Con $\lambda>0$, $A=Z^TZ+\lambda I$ es simétrica y definida positiva: $v^TAv=\|Zv\|^2+\lambda\|v\|^2>0$ si $v\ne0$. Por eso existe $A^{-1}$ aunque $Z^TZ$ sea singular. Completando el cuadrado,

$$\beta_s^TA\beta_s-2b^T\beta_s=(\beta_s-A^{-1}b)^TA(\beta_s-A^{-1}b)-b^TA^{-1}b,\qquad b=Z^Ty,$$

y el primer término es $\ge0$ con igualdad solo en $\beta_s=A^{-1}b$. Es el único mínimo global.

## Parte II. Propiedades del estimador (3.12)

:::{admonition} Enunciado
Con $y=X\beta+\varepsilon$, $\mathbb{E}(\varepsilon)=0$, $\operatorname{Cov}(\varepsilon)=\sigma^2I_n$ y $A=X^TX+\lambda I_p$, se tiene $\hat\beta_R=A^{-1}X^Ty$ y:

(a) $\mathbb{E}(\hat\beta_R)=A^{-1}X^TX\beta$ · (b) $\operatorname{Cov}(\hat\beta_R)=\sigma^2A^{-1}X^TXA^{-1}$ · (c) sesgo $=-\lambda A^{-1}\beta$ · (d) $\mathbb{E}\|\hat\beta_R-\beta\|^2=\sigma^2\sum_j\dfrac{l_j}{(l_j+\lambda)^2}+\lambda^2\beta^TA^{-2}\beta$
:::

En esta parte $X$ es la matriz de datos centrada y estandarizada de la Parte I (paso 8), así que el modelo no lleva intercepto.

### Paso 0 · Descomponer el estimador

*Se usa: distributiva.*

$$\hat\beta_R=A^{-1}X^T(X\beta+\varepsilon)=A^{-1}X^TX\beta+A^{-1}X^T\varepsilon$$

El primer sumando es constante; el aleatorio es $A^{-1}X^T\varepsilon$.

### Paso 1 · (a) Esperanza

*Se usa: linealidad; $\mathbb{E}(\varepsilon)=0$.*

$$\mathbb{E}(\hat\beta_R)=A^{-1}X^TX\beta+A^{-1}X^T\,\mathbb{E}(\varepsilon)=A^{-1}X^TX\beta$$

### Paso 2 · (b) Covarianza

*Se usa: $\operatorname{Cov}(M\varepsilon)=M\operatorname{Cov}(\varepsilon)M^T$; una constante no aporta covarianza.*

Con $M=A^{-1}X^T$ y $A$ simétrica, $M^T=XA^{-1}$.

$$
\begin{aligned}
&\operatorname{Cov}(\hat\beta_R)=A^{-1}X^T\,(\sigma^2I_n)\,XA^{-1} \\
&{}=\sigma^2A^{-1}X^TXA^{-1}=\sigma^2(X^TX+\lambda I_p)^{-1}X^TX(X^TX+\lambda I_p)^{-1}
\end{aligned}
$$

### Paso 3 · (c) Sesgo

*Se usa: $X^TX=A-\lambda I$.*

$$
\begin{aligned}
&\mathbb{E}(\hat\beta_R)-\beta=\big(A^{-1}X^TX-I\big)\beta=A^{-1}\big(X^TX-A\big)\beta \\
&{}=-\lambda A^{-1}\beta=-\lambda(X^TX+\lambda I_p)^{-1}\beta
\end{aligned}
$$

### Paso 4 · (d) Error cuadrático medio

*Se usa: $\mathbb{E}\|v\|^2=\operatorname{tr}\operatorname{Cov}(v)+\|\mathbb{E}v\|^2$.*

$$
\begin{aligned}
&\mathbb{E}\big[(\hat\beta_R-\beta)^T(\hat\beta_R-\beta)\big] \\
&{}=\operatorname{tr}\big(\operatorname{Cov}(\hat\beta_R)\big)+\big\|\mathbb{E}\hat\beta_R-\beta\big\|^2
\end{aligned}
$$

Sea $X^TX=Q\,\mathrm{diag}(l_1,\dots,l_p)\,Q^T$ con $Q$ ortogonal. Entonces $A^{-1}=Q\,\mathrm{diag}\big(\tfrac1{l_j+\lambda}\big)Q^T$ y, por la propiedad cíclica de la traza,

$$
\begin{aligned}
&\operatorname{tr}\big(\sigma^2A^{-1}X^TXA^{-1}\big)=\sigma^2\sum_{j=1}^p\frac{l_j}{(l_j+\lambda)^2}, \\
&\qquad \|{-\lambda}A^{-1}\beta\|^2=\lambda^2\beta^TA^{-2}\beta
\end{aligned}
$$

$$
\begin{aligned}
&\mathbb{E}\|\hat\beta_R-\beta\|^2 \\
&{}=\sigma^2\sum_{j=1}^p\frac{l_j}{(l_j+\lambda)^2}+\lambda^2\beta^T(X^TX+\lambda I_p)^{-2}\beta \\
&\qquad\blacksquare
\end{aligned}
$$

### Comentario: compromiso sesgo-varianza

La varianza decrece con $\lambda$, porque cada sumando $l_j/(l_j+\lambda)^2$ disminuye; el sesgo al cuadrado crece con $\lambda$. Si algún $l_j$ es muy pequeño (multicolinealidad), el término $\sigma^2\sum_j 1/l_j$ de mínimos cuadrados explota, mientras que ridge lo mantiene acotado.

:::{admonition} Nota de notación
En las notas aparece $\operatorname{Cov}(\beta_R)$ donde debe ir $\operatorname{Cov}(\hat\beta_R)$.
:::
