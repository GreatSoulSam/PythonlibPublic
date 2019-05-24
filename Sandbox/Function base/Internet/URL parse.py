#
#
#

#URL-aдpec состоиr из следующих элементов:
#<Протокол>://<Домен>:<Порт>/<Путь>;<Параметры>?<Заnрос>#<Якорь>

#Схема URL-aдpeca для протокола FTP выглядит по-другому:
#<Протокол>://<Пользователь>:<Пароль>@<Домен>
#Разобрать URL-aдpec на составляющие позволяет функция urlparse ( ):
#urlparse(<URL-aдpec>[, <Схема>[, <Разбор якоря>]])

#Элементы соответствуют схеме URL-aдpeca:
#<scheme>://<netloc>/<path>;<params>?<query>#<fragment>.
#Обратите внимание на то, что название домена будет содержать номер порта.

from urllib.parse import urlparse
url = urlparse("http://wwwadmin.ru:80/test.php:st?var=5#metka")
print(url)
print(tuple(url))

#Во втором параметре функции urlparse () можно указать название протокола,
# которое будетиспользоваться, если протокола нет в составе URL-aдpeca.
# По умолчанию используется пустая строка.

url=urlparse ( "//wwwadmin.ru/test.php")
print(url)
#(ParseResult(scheme= ' ', netloc='wwwadmin.ru ', path='/test.php',
#params= ' ' , query= ' ' , fragment= ' ' ))
url1 = urlparse("//wwwadmin.ru/test.php","http")
print(url1)

#Объект ParseResul t, возвращаемый функцией urlparse (), содержит следующие атрибуты:

# scheme - название протокола. Значение доступно также по индексу О.
# По умолчанию пустая строка. Пример:.
#url. scheme, .url [0]
#('http', 'http')

# netloc- название домена вместе с номером порта. Значение доступно также
# по индексу 1. По умолчанию пустая строка. Пример:
# url.netloc, url[l]
#( 'wwwadmin.ru:80', 'wwwadmin.ru:80')

# hostname - название домена в нижнем регистре. Значение по умолчанию: None;

# port- номер порта. Значение по умолчанию: None. Пример:
#url.hostname, url.port
#('wwwadmin.ru', 80)

# path- путь. Значение доступно также по индексу 2. По умолчанию пустая строка.
#Пример:
#urlopath, url[2]
#('/test.php', '/testophp')

# params- параметры. Значение доступно также по индексу 3. По умолчанию пустая
#строка. Пример:
# url.params, url[З]
#('st 1','st ')

# query- строка запроса. Значение доступно также по индексу 4. По умолчанию пустая
#строка. Пример:
# url.query, url[4]
#( 'Var=5', 'Var=5')

# fragment- якорь. Значение доступно также по индексу 5. По умолчанию пустая строка.
#Пример:
# url.fragment, url[5]
#( 'metka', 'metka')

#############
#Если третий nараметр в функuии ur1parse 1) имеет значение fa1se, то якорь будет
# входить в состав значения других атрибутов, а не fragment.
# По умолчанию nараметр имеет значение True.
#############

# username- имя nользователя. Значение по умолчанию: None;

# password- nароль. Значение по умолчанию: None. Пример:
# ftp = urlparse("ftp://user:123456@mysite.ru")
# ftp.scheme, ftp.hostname, ftp.username, ftp.password
# ('ftp', 'mysite.ru', 'user', '123456')

# geturl () -метод возвращает URL-aдpec. Пример:
# url.geturl ()
#'http://wwwadmin.ru:80/test.php:st?var=5#metka'


#Выnолнить обратную оnераuию (собрать URL-aдpec из отдельных значений) nозволяет
#функuия urlunparse ( <Последовательность>)

from urllib.parse import urlunparse
t = ('http','wwwadmin.ru:80','/test.php','','var=5','metka')
print(urlunparse(t))