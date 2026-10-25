# Machine Learning: demostraciones

**Autores:** Lina Buelvas y Camilo Molina

**Curso:** Machine Learning (doctorado)

Este libro reúne las demostraciones de las notas del curso. Cada una se presenta igual: primero el **enunciado**, luego una serie de **pasos numerados**, y en cada paso se indica la propiedad que se usa. Todas las fórmulas están escritas en notación matemática y el final de cada demostración se marca con $\blacksquare$.

## Contenido

| Sección de las notas | Capítulo | Resultado que se demuestra |
|:--|:--|:--|
| 2 | {doc}`Lema 2.1 <lema_21>` | Cota del error esperado de 1-NN: $\mathbb{E}[L_{\mathcal D}(h_S)]\le 2L_{\mathcal D}(h^\star)+c\,\mathbb{E}\|x-x'\|$ |
| 2 | {doc}`Lema 2.2 <lema_22>` | Masa de las celdas no visitadas: $\mathbb{E}\big[\sum_{C_i\cap S=\emptyset}P(C_i)\big]\le r/(me)$ |
| 3.4 y 3.12 | {doc}`Regresión ridge <ridge>` | Estimador ridge, esperanza, covarianza, sesgo y error cuadrático medio |
| 3.5 | {doc}`Lasso y LARS <lasso_lars>` | Condiciones KKT, umbralización suave, descenso por coordenadas y LARS |
| 4.1 | {doc}`Clasificador bayesiano <bayes_41>` | Frontera cuadrática y frontera lineal para dos clases normales |
| 4 | {doc}`Regla óptima de Bayes <regla_optima_bayes>` | Desigualdad (A) e igualdad (B) para $L_{\mathcal D}(h^\star)$ |
| 5.3 | {doc}`AdaBoost <adaboost_53>` | Elección de $\theta_i$, $\alpha_i$ y actualización de pesos |
| 6.13 | {doc}`Regresión SVR <svr_613>` | Primal, Lagrangiano, dual de Wolfe y truco del núcleo |

El {doc}`anexo <apendice_codigo>` contiene la comprobación numérica de los resultados y las {doc}`referencias <referencias>` la bibliografía.

## Convenciones

- Las referencias del tipo (3.12), "sección 3.5" o "Ejercicio 1 de la sección 3.6" remiten a la numeración de las notas del curso (véase {doc}`referencias`).
- Los vectores y las matrices se escriben en negrita o con mayúscula ($\boldsymbol{\beta}$, $X$); $\hat{\boldsymbol{\beta}}$ denota un estimador.
- $\mathbb{E}$ es la esperanza, $\operatorname{Cov}$ la matriz de covarianza y $\operatorname{tr}$ la traza.
- Las notas contienen dos erratas de notación: en el desarrollo de $S_\lambda$ aparece $2\beta_0$ en lugar de $2\beta_0^\star$, y en (3.12) aparece $\operatorname{Cov}(\boldsymbol{\beta}_R)$ en lugar de $\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)$. En el libro se escriben corregidas.
