# Lema 2.2: masa de las celdas no visitadas

:::{admonition} Enunciado
Sean $C_1,\dots,C_r\subseteq\mathcal{X}$ y $S$ una muestra i.i.d. de tamaño $m$ con densidad $\mathcal{D}$ sobre $\mathcal{X}$:

$$\mathbb{E}_{S\sim\mathcal{D}^m}\Big[\sum_{i:\,C_i\cap S=\emptyset} P(C_i)\Big] \le \frac{r}{m\,e}$$
:::

## Demostración

### Paso 1 · Indicadoras y linealidad

*Se usa: $\mathbb{E}[\sum c_iZ_i]=\sum c_i\mathbb{E}[Z_i]$.*

Los índices con $C_i\cap S=\emptyset$ dependen de la muestra, así que no se puede aplicar linealidad todavía. Se suma sobre los $r$ índices fijos y la indicadora apaga las celdas visitadas.

$$
\begin{aligned}
&\mathbb{E}_S\Big[\sum_{i:\,C_i\cap S=\emptyset} P(C_i)\Big] \\
&{}= \sum_{i=1}^r P(C_i)\,\mathbb{E}_S\big[\mathbf 1_{C_i\cap S=\emptyset}\big] \\
&{}= \sum_{i=1}^r P(C_i)\,P_S\big(C_i\cap S=\emptyset\big)
\end{aligned}
$$

### Paso 2 · Independencia

*Se usa: puntos i.i.d. y complemento.*

La celda queda vacía cuando ninguno de los $m$ puntos cae en ella.

$$
\begin{aligned}
&P_S\big(C_i\cap S=\emptyset\big) = \big(1-P(C_i)\big)^m \quad\Rightarrow \\
&\quad \mathbb{E}_S[\cdot] = \sum_{i=1}^r P(C_i)\big(1-P(C_i)\big)^m
\end{aligned}
$$

### Paso 3 · Desigualdad de Bernoulli

*Se usa: $(1+x)^n\ge 1+nx$ para $x\ge-1$.*

Con $p=P(C_i)$ y $x=-p/n$ (cumple $x\ge-1$ para $n\ge1$):

$$\Big(1-\frac{p}{n}\Big)^n \ge 1-p$$

### Paso 4 · Límite $n\to\infty$

*Se usa: logaritmo y regla de L'Hôpital.*

Sea $y=\lim_{n\to\infty}(1-p/n)^n$. Entonces

$$
\begin{aligned}
&\ln y = \lim_{n\to\infty}\frac{\ln(1-p/n)}{1/n} = \lim_{n\to\infty}\frac{\dfrac{p/n^2}{1-p/n}}{-1/n^2} \\
&{}= \lim_{n\to\infty}\frac{-p}{1-p/n} = -p \quad\Rightarrow\quad y=e^{-p}
\end{aligned}
$$

Como la desigualdad del paso 3 vale para todo $n$, se conserva en el límite:

$$e^{-p}\ge 1-p$$

### Paso 5 · Elevar a la $m$

*Se usa: $0\le a\le b\Rightarrow a^m\le b^m$.*

Hace falta $1-p\ge0$, que se cumple porque $p$ es una probabilidad.

$$\big(1-p\big)^m \le e^{-mp}$$

### Paso 6 · Multiplicar por $p\ge0$ y sumar

$$\mathbb{E}_S\Big[\sum_{i:\,C_i\cap S=\emptyset} P(C_i)\Big] \le \sum_{i=1}^r P(C_i)\,e^{-mP(C_i)}$$

### Paso 7 · Maximizar $f(p)=p\,e^{-mp}$

*Se usa: derivada del producto.*

$$f'(p)=e^{-mp}-mp\,e^{-mp}=e^{-mp}(1-mp)=0 \iff p=\frac1m$$

$$f''(p)=e^{-mp}\,(m^2p-2m)\quad\Rightarrow\quad f''\!\Big(\frac1m\Big)=-\frac{m}{e}<0$$

El signo negativo confirma un máximo. Además $f'>0$ para $p<1/m$ y $f'<0$ para $p>1/m$, así que es el máximo global en $[0,1]$.

### Paso 8 · Sumar las $r$ cotas

$$
\begin{aligned}
&\mathbb{E}_S\Big[\sum_{i:\,C_i\cap S=\emptyset} P(C_i)\Big] \le \sum_{i=1}^r f\!\Big(\frac1m\Big) \\
&{}= \sum_{i=1}^r \frac{1}{m}\,e^{-1} = \frac{r}{m\,e} \qquad\blacksquare
\end{aligned}
$$


