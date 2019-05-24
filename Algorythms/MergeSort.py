# Первая строка содержит число 1≤n≤105, вторая — массив A[1…n],
# содержащий натуральные числа, не превосходящие 109. Необходимо
# посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
# (Такая пара элементов называется инверсией массива. Количество
# инверсий в массиве является в некотором смысле его мерой
# неупорядоченности: например, в упорядоченном по неубыванию
# массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию,
# инверсию образуют каждые два элемента.)
"""
def Merge(a,b):
    c=[]
    c.append(min(min(a),min(b)))
    return(c)


n = int(input())
a = list(map(int,input().split()))
#for i in range(0,n):
#    a[i] = [a[i]]
# if len(a)//2>0:
#    a.append(10**9+1)

print(a)

def mergesort(a):
    cnt = 0
    if len(a) > 1:
        lh = a[:len(a) // 2]
        rh = a[len(a) // 2:]
        # lst=[]
        mergesort(lh)
        mergesort(rh)
        i = 0
        j = 0
        k = 0

        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                a[k] = lh[i]
                i += 1
            else:
                a[k] = rh[j]
                j += 1
                cnt += 1
            k += 1

        while i < len(lh):
            a[k] = lh[i]
            i += 1
            k += 1

        while j < len(rh):
            a[k] = rh[j]
            j += 1
            k += 1
    print(a,cnt)
mergesort(a)
"""
import copy

n = int(input())
a = list(map(int,input().split()))
count = 0


def merge(a,b):
    global count
    i=0
    j=0
    res = [0 for m in range(len(a)+ len(b))]
    for k in range(0,len(res)):
        if (j == len(b) or (i<len(a) and a[i]<=b[j])):
            res[k] = a[i]
            i+=1
        else:
            """
            сюда заходим, если аi строго больше бj
            В этом моменте происходит проверка того, что эл-т массива а больше
            элемента масива б, что и требуется в задаче. 
            """
            #a[i,i+1...len(a)-1]>b[j]
            count+=len(a)-i
            res[k]=b[j]
            j+=1

        k+=1
    return res





def mergeSort(a):
    if len(a)==1:
        return a
    n = len(a)
    m = n//2
    #left = ['' for l in range(m)]
    #right = ['' for l in range(n-m)]
    left = copy.copy(a[:m])
    right = copy.copy(a[m:n])
    left = mergeSort(left)
    right = mergeSort(right)
    z = merge(left,right)
    return z

def main():
    mergeSort(a)
    print(count)

if __name__ == "__main__":
    main()


