#This file contains methods for working with strings
s = "Python"
print(s[0])

print("Strings are immutable")

print("String length: ",len(s))

print(s+"3.7")

print("""String1 String2 
String3""")

print("str1\nstr2")
print(r"String1\nString2")
print(r"С:\\Python32\\lib\\site-packages") #вывод символов форматир-я "как есть"

#Спец.символы

#\n - перевод строки
#\r - возврат каретки
#\t - табуляция
#\v - вертикальная табуляция
#\" - кавычка
#\' - апостроф
#\\ - один обратный слеш

#Собственно, методы

s = "python"
#вывод последнего элемента
print(s[-1], s[len(s)-1])

#Вывод части строки (срезы)
print(s[:]) # от 0 до конца
print(s[::-1]) # от 0 до конца с шагом -1
print("J"+s[1:]) # J + вывод со второго элемента
print(s[:-1]) # от 0 до len(s)-1
print(s[0:1]) # первый символ
print(s[-1:]) # от предпоследнего до конца
print(s[2:5]) # индекс 2,3,4
print(len(s))

#перебор с помощью for
for i in s:
    print(i, end = " ")

t = "str1","str2"
print(t)
print(type(t))

str([1,2]) #Преобразует любой объект в строку

print(len(s)) #длина строки
s1, s2 = " str\n\r\v\t", "strstrstrokstrstrstr"
print("'%s' - '%s'"% (s1.strip(), s2.strip("tsr")))
#Удаляет пробельные или указанные символы в конце и начале строки
#lstrip() & rstrip() - то же самое, только либо слева, либо справа
print()

#split ( [<Разделитель> [, <Лимит> ] ]) разделяет строку на подстроки по указанному
#разделителю и добавляет их в список.Если первый параметр не указан или имеет зна••ение
#None, то в качестве разделителя используется символ пробела. Если во втором параметре
#задано число, то в списке будет указанное количество подстрок. Если подстрок
#больше указанного количества, то список будет содержать еше один элемент, в котором
#будет остаток строки.
s1 = "word1 word2 word3"
print(s1.split())
print(s1.split(None,1))
s1 = "wordl \nword2\nword3"
print(s1.split("\n"))
#Пустые элементы не добавляются:
s1 = "word1                word2 word3          "
print(s1.split())
#Пустые элементы могут появиться при исп-и иного разделителя
s1 = ",,wordl,,word2,,word3,,"
print(s1.split(","))
#если разделитель не найден, список состоит из одного элемента:
print("word1 word2 word3".split("\n"))

#Метод splitlines() - разделяет строку на подстроки по символу \n
print("word1\nword2\nword3".splitlines())
print("word1\nword2\nword3".splitlines(True))
print("word1\nword2\nword3".splitlines(False))
print("wordl word2 wordЗ".splitlines())

#Метод partition() - ищет первое (слева направо) вхождение разделителя в строку,
# и возвращает кортеж ('до разделителя','разделитель','после разделителя')
print("wordl word2 wordЗ".rpartition(" "))

#Метод join() -оследов-ть в строку через указанный разделитель
#<Строка> = <Разделитель>.jоin(<Последовательность>)
print(" => ".join(["wordl", "word2", "wordЗ"]))

#Изменение регистра
print ("строка". upper ())
print ("СТРОКА" .lower ())
print ("СТРОКА строка". swapcase () )
print ("cтpoкa строка" .capitalize ())
s = "первая буква каждого слова станет прописной"
print(s.title())

#Поиск и замена в строке

#<Строка>.find(<Подстрока>[, <Начало>[, <Конец>]])

s = "пример пример Пример"
print(s. find ("при"), s. find ("При") , s. find ("тест"))

#<Строка>.indех(<Подстрока>[, <Начало>[, <Конец>]])
#если подстрока не найдена, выдается ValueError

s = "пример пример Пример Пример"
print(s.rfind("при"), s.rfind("При"), s.rfind("тecт"))

#аналогично rindex()

#<Строка>.соunt(<Подстрока>[, <Начало>[, <Конец>]])
s = "пример пример Пример Пример"
print(s. count ("при") , s. count ("при", 6) , s. count ("При"))

#<Cтpoкa>.startswith(<Пoдcтpoкa>[, <Начало>[, <Конец>]])
s = "пример пример Пример ,Пример"
print(s.startswith("при"), s.startswith("Пpи"))
print(s. startswith ("при", 6), s. startswith ("При", 14))

#Аналогично с endswith()
#Оба метода зависят от регистра

#replace() - вовращает новую строку, зависит от регистра
#<Строка>.rер1асе(<Подстрока для заменьD, <Новая подстрока>[,
#<Максимальное количество замен>])

s = "Привет, Петя"
print(s.replace("Петя", "Вася"))
print(s.replace("пeтя", "вася")) #Зависит от регистра
s = "strstrstrstrstr"
print(s.replace("str", ""), s.replace("str","", 3))

#Проверка типа содержимого строки
# Возвращает True или False
#isdigit(), isdecimal(), isnumeric(), isalpha() - буквы, isspace(), isalnum()
# islower(), isupper(), istitle()

