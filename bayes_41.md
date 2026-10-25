# Clasificador bayesiano (sección 4.1)

## Demostración

### Paso 1 · Teorema de Bayes

*Se usa: definición de condicional y probabilidad total.*

$P(G_i)$ es la probabilidad a priori, $P(G_i\mid D)$ la a posteriori, $P(D)$ la probabilidad total y $P(D\mid G_i)$ la condicional del evento. De $P(G_i\mid D)=P(G_i\cap D)/P(D)$ y $P(D\mid G_i)=P(G_i\cap D)/P(G_i)$ se obtiene $P(G_i\cap D)=P(G_i)\,P(D\mid G_i)$. La partición $G_1,\dots,G_r$ cubre el espacio con piezas disjuntas, así que $P(D)=\sum_jP(D\mid G_j)P(G_j)$.

$$P(G_i\mid D)=\frac{P(G_i)\,P(D\mid G_i)}{\sum_{j=1}^rP(D\mid G_j)\,P(G_j)}$$

El denominador no depende de $i$; solo normaliza.

### Paso 2 · Dos clases normales y estimadores

*Se usa: máxima verosimilitud.*

Con $n=n_1+n_2$ observaciones, $G_i:\ x^{(i)}_j\sim N_p(\mu_i,\Sigma_i)$. Los estimadores de máxima verosimilitud son

$$
\begin{aligned}
&\bar x_i=\frac1{n_i}\sum_{j=1}^{n_i}x_j^{(i)},\qquad S_i \\
&{}=\frac1{n_i}\sum_{j=1}^{n_i}\big(x_j^{(i)}-\bar x_i\big)\big(x_j^{(i)}-\bar x_i\big)^T
\end{aligned}
$$

### Paso 3 · Regla basada en la razón de posteriores

*Se usa: el logaritmo es estrictamente creciente.*

$$\frac{P(G_1\mid x)}{P(G_2\mid x)}\ \begin{cases}\ge1 & x\in G_1\\ \lt1 & x\in G_2\end{cases}\qquad\Longleftrightarrow\qquad \log\frac{P(G_1\mid x)}{P(G_2\mid x)}\ \begin{cases}\ge0 & x\in G_1\\ \lt0 & x\in G_2\end{cases}$$

### Paso 4 · Cociente con verosimilitudes normales

*Se usa: los denominadores se cancelan.*

Ambas posteriores comparten el denominador $P(x)$, así que se cancela. Con $P(x\mid G_i)=f(x\mid\bar x_i,S_i)$ y a priori iguales, $P(G_1)=P(G_2)=0{,}5$, también se cancelan:

$$
\begin{aligned}
&\frac{P(G_1\mid x)}{P(G_2\mid x)}=\frac{f(x\mid\bar x_1,S_1)\,P(G_1)}{f(x\mid\bar x_2,S_2)\,P(G_2)} \\
&{}=\frac{f(x\mid\bar x_1,S_1)}{f(x\mid\bar x_2,S_2)}
\end{aligned}
$$

$$e^{h(x)}=\frac{f(x\mid\bar x_1,S_1)}{f(x\mid\bar x_2,S_2)}\ \Rightarrow\ h(x)=\log\frac{f(x\mid\bar x_1,S_1)}{f(x\mid\bar x_2,S_2)}\ \begin{cases}\ge0&x\in G_1\\ \lt0&x\in G_2\end{cases}$$

Con a priori distintas, el umbral pasa a ser $\log(P(G_2)/P(G_1))$.

### Paso 5 · Frontera cuadrática

*Se usa: logaritmo de la densidad normal.*

La densidad es $f(x\mid\bar x_i,S_i)=\dfrac{1}{(2\pi)^{p/2}|S_i|^{1/2}}\exp\!\big[-\tfrac12(x-\bar x_i)^TS_i^{-1}(x-\bar x_i)\big]$. Sea $Q_i=(x-\bar x_i)^TS_i^{-1}(x-\bar x_i)$. Al restar los logaritmos, $\tfrac p2\log2\pi$ se cancela:

$$
\begin{aligned}
&h(x)=-\tfrac12\log|S_1|-\tfrac12Q_1+\tfrac12\log|S_2|+\tfrac12Q_2 \\
&{}=\tfrac12\Big[Q_2-Q_1-\log\frac{|S_1|}{|S_2|}\Big]
\end{aligned}
$$

### Paso 6 · Frontera lineal

*Se usa: $S_1=S_2=S$, $S^{-1}$ simétrica.*

Con covarianza conjunta $S=(n_1S_1+n_2S_2)/n$ (la misma para las dos clases), $\log(|S_1|/|S_2|)=0$. En $Q_2-Q_1$ el término $x^TS^{-1}x$ se cancela, y como $x^TS^{-1}m=m^TS^{-1}x$ los términos cruzados se agrupan.

$$
\begin{aligned}
&h(x)=\tfrac12\Big[(x-\bar x_2)^TS^{-1}(x-\bar x_2)-(x-\bar x_1)^TS^{-1}(x-\bar x_1)\Big] \\
&{}=\tfrac12\Big[2(\bar x_1-\bar x_2)^TS^{-1}x+\bar x_2^TS^{-1}\bar x_2-\bar x_1^TS^{-1}\bar x_1\Big]
\end{aligned}
$$

$$
\begin{aligned}
&h(x)=\underbrace{(\bar x_1-\bar x_2)^TS^{-1}}_{w^T}\,x+\underbrace{\tfrac12\big(\bar x_2^TS^{-1}\bar x_2-\bar x_1^TS^{-1}\bar x_1\big)}_{w_0} \\
&{}=w^Tx+w_0 \qquad\blacksquare
\end{aligned}
$$

Equivalente: $h(x)=(\bar x_1-\bar x_2)^TS^{-1}\big(x-\tfrac{\bar x_1+\bar x_2}{2}\big)$.


