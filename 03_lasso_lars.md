# Estimación lasso y algoritmo LARS

## 1. Planteamiento

Se trabaja con los datos observados normalizados como en (3.11), verificado en el {doc}`capítulo 1 <01_verificaciones>`: $\sum_i y_i=0$, $\sum_i x_{ij}=0$ y $\sum_i x_{ij}^2=n$. El estimador lasso minimiza

$$
S_\lambda(\boldsymbol{\beta})=(\boldsymbol{y}-X\boldsymbol{\beta})^T(\boldsymbol{y}-X\boldsymbol{\beta})+\lambda\sum_{j=1}^{p}|\beta_j|,\qquad \lambda>0 .
$$

A diferencia de ridge, la penalización $|\beta_j|$ no es diferenciable en $\beta_j=0$. Por eso no se puede igualar el gradiente a cero y despejar, y no existe una fórmula cerrada general como $(X^TX+\lambda I_p)^{-1}X^T\boldsymbol{y}$. El análisis se hace con subgradientes y conduce a tres resultados: las condiciones de optimalidad (KKT), la solución exacta en el caso ortogonal y dos algoritmos para el caso general (descenso por coordenadas y LARS).

## 2. Condiciones de optimalidad (KKT)

$S_\lambda$ es convexa: suma de una forma cuadrática convexa y de una norma $\ell_1$. Por tanto, $\hat{\boldsymbol{\beta}}$ es un mínimo global si y solo si $\boldsymbol{0}\in\partial S_\lambda(\hat{\boldsymbol{\beta}})$. El subdiferencial de $|b|$ es $\{\operatorname{sign}(b)\}$ si $b\neq 0$ y el intervalo $[-1,1]$ si $b=0$. La parte cuadrática tiene gradiente $-2X^T(\boldsymbol{y}-X\boldsymbol{\beta})$, como en (3.10) con $\lambda=0$. Entonces, para cada $j=1,\dots,p$:

$$
-2\boldsymbol{x}_j^T(\boldsymbol{y}-X\hat{\boldsymbol{\beta}})+\lambda s_j=0,\qquad s_j\in\partial|\hat\beta_j| .
$$

Esto equivale a

$$
\begin{aligned}
2\,\boldsymbol{x}_j^T(\boldsymbol{y}-X\hat{\boldsymbol{\beta}})&=\lambda\operatorname{sign}(\hat\beta_j) &&\text{si }\hat\beta_j\neq 0,\\
\left|2\,\boldsymbol{x}_j^T(\boldsymbol{y}-X\hat{\boldsymbol{\beta}})\right|&\le\lambda &&\text{si }\hat\beta_j=0 .
\end{aligned}
$$

Interpretación: la correlación de cada variable con el residuo nunca supera $\lambda/2$ en valor absoluto. Las variables con coeficiente distinto de cero la alcanzan exactamente, y su signo coincide con el del coeficiente. Como consecuencia, $\hat{\boldsymbol{\beta}}=\boldsymbol{0}$ cuando

$$
\lambda\ge\lambda_{\max}=2\max_j|\boldsymbol{x}_j^T\boldsymbol{y}| .
$$

## 3. Caso ortogonal: umbralización suave

Si $X^TX=nI_p$, el estimador de mínimos cuadrados es $\hat\beta_j^{\mathrm{MCO}}=\boldsymbol{x}_j^T\boldsymbol{y}/n$. Al desarrollar $S_\lambda$:

$$
S_\lambda(\boldsymbol{\beta})=\boldsymbol{y}^T\boldsymbol{y}+\sum_{j=1}^p\left[n\beta_j^2-2n\hat\beta_j^{\mathrm{MCO}}\beta_j+\lambda|\beta_j|\right].
$$

El problema se separa en $p$ problemas unidimensionales. La condición KKT de cada coordenada es $2n\beta_j-2n\hat\beta_j^{\mathrm{MCO}}+\lambda s_j=0$, que da tres casos:

