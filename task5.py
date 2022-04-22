# СеМО с управлением

import numpy as np


def get_prod(k, lambda_, mu, N):
    tmp = 1
    for l in range(k):
        tmp *= lambda_[N - l] / mu[l + 1]
    return tmp

def get_p_0(lambda_, mu, N):
    return (1 + sum([get_prod(k, lambda_, mu) for k in range(N)])) ** (-1)

def get_p(k, lambda_, mu, N):
    return get_prod(k, lambda_, mu) * get_p_0(lambda_, mu, N)

def get_tau(N, mu, p):
    tmp1 = sum([p[k - 1] * k for k in range(1, N + 1)])
    tmp2 = sum([p[k - 1] * mu[k - 1] for k in range(1, N + 1)])
    return tmp1 / tmp2

def get_rho(k, c, mu):
    tmp = 1
    for l in range(k):
        tmp *= c / mu[l - 1]
    return tmp

def get_lambda_6(k, L, N, c, mu, T):
    # 2 <= L <= N — число пакетов?
    # mu_L — что за зверь?
    if N - L + 2 <= k <= N:
        ans = c
    elif 1 <= k <= N - L:
        ans = 0
    elif k == N - L + 1:
        ans = 1 / (L / mu[6] - T) * \
            sum([(mu[6] * T - l) * get_rho(l, c, mu) / get_rho(L - 1, c, mu) for l in range(1, L)])
    return ans

S = 6 # 5 смо + 1 управляющая
sub_S = S - 1 # подсеть
kappa = [1, 1, 1, 1, 1, 1]
N = 10 # число требований в сети
с = 0 # предельное значение lambda_6

theta = np.array([
                [0, .5, .5, 0, 0, 0],
                [0, 0, 0, 0, 0, 1],
                [0, .7, 0, 0, .3, 0],
                [.2, 0, 0, 0, 0, .8],
                [0, 0, 0, 1, 0, 0]
                [0, 0, 1, 0, 0, 0]])

mu = [1, 1, 1, 1, 1]
T = 4

