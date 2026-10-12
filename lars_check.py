"""Verificación numérica: LARS con modificación lasso, descenso por coordenadas y soft-thresholding."""
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, lars_path


def lars_lasso(X, y, tol=1e-12):
    """Camino lasso exacto por LARS. Columnas de X con norma 1 y y centrada.
    Devuelve lista de (C, beta, n_drops): C = max|x_j^T r| en cada nudo (lambda = 2C)."""
    n, p = X.shape
    beta = np.zeros(p)
    c = X.T @ y
    active = [int(np.argmax(np.abs(c)))]
    knots = []
    drops = 0
    for _ in range(10 * p):
        C = np.max(np.abs(c))
        knots.append((C, beta.copy()))
        if C < 1e-10:
            break
        XA = X[:, active]
        s = np.sign(c[active])
        Ginv_s = np.linalg.solve(XA.T @ XA, s)
        A = 1.0 / np.sqrt(s @ Ginv_s)
        w = A * Ginv_s                      # direccion de los coeficientes activos
        u = XA @ w                          # vector equiangular (norma 1)
        a = X.T @ u
        inactive = [k for k in range(p) if k not in active]
        gamma, new = C / A, None            # si no hay inactivas: se llega a OLS
        for k in inactive:
            for g in ((C - c[k]) / (A - a[k]), (C + c[k]) / (A + a[k])):
                if tol < g < gamma:
                    gamma, new = g, k
        drop = None
        for i, j in enumerate(active):      # modificacion lasso: cruce por cero
            g = -beta[j] / w[i]
            if tol < g < gamma:
                gamma, drop, new = g, j, None
        beta[active] += gamma * w
        c = X.T @ (y - X @ beta)
        if drop is not None:
            beta[drop] = 0.0
            active.remove(drop)
            drops += 1
        elif new is not None:
            active.append(new)
        else:
            knots.append((np.max(np.abs(c)), beta.copy()))
            break
    return knots, drops


def soft(z, t):
    return np.sign(z) * np.maximum(np.abs(z) - t, 0.0)


def cd_lasso(X, y, lam, iters=5000):
    """Descenso por coordenadas para ||y-Xb||^2 + lam*|b|_1 con sum x_ij^2 = n."""
    n, p = X.shape
    b = np.zeros(p)
    for _ in range(iters):
        for j in range(p):
            r = y - X @ b + X[:, j] * b[j]
            b[j] = soft(X[:, j] @ r / n, lam / (2 * n))
    return b


# ---------- 1) Orto-normal: soft-thresholding vs ridge ----------
rng = np.random.default_rng(0)
n, p = 200, 5
Q, _ = np.linalg.qr(rng.normal(size=(n, p)))
Xo = np.sqrt(n) * Q                     # X^T X = n I
yo = Xo @ np.array([3.0, -2.0, 0.5, 0.0, 0.0]) + rng.normal(size=n)
yo -= yo.mean()
lam = 150.0
b_ols = Xo.T @ yo / n
b_soft = soft(b_ols, lam / (2 * n))
b_sk = Lasso(alpha=lam / (2 * n), fit_intercept=False, tol=1e-12, max_iter=100000).fit(Xo, yo).coef_
b_ridge = np.linalg.solve(Xo.T @ Xo + lam * np.eye(p), Xo.T @ yo)
print("1) ortonormal  max|soft - sklearn| =", np.abs(b_soft - b_sk).max())
print("   ridge = ols*n/(n+lam):", np.allclose(b_ridge, b_ols * n / (n + lam)))

# ---------- 2) Descenso por coordenadas (columnas con sum x^2 = n) ----------
X = load_diabetes().data
X = X - X.mean(0)
X = X / np.linalg.norm(X, axis=0)       # norma 1
y = load_diabetes().target
y = y - y.mean()
Xn = X * np.sqrt(len(y))                # sum x_ij^2 = n
lam = 2 * 0.15 * np.abs(X.T @ y).max()
b_cd = cd_lasso(Xn, y, lam)
b_sk = Lasso(alpha=lam / (2 * len(y)), fit_intercept=False, tol=1e-12, max_iter=100000).fit(Xn, y).coef_
print("2) coord. descent max|cd - sklearn| =", np.abs(b_cd - b_sk).max())

# ---------- 3) LARS-lasso vs sklearn.lars_path ----------
knots, drops = lars_lasso(X, y)
alphas, _, coefs = lars_path(X, y, method="lasso")
mine = np.array([b for _, b in knots]).T
Cs = np.array([C for C, _ in knots])
print("3) LARS-lasso: nudos propios =", mine.shape[1], " sklearn =", coefs.shape[1], " cruces por cero =", drops)
if mine.shape[1] == coefs.shape[1]:
    # en sklearn, alpha = C / n  (lambda = 2C en la escala de columnas con norma 1)
    print("   max|C - n*alpha| =", np.abs(Cs - alphas * len(y)).max())
    print("   max|beta - beta_sklearn| =", np.abs(mine - coefs).max())

# KKT en cada nudo: |2 x_j^T r| = lam para activas (con signo), <= lam para inactivas
viol = 0.0
for C, b in knots:
    g = 2 * X.T @ (y - X @ b)
    lam_k = 2 * C
    act = b != 0
    viol = max(viol, np.abs(g[act] - lam_k * np.sign(b[act])).max() if act.any() else 0,
               max(0.0, (np.abs(g[~act]) - lam_k).max()) if (~act).any() else 0)
print("   violacion maxima de KKT en los nudos =", viol)
