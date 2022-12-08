# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'АВЫВППабвРВ ОЫПВЗРЫВЗАР ВАЛОПЛРАПЫВА ВАПЗРЗЫВ ЫРабвПЗЫВРА ЫЗВАОЗЩРОКУ абв'
substr = 'абв'
print(text)
text_lst = text.split()
for i in text_lst:
    if substr in i:
        text_lst.remove(i)
print(' '.join(text_lst))