# a = 60
# b = 12


# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(a)

import random
a = random.randint(1, 50)
b = random.randint(1, 50)
c = [a, b]
print(c)
while max(a, b) % min(a, b) != 0:
    if a > b:
        a = a % b
    elif a < b:
        b = b % a
print(min(a, b))
