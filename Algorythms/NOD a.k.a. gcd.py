

import random

def test(gcd, n_iter = 100): # Проверка функции на корректность
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c*random.randint(0, 128)
        b = c*random.randint(0,128)
        assert gcd(a,a) == gcd(a,0) ==a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a,1) == gcd(b,1) ==1
        d = gcd(a,b)
        assert a % d == b % d == 0


def gcd1(a,b): # линейная сложность
    assert a>=0 and b>=0
    for d in reversed(range(max(a, b)+1)): # от макс+1 до нуля
        if d == 0 or a%d == b%d ==0:
            return d

print(test(gcd1),gcd1(8,3), gcd1(8,0), gcd1(0,0), gcd1(16,24))


def gcd2(a,b): # алгоритм Евклида
    assert a >= 0 and b >= 0
    while a and b: # !=0
        if a>=b:
            a%=b
        else:
            b%=a
    return max(a,b)

print(test(gcd2), gcd2(100000000000,1000000000000000000))


def gcd3(a,b): # gcd2 через рекурсию
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a,b)
    elif a>=b:
        return gcd3(a%b,b)
    else:
        return gcd3(a,b%a)

print(test(gcd3),gcd3(24,9), gcd3(100000000000,1000000000000000000))

def gcd4(a,b):
    assert a >= 0 and b >= 0
    if a ==0 or b == 0:
        return max(a,b)
    return gcd4(b%a,a)