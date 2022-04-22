# Оптимизация СеМО

import numpy as np
 

def get_c(c, mu, b):
    return sum([c[i] * mu[i]**b[i] for i in range(5)])

# 2.8
def get_mu(L, N, c, b, alpha, c_opt):
    ans = []
    for j in range(L):
        tmp_1 = (c_opt / c[j]) * c[j] ** (N / (N + b[0])) * alpha[j] ** (N * b[0] / (N + b[0]))
        tmp_2 = sum([c[i] ** (N / (N + b[0])) * alpha[i] ** (N * b[0] / (N + b[0])) for i in range(L)])
        ans.append((tmp_1 / tmp_2) ** (1 / b[0]))
    return ans

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
# print(alpha)

c_first = [10, 5, 15, 10, 20]
b = [1, 1, 1, 1, 1]
c_opt = 100

print(f'mu = {get_mu(L, N, c_first, b, alpha, c_opt)}')
print(f'C = {get_c(c_first, get_mu(L, N, c_first, b, alpha, c_opt), b)} <= C* = {c_opt}')