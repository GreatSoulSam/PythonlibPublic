arr = [1,2,3]
tuple = ("a","b","c")
print(arr,tuple)
arr[0]=10
print(arr)
arr = list("string")
print(arr)
print()

#append()
print("\nappend()")
arr.append(1)
arr.append("str")
print(arr)

#Ссылка на один объект в памяти
print("\nСсылка на один объект в памяти")
x = y = [1,2]
print(x,y)

y[1]=100
print(x,y)
# Как НАДО делать:
x,y = [1,2],[1,2]
y[1]=100
print(x,y)

#Вложенные списки
#Генерация
print("\nВложенные списки","Генерация","через append внутри цикла",sep="\n")
#через append внутри цикла
arr = []
for i in range(3):
    arr.append([])
print(arr)

#Генератор списков:
print("\nГенератор списков:")
arr = [ [] for i in range(3)]
print(arr)

arr[0].append((5,[6,7]))
print(arr)

#Так как присваивание сохраняет ссылку, а не сам объект,
# рассмотрим как создавать копию списка
print("copy()")
import copy
x = [1,[2,3,4,5]]
y = copy.deepcopy(x)
print(y is x) #разные объекты
y[1][1]=100
print(x,y)
#deepcopy - создает копию объекта с сохранением структуры

#Операции над списками
# позиционное присваивание, длина

# Срезы [<Начало>:<Конец>:<Шаг>]
#по умолчанию: 0, len-1, 1
print("\nСрезы")
arr = [1, 2, 3, 4, 5]
m = arr[:]
print(m)
print(m is arr) # поверхностная копия
print(arr[::-1])
print(arr[1:])
print(arr[1:len(arr)-1])

#Изменение списка с помощью среза
print("\nИзменение списка с помощью среза")
arr[1:3]= [6,7]
print(arr)
arr[1:3]=[]
print(arr)

#объединение списков
print("\nобъединение списков")
arr1 = [7, 8, 9]
print(arr + arr1)

#Умножение (повтор)
print("\nУмножение (повтор)")
print(arr1*3)

#Многомерные списки
print("\nМногомерные списки")
arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
      ]
print(arr[1][1])

