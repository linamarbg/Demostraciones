# Machine Learning: demostraciones

**Autores:** Lina Buelvas y Camilo Molina

Jupyter Book con las demostraciones de las notas del curso de Machine Learning (doctorado): vecino más cercano, regresión ridge y lasso/LARS, clasificación bayesiana, AdaBoost y regresión SVR.

## Contenido

| Archivo | Capítulo |
|:--|:--|
| `intro.md` | Portada e índice |
| `lema_21.md`, `lema_22.md` | Lemas 2.1 y 2.2 (1-NN) |
| `ridge.md` | Regresión ridge (3.4 y 3.12) |
| `lasso_lars.md` | Lasso y algoritmo LARS |
| `bayes_41.md` | Clasificador bayesiano (4.1) |
| `regla_optima_bayes.md` | Regla óptima de Bayes |
| `adaboost_53.md` | AdaBoost (5.3) |
| `svr_613.md` | Regresión SVR (6.13) |
| `apendice_codigo.md` | Verificación numérica (`lars_check.py`, `verificacion_numerica.py`) |
| `referencias.md` | Referencias |

## Cómo construir el libro

```bash
pip install -r requirements.txt     # jupyter-book 1.x
jupyter-book build .
```

El resultado queda en `_build/html/index.html`. La carpeta `_extra/mathjax` contiene una copia local de MathJax 3, así que las ecuaciones se ven también sin conexión a internet. Para publicarlo en GitHub Pages se copia `_build/html` en `docs/` (con un archivo `.nojekyll`).
