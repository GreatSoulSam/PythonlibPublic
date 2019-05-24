

#try:
#   <Блок, в котором nерехватьшаются исключения>
#[ except [ <Исключение1> [ as <Объект исключения>] ] :
#   <Блок, вьmолняемьм nри возникновении исключения>
#[ ...
#except [<ИсключениеN>[ as <Объект исключения>]]:
#   <Блок, вьmолняемьм nри возникновении исключения>]]
#[e1se:
#   <Блок, вьmолняемьм, если исключение не возникло>]
#[finally:
#   <Блок, вьmолняемьм в любом случае>]

#Пример - обработка деления на ноль

try: # Перехватьшаем исключения
    x = 1 / 0# Ошибка: деление на О
except ZeroDivisionError: # Указьшаем класс исключения
    print ("Обработали деление на О")
    x = 0
print(x) # Выведет: О


#Вложенные обработчики

try:    # Обрабатьшаем исключения
    try:    # Вложенньм обработчик
        x = 1 / 0   # Ошибка: деление на О
    except NameError:
        print( "Неоnределенный идентификатор")
    except IndexError:
        print ("Несуществую!Ш1й индекс")
    print("Bыpaжeниe nосле вложенного обработчика")
except ZeroDivisionError:
    print ( "Обработка деления на О")
    х = 0
print(x) # Выведет: О

#Обработка нескольких исключений

try:
    х = 1 /0
except (NameError, IndexError, ZeroDivisionError):
# Обработка сразу нескольких исключений
    х = 0
print(x) # Вьшедет: О


#Обработка всех исключений

try:
    x = 1/0
except:
    x = 0
print(x)



#else и finally

try:
    х = 10 / 2
    #х = 10 1 О
except ZeroDivisionError:
    print ("Деление на 0")
else:
    print ( "Блок e1se")
finally:
    print ("Блок finally")


# with...as - гарантия выполнения завершающих действий (напр закрытие файла)
# даже при возникновении исключения

#with <Выражениеl>[ as <Переменная>] [, ... ,
#   <ВыражениеN>[ as <Переменная>]]:
#   <Блок, в котором перехватываем исключения>

class MyClass:
    #enter И exit - обязательно должны быть
    def __enter__(self):
        print("Вызван метод __enter__ ()")
        return self
    def __exit__(self, Туре, Value, Trace):
        print("Вызван метод exit () ")
        if Туре is None: # Если исключение не возникло
            print ( "Исключение не возникло")
        else: # Если возникло исключение
            print("Value =", Value)
            return False # False ~ исключение не обработано
                        # True ~ исключение обработано
print("Последовательность nри отсутствии исключения:")
with MyClass():
    print ("Блок внутри with")
    print("\nПоследовательность nри наличии исключения:")
with MyClass() as obj:
    print ("Блок внутри with")
    #raise TypeError("Исключение TypeError")
    print(" blabla")

#Another ex
#with open("test.txt", "а", encoding="utf-8") as f:
#   f.write("Cтpoкa\n") # Записываем строку в конец файла

print()
#################
#Пользовательские исключения (raise, assert)

#raise <Экземnляр класса>
#raise <Название класса>
#raise <Экземnляр или название класса> from <Объект исключения>
#raise

#try:
#    raise ValueError("error description")
#except ValueError as msg:
#    print(msg)

class MyError(Exception):
    def __init__ (self, value) :
        self.msg = value
    def str (self):
        return self.msg
# ООработка пользовательского исключения
#try:
#    raise MyError("Описание исключения")
#except MyError as err:
#    print(err)
#    print(err.msg)
# Вызывается метод str ()
# Обращение к атрибуту класса
# Повторно возбуждаем исключение
#raise MyError ("Описание исключения")

#assert - для ошибок в логических выражениях