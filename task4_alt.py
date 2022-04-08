# Оптимизация СеМО

# АЛГОРИТМ

# 1
# вычислить:
# составляющие mu_1 по 2.8
# компоненты c_1 по 5.1 при mu = mu_1
# составляющие mu_2 при c = c_1 по 2.8
# производиельности сети lambda_1 = lambda_(mu_1) и lambda_2 = lambda_(mu_2) при исходных c_first

# 2
# если (lambda_1 - lambda_2) / lambda_1 < delta,
# то mu_opt = mu_1 и конец
# иначе Z = mu_1

# 3
# вычислить e_i = c[i] * z_i ** (b - 1) * sqrt(sum([(c[j] * z_j ** (b - 1)) ** 2 for j in range(1, L + 1)]))
# найти mu_3 = 2 * Z - mu_2
# вычислить mu_4_i = mu_3_i + e_i * sum([e_j * (z_j - mu_3_j) for j in range(1, L + 1)])
# построить mu_5 = Z + (mu_4 - Z) * abs(mu_3 - Z) / abs(mu_4 - Z)
# и mu_6 = mu_5 * (c_opt * sum([(c[i] * mu_5_i) ** b for i in range(1, L + 1)])) ** (1 / b)
# удовлетворяющие условиям 2.3
# вычислить:
# компоненты c_6 по 5.1 при mu = mu_6
# составляющие mu_2 при c = c_6, lambda_2 = lambda_(mu_2) при исходных c_first по 2.8
# mu_2 = mu_6 + mu_2 - mu_1

# 4
# если (lambda_1 - lambda_2) / lambda_1 > delta,  
# то Z = mu_6 и перейти к 3
# иначе mu_opt = mu_6 и конец

import numpy as np
 

def get_c(c, mu, b):
    return sum([c[i] * mu[i]**b[i] for i in range(5)])

# 2.8
def get_mu(L, N, c, b, alpha):
    ans = []
    for j in range(L):
        tmp_1 = (c_opt / c[j]) * c[j] ** (N / (N + b)) * alpha(j) ** (N * b / (N + b))
        tmp_2 = sum([c[i] ** (N / (N + b)) * alpha(i) ** (N * b / (N + b)) for i in range(L)])
        ans.append((tmp_1 / tmp_2) ** (1 / b))
    return ans

# 5.1
# частные производные??
# а надо ли вообще пересчитывать c?..
def get_c(L, c_opt, lambda_, mu, b):
    ans = []
    for j in range(L):
        ans.append(c_opt * (d lambda_ / d mu[i]) / sum([mu[i] ** (b - 1) * mu[j] * (d lambda_ / d mu[j]) for i in range(L)]))
    return ans

# подсчёт пропускной способности сети
def get_lambda():
    pass


# входные данные
L = 5 # число систем
N = 10 # число требований в сети

theta = np.array([
                [0, .2, .3, .4, .1],
                [.3, 0, .1, .2, .4],
                [.2, .2, 0, .3, .3],
                [.3, .2, .2, 0, .3],
                [.1, .4, .4, .1, 0]])

# коэффы передачи
alpha = [1] + [0] * (L - 1)
for j in range(1, L):
    alpha[j] = (sum([theta[i][j] * alpha[i] for i in range(L)]))
print(alpha)

c_first = [10, 5, 15, 10, 20]
b = [1, 1, 1, 1, 1]
c_opt = 100
