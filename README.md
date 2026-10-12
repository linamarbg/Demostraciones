# Demostraciones de regresión ridge, lasso y regla óptima de Bayes

**Autores:** Lina Buelvas y Camilo Molina · **Curso:** Aprendizaje Automático (doctorado)

Jupyter Book con las demostraciones que las notas del curso dejan "para el lector" en la regresión ridge y lasso (secciones 3.4.2 y 3.5) y la verificación de la regla óptima de Bayes. Todas las fórmulas están en notación matemática.

## Libro en línea

Con GitHub Pages activado (véase abajo), el libro queda en `https://<usuario>.github.io/<repositorio>/`. También se puede abrir sin internet: `docs/index.html`.

## Contenido

| Archivo | Capítulo |
|:--|:--|
| `intro.md` | Portada |
| `01_verificaciones.md` | Verificaciones de la sección 3.4.2 |
| `02_ridge.md` | Propiedades del estimador ridge (3.12) |
| `03_lasso_lars.md` | Estimación lasso y algoritmo LARS |
| `04_bayes.md` | Verificación de la regla óptima de Bayes |
| `apendice_codigo.md` | Código de verificación numérica (`lars_check.py`) |
| `referencias.md` | Referencias |

## Estructura del repositorio

```
.
├── intro.md, 01_… 04_….md, apendice_codigo.md, referencias.md   # fuente del libro
├── _config.yml, _toc.yml                                        # configuración de Jupyter Book
├── _extra/mathjax/                                              # MathJax local (ecuaciones sin conexión)
├── lars_check.py, lars_check_salida.txt                         # verificación numérica de LARS
├── requirements.txt
├── word/                                                        # versiones en Word de las demostraciones
└── docs/                                                        # HTML del libro (lo que publica GitHub Pages)
```

## Publicar en GitHub Pages

1. Crear un repositorio vacío en GitHub y subir esta carpeta desde la terminal:

   ```bash
   git init -b main
   git add .
   git commit -m "Libro de demostraciones: ridge, lasso y Bayes"
   git remote add origin https://github.com/<usuario>/<repositorio>.git
   git push -u origin main
   ```

2. En el repositorio: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, carpeta `/docs` → Save**.

## Reconstruir el libro

```bash
pip install -r requirements.txt      # jupyter-book 1.x
jupyter-book build .
rm -rf docs && cp -r _build/html docs && touch docs/.nojekyll
```

`docs/.nojekyll` es necesario para que GitHub Pages sirva las carpetas que empiezan con guion bajo (`_static`, `_sources`).
