from math import factorial as f

# система M/M/k/0
# 600 байт — м.о. длины сообщения
# 2.3 сообщ/сек — инт-ть входящего потока
# 1024 байт/сек — инт-ть обслуживания

k = 4 # число каналов
lambda_ = 2.3*600
mu = 1024

ro = lambda_/mu
p = []
for n in range(k+1):
    p.append((ro**n / f(n)) / (sum([ro**m / f(m) for m in range(k+1)])))

print("Стационарное распределение:")
[print(f'p{p.index(item)} = {item:.3f}') for item in p]
print(f'Check: sum p = {sum(p)}')

h = sum([i * p[i] for i in range(k+1)]) + k * sum([p[i] for i in range(k+1, len(p))])
print(f'Математическое ожидание числа занятых приборов: {h:.3f}')

print(f'Вероятность потери сообщения: {p[-1]:.3f}')