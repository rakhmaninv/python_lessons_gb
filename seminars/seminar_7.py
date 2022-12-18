def t1():
    print('C:\\WINDOWS\\System32\\drivers\\etc\\nst')

def t2():
# a = [4, 3, -10, 1, 7, 12]a=[4, -10, 12, 3, 1, 7]
    return 0

def t3():
    print(sum(map(lambda x: x*x, filter(lambda x: x % 9 == 0, [i for i in range(10, 100)]))))

def t4():
    triangle = (4,3,2)
    print((lambda a: a[0] + a[1] > a[2] )(sorted(triangle)))