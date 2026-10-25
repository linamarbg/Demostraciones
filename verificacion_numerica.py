"""Comprobación numérica de las demostraciones del libro (numpy y scipy)."""
import numpy as np
from scipy.optimize import minimize
from scipy.stats import multivariate_normal as mvn

rng = np.random.default_rng(1)

# Lema 2.1: identidad P(y != y') y cota 2 eta (1-eta) <= 2 min(eta, 1-eta)
e, e2 = rng.random(1000), rng.random(1000)
lhs = e2 * (1 - e) + (1 - e2) * e
rhs = 2 * e * (1 - e) + (e - e2) * (2 * e - 1)
print("Lema 2.1  max |identidad|        =", np.abs(lhs - rhs).max())
print("Lema 2.1  2n(1-n) <= 2 min{n,1-n} =", bool(np.all(2*e*(1-e) <= 2*np.minimum(e, 1-e) + 1e-15)))

# Lema 2.2: Monte Carlo de E[suma de P(C_i) de celdas vacias] frente a r/(m e)
r, m, N = 6, 20, 200000
P = rng.dirichlet(np.ones(r))
cells = rng.choice(r, size=(N, m), p=P)
mc = sum(P[i] * (~(cells == i).any(1)).mean() for i in range(r))
print(f"Lema 2.2  Monte Carlo = {mc:.4f}  exacto = {sum(P*(1-P)**m):.4f}  cota r/(m e) = {r/(m*np.e):.4f}")

# Ridge: sesgo y ECM con las formulas del capitulo
n, p, lam, s2 = 40, 4, 2.0, 1.5
X = rng.normal(size=(n, p)); X -= X.mean(0); X /= X.std(0)
beta = rng.normal(size=p)
A = X.T @ X + lam * np.eye(p); Ai = np.linalg.inv(A)
l = np.linalg.eigvalsh(X.T @ X)
Y = X @ beta + np.sqrt(s2) * rng.normal(size=(200000, n))
bh = Y @ X @ Ai
ecm_mc = ((bh - beta) ** 2).sum(1).mean()
ecm_f = s2 * (l / (l + lam) ** 2).sum() + lam**2 * beta @ Ai @ Ai @ beta
print(f"Ridge     ECM Monte Carlo = {ecm_mc:.4f}  formula (3.12) = {ecm_f:.4f}")
print("Ridge     sesgo MC - formula =", np.abs(bh.mean(0) - beta + lam * Ai @ beta).max().round(3))

# Bayes 4.1: h(x) lineal y cuadratica
pp = 3
m1, m2 = rng.normal(size=pp), rng.normal(size=pp)
M = rng.normal(size=(pp, pp)); S = M @ M.T + np.eye(pp); Si = np.linalg.inv(S)
x = rng.normal(size=pp)
h = np.log(mvn.pdf(x, m1, S) / mvn.pdf(x, m2, S))
w, w0 = Si @ (m1 - m2), 0.5 * (m2 @ Si @ m2 - m1 @ Si @ m1)
print("Bayes 4.1 |h - (w'x + w0)|        =", abs(h - (w @ x + w0)))
S1 = M @ M.T + np.eye(pp); B = rng.normal(size=(pp, pp)); S2 = B @ B.T + np.eye(pp)
h = mvn.logpdf(x, m1, S1) - mvn.logpdf(x, m2, S2)
Q1 = (x-m1) @ np.linalg.inv(S1) @ (x-m1); Q2 = (x-m2) @ np.linalg.inv(S2) @ (x-m2)
print("Bayes 4.1 |h - cuadratica|        =", abs(h - 0.5*(Q2 - Q1 - np.log(np.linalg.det(S1)/np.linalg.det(S2)))))

# AdaBoost: alpha_i, Z_i y peso de mal clasificados
N = 50
y = rng.choice([-1, 1], N); phi = np.where(rng.random(N) < 0.3, -y, y)  # error aprox. 30 %
w = rng.random(N); w /= w.sum()
Pi = w[y * phi == -1].sum(); al = 0.5 * np.log((1 - Pi) / Pi)
J = lambda a: (w * np.exp(-a * y * phi)).sum()
g = np.linspace(-3, 3, 60001)
print(f"AdaBoost  alpha numerico = {g[np.argmin([J(a) for a in g])]:.4f}  alpha_i = {al:.4f}")
print(f"AdaBoost  Z = {J(al):.6f}  2 sqrt(P(1-P)) = {2*np.sqrt(Pi*(1-Pi)):.6f}")
print("AdaBoost  peso de mal clasificados =", (w * np.exp(-al*y*phi) / J(al))[y*phi == -1].sum().round(6))

# SVR: primal y dual alcanzan el mismo valor, y theta = sum (lt - l) x
n = 25
X = rng.normal(size=(n, 2)); yy = X @ [1.5, -2] + 0.3 + 0.4 * rng.normal(size=n)
C, eps = 1.0, 0.2
f = lambda v: .5 * v[:2] @ v[:2] + C * v[3:].sum()
cons = [{'type': 'ineq', 'fun': lambda v: eps + v[3+n:] - (yy - X@v[:2] - v[2])},
        {'type': 'ineq', 'fun': lambda v: eps + v[3:3+n] - (X@v[:2] + v[2] - yy)}]
bnd = [(None, None)] * 3 + [(0, None)] * (2*n)
pr = minimize(f, np.zeros(3+2*n), constraints=cons, bounds=bnd, method='SLSQP', options={'maxiter': 1000, 'ftol': 1e-12})
dual = lambda u: -(-.5 * ((u[:n]-u[n:]) @ X) @ ((u[:n]-u[n:]) @ X) + yy @ (u[:n]-u[n:]) - eps * u.sum())
du = minimize(dual, np.zeros(2*n), bounds=[(0, C)]*(2*n),
              constraints=[{'type': 'eq', 'fun': lambda u: (u[:n]-u[n:]).sum()}],
              method='SLSQP', options={'maxiter': 1000, 'ftol': 1e-12})
d = du.x[:n] - du.x[n:]
print(f"SVR       primal = {pr.fun:.6f}  dual = {-du.fun:.6f}")
print("SVR       theta primal =", pr.x[:2].round(4), " theta desde el dual =", (X.T @ d).round(4))
print("SVR       max lt*l (holgura complementaria) =", np.abs(du.x[:n]*du.x[n:]).max())
