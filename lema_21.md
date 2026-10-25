# Lema 2.1: cota del error de 1-NN

:::{admonition} Enunciado
Sea $\mathcal{X}=[0,1]^d$, $\mathcal{Y}=\{0,1\}$, $\mathcal{D}$ una distribución sobre $\mathcal{X}\times\mathcal{Y}$ cuya probabilidad condicional $\eta(x)=P(y=1\mid x)$ es $c$-Lipschitz. Sea $S=((x_1,y_1),\dots,(x_m,y_m))$ i.i.d., $h_S$ la regla 1-NN y $h^\star$ la regla de Bayes para $\eta$. Entonces

$$
\begin{aligned}
&\mathbb{E}_{S\sim\mathcal{D}^m}\big[L_{\mathcal{D}}(h_S)\big] \\
&{}\le 2\,L_{\mathcal{D}}(h^\star) + c\;\mathbb{E}_{S,x}\big[\|x-x_{\pi_1(x)}\|\big]
\end{aligned}
$$
:::

Notación: $x' = x_{\pi_1(x)}$ es el vecino más cercano de $x$ en $S$, y $y' = y_{\pi_1(x)}$ su etiqueta.

## Demostración

### Paso 1 · Esperanza de una indicadora

*Se usa: $\mathbb{E}[\mathbf 1_A]=P(A)$.*

El error es la probabilidad de que la etiqueta de $x$ difiera de la de su vecino. Se sortea primero el conjunto de puntos $S_x$ y el punto nuevo $x$; luego las etiquetas $y\sim\eta(x)$ y $y'\sim\eta(x')$. El vecino $x'$ depende solo de los puntos, así que queda fijo al sortear las etiquetas.

$$
\begin{aligned}
&\mathbb{E}_{S}[L_{\mathcal{D}}(h_S)] \\
&{}= \mathbb{E}_{S_x\sim\mathcal{D}_x^m,\,x\sim\mathcal{D}_x}\Big[\ \mathbb{E}_{y\sim\eta(x),\,y'\sim\eta(x')}\big[\mathbf 1[y\ne y']\big]\Big] \\
&{}= \mathbb{E}_{S_x,x}\Big[P_{y,y'}\big(y\ne y'\big)\Big]
\end{aligned}
$$

### Paso 2 · Probabilidad de desacuerdo

*Se usa: independencia y casos disjuntos.*

Dados los puntos, $y$ e $y'$ son independientes. Los casos $(y'=1,\,y=0)$ y $(y'=0,\,y=1)$ son disjuntos y cada uno es un producto.

$$P(y\ne y') = \eta(x')\big(1-\eta(x)\big) + \big(1-\eta(x')\big)\eta(x)$$

### Paso 3 · Sumar y restar $\eta(x)$

*Se usa: álgebra.*

Se escribe $\eta(x') = \eta(x) - \big(\eta(x)-\eta(x')\big)$ y se llama $\delta=\eta(x)-\eta(x')$. Al expandir, los términos con $\eta(x)$ solos dan $2\eta(1-\eta)$ y los que contienen $\delta$ dan $\delta(2\eta-1)$.

$$\begin{aligned}
P(y\ne y') &= (\eta-\delta)(1-\eta) + (1-\eta+\delta)\,\eta = 2\eta-2\eta^2-\delta+2\eta\delta\\
&= 2\eta(x)\big(1-\eta(x)\big) + \big(\eta(x)-\eta(x')\big)\big(2\eta(x)-1\big)
\end{aligned}$$

### Paso 4 · Acotar $|2\eta-1|$

*Se usa: $\eta\in[0,1]$.*

Como $\eta$ es una probabilidad, $0\le\eta\le1$. Multiplicando por 2 y restando 1: $-1\le 2\eta-1\le 1$, es decir, $|2\eta(x)-1|\le 1$.

### Paso 5 · Desigualdad triangular y Lipschitz

*Se usa: $|a+b|\le|a|+|b|$, hipótesis $c$-Lipschitz.*

El primer sumando es no negativo, así que su valor absoluto es él mismo.

$$
\begin{aligned}
&P(y\ne y') \le 2\eta(x)\big(1-\eta(x)\big) + |\eta(x)-\eta(x')|\cdot|2\eta(x)-1| \\
&{}\le 2\eta(x)\big(1-\eta(x)\big) + c\,\|x-x'\|
\end{aligned}
$$

### Paso 6 · Tomar esperanza

*Se usa: monotonía y linealidad.*

$$
\begin{aligned}
&\mathbb{E}_S[L_{\mathcal{D}}(h_S)] \\
&{}\le \mathbb{E}_{x}\big[2\eta(x)(1-\eta(x))\big] + c\,\mathbb{E}_{S,x}\|x-x'\|
\end{aligned}
$$

El primer término depende solo de $x$, así que promediar sobre $S$ no lo cambia.

### Paso 7 · Comparar con el error de Bayes

*Se usa: mínimo por máximo.*

Por punto, $\eta(1-\eta)=\min\{\eta,1-\eta\}\cdot\max\{\eta,1-\eta\}$ y $\max\le1$, luego $2\eta(1-\eta)\le 2\min\{\eta,1-\eta\}$. El error de Bayes en $x$ es justo $\min\{\eta(x),1-\eta(x)\}$: si $\eta\ge\tfrac12$, $h^\star$ predice 1 y falla con probabilidad $1-\eta$; si no, predice 0 y falla con probabilidad $\eta$.

$$
\begin{aligned}
&\mathbb{E}_x\big[2\eta(1-\eta)\big] \\
&{}\le 2\,\mathbb{E}_x\big[\min\{\eta,1-\eta\}\big] = 2\,L_{\mathcal{D}}(h^\star)
\end{aligned}
$$

$$
\begin{aligned}
&\mathbb{E}_S[L_{\mathcal{D}}(h_S)] \\
&{}\le 2\,L_{\mathcal{D}}(h^\star) + c\,\mathbb{E}_{S,x}\|x-x'\| \qquad\blacksquare
\end{aligned}
$$


