from pprint import pprint
import numpy as np
from decimal import *

def stationary_distribution(omega, theta, eps):
    while np.linalg.norm(omega.dot(theta) - omega) > eps:
        omega = omega.dot(theta)
    return omega

def get_A(kappa, L, N):
    A = np.ones((L, N + 1))
    for i in range(L):
        for m in range(1, N):
            tmp = 1
            for l in range(1, m + 1):
                tmp *= min(l, kappa[i]) 
            A[i][m] = tmp
    return A

# нормализующие константы
def get_G(L, N, x):
    G = np.zeros((N+1, L))
    for i in range(N + 1):
        G[i][0] = x[0]**i
    G[0] = [1]*L    
    for i in range(1, N + 1):
        for j in range(1, L):
            # изменения для системы вида M/M/N
            if j == 1:
                G[i][j] = G[i][j-1] + x[j]**i / A[j][i] * G[i-1][j]
            else:
                G[i][j] = G[i][j-1] + x[j] * G[i-1][j]
    return G

L = 9 # 8 M/M/1 + 1 M/M/N
N = 13 # число требований в сети
kappa = np.ones(L)
kappa[1] = N

# нормальное
mu = np.array([10, 100, 10000, 100000, 1000, 10000, 120000, 1500, 12000])
# моё
mu = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10])

theta = np.array([
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, .5, 0, 0, .5, 0, 0],
                [0, 0, 0, 0, .08, .92, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, .05, .95],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0]])

# нахождение вектора omega
omega = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0])
eps = 0.0001
omega = stationary_distribution(omega, theta, eps)
print(f'Omegas: {omega},\nCheck (~1): {sum(omega)}')

x = omega / mu 
print(f'x = {x}')
A = get_A(kappa, L, N)
print(f'A = ')
pprint(A)
G = get_G(L, N, x)
print(f'G = ')
pprint(G)
# вероятности что в системах m и более требований
p = np.zeros((N+1, L))
# вероятности что в системах ровно m требований
p_m = np.zeros((N+1,L))
# м.о. числа требований в системах
s = np.zeros(L)
# м.о. числа занятых приборов в системах
h = np.zeros(L, dtype=Decimal)
# интенсивности входного потока требований в системах
lmbds = np.zeros(L)
# м.о. длительности пребывания требований в системах
u = np.zeros(L)

for i in range(N + 1):
    for j in range(L):
        p[i][j] = x[j]**i * (G[N-i][L-1] / G[N][L-1])

for i in range(N + 1):
    for j in range(L):
        p_m[i][j] = (x[j]**i / G[N][L-1]) * (G[N-i][L-1] - x[j] * G[N-i-1][L-1])

for i in range(L):
    for j in range(1, N + 1):
        s[i] += x[i]**j * (G[N-j][L-1] / G[N][L-1])
    getcontext().prec = 50
    h[i] = Decimal(x[i]) * (Decimal(G[N-1][L-1]) / Decimal(G[N][L-1]))
    lmbds[i] = h[i] * mu[i]
    u[i] = s[i] / lmbds[i]
print(f'lambdas = {lmbds}')
# математическое ожидание длительности пребывания требований в системах обслуживания
print('\n\nМ.о. длительности пребывания требований в системах:\n')
for i in range(L):
    print(f'Система {i + 1}: {u[i]}')