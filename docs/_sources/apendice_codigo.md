# Anexo: verificación numérica

Los resultados del libro se comprobaron con dos scripts de Python, incluidos en el repositorio.

**`lars_check.py`** verifica los resultados del {doc}`capítulo de lasso y LARS <lasso_lars>`: la umbralización suave en el caso ortogonal, el descenso por coordenadas y el algoritmo LARS con la modificación lasso, comparados con scikit-learn. Se ejecuta con `python lars_check.py` (requiere `numpy` y `scikit-learn`).

**`verificacion_numerica.py`** comprueba las demostraciones de los demás capítulos (requiere `numpy` y `scipy`):

| Capítulo | Qué se comprueba |
|:--|:--|
| {doc}`Lema 2.1 <lema_21>` | La identidad de $P(y\ne y')$ y la cota $2\eta(1-\eta)\le2\min\{\eta,1-\eta\}$ |
| {doc}`Lema 2.2 <lema_22>` | El valor esperado (simulación Monte Carlo) frente a la cota $r/(me)$ |
| {doc}`Ridge <ridge>` | El sesgo y el error cuadrático medio de (3.12), frente a una simulación |
| {doc}`Bayes 4.1 <bayes_41>` | Las formas lineal y cuadrática de $h(x)$ frente al cociente de densidades normales |
| {doc}`AdaBoost 5.3 <adaboost_53>` | $\alpha_i$ óptimo, $Z_i=2\sqrt{P_i(1-P_i)}$ y que los mal clasificados pesan $\tfrac12$ |
| {doc}`SVR 6.13 <svr_613>` | Primal y dual alcanzan el mismo valor, y $\hat\theta=\sum_n(\tilde\lambda_n-\lambda_n)x_n$ |

Salida del script:

```text
Lema 2.1  max |identidad|        = 1.1102230246251565e-16
Lema 2.1  2n(1-n) <= 2 min{n,1-n} = True
Lema 2.2  Monte Carlo = 0.0358  exacto = 0.0358  cota r/(m e) = 0.1104
Ridge     ECM Monte Carlo = 0.1532  formula (3.12) = 0.1531
Ridge     sesgo MC - formula = 0.0
Bayes 4.1 |h - (w'x + w0)|        = 4.961309141293668e-16
Bayes 4.1 |h - cuadratica|        = 4.440892098500626e-16
AdaBoost  alpha numerico = 0.4129  alpha_i = 0.4129
AdaBoost  Z = 0.920431  2 sqrt(P(1-P)) = 0.920431
AdaBoost  peso de mal clasificados = 0.5
SVR       primal = 5.568999  dual = 5.568999
SVR       theta primal = [ 1.5195 -1.8013]  theta desde el dual = [ 1.5195 -1.8013]
SVR       max lt*l (holgura complementaria) = 0.0
```
