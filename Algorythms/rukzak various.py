#line = input()
#
# аналог (быстрее):
#import sys
#line1=next(sys.stdin)
"""
import sys

def fractional_knapsack(capacity, values_and_weights):
    order = [(v/w,w) for v,w in values_and_weights]
    order.sort(reverse=True)

    acc = 0
    for v_per_w,w in order:
        if w < capacity:
            acc+=v_per_w*w
            capacity-=w
        else:
            acc += v_per_w * capacity
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin) #генератор
    n, capacity = next(reader)# считываем строку, запрашивая следующий элемент из генератора
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity,values_and_weights)
    print("{:.3f}".format(opt_value))

if __name__ == "__main__":
    main()
"""

# solution #2
# без сортировки. используем двоичную кучу

import heapq
import sys

def fractional_knapsack(capacity, values_and_weights):
    order = [(-v/w,w) for v,w in values_and_weights]
    heapq.heapify(order) #minheap

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w,capacity)
        acc -= v_per_w*can_take
        capacity -= can_take
    return acc

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin) #генератор
    n, capacity = next(reader)# считываем строку, запрашивая следующий элемент из генератора
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity,values_and_weights)
    print("{:.3f}".format(opt_value))

import time
def timed(f, *args, n_iter=100):
    accumulator = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)  # Измеряем время работы в-и f на аргументах *args
        t1 = time.perf_counter()
        accumulator = min(accumulator, t1 - t0)
    return accumulator

def test(): # проверка кривых случаев
    assert fractional_knapsack(0,[(60,20)]) == 0.0 # при нулевой емкости ничего не возьмется
    assert fractional_knapsack(25,[(60,20)]) == 60.0 # рюкзак полупустой, если брать нечего
    assert fractional_knapsack(25,[(60,20),(0,100)])== 60.0 # нулевая стоимость
    assert fractional_knapsack(25, [(60,20),(50,50)]) == 60.0 + 5.0# еслм пердметов больше, берем оптимально
    assert fractional_knapsack(50,[(60,20),(100,50),(120,30)]) == 180.0 # пример из курса

    # змерим время работы
    from random import randint


    for attempts in range(100):
        n = randint(1,1000)
        capacity = randint(0,2*10**6)
        values_and_weights = []
        for i in range(n):
            values_and_weights.append(
                (randint(0,2*10**6),randint(1,2*10**6)))
        t = timed(fractional_knapsack,capacity,values_and_weights)
        assert  t<5

if __name__ == "__main__":
    test()#main()