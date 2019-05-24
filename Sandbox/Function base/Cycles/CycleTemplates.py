#1)For
for x in range (1,11):
    print(x)

for s in"str":
    print(s,end = " ")
else:
    print("\nCycle is over")

#То же самое для списков и кортежей
#Перенбор элементов словаря
arr = {"х": 1, "у": 2, "z": 3}
arr.keys() #Возвращает объект, содержащий все ключи словаря
for key in arr.keys():
    print(key,arr[key])
print("//////////Второй способ")
for key in arr:
    print(key, arr[key])
print()
#Перебор сложных структур (список кортежей)
arr = [(1, 2), (3, 4)]
for a,b in arr:
    print(a,b)
print()

#range()
arr = [1, 2, 3]
for i in range(len(arr)):
    arr[i] *= 2
print (arr)
print()

for i in range(1,11):
    print(i)
for i in range(1,11,-1):
    print(i)
for i in range(1,11,2):
    print(i)

#enumerate()
#Возвращает итератор. параметры - объект и необяз. start=0
#На каждой итерации возвращает кортеж (индекс, значение текущего эл-та)
arr = [1,2,3,4,5,6,7,8]
for i,element in enumerate(arr):
    if element % 2 == 0:
        arr[i] *= 2
print(arr)
print()

#использование next() для обхода последовательности
#start задает значение индекса первого элемента.
#по умолчанию индексация с нуля, но можно и с любого числа
arr = [1,2,3]
obj = enumerate(arr)
print(next(obj))
obj = enumerate(arr,start = 7)
print(next(obj))
print(next(obj))
print(next(obj))
print()

#2) While

i = 1
while i<10:
    print(i)
    i+=2

arr = [1,2,3]
i, count = 0, len(arr)
while i<count:
    arr[i]*=2
    i+=1
print(arr,"\n")

#continue - переход на следующую итерацию с пропуском последующего кода
for i in range (1 , 15):
    if 4 < i < 11:
        continue
    print(i)
print()

#break - прерывание цикла
i = 1
while True:
    if i > 5: break
    print(i)
    i += 1
print()

