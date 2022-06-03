import telebot
from telebot import types
import os
import logging
from dotenv import load_dotenv
from data_base import DataBaseWorker


dotenv_path = os.path.join(os.path.dirname(__file__), 'token.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

BOT_TOKEN = os.getenv("TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)
db = DataBaseWorker('database.db')
logging.basicConfig(level=logging.INFO)


def welcome(bot):
    def welcom_message(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        farther = types.KeyboardButton('/Регистрация')
        markup.add(farther)
        bot.send_message(chat_id=message.chat.id,
                         text= '<b>Привет! \n</b>'
                         'Это мой проект по Питон\n'
                         'Здесь можно найти собиседников и погворить с ними о:\n'
                         '-жизни 👀\n'
                         '-работе 💼\n'
                         'любви ❤️', parse_mode='html', reply_markup=markup)
    return welcom_message


def registration(bot):
    def input_reson(message):
        bot.send_message(message.chat.id, 'Введите причину:')
        reason = message.text
        db.add_user(message.from_user.id, message.from_user.username, reason)
    return input_reson


def menu(bot):
    def welcom_menu(message):
        markup = types.ReplyKeyboardMarkup()
        update = types.KeyboardButton('/ОбновитьАнкету')
        delete = types.KeyboardButton('/УдалитьАнкету')
        find = types.KeyboardButton('/НайтиСобиседника')
        markup.add(update, delete, find)
        bot.send_message(chat_id=message.chat.id,text="",reply_markup=markup)


def update_questionnaire(bot):
    def up(message):
        bot.send_message(message.chat.id, 'Введите новую причину:')
        old_reason = db.get_info_user(message.from_user.id)
        db.update_user_reason(old_reason, message.text)


def delete_quastionnaire(bot):
    def dlt(message):
        db.delete_user(message.from_user.id)
        bot.send_message(message.chat.id, "Ваша анкета удалена")


def find_users(bot):
    def fnd(message):
        data = []
        data = db.find_user(db.get_info_user(message.from_user.id))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu = types.KeyboardButton('/Меню')
        markup.add(menu)
        for mass in data:
            bot.send_message(message.chat.id,mass[1], "/n", mass[2], "/n", reply_markup=markup)



def main():
    bot.message_handler(commands=['start'])(welcome(bot))
    bot.message_handler(commands=['Регистрация'])(registration(bot))
    bot.message_handler(content_types=['text'])(menu(bot))
    bot.message_handler(commands=['ОбновитьАнкету'])(update_questionnaire(bot))
    bot.message_handler(commands=['УдалитьАнкету'])(delete_quastionnaire(bot))
    bot.message_handler(commands=['НайтиСобиседника'])(find_users(bot))
    bot.polling(none_stop=True)

if __name__ == '__main__':
    main()


