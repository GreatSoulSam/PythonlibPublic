#
#
#
#
f = open(r"file.txt",'w')
f.close() # Очистка файла перед запуском

import sys # Подключаем модуль sys
tmp_out = sys.stdout # Сохраняем ссьmку на sys.stdout
f = open(r"file.txt",'a') # Открываем файл на дозапись
sys.stdout = f # Перенаправляем вывод в файл
print("Пишем строку в файл")
sys.stdout = tmp_out # Восстанавливаем
print ("Пишем строку в стандартный вывод")
#Пишем строку в стандартньм вьшод
f. close () # Закрьшаем файл

#В этом примере мы вначале сохранили ссылку на стандартный вывод в переменной tmp out.
#С помошью этой переменной можно в дальнейшем восстановить вывод в стандартный поток.
#Функuия print () напрямую поддерживает перенаправление вывода. Для этого используется
#параметр file, который по умолчанию ссылается на стандартный поток вывода.

f = open(r"file.txt",'a')
print("Add string to file", file=f)
f.close()


#перенаправление стандартного ВВОДА
import sys
tmp_in = sys.stdin # Сохраняем ссьmку на sys.stdin
f = open(r"file.txt", "r") # Открьшаем файл на чтение
sys.stdin = f # Перенаправляем ввод
while True:
    try:
        line = input() # Считьшаем строку из файла
        print(line)# Выводим строку
    except EOFError: # Если достигнут конец файла,
        print("EOF reached")
        break       # выходим из цикла
sys.stdin = tmp_in # Восстанавливаем стандартньМ ввод
f.close () # Закрьшаем файл
input() # ввод восстановлен










