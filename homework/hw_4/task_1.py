# Вычислить число c заданной точностью d
# Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

while True:
    epsilon = float(input('введите необходимую точность: '))
    if epsilon <= 0.1 and epsilon >= 0.0000000001:
        break
    else:
        print('минимум: 0.1, максимум: 0.0000000001')

# вычисление пи рядами Лейбница: pi= 4/1 - 4/3 + 4/5 - 4/7 + 4/9 ...
pi = 0
step = 1
sign = 1
while True:
    term = 4 / step
    pi += term * sign
    if term < epsilon:
        break
    sign = -sign
    step += 2
print(pi)