#тип элеиентов может юыть любым
arr = [
        [1, ["a", "b"], 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
print(arr[0][1][0])

# Создание матрицы генератором:
print("\nСоздание матрицы генератором")
import random
M,N = 5,6
matrix = [[random.randrange(0,10) for y in range(M)] for x in range(N)]
print(matrix)
for im in range(N):
    print(matrix[im])

#Перебор элементов списка
print("\nПеребор элементов списка")
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i, end=" ")
print()

#через range():
print("\nчерез range():")
for i in range(len(arr)):
    arr[i]*= 2
print(arr)

#через while
print("\nчерез while")
arr = [1, 2, 3, 4]
i,c = 0,len(arr)
while i<c:
    arr[i]*=2
    i+=1
print(arr)


#Генераторы списков
print("\nГенераторы списков")
arr = [1,2,3,4]
arr = [i*2 for i in arr]
print(arr)

#ПРимер генератора со сложной структурой
arr = [1,2,3,4]
arr = [ i*10 for i in arr if i%2 ==0 ]
print(arr)

#Что аналогично конструкции
#arr = []
#for i in [1, 2, 3, 4]:
#    if i % 2 == 0:
#        arr.append(i * 10)
#print (arr)

#Более сложный пример
arr = [[1, 2], [3, 4], [5, 6]]
arr = [ j*10 for i in arr for j in i if j%2 == 0 ]
print(arr)

#При использовании круглых скобок вместо квадратных будет возвращаться не список,
#а итератор
arr = [1,4,7,88]
a = sum( ( i for i in arr if i%2 == 0))
print(a)


#/////////////////////////////////////////////////////////////////////////////////////

#Функции map(), zip(), filter(), reduce()
print("\nmap()")
#map() позволяет применить ф-ю к каждому элементу последовательности
#mар(<Функция>, <Последовательность1>[, ... , <ПоследовательностьN>])
def func (e1em) :
    """ Увеличение значения каждого элемента списка"""
    return e1em + 10 # Возвращаем новое значение
arr = [1, 2, 3, 4, 5]
print(list(map(func, arr)))


def func(e1, е2, е3):
    """ Суммирование элементов трех разных списков """
    return e1 + е2 + е3 # Возвращаем новое значение
arr1 = [1, 2, 3, 4, 5]
arr2 = [10, 20, 30, 40, 50]
arr3 = [100, 200, 300, 400, 500]
print( list( map(func, arr1, arr2, arr3) ) )
print()


#zip() на каждой итерации возвращает кортеж, содерж.элементы последов-тей,
# которые расположены на одинаковом смещении
#zip 1 <Последовательностьl> [, ... , <ПоследовательностьN>] )
print("\nzip()")
a = zip([1,2,3],[4,5,6],[7,8,9])
print(list(a))
print()


#filter() прооводит проверку элементов послед-ти
#filtеr(<Функция>, <Последовательность>)
#Eсли Функция == None, то проверка идет на соотв-е True
print("\nfilter()")
a = filter(None,[1,0,None,[],2])
print(list(a))

#Пример с функцией:
def func (e1em) :
    return e1em >= 0

arr = [-1, 2, -3, 4, 0, -20, 10]
arr = list(filter(func, arr))
print (arr)
# Использование генераторов сnисков
arr = [-1, 2, -3, 4, 0, -20, 10]
arr = [ i for i in arr if func(i) ]
print(arr)
print()


#Функция reduce 1) из модуля functoo1s nрименяет указанную функцию
# к nарам элементов и накаnливает результат.
#rеduсеi<Функция>, <Последовательность>[, <Начальное значение>])
print("\nreduce")
from functools import reduce

def func(x, y):
    print("({0}, {1})".format(x,y),end=" ")
    return x+y

arr = [1,2,3,4,5]
sum = reduce(func,arr)
print(sum)

sum = reduce(func,arr,10)
print(sum)

sum = reduce(func,[],10)
print(sum)

print()


#Добавление и удаление элементов списка
print("Добавление и удаление элементов списка")
arr = [1,2,3]
arr.append(4)
print(arr)
arr.append([5,6])
print(arr)
arr.append((7,8))
print(arr)

arr = [1,2,3]
arr.extend([4,5,6])
arr.extend((7,8,9))
arr.extend('abc')
print(arr)

arr = [1,2,3]
arr.insert(0,0)
print(arr)
arr.insert(-1,20)
print(arr)
arr.insert(2,10)
print(arr)
arr.insert(10,[4,5])
print(arr)

#для добавления нескольких объектов нужно использовать срезы
arr = [1,2,3]
arr[:0] = [-2,-1,0]
print(arr)

#pop() - удаляет элемент по индексу и возвращает его. Default -последний эл-т
print("\npop()")
arr = [1,2,3,4,5]
arr.pop()
print(arr)
a = arr.pop(0)
print(a)
arr.append(a)
print(arr)

print("\ndel()")
arr = [1,2,3,4]
del arr[2]
print(arr)

#remove- удаляет первый элемент с указанным значением
print("\nremove()")

arr = [1,2,3,1,1]
arr.remove(1)
print(arr)

#удаление повторяющихся элементов
#Приводим список к множеству, затем обратно
print("\nудаление повторяющихся элементов")
print("\nПриводим список к множеству, затем обратно")
arr = [1,2,3,1,1,2,3,2,1]
s = set(arr)
print(s)
arr = list(s)
print(arr)

print("\nindex()")
#возвращает индекс эл-та с указ.значением в диапазоне[начало,конец-1]
arr = [1,2,1,2,1]
print(arr.index(1),arr.index(2))
print(arr.index(1,1),arr.index(1,3,5))

print("\ncount()")
arr = [1,2,1,2,1]
print(arr.count(1))

print("max= ",max(arr),", min= ",min(arr))

#Переворачивание и перемешивание списка
print("\nПереворачивание и перемешивание списка")
print('\nreverse()')
arr = [1,2,3,4]
arr.reverse() #Изменяет текущий список
print(arr)

arr1 = [1,2,3,4,7,88]
print(list(reversed(arr1)))
#analog:
for i in reversed(arr1):
    print(i, end=" ")
print()
#analog 2:
print([i for i in reversed(arr1)])
print()


#Сортировка списка
print("\ncортировка списка")
#sort([key=None] [, reverse=fa1se])
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
print(arr)
arr.sort()
print(arr)

#сортировка по убыванию: reverse=True
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
arr.sort(reverse=True)
print(arr)

#Для чего нужен key:
# При сортировке учитывается регистр
arr = [ "единица1", "Единый", "Единица2"]
arr.sort ()
for i in arr:
    print(i, end=" ")

print()
#using key:
arr = ["единица1", "Единый", "Единица2"]
arr.sort(key=str.lower)
for i in arr:
    print(i, end=" ")

print()
#sorted() - аналогично reversed() - возвращает новый список
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
print(sorted(arr))

#Заполнение списка числами
print("\nЗаполнение списка числами")
print(list(range(11)))
print(list(range(2,7)))
print(list(range(15,0,-3)))

import random
print(random.sample(range(900),4))

#Преобразование в строку
print("\nПреобразование в строку")
arr = [ "word1", "word2", "word3"]
print(" - ".join(arr))

#При наличии нестроковых данных в списке:
arr = [ "word1", "word2", "word3",2]
print(" - ".join((str(i) for i in arr)))

print(str(arr))



##########################################################################
#Кортежи
# кортеж- это список, доступный "только для чтения".
print("\n\n\nКортежи")
tuple()
tuple("String") # ('S', 't', 'r', 'i', 'n', 'g')
t1 = ()
t2 = (5,) #Если не добавлять запятую, получится объект int
t3 = 1,"str",[5,6],(3,8)
print(t1,t2,t3)

#В кортежах работает:
# - Получение элемента по индексу
# - Извлечение среза
# - Проверка на вхождение
# - Повторение
# - Конкатенация
# - получение длины
# - index() & count()


########################################################################3
#Itertools
print("\n\n\nitertools")
#TODO

