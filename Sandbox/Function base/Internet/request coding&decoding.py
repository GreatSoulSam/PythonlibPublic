#
#
#
# "Строка" => str=%Dl%F2%F0%EE%EA%E0

# добавим параметров str=%Dl%F2%F0%EE%EA%E0&v=10&v=20&t=

# Разобрать строку заnроса на составляющие и декодировать данные nозволяют следующие
# функции из модуля urllib.parse:

# parse_qs() разбирает строку заnроса и возвращает словарь с ключами, содержащими
# названия nараметров, и сnиском значений.
# parse~qs(<Cтpoкa заnроса>[, keep_blank_values=False] [,
# strict_parsing=False] [, encoding='utf-8'] [, errors='replace'])

# Если в nараметре keep_blank_values указано значение True, то nараметры,
# не имеющие # значений внутри строки заnроса, также будут добавлены в результат.
# По умолчанию # nустые nараметры игнорируются.
# Если в nараметре strict_parsing указано значение True, то
# при наличии ошибки возбуждается исключение ValueError. По умолчанию
# ошибки игнорируются. Параметр encoding позволяет указать кодировку данных.
# а параметр errors- уровень обработки ошибок.

from urllib.parse import parse_qs
s = "str=%D1%F2%F0%EE%EA%E0&v=10&v=20&t="
out =parse_qs(s,encoding="cp1251")
print(out)
print(parse_qs(s, keep_blank_values=True, encoding="cp1251"))
# parse_qsl() -функция аналогична parse_qs(), но возвращает не словарь, а список
# кортежей из двух элементов. Первый элемент кортежа содержит название параметра,
# а второй элемент его значение. Если строка запроса содержит несколько
# параметров с одинаковым # значением, то они будут расположены в разных кортежах.

from urllib.parse import parse_qsl
print(parse_qsl(s,encoding="cp1251"))

#####################

# Обратное преобразование - urlencode()

from urllib.parse import urlencode
params = {"str": "Строка 2", "var": 20}
print(urlencode(params, encoding="cp1251"))


#################################
print()

# Выполнить кодирование и декодирование отдельных элементов строки запроса позволяют
# следующие функuии 113 модуля urllib.parse:

# quote 1) ~заменяет все спеuиальные символы последовательностями %nn. Цифры,
# английские буквы и символы подчеркивания (_), точки (.) и дефиса(-) не кодируются.
# Пробелы преобразуются в последовательность %20. Формат функuии:
# quotei<Cтpoкa>[, safe='/'] [, encoding=None] [, errors=None])
# В параметре safe можно указать символы, которые преобразовывать нельзя.

from urllib.parse import quote
print(quote("Строка",encoding="cp1251"))
print(quote("Строка",encoding="utf-8"))
print(quote("/-nik/"), quote("/-nik/", safe='"'))
print(quote(quote("/-nik/", safe="/-")))

# quote_p1us 1) ~ функuия аналогична quote(), но пробелы заменяются символом +,
# а не преобразуются в последовательность %20. Кроме того, по умолчанию
# символ / преобразуется в последовательность %2F

# quote from bytes () - функция аналогична quote (), но в качестве первого параметра
# принимает последовательность байтов, а не строку.

##############

# Обратная операция: unquote () -заменяет последовательности %nn
# соответствующими символами. Символ + пробелом не заменяется.

# Аналогично unquote_plus() и unquote_to_bytes()
