
def fib1(n):
    assert n>=0
    return n if n<=1 else fib1(n-1)+fib1(n-2)

print(fib1(8))

#print(fib1(80))
def old_fib1(n):
    assert n>=0
    return n if n<=1 else old_fib1(n-1)+old_fib1(n-2)

cache = {}

def fib2(n):
    assert n>=0
    if n not in cache:
        cache[n]=n if n<=1 else fib2(n-1) +fib2(n-2)
    return cache[n]

print(fib2(8))
print(fib2(80))
print(fib2(800))


def memo(f): # декоратор
    cache = {}
    def inner(n): # Обертка
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner

fib1 = memo(fib1) # Переопределяем старую медленную ф-ю
print(fib1(80))

from functools import lru_cache

fib1 = lru_cache(maxsize=None)(fib1) # тот же memo, но из стандартной библиотеки
print(fib1(80))

# print(fib1(8000))#error maximum recursion depth exceeded in comparison

def fib3(n): # fuck recursion, делаем через итерации
    assert n>=0
    f0,f1 = 0,1
    for i in range(n-1):
        f0,f1 = f1,f0+f1
    return f1

print(fib3(8))
print(fib3(8000))

# измерение времени работы функции

import time

def timed(f, *args, n_iter=100):
    accumulator = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)            # Измеряем время работы в-и f на аргументах *args
        t1 = time.perf_counter()
        accumulator = min(accumulator,t1-t0)
    return accumulator

a=timed(fib3,800)
print(a," seconds")

from matplotlib import pyplot as plt

def compare(fs,args):
    for f in fs:
        plt.plot(args,[timed(f,arg) for arg in args],label = f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

compare([old_fib1,fib3],list(range(20)))