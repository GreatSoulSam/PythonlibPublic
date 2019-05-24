
# Первая строка входа содержит целые числа
# 1≤W≤104 и 1≤n≤300 — вместимость рюкзака и число золотых
# слитков. Следующая строка содержит
# n целых чисел 0≤w1,…,wn≤105, задающих веса слитков.
# Найдите максимальный вес золота, который можно
# унести в рюкзаке.

W,n = map(int, input().split())
wg = []
for i in (input().split()):
    wg.append(int(i))
wg.sort()
#print(wg)
D = [[0 for x in range(W+1)]for y in range(n+1)]

#for im in D:
#    print(im)

for i in range(1,n+1):
    for w in range(1,W+1):
        #print(w,i)
        #wgh = wg.copy()
        D[i][w]= D[i-1][w]
        #for j in range(0,i):
            #print(i,w)
            #print(wg[j], w)

        if wg[i-1]<=w:
            D[i][w] = max(D[i][w],
                              D[i - 1][w - wg[i-1]] + max(wg[:i]))

#print(list((0,1,2,3,4,5,6,7,8,9,10)))
#print()
#for im in D:
#    print(im)

print(D[n][W])