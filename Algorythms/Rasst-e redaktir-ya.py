# Вычислите расстояние редактирования двух данных
# непустых строк длины не более 102, содержащих
# строчные буквы латинского алфавита.

# short
# ports

# 3
def diff(a,b):
    if a==b:
        return 0
    else:
        return 1

a = input()
b = input()
#while len(a)>len(b):
#    b+=" "
#while len(a)<len(b):
#    a+=" "
n,m = len(a)+1,len(b)+1
D = [[0 for y in range(n)]for x in range(m)]
for i in range(n): # столбцы
    D[0][i]=i
for j in range(m): # строки
    D[j][0]=j
# контрольный вывод
#for im in D:
#    print(im)
##########
for j in range(1,m):
    for i in range(1,n):
        #c = 0 if a[i-1]==b[j-1] else 1
        c = diff(a[i-1],b[j-1])
        D[j][i]= min(D[j][i-1]+1,D[j-1][i]+1,D[j-1][i-1]+c)
#        print(c,D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+c)
#print("\n")
#for im in D:
#    print(im)

print(D[m-1][n-1])
