# Оптимизация СеМО

import numpy as np
 

def get_c(c, mu, b):
    return sum([c[i] * mu[i]**b[i] for i in range(5)])

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
        # закомментить, иначе будет больно глазам
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
        for i in range(L):
            u[Y][i] = (1 / mu[i]) * (s[Y-1][i] + 1)
        for i in range(L):
            summa = 0
            for j in range(L):
                summa += omega[j] * u[Y][j]
            s[Y][i] = omega[i] * u[Y][i] * Y / summa

    # вычисление остальных характеристик сети
    for i in range(L):
        w[i] = u[Q][i] - (1 / mu[i])
        b[i] = s[Q][i] * w[i] / u[Q][i]
        h[i] = s[Q][i] - b[i]
        lmbds[i] = h[i] * mu[i]

    return omega, u, w, b, s, h, lmbds

L = 5
N = 10 # число требований в сети

theta = np.array([
                [0, .2, .3, .4, .1],
                [.3, 0, .1, .2, .4],
                [.2, .2, 0, .3, .3],
                [.3, .2, .2, 0, .3],
                [.1, .4, .4, .1, 0]])

ans = []

c = [10, 5, 15, 10, 20]
b = [1, 1, 1, 1, 1]
c_opt = 100
lambda_ans, mu = get_mu(c_opt, L)
ans.append([lambda_ans, mu, get_c(c, mu, b)])

c = [15, 10, 20, 10, 20]
b = [1, 1, 2, 1, 1]
c_opt = 150
lambda_ans, mu = get_mu(c_opt, L)
ans.append([lambda_ans, mu, get_c(c, mu, b)])

c = [15, 10, 20, 15, 25]
b = [1, 2, 2, 1, 1]
c_opt = 200
lambda_ans, mu = get_mu(c_opt, L)
ans.append([lambda_ans, mu, get_c(c, mu, b)])

print('—' * 50)
[print(f'{i + 1}) Lambda = {ans[i][0]}\n\t mu* = {ans[i][1]}\n\t C = {ans[i][2]}') for i in range(3)]
print('—' * 50)