- Si $\beta_j>0$ (con $s_j=1$): $\beta_j=\hat\beta_j^{\mathrm{MCO}}-\lambda/(2n)$, válido cuando $\hat\beta_j^{\mathrm{MCO}}>\lambda/(2n)$.
- Si $\beta_j<0$ (con $s_j=-1$): $\beta_j=\hat\beta_j^{\mathrm{MCO}}+\lambda/(2n)$, válido cuando $\hat\beta_j^{\mathrm{MCO}}<-\lambda/(2n)$.
- Si $|\hat\beta_j^{\mathrm{MCO}}|\le\lambda/(2n)$: $\beta_j=0$ con $s_j=2n\hat\beta_j^{\mathrm{MCO}}/\lambda\in[-1,1]$.

Los tres casos se resumen en el operador de umbralización suave:

$$
\hat\beta_j^{\mathrm{lasso}}=\operatorname{sign}\!\left(\hat\beta_j^{\mathrm{MCO}}\right)\left(\left|\hat\beta_j^{\mathrm{MCO}}\right|-\frac{\lambda}{2n}\right)_+ ,\qquad (t)_+=\max(t,0).
$$

En el mismo caso ortogonal, el estimador ridge es $\hat{\boldsymbol{\beta}}_R=(nI_p+\lambda I_p)^{-1}X^T\boldsymbol{y}=\dfrac{n}{n+\lambda}\hat{\boldsymbol{\beta}}^{\mathrm{MCO}}$. Ridge contrae todos los coeficientes por el mismo factor y nunca produce ceros exactos. Lasso resta una constante y trunca en cero, de modo que los coeficientes pequeños quedan exactamente en cero. Esta es la diferencia de fondo entre ambos estimadores.

## 4. Caso general: descenso por coordenadas

Para $X^TX$ arbitraria con $\sum_i x_{ij}^2=n$, se fijan todos los coeficientes salvo $\beta_j$ y se define el residuo parcial $\boldsymbol{r}_j=\boldsymbol{y}-\sum_{k\neq j}\boldsymbol{x}_k\beta_k$. Como $\boldsymbol{x}_j^T\boldsymbol{x}_j=n$,

$$
S_\lambda=\|\boldsymbol{r}_j-\boldsymbol{x}_j\beta_j\|^2+\lambda|\beta_j|+\text{const}=n\beta_j^2-2\beta_j\,\boldsymbol{x}_j^T\boldsymbol{r}_j+\lambda|\beta_j|+\text{const}.
$$

Esto es el problema unidimensional de la sección 3 con $\hat\beta_j^{\mathrm{MCO}}$ reemplazado por $\boldsymbol{x}_j^T\boldsymbol{r}_j/n$. La actualización de cada coordenada es

$$
\beta_j\leftarrow \mathcal{S}_{\lambda/(2n)}\!\left(\frac{\boldsymbol{x}_j^T\boldsymbol{r}_j}{n}\right),\qquad \mathcal{S}_t(z)=\operatorname{sign}(z)(|z|-t)_+ .
$$

Se recorren las coordenadas $j=1,\dots,p$ cíclicamente hasta convergencia. Como $S_\lambda$ es convexa y la penalización es separable, el procedimiento converge al mínimo global. Este método resuelve un valor de $\lambda$ cada vez; es el que usa `Lasso` de scikit-learn. LARS, en cambio, entrega el camino completo para todos los $\lambda$.

## 5. El algoritmo LARS (Efron et al., 2004)

### 5.1 Idea

La selección progresiva (*forward selection*) incorpora la variable más correlacionada con el residuo y ajusta por completo, lo que es demasiado agresivo. La regresión por etapas (*stagewise*) avanza en pasos diminutos. LARS avanza exactamente lo necesario: mueve los coeficientes de las variables activas en la dirección que mantiene iguales sus correlaciones con el residuo, hasta que una variable inactiva alcanza esa misma correlación y entra al conjunto activo.

En esta sección las columnas se escalan a norma unitaria, $\boldsymbol{x}_j^T\boldsymbol{x}_j=1$, que es la convención del artículo. Basta reescalar (3.11) por $1/\sqrt{n}$; el problema es el mismo con $\lambda$ y los coeficientes reescalados.

