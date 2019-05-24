#
# This file describes a custom keyboard with reply options
#

import telebot

class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def add_phone_number(self,message):
        phone_markup = telebot.types.ReplyKeyboardMarkup(True,False)
        phone_markup.row('1','2','3')
        phone_markup.row('4','5','6')
        phone_markup.row('7','8','9')
        phone_markup.row('+','0','Delete')
        phone_markup.row("Вернуться назад")
        self.bot.send_message(message.from_user.id,'Введите ваш номер телефона: ',
                              reply_markup=phone_markup)

    def registration_menu(self,message):
        reg_markup = telebot.types.ReplyKeyboardMarkup(True,False)
        reg_markup.row("Ввести имя ребенка")
        reg_markup.row("Ввести имя родителя")
        reg_markup.row("Ввести номер телефона")
        reg_markup.row("Ввести электронную почту")
        reg_markup.row("Ввести комментарии")
        reg_markup.row("Проверить правильность")
        reg_markup.row("Вернуться назад")
        self.bot.send_message(message.from_user.id,
                              'Выберите пункт меню: ')

    def email_menu(self,message):
        email_markup = telebot.types.KeyboardButton()
        email_markup.text("Вернуться назад")
        self.bot.send_message(message.from_user.id,
                              "Введите адрес электронной почты. "
                              "\nНесколько адресов моно ввести через запятую")