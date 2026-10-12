# Verificación de la regla óptima de Bayes

**Desigualdad e igualdad de la pérdida esperada del clasificador.**

La expresión contiene **dos afirmaciones distintas**:

$$
\mathbb{E}_x\Big(2\eta(x)\big(1-\eta(x)\big)\Big)\;\overset{(A)}{\le}\;2\,\mathbb{E}_x\Big(\min\{\eta(x),\,1-\eta(x)\}\Big)\;\overset{(B)}{=}\;2\,L_D(h^\star),
$$

donde (A) es una desigualdad y (B) es una igualdad. Ambas se cumplen. A continuación se verifican por separado.

## Paso 0: qué significa cada símbolo

- $x$: un ejemplo (por ejemplo, un correo electrónico).
- $y\in\{0,1\}$: su etiqueta real (por ejemplo, spam $=1$, no spam $=0$).
- $\eta(x)=\mathbb{P}(Y=1\mid X=x)$: la probabilidad de que la etiqueta sea $1$ dado que vemos $x$. Es un número entre $0$ y $1$.
- $h(x)$: un clasificador, es decir, una regla que predice $0$ o $1$.
- $L_D(h)=\mathbb{P}\big(h(X)\neq Y\big)$: la pérdida (error) esperada del clasificador. Es la probabilidad de equivocarse (pérdida $0$-$1$).
- $h^\star$: la regla óptima de Bayes, definida como

$$
h^\star(x)=\begin{cases}1 & \text{si } \eta(x)\ge \tfrac{1}{2},\\[1mm] 0 & \text{si } \eta(x)<\tfrac{1}{2}.\end{cases}
$$

En palabras: predice la etiqueta más probable.

## Parte B: la igualdad (B)

Se prueba que

$$
L_D(h^\star)=\mathbb{E}_x\Big[\min\{\eta(x),\,1-\eta(x)\}\Big].
$$

**Paso 1: error en un punto fijo $x$.** Si fijamos $x$, la etiqueta real sigue siendo aleatoria:

- Si predecimos $1$, nos equivocamos cuando la etiqueta real es $0$. Eso ocurre con probabilidad $1-\eta(x)$.
- Si predecimos $0$, nos equivocamos cuando la etiqueta real es $1$. Eso ocurre con probabilidad $\eta(x)$.

**Paso 2: elegir la mejor predicción en ese $x$.** Para equivocarnos lo menos posible, elegimos la opción con **menor** probabilidad de error:

$$
\text{error mínimo en } x=\min\{\eta(x),\,1-\eta(x)\}.
$$

Esto es exactamente lo que hace $h^\star$:

- Si $\eta(x)\ge\tfrac{1}{2}$, predice $1$ y su error es $1-\eta(x)$, que es el menor de los dos.
- Si $\eta(x)<\tfrac{1}{2}$, predice $0$ y su error es $\eta(x)$, que de nuevo es el menor.

**Paso 3: promediar sobre todos los $x$.** Por la ley de la esperanza total:

$$
L_D(h^\star)=\mathbb{E}_x\Big[\mathbb{P}\big(h^\star(x)\neq Y\mid X=x\big)\Big]=\mathbb{E}_x\Big[\min\{\eta(x),\,1-\eta(x)\}\Big].
$$

Multiplicando por $2$ se obtiene la **igualdad (B)**:

$$
2\,\mathbb{E}_x\Big[\min\{\eta(x),\,1-\eta(x)\}\Big]=2\,L_D(h^\star).
$$

Aquí es donde se usa que $h^\star$ minimiza la pérdida esperada: como en **cada** $x$ escoge la mejor opción, ningún otro clasificador puede tener menor error promedio. ✓

## Parte A: la desigualdad (A)

Primero se prueba, **punto a punto**, que

$$
2\eta(1-\eta)\le 2\min\{\eta,\,1-\eta\},
$$

es decir, que se cumple para cada valor de $\eta\in[0,1]$. Después se toma esperanza.

**Paso 4: truco clave.** Para cualquier número $\eta\in[0,1]$, el producto se puede escribir como

$$
\eta(1-\eta)=\min\{\eta,\,1-\eta\}\cdot\max\{\eta,\,1-\eta\},
$$

porque $\eta$ y $1-\eta$ son justamente el mínimo y el máximo de ese par, en algún orden.

**Paso 5: acotar el máximo.** Como $\max\{\eta,1-\eta\}\le 1$ (ambos números son probabilidades), queda

$$
\eta(1-\eta)=\min\{\eta,\,1-\eta\}\cdot\max\{\eta,\,1-\eta\}\;\le\;\min\{\eta,\,1-\eta\}.
$$

**Paso 6: multiplicar por $2$ y tomar esperanza.** La esperanza preserva las desigualdades (si $a(x)\le b(x)$ para todo $x$, entonces $\mathbb{E}[a]\le\mathbb{E}[b]$):

$$
\mathbb{E}_x\Big(2\eta(x)\big(1-\eta(x)\big)\Big)\;\le\;2\,\mathbb{E}_x\Big(\min\{\eta(x),\,1-\eta(x)\}\Big).
$$

Esta es la **desigualdad (A)**. ✓

## Comprobación numérica

| $\eta$ | $2\eta(1-\eta)$ | $2\cdot\min\{\eta,\,1-\eta\}$ | ¿Se cumple $\le$? |
|:--|:--|:--|:--|
| 0 | 0 | 0 | Sí (igualdad) |
| 0,1 | 0,18 | 0,20 | Sí |
| 0,3 | 0,42 | 0,60 | Sí |
| 0,5 | 0,50 | 1,00 | Sí (mayor diferencia) |
| 0,9 | 0,18 | 0,20 | Sí |
| 1 | 0 | 0 | Sí (igualdad) |

La igualdad ocurre solo cuando $\eta\in\{0,1\}$, es decir, cuando no hay incertidumbre en la etiqueta. La brecha es mayor cuando $\eta=0{,}5$.

## Dos observaciones importantes

1. **Una precisión sobre la redacción.** La frase "$h^\star$ minimiza la pérdida esperada" justifica la **igualdad (B)**, no la desigualdad (A). La desigualdad (A) es puramente algebraica y se cumple para cualquier $\eta$. Por eso conviene separar ambas ideas al escribir el argumento.

2. **De dónde sale el $2\eta(1-\eta)$.** Es la probabilidad de que dos etiquetas independientes, ambas con probabilidad $\eta$ de ser $1$, **sean distintas**:

    $$
    \eta(1-\eta)+(1-\eta)\eta=2\eta(1-\eta).
    $$

    Esta cantidad aparece al analizar el error asintótico del clasificador de **$1$ vecino más cercano**. La cadena de desigualdades suele usarse para demostrar que su error está acotado por el doble del error de Bayes (resultado clásico de Cover y Hart, que también aparece en Shalev-Shwartz y Ben-David, capítulo 19; véase {doc}`referencias`).

## Conclusión

$$
\mathbb{E}_x\Big(2\eta(1-\eta)\Big)\;\le\;2\,\mathbb{E}_x\Big(\min\{\eta,\,1-\eta\}\Big)\;=\;2\,L_D(h^\star).\qquad\blacksquare
$$

:::{admonition} La expresión es correcta
La **igualdad** se debe a que $h^\star$ elige, en cada punto, la predicción con menor probabilidad de error.

La **desigualdad** se debe a que $\eta(1-\eta)=\min\cdot\max$ y el máximo nunca supera $1$.
:::