### 5.2 Notación y dirección equiangular

Sea $\boldsymbol{r}=\boldsymbol{y}-X\boldsymbol{\beta}$ el residuo actual, $\boldsymbol{c}=X^T\boldsymbol{r}$ las correlaciones, $C=\max_j|c_j|$ y $\mathcal{A}$ el conjunto activo, con signos $\boldsymbol{s}_\mathcal{A}=\operatorname{sign}(\boldsymbol{c}_\mathcal{A})$. Con $G_\mathcal{A}=X_\mathcal{A}^TX_\mathcal{A}$ se define

$$
A_\mathcal{A}=\left(\boldsymbol{s}_\mathcal{A}^TG_\mathcal{A}^{-1}\boldsymbol{s}_\mathcal{A}\right)^{-1/2},\qquad
\boldsymbol{w}_\mathcal{A}=A_\mathcal{A}\,G_\mathcal{A}^{-1}\boldsymbol{s}_\mathcal{A},\qquad
\boldsymbol{u}_\mathcal{A}=X_\mathcal{A}\boldsymbol{w}_\mathcal{A}.
$$

Se verifica que $\boldsymbol{u}_\mathcal{A}$ es el vector equiangular:

$$
\|\boldsymbol{u}_\mathcal{A}\|^2=\boldsymbol{w}_\mathcal{A}^TG_\mathcal{A}\boldsymbol{w}_\mathcal{A}=A_\mathcal{A}^2\,\boldsymbol{s}_\mathcal{A}^TG_\mathcal{A}^{-1}\boldsymbol{s}_\mathcal{A}=1,
\qquad
X_\mathcal{A}^T\boldsymbol{u}_\mathcal{A}=G_\mathcal{A}\boldsymbol{w}_\mathcal{A}=A_\mathcal{A}\,\boldsymbol{s}_\mathcal{A}.
$$

Cada variable activa forma el mismo ángulo con $\boldsymbol{u}_\mathcal{A}$. Si los coeficientes activos avanzan una longitud $\gamma$ en esa dirección, $\boldsymbol{\beta}_\mathcal{A}(\gamma)=\boldsymbol{\beta}_\mathcal{A}+\gamma\boldsymbol{w}_\mathcal{A}$, entonces el residuo y las correlaciones cambian así:

$$
\boldsymbol{r}(\gamma)=\boldsymbol{r}-\gamma\boldsymbol{u}_\mathcal{A},\qquad
c_j(\gamma)=c_j-\gamma a_j,\quad \boldsymbol{a}=X^T\boldsymbol{u}_\mathcal{A}.
$$

Para $j\in\mathcal{A}$ se tiene $a_j=A_\mathcal{A}s_j$, luego $|c_j(\gamma)|=C-\gamma A_\mathcal{A}$: todas las correlaciones activas permanecen iguales y decrecen linealmente.

### 5.3 Longitud del paso

Una variable inactiva $k$ entra cuando $|c_k(\gamma)|=C-\gamma A_\mathcal{A}$, es decir, en

$$
\hat\gamma_k=\min\nolimits^{+}\left\{\frac{C-c_k}{A_\mathcal{A}-a_k},\ \frac{C+c_k}{A_\mathcal{A}+a_k}\right\},\qquad \hat\gamma=\min_{k\notin\mathcal{A}}\hat\gamma_k ,
$$

donde $\min^{+}$ es el menor de los valores positivos. Si no quedan variables inactivas, $\hat\gamma=C/A_\mathcal{A}$ y se llega a la solución de mínimos cuadrados.

### 5.4 Algoritmo con la modificación lasso

