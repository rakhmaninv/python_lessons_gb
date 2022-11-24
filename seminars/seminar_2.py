def t1():
    userstr = input()
    cop = len(userstr) * 60
    rub = cop // 100
    print(f'{rub} рублей {cop % 100} копеек')

def t2():
    print(len(input().split()))

def t3():
    userstr = list(input().split())
    c = 0
    print('коды: ', end='')
    for i in userstr:
        print(f'{i} = {c + ord(i)}, ', end='')

def t4():
    num = int(input())
    for i in range(num):
        print(-3**i, end='')

def t5():
    num = int(input())
    numlist = {}
    for i in range(1, num + 1):
        numlist[i] = 3 * i + 1
    print(numlist)

def t6():
    test = 'asdasdasdfa dsfrhger dsgsgsda'
    counter = test.count('s')
    print(counter)

