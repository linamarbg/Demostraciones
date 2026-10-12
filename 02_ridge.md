# Propiedades del estimador ridge (3.12)

## Preliminares

Las cuatro propiedades de (3.12) se verifican con el modelo $\boldsymbol{y}=X\boldsymbol{\beta}+\boldsymbol{\varepsilon}$, $\mathbb{E}(\boldsymbol{\varepsilon})=\mathbf{0}$ y $\operatorname{Cov}(\boldsymbol{\varepsilon})=\sigma^2I_n$, con $X$ centrada y estandarizada como en (3.11), verificado en el {doc}`capítulo 1 <01_verificaciones>`. El estimador ridge es

$$
\hat{\boldsymbol{\beta}}_R=(X^TX+\lambda I_p)^{-1}X^T\boldsymbol{y},\qquad \lambda>0 .
$$

Sea $M=X^TX+\lambda I_p$. Se usan cuatro hechos:

- $M$ es simétrica porque $X^TX$ lo es; por tanto, $M^{-1}$ también.
- $M$ es invertible para todo $\lambda>0$: si $\boldsymbol{v}\neq\mathbf{0}$, entonces $\boldsymbol{v}^TM\boldsymbol{v}=\|X\boldsymbol{v}\|^2+\lambda\|\boldsymbol{v}\|^2>0$. Esto vale aunque $X^TX$ sea singular, y por eso ridge funciona con multicolinealidad.
- El estimador es lineal en $\boldsymbol{y}$: $\hat{\boldsymbol{\beta}}_R=A\boldsymbol{y}$, con $A=M^{-1}X^T$ constante (no aleatoria).
- $\mathbb{E}(\boldsymbol{y})=X\boldsymbol{\beta}$ y $\operatorname{Cov}(\boldsymbol{y})=\sigma^2I_n$.

## 1. Esperanza

El estimador ridge es sesgado: su esperanza es $M^{-1}X^TX\boldsymbol{\beta}$, no $\boldsymbol{\beta}$. Por linealidad de la esperanza:

$$
\mathbb{E}(\hat{\boldsymbol{\beta}}_R)=A\,\mathbb{E}(\boldsymbol{y})=M^{-1}X^TX\boldsymbol{\beta}=(X^TX+\lambda I_p)^{-1}X^TX\boldsymbol{\beta} .\qquad\blacksquare
$$

## 2. Matriz de covarianza

Con el Ejercicio 1 de la sección 3.6, $\operatorname{Cov}(A\boldsymbol{y})=A\operatorname{Cov}(\boldsymbol{y})A^T$. Como $M^{-1}$ es simétrica, $(M^{-1})^T=M^{-1}$:

$$
\begin{aligned}
\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)&=\sigma^2M^{-1}X^T\left(M^{-1}X^T\right)^T\\
&=\sigma^2(X^TX+\lambda I_p)^{-1}X^TX(X^TX+\lambda I_p)^{-1} .\qquad\blacksquare
\end{aligned}
$$

En el enunciado de la página aparece $\operatorname{Cov}(\boldsymbol{\beta}_R)$; debe ser $\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)$. Es una errata de notación.

## 3. Sesgo

Como $X^TX=M-\lambda I_p$, se resta $\boldsymbol{\beta}$ de la esperanza de la propiedad 1:

$$
\begin{aligned}
\mathbb{E}(\hat{\boldsymbol{\beta}}_R)-\boldsymbol{\beta}&=M^{-1}X^TX\boldsymbol{\beta}-M^{-1}M\boldsymbol{\beta}\\
&=M^{-1}\left(X^TX-M\right)\boldsymbol{\beta}=-\lambda(X^TX+\lambda I_p)^{-1}\boldsymbol{\beta} .\qquad\blacksquare
\end{aligned}
$$

Para $\lambda>0$ el sesgo es no nulo; se anula cuando $\lambda=0$ (caso de mínimos cuadrados).

## 4. Error cuadrático medio total

El error cuadrático medio total es la suma de la traza de la covarianza (varianzas) y el sesgo al cuadrado. Sea $\boldsymbol{W}=\hat{\boldsymbol{\beta}}_R-\boldsymbol{\beta}$ y $\boldsymbol{\mu}=\mathbb{E}(\boldsymbol{W})$. Restar la constante $\boldsymbol{\beta}$ no cambia la covarianza, así que $\operatorname{Cov}(\boldsymbol{W})=\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)$. Como $\boldsymbol{W}^T\boldsymbol{W}=\operatorname{tr}(\boldsymbol{W}\boldsymbol{W}^T)$ y $\mathbb{E}(\boldsymbol{W}\boldsymbol{W}^T)=\operatorname{Cov}(\boldsymbol{W})+\boldsymbol{\mu}\boldsymbol{\mu}^T$:

$$
\mathbb{E}\left[\boldsymbol{W}^T\boldsymbol{W}\right]=\operatorname{tr}\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)+\boldsymbol{\mu}^T\boldsymbol{\mu} .
$$

**Término de varianza.** $X^TX$ es simétrica y semidefinida positiva, luego existe una matriz ortogonal $\Gamma$ con $X^TX=\Gamma L\Gamma^T$ y $L=\operatorname{diag}(l_1,\dots,l_p)$. Entonces $M^{-1}=\Gamma(L+\lambda I)^{-1}\Gamma^T$. Con la propiedad 2 y la invariancia de la traza bajo permutaciones cíclicas:

$$
\operatorname{tr}\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)=\sigma^2\operatorname{tr}\!\left[(L+\lambda I)^{-1}L(L+\lambda I)^{-1}\right]=\sigma^2\sum_{j=1}^p\frac{l_j}{(l_j+\lambda)^2} .
$$

**Término de sesgo al cuadrado.** Por la propiedad 3 y la simetría de $M^{-1}$:

$$
\boldsymbol{\mu}^T\boldsymbol{\mu}=\lambda^2\left(M^{-1}\boldsymbol{\beta}\right)^T\left(M^{-1}\boldsymbol{\beta}\right)=\lambda^2\boldsymbol{\beta}^T(X^TX+\lambda I_p)^{-2}\boldsymbol{\beta} .
$$

Sumando ambos términos se obtiene la propiedad 4:

$$
\begin{aligned}
\mathbb{E}\left[(\hat{\boldsymbol{\beta}}_R-\boldsymbol{\beta})^T(\hat{\boldsymbol{\beta}}_R-\boldsymbol{\beta})\right]&=\sigma^2\sum_{j=1}^p\frac{l_j}{(l_j+\lambda)^2}\\
&\quad+\lambda^2\boldsymbol{\beta}^T(X^TX+\lambda I_p)^{-2}\boldsymbol{\beta} .\qquad\blacksquare
\end{aligned}
$$

## Comentario

La varianza decrece con $\lambda$, porque cada sumando $l_j/(l_j+\lambda)^2$ disminuye; el sesgo al cuadrado crece con $\lambda$. De ahí el compromiso sesgo-varianza. Si algún $l_j$ es muy pequeño (multicolinealidad), el término $\sigma^2\sum_j 1/l_j$ de mínimos cuadrados explota, mientras que ridge lo mantiene acotado.
