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
lambda_ = lambda_1 + lambda_2
mu = 1

rho = lambda_/mu
p = []
for n in range(k+1):
    p.append((rho**n / f(n)) / (sum([rho**i / f(i) for i in range(k+1)])))

print("Стационарное распределение:")
[print(f'p{p.index(item)} = {item:.3f}') for item in p]
print(f'Check: sum p = {sum(p)}')

print(f'Вероятность потери вызова (и хэндовер, и новый): {p[-1]:.3f}')
