# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

check = 0
for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            if not (x or y or z) != (not x) and (not y) and (not z):
            # без скобок ошибка     ^
                check += 1
if check == 0:
    print('утверждение истинно')
else:
    print('утверждение ложно')