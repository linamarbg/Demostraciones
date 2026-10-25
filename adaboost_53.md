# AdaBoost (sección 5.3)

:::{admonition} Enunciado
Datos $(y_n,x_n)$, $n=1,\dots,N$, $y_n\in\{-1,1\}$. El clasificador es $f(x)=\operatorname{sgn}F(x)$, con $F(x)=\sum_{k=1}^K\alpha_k\phi(x;\theta_k)$ y $\phi\in\{-1,1\}$. Se construye por etapas: $F_i=F_{i-1}+\alpha_i\phi(x;\theta_i)$, $F_0=0$. Con la pérdida exponencial $\mathcal{L}(y,F(x))=\exp(-yF(x))$:

$$
\begin{aligned}
&(\alpha_i,\theta_i)=\arg\min_{\alpha,\theta}J(\alpha,\theta),\qquad J(\alpha,\theta) \\
&{}=\sum_{n=1}^N\exp\!\big(-y_n(F_{i-1}(x_n)+\alpha\,\phi(x_n;\theta))\big)
\end{aligned}
$$
:::

## Demostración

### Paso 1 · Separar el exponencial

*Se usa: $e^{u+v}=e^ue^v$.*

$$
\begin{aligned}
&J(\alpha,\theta)=\sum_{n=1}^N w_n^{(i)}\,\exp\!\big(-y_n\alpha\,\phi(x_n;\theta)\big), \\
&\qquad w_n^{(i)}=\exp\!\big(-y_nF_{i-1}(x_n)\big)
\end{aligned}
$$

Los pesos no dependen de $\alpha$ ni de $\theta$. Se normalizan para que $\sum_nw_n^{(i)}=1$; dividir por una constante positiva no cambia los minimizadores.

### Paso 2 · Partir la suma

*Se usa: $y_n\phi\in\{-1,1\}$.*

Si el punto está bien clasificado ($y_n\phi=1$) su factor es $e^{-\alpha}$; si está mal ($y_n\phi=-1$), es $e^{\alpha}$. Sea $P_i(\theta)$ el error ponderado:

$$
\begin{aligned}
&P_i(\theta)=\sum_{n=1}^Nw_n^{(i)}\,\mathbf 1\big[y_n\phi(x_n;\theta)=-1\big],\qquad J \\
&{}=e^{-\alpha}\big(1-P_i\big)+e^{\alpha}P_i=e^{-\alpha}+\big(e^{\alpha}-e^{-\alpha}\big)P_i(\theta)
\end{aligned}
$$

### Paso 3 · Elección de $\theta_i$

*Se usa: función afín creciente de $P_i$ si $\alpha>0$.*

Se busca $\alpha>0$ (basta con $P_i<\tfrac12$, es decir, que el clasificador débil sea mejor que el azar; si la familia contiene a $-\phi$, esto no pierde generalidad). Entonces $e^{\alpha}-e^{-\alpha}>0$. Minimizar $J$ en $\theta$ es entonces minimizar $P_i(\theta)$, sin importar el valor de $\alpha$.

$$\theta_i=\arg\min_\theta P_i(\theta)$$

### Paso 4 · Coeficiente $\alpha_i$

*Se usa: derivada e igualdad a cero; convexidad.*

$$g(\alpha)=e^{-\alpha}(1-P_i)+e^{\alpha}P_i,\qquad g'(\alpha)=-e^{-\alpha}(1-P_i)+e^{\alpha}P_i=0$$

$$
\begin{aligned}
&e^{\alpha}P_i=e^{-\alpha}(1-P_i)\ \Rightarrow\ e^{2\alpha}=\frac{1-P_i}{P_i}\ \\
&\Rightarrow\ 2\alpha_i=\ln\frac{1-P_i}{P_i}\ \Rightarrow\ \alpha_i=\frac12\ln\frac{1-P_i}{P_i}
\end{aligned}
$$

Como $g''(\alpha)=e^{-\alpha}(1-P_i)+e^{\alpha}P_i>0$, $g$ es estrictamente convexa y el punto crítico es el mínimo global. Además $J(\alpha,\theta)\ge g(\alpha)\ge g(\alpha_i)=J(\alpha_i,\theta_i)$: el par $(\alpha_i,\theta_i)$ es el minimizador conjunto.

### Paso 5 · Actualización de pesos

*Se usa: normalización.*

Como $F_i(x_n)=F_{i-1}(x_n)+\alpha_i\phi(x_n;\theta_i)$, se tiene $\exp(-y_nF_i(x_n))=\exp(-y_nF_{i-1}(x_n))\,\exp(-y_n\alpha_i\phi(x_n;\theta_i))$. Los pesos nuevos son los anteriores multiplicados por ese factor y normalizados:

$$
\begin{aligned}
&w_n^{(i+1)}=\frac{1}{Z_i}\,w_n^{(i)}\,e^{-y_n\alpha_i\phi(x_n;\theta_i)},\qquad Z_i \\
&{}=\sum_{n=1}^Nw_n^{(i)}e^{-y_n\alpha_i\phi(x_n;\theta_i)}=g(\alpha_i)=2\sqrt{P_i(1-P_i)}
\end{aligned}
$$

Los mal clasificados se multiplican por $e^{\alpha_i}$. Su peso total queda $P_ie^{\alpha_i}/Z_i=\tfrac12$, así que el siguiente clasificador parte al nivel del azar.

### Paso 6 · Clasificador final

$$f(x)=\operatorname{sgn}\Big(\sum_{k=1}^K\alpha_k\,\phi(x;\theta_k)\Big) \qquad\blacksquare$$


