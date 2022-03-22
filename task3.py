import numpy as np


def stationary_distribution(omega, theta, eps):
    while np.linalg.norm(omega.dot(theta) - omega) > eps:
        omega = omega.dot(theta)
    return omega

# нормализующие константы
def get_G(L, N, x):
    G = np.zeros((N+1, L))
    for i in range(N + 1):
        G[i][0] = x[0]**i
    G[0] = [1]*L    
    for i in range(1, N + 1):
        for j in range(1, L):
            G[i][j] = G[i][j-1] + x[j] * G[i-1][j]
    return G

L = 9 # 8 M/M/1 + 1 M/M/N
N = 13 # число требований в сети
kappa = 13

mu = np.array([10, 100*kappa, 10000, 100000, 1000, 10000, 120000, 1500, 12000])

theta = np.array([
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, .5, .5, 0, 0, 0, 0],
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
G = get_G(L, N, x)
# вероятности что в системах m и более требований
p = np.zeros((N+1, L))
# вероятности что в системах ровно m требований
p_m = np.zeros((N+1,L))
# м.о. числа требований в системах
s = np.zeros(L)
# м.о. числа занятых приборов в системах
h = np.zeros(L)
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
    h[i] = x[i] * (G[N-1][L-1] / G[N][L-1])
    lmbds[i] = h[i] * mu[i]
    u[i] = s[i] / lmbds[i]

# математическое ожидание длительности пребывания требований в системах обслуживания
print('\n\nМ.о. длительности пребывания требований в системах:\n')
for i in range(L):
    print(f'Система {i + 1}: {u[i]}')