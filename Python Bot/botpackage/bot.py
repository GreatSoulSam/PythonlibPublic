import time
import botconfig
import telebot
import os
import utils
import requests
from reply_keyboard_markups import Keyboard
from flask import Flask, request


# proxy_ip = '103.109.52.59:9999'
# proxies = {'http'  : 'socks5://%s' %(proxy_ip), 'https' : 'socks5://%s' %(proxy_ip)}
# telebot.apihelper.proxies = proxies

bot = telebot.TeleBot(botconfig.token)
keyboard = Keyboard(bot)
server = Flask(__name__)


# @bot.message_handler(content_types=["text"])
# def popugay(message):
#     bot.send_message(message.chat.id,message.text)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, '+message.from_user.first_name)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # send VDOGONKU file_id
            bot.send_message(message.chat.id, msg.voice.file_id,
                             reply_to_message_id=msg.message_id)
        time.sleep(3)  # Delay execution for a given number of seconds.
# the code above sends audio files and their file_id's in response to \test command

@bot.message_handler(func=lambda mes: "Главное меню" == mes.text,
                     content_types=['text'])
def handle_text(message):
    keyboard.registration_menu(message)

@bot.message_handler(func=lambda mes: 'Ввести электронную почту'== mes.text,
                     content_types=['text'])
def handle_text(message):
    keyboard.email_menu(message)

@bot.message_handler(func=lambda mes: 'Ввести номер телефона'== mes.text,
                     content_types=['text'])
def handle_text(message):
    keyboard.add_phone_number(message)




@server.route('/'+botconfig.token,methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.
                            de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://HEROKU LINK"+botconfig.token)
    return "CONNECTED",200

#server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

if __name__ == '__main__':
    bot.polling(none_stop=True)
