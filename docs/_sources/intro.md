# Demostraciones de regresión ridge, lasso y regla óptima de Bayes

**Autores:** Lina Buelvas y Camilo Molina

**Curso:** Aprendizaje Automático (doctorado)

## Qué contiene este libro

Este libro reúne, en un solo documento, las demostraciones que las notas del curso dejan "para el lector" en la regresión ridge y lasso, y la verificación de la regla óptima de Bayes. Cada capítulo es autocontenido y todas las fórmulas están escritas en notación matemática.

| Capítulo | Contenido |
|:--|:--|
| {doc}`1. Verificaciones de la sección 3.4.2 <01_verificaciones>` | $Z^T\mathbf{1}=\mathbf{1}^TZ=\mathbf{0}$ y las igualdades (3.11) ("verifíquelo", "verifíquelas") |
| {doc}`2. Propiedades del estimador ridge <02_ridge>` | Esperanza, covarianza, sesgo y error cuadrático medio, ecuación (3.12) (ejercicio de la sección 3.4.2) |
| {doc}`3. Estimación lasso y LARS <03_lasso_lars>` | Condiciones KKT, umbralización suave, descenso por coordenadas y algoritmo LARS (ejercicio de la sección 3.5) |
| {doc}`4. Regla óptima de Bayes <04_bayes>` | Desigualdad (A) e igualdad (B) para la pérdida esperada $L_D(h^\star)$ |
| {doc}`Apéndice: código <apendice_codigo>` | Script en Python de la verificación numérica de LARS y su salida |
| {doc}`Referencias <referencias>` | Bibliografía |

## Convenciones

- Las referencias del tipo (3.12), "sección 3.5" o "Ejercicio 1 de la sección 3.6" remiten a la numeración de las notas del curso (véase {doc}`referencias`).
- Los vectores y las matrices se escriben en negrita o con mayúscula ($\boldsymbol{\beta}$, $X$); $\hat{\boldsymbol{\beta}}$ denota un estimador.
- $\mathbb{E}$ es la esperanza, $\operatorname{Cov}$ la matriz de covarianza, $\operatorname{tr}$ la traza y $\blacksquare$ marca el final de una demostración.
- Se señalan dos erratas de notación de las notas: en el desarrollo de $S_\lambda$ aparece $2\beta_0$ en lugar de $2\beta_0^\star$ (capítulo 1), y en (3.12) aparece $\operatorname{Cov}(\boldsymbol{\beta}_R)$ en lugar de $\operatorname{Cov}(\hat{\boldsymbol{\beta}}_R)$ (capítulo 2).
