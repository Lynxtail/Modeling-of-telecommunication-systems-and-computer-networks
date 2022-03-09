from math import factorial as f

# система M/M/k/0 с двумя классами требований
# 32 — число радиоканалов
# 9 — инт-ть входящего потока 1
# 12 — инт-ть входящего потока 2
# 1 — инт-ть обслуживания

# стационарное распределение
# вероятность отказа хэндовер-вызову
# вероятность отказа новому вызову

k = 32
lambda_1 = 9
lambda_2 = 12
mu = 1

rho_1 = lambda_1/mu
rho_2 = lambda_2/mu
p = []
g = 16

p_0 = 1 / (sum([rho_1**n / f(n) for n in range(g+1)]) + \
        sum([rho_1**g * rho_2**(n-g) / f(n) for n in range(g+1, k+1)]))
p.append(p_0)

for n in range(1, k+1):
    if 1 <= n <= g:
        p.append((rho_1**n / f(n)) * p_0)
    if g + 1 <= n <= k:
        p.append((rho_1**g * rho_2**(n-g) / f(n)) * p_0)


print("Стационарное распределение:")
[print(f'p{p.index(item)} = {item:.3f}') for item in p]
print(f'Check: sum p = {sum(p)}')

b_1 = sum([(rho_1**g * rho_2**(n-g) / f(n)) for n in range(g, k+1)]) / \
        (sum([rho_1**n / f(n) for n in range(g+1)]) + \
        sum([(rho_1**g * rho_2**(n-g) / f(n)) for n in range(g+1, k+1)]))

b_2 = (rho_1**g * rho_2**(k - g) / f(k)) / (sum([rho_1**n / f(n) for n in range(g+1)]) + \
        sum([(rho_1**g * rho_2**(n-g) / f(n)) for n in range(g+1, k+1)]))
print(f'Вероятность потери вызова (новый): {b_1:.3f}')
print(f'Вероятность потери вызова (хэндовер): {b_2:.3f}')