1. Inicializar $\boldsymbol{\beta}=\boldsymbol{0}$, $\boldsymbol{r}=\boldsymbol{y}$ y $\mathcal{A}=\{\arg\max_j|\boldsymbol{x}_j^T\boldsymbol{y}|\}$.
2. Calcular $\boldsymbol{c}$, $C$, $\boldsymbol{s}_\mathcal{A}$, $A_\mathcal{A}$, $\boldsymbol{w}_\mathcal{A}$, $\boldsymbol{u}_\mathcal{A}$ y $\boldsymbol{a}$.
3. Calcular $\hat\gamma$ y la variable $k^\star$ que lo alcanza (sección 5.3).
4. Modificación lasso: para $j\in\mathcal{A}$ calcular $\gamma_j=-\beta_j/w_j$ (solo si es positivo) y $\tilde\gamma=\min_j\gamma_j$.
    - Si $\tilde\gamma<\hat\gamma$: avanzar $\tilde\gamma$ (con $\boldsymbol{\beta}_\mathcal{A}\leftarrow\boldsymbol{\beta}_\mathcal{A}+\tilde\gamma\boldsymbol{w}_\mathcal{A}$), fijar $\beta_j=0$ y retirar $j$ de $\mathcal{A}$.
    - En caso contrario: avanzar $\hat\gamma$ y agregar $k^\star$ a $\mathcal{A}$.
5. Repetir los pasos 2 a 4 hasta que $C=0$ (solución de mínimos cuadrados).

El paso 4 es necesario. La condición KKT exige $\operatorname{sign}(\hat\beta_j)=\operatorname{sign}(c_j)$ para las variables activas. LARS sin modificar puede hacer que un coeficiente cruce por cero mientras su correlación conserva el signo, y entonces el resultado deja de ser lasso. Con la modificación, el camino coincide exactamente con el de lasso.

### 5.5 Relación con el parámetro $\lambda$

En cada punto del camino, las variables activas cumplen $|c_j|=C$. Comparando con la condición KKT de la sección 2, el punto es la solución lasso para

$$
\lambda=2C ,
$$

donde, con columnas de norma unitaria, $\lambda$ está medido en la escala reescalada. Se concluye que:

- El camino $\hat{\boldsymbol{\beta}}(\lambda)$ es lineal a trozos, con nudos donde cambia el conjunto activo.
- El primer nudo es $\lambda_{\max}=2\max_j|\boldsymbol{x}_j^T\boldsymbol{y}|$, donde $\hat{\boldsymbol{\beta}}=\boldsymbol{0}$.
- Basta calcular los nudos e interpolar linealmente para obtener la solución con cualquier $\lambda$. El costo total es del mismo orden que un ajuste de mínimos cuadrados con las $p$ variables.
- Cada solución corresponde a la forma restringida del Ejercicio 5: minimizar la suma de cuadrados sujeto a $\sum_j|\beta_j|\le\eta$, con $\eta=\|\hat{\boldsymbol{\beta}}(\lambda)\|_1$.

## 6. Verificación numérica

Se programó el algoritmo de la sección 5.4 en Python (código completo en el {doc}`apéndice <apendice_codigo>`) y se comparó con scikit-learn. Para LARS se usó el conjunto *diabetes* ($n=442$, $p=10$), centrado y con columnas de norma unitaria.

| Comprobación | Resultado |
|:---------------------------------------------|:-----------------------------|
| Umbralización suave vs. `Lasso` (caso ortogonal, $n=200$, $p=5$) | diferencia máxima 8.9e-16 |
| Ridge ortogonal igual a $\hat\beta^{\mathrm{MCO}}\,n/(n+\lambda)$ | se cumple |
| Descenso por coordenadas vs. `Lasso` (diabetes, $\lambda=0.15\,\lambda_{\max}$) | diferencia máxima 1.8e-10 |
| LARS propio vs. `lars_path(method="lasso")` | 13 nudos en ambos; coeficientes difieren 1.5e-11 |
| Relación $\lambda=2C$ (en sklearn, $\alpha=C/n$) | diferencia máxima 2.5e-12 |
| Condiciones KKT en cada nudo | violación máxima 5.3e-12 |

En este conjunto hay un cruce por cero: una variable sale del conjunto activo y vuelve a entrar. Por eso el camino tiene más nudos que variables entradas, y muestra que la modificación del paso 4 es necesaria.
