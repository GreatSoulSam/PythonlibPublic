# В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных
# натуральных чисел, не превышающих 10^9, в порядке возрастания,
# во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk,
# не превышающих 10^9. Для каждого i от 1 до k необходимо вывести
# индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.

len_a,*a = map(int,input().split()) # already sorted
len_b,*b = map(int, input().split())
out =[]

for i in range(0,len_b):
    L,R=0,len_a-1
   # while L <= R:
    for j in range(L, R):
        m = (L + R) // 2
        if a[m] == b[i]:
            out.append(m+1)
            break
        elif a[m] < b[i]:
            L = m + 1
            if L > R:
                out.append(-1)
                break
        elif a[m] > b[i]:
            R = m - 1
            if L > R:
                out.append(-1)
                break
print(" ".join(map(str, out)))