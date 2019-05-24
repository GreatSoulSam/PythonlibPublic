


#
#
#
#
# HERE GOES FUNC DESCRIPTION

# Функция polling запускает т.н. Long Polling, а параметр
# none_stop=True говорит, что бот должен стараться
# не прекращать работу при возникновении каких-либо ошибок.
# https://www.pubnub.com/blog/2014-12-01-http-long-polling/
# client polls the server requesting new information.
# The server holds the request open until new data is available.
# Once available, the server responds and sends the new information.
# When the client receives the new information, it immediately
# sends another request, and the operation is repeated.

# file_id -s :
# AwADAgADQgMAAvzAQEnEdZUi1m693gI Army Of The Night

#
# AwADAgADQwMAAvzAQEmymwOLyVJ5xwI Dead boys don't cry

#
# AwADAgADRAMAAvzAQEkCdRI6ruoe1QI Son Of A Wolf

# При отправке медиафайлов большого размера вы можете столкнуться с
# ошибкой ConnectionError: ('Connection aborted.', timeout('The write operation timed
# out',)) . Чтобы её избежать, при вызове методов для медиа send_audio , send_video и
# остальных аргумент timeout=ЧИСЛО , где значение ЧИСЛО укажите в соответствии с
# вашими потребностями (например, 5, 10 или что-то ещё, в зависимости от размера
# файла)

# "игровой режим": Как только юзер нажимает на /game, мы заносим его ID в
# хранилище (именно поэтому его и используем, каждый раз дергать БД некошерно) и
# предполагаем, что следующее сообщение - ответ на вопрос. Всё, что юзер введёт с
# клавиатуры или любая кнопка в разметке (суть отправка сообщения) считается
# ответом.

# Устанавливая вебхук, вы как бы говорите
# серверам Telegram: "Слышь, если кто мне напишет, стукни сюда — (ссылка)".
# Отпадает необходимость периодически самому опрашивать серверы, тем самым,
# исчезает неприятная причина падений ботов. Однако за это приходится платить
# необходимостью установки полноценного веб-сервера

# Как коммитить и запускать на хероку:
# git add .
# git commit -m "Demo"
# git push heroku master

# Запуск:
# локальный запуск: heroku local web -f Procfile.windows
# Остановка: Ctrl+C. Полная остановка: heroku ps:scale web=0    web=1 - запуск
