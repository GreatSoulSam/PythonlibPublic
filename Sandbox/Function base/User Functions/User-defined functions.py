
#def <Имя функции> ( [ <Параметры>] ) :
#   [""" Строка документирования """]
#   <Тело функции>
#   [return <Значение>]

def func():
    print ("Текст до инструкции return")
    return "Возвращаемое значение"
    print ("Эта инструкция никогда не будет вьmолнена")

print(func())

def prlnt_ok():
    """ Пример функции без nараметров """
    print ("Сообщение при удачно вьmолненной операции")

def echo (m) :
    """ Пример функции с параметром """
    print(m)

def summa(x, у):
    """ Пример"функции с параметрами,
    возвращающей сумму двух переменных"""
    return x + у

print(summa(1,2)," ",summa([1,2],[3,4]))

#функции с необязательными параметрами
def summa(x, y=2):
    return x+y
a = summa(5)
b = summa(5,6)
print(a,b)

# Сопоставление по ключам
def summa(a=2, b=3, c=4): #Все параметры являются необязательными
    return a + b + c
print(summa(2, 3, 20))# Позиционное присваивание
print(summa(c=20)) # Сопоставление по ключам

#Если значения параметров, которые планируется передать в функцию,
# содержатся в кортеже или списке, то перед объектом следует указать символ *.

def summa(a, b, c):
    return a + b + c
t1, arr = (1, 2, 3), [1, 2, 3]
print(summa(*t1)) # Распаковьшаем кортеж
print(summa(*arr)) # Распаковываем список
t2 = (2, 3)
print(summa(3, *t2)) # Можно комбинировать значения

#Если значения параметров содержатся в словаре, то распаковать словарь можно,
# указав перед ним две звездочки(**)

def summa(a, b, c):
    return a + b + c
d1 = {"a": 1, "b": 2, "c": 3}
print(summa(**d1)) # Распаковьшаем словарь
t, d2 = ( 1, 2) , { "c" : 3}
print(summa(*t, **d2))

#Переменное число параметров

#Если перед параметром в определении функции указать символ *,то функции
# можно будет передать произвольное количество параметров.
# Все переданные параметры сохраняются в кортеже.

def summa(*t):
    """Функция принимает Произвольное количество параметров """
    res = 0
    for i in t:
        res += i
    return res
# Перебираем кортеж с переданньми параметрами
print(summa(10, 20)) # Выведет: 30
print(summa(10, 20, 30, 40, 50, 60)) # Выведет: 210


#добавим обязательные и дефолтные параметры
def summa(x, y=5, *t): #Комбинация параметров
    res = x + y
    for i in t: # Перебираем кортеж с переданньми параметрами
        res += i
    return res
print(summa(10)) # Выведет: 15
print(summa(10, 20, 30, 40, 50, 60))# Выведет: 210


#Если перед параметром в определении функции указать две звездочки(**),
# то все именованные параметры будут сохранены в словаре

def func(**d):
    for i in d: # Перебираем словарь с переданнь~ параметрами
        print("{0} => {1}".format(i, d[i]), end=" ")
func(a=1, b=2, c=3) # Вьшедет: а=> 1 с=> 3 Ь => 2

print()
#КОмбинация параметров
def func(*t, **d):
    """Функция примет любые параметры """
    for i in t:
        print(i, end=" ")
    for i in d: # Перебираем словарь с переданньми параметрами
        print("{0} => {1}".format(i, d[i]), end=" ")
func(35, 10, а=1, Ь=2, с=3) # Вьшедет: 35 10 а=> 1 с=> 3 Ь => 2
print()
func (10) # Вьшедет: 10
print()
func(a=1, Ь=2) # Вьшедет: а => 1 Ь => 2
print()

#Параметры, передаваемые по именам - должны стоять после *, но перед **
#Именованные параметры могут иметь значения по умолчанию.

def func(*t, a, b=10, **d):
    print(t, a, b, d)
func(35, 10, a=1, с=3)# Выведет: (35, 10) 1 10 {'с': 3}
func(10, a=5)# Выведет: (10,) 5 10 {}
func(a=1, b=2)# Выведет: () 1 2 { }
#func (1, 2, 3) # Ошибка. Параметр а обязателен!


###########################################################
#Анонимные (Лямбда) функции
# lamЬda[<Параметрl>[, ... ,<ПараметрN>]]: <Возвращаемое значение>

fl = lambda: 10 + 20 # Функция без nараметров
f2 = lambda х, у: х + у # Функция с двумя nараметрами
f3 = lambda х, у, z: х + у + z # Фунция с тремя nараметрами
print (fl ()) # Выведет: 30
prim: (f2 (5, 10)) # Выведет: 15
print(f3(5, 10, 30)) # Выведет: 45

#Необязательные параметры тоже используются, как и в обычных функциях

f = lambda х, у=2: х + у
print (f (5))# Выведет: 7
print:(f(5, 6))# Выведет: 11

#Сортировка без учета реrистра символов
# - пример того, что рез-т лямбды можно напрямую переедавать в другую функцию
arr = ["единица1", "Единый", "Единица2"]
arr.sort(key=lambda s: s.lower())
for i in arr:
    print(i, end=" ")
# Результат вьmолнения: единица1 Единица2 Единьм
print()

##############################################################
#Функции-генераторы
#Функцией-генератором называется функция, которая может возвращать
# одно значение нз нескольких значений на каждой итерации.
# Приостановить выполнение функции и превратить функцию в генератор
# позволяет ключевое слово yie1d.

def func(x,y):
    for i in range(1,x+1):
        yield i**y

for n in func(10,2):
    print(n, end=" ")# Вьrnедет: 1 4 9 16 25 36 49 64 81 100
print()
for n in func(10,3):
    print(n, end=" ")# Вьшедет: 1 8 27 64 125 216 343 512 729 1000
print()

#Функuии-генераторы поддерживают метод __next__( ), который позволяет
# получить следуюшее значение.

def func(x, y):
    for i in range(1, x+1):
        yield i ** y
i = func(3, 3)
print(i.__next__()) #Выведет: 1 (1 ** 3)
print(i.__next__()) #Вьrnедет: 8 (2 ** 3)
print(i.__next__()) #Выведет: 27 (3 ** 3)
#print(i.__next__()) # Исключение Stopiteration
print()


######################################################################
#Декораторы функций
#Изменение поведения функций

def deco(f):
    print("Вызвана функция func() ")
    return f
@deco
def func(x):
    return "x = {0}".format(x)

print(func(10))
print()

#multiple decorators
def decol(f):
    print ("Вызвана функция decol () ")
    return f
def deco2(f):
    print ("Вызвана функция deco2 () ")
    return f
@decol
@deco2
def func (x) :
    return "х = {0}".format(x)

print(func(10))

#Аналогично func = decol(deco2(func))

passw = input ("Введите пароль: ")
passw = passw.rstrip("\r") # Для версии 3.2.0
def test_passw(p):
    def deco(f) :
        if p == "10":# Сравниваем парали
            return f
        else:
            return lambda: "Доступ закрыт"
    return deco # Возвращаем функцию-декоратор

@test_passw(passw)
def func():
    return "Доступ открыт"
print(func()) # Вызываем функцию



#########################################################################
#Рекурсия.
#ПРимер - вычисление факториала

def factorial(n):
    if n == 0 or n == 1: return 1
    else:
        return n * factorial(n-1)

while 1:
    x = input("enter number: ")
    x = x.rstrip("\r")
    if x.isdigit():
        x = int(x)
        break
    else:
        print("not a number!")
print("Факториал числа {0} = {1}". format (x, factorial(x)))