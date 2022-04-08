# СеМО с управлением

import numpy as np


def get_mu(c_opt, L):
    mu = [.01] * L
    h = 0.01
    index = 0
    lambda_ans = 0.
    lambda_ans_past = -1
    while lambda_ans < c_opt and lambda_ans > lambda_ans_past:
        # !!!!
        # заменить на перераспределение мю
        mu[index % L] += h
        index += 1
        lambda_ans_past = lambda_ans
        # пропускная способность сети
        *_, lmbds = recurrent_method(mu, N, theta, L)
        lambda_ans = sum(lmbds)
        print(f'mu = {mu}')
        print(f'Lambda_old = {lambda_ans_past}, Lambda_new = {lambda_ans}')
    return lambda_ans, mu

def stationary_distribution(omega, theta, eps):
    while np.linalg.norm(omega.dot(theta) - omega) > eps:
        omega = omega.dot(theta)
    return omega

def recurrent_method(mu, Q, theta, L):
    # нахождение вектора omega
    omega = np.zeros(L)
    omega[0] = 1
    eps = 0.0001
    omega = stationary_distribution(omega, theta, eps)
    # print(f'Omegas: {omega},\nCheck (~1): {sum(omega)}')
    
    # м.о. числа требований в системах
    s = np.zeros((Q+1, L))
    # м.о. длительности пребывания требований в системах
    u = np.zeros((Q+1, L))
    # м.о. длительности ожидания требований в очереди системы
    w = np.zeros(L)
    # м.о. числа требований, ожидающих обслуживание в очереди системы
    b = np.zeros(L)
    # м.о. числа занятых приборов в системах
    h = np.zeros(L)
    # интенсивность входящего потока требований в системы
    lmbds = np.zeros(L)
    
    # м.о. длительности пребывания требований в системах и м.о. числа требований в системах
    for Y in range(1, Q + 1):
        for i in range(L - 1):
            u[Y][i] = (1 / mu[i]) * (s[Y-1][i] + 1)
        for i in range(L - 1):
            summa = 0
            for j in range(L):
                summa += omega[j] * u[Y][j]
            s[Y][i] = omega[i] * u[Y][i] * Y / summa

    # вычисление остальных характеристик сети
    for i in range(L - 1):
        w[i] = u[Q][i] - (1 / mu[i])
        b[i] = s[Q][i] * w[i] / u[Q][i]
        h[i] = s[Q][i] - b[i]
        lmbds[i] = h[i] * mu[i]

    return omega, u, w, b, s, lmbds

# м.о. длительности пребывания требований в подсети N (S_1 - S_5)
def get_tau(lmbds, u, L, lambda_L):
    for i in range(L - 1):
        tau += lmbds[i] * u[i]
    tau /= lambda_[L]

# м.о. числа требований в подсети N (S_1 - S_5)
def get_s_N(lmbds, s, L):
    for i in range(L - 1):
        s_N += lmbds[i] * s[i]
    # s_N /= lmbds[L]

def get_lambda_L():
    lambda_L = [0] * L
    for item in lambda_L:
        while get_tau(lmbds, u, L, item) <= T:
            # подбор значения lambda_6 для каждого k = 1, ... 10

L = 6 # 5 смо + 1 управляющая
N = 10 # число требований в сети
с = 0 # предельное значение lambda_6

theta = np.array([
                [0, .5, .5, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, .7, 0, 0, .3, 0],
                [.2, 0, 0, 0, 0, .8],
                [0, 0, 1, 0, 0, 0]])

mu = [1, 1, 1, 1, 1]
T = 4

mu = [2, 1, 1, 2, 1]
T = 5

mu = [2, 1, 2, 2, 2]
T = 3