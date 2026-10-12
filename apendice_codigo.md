# Apéndice: código de verificación numérica

El script `lars_check.py` verifica numéricamente los resultados del {doc}`capítulo 3 <03_lasso_lars>`: la umbralización suave en el caso ortogonal, el descenso por coordenadas y el algoritmo LARS con la modificación lasso, comparados con scikit-learn. Para reproducirlo basta con `python lars_check.py` (requiere `numpy` y `scikit-learn`).

## Código

```{literalinclude} lars_check.py
:language: python
:linenos:
```

## Salida

```{literalinclude} lars_check_salida.txt
:language: text
```
