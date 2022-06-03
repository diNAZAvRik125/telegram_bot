import datetime
import pandas as pd
import requests
import telebot
from tabulate import tabulate
from constants import CODE, TOKEN, URL
def send_welcome_fun(bot):
    def send_welcome(message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = telebot.types.KeyboardButton('Расписание занятий')
        markup.add(item1)
        bot.send_message(
            chat_id=message.chat.id,
            text=f'Здравствуйте, {message.from_user.first_name} :) ',
            reply_markup=markup,
        )
    return send_welcome
def bot_message_fun(bot):
    def bot_message(message):
        day = datetime.datetime.today().isoweekday()
        if message.text == 'Расписание занятий':
            if day == 7:
                bot.send_message(message.chat.id, 'Сегодня выходной. Занятий нет')
            else:
                msg1 = bot.send_message(message.chat.id, 'Введите номер группы')
                bot.register_next_step_handler(msg1, today_time_fun(bot))
        else:
            bot.send_message(message.chat.id, 'УТОЧНИТЕ ЗАПРОС\nЯ вас не понимаю\n')
    return bot_message
def today_time_fun(bot):
    def today_time(message):
        url = URL + str(message.text)
        time_table = requests.get(url)
        if time_table.status_code == CODE:
            dfs = pd.read_html(url)
            day = datetime.datetime.today().isoweekday()
            week_day = dfs[1].columns[day]
            cur_table = dfs[1][['Время', week_day]]
            cur_table = cur_table.fillna('-').set_index('Время')
            bot.send_message(chat_id=message.chat.id, text=tabulate(cur_table, headers='keys'))
        else:
            msg2 = bot.send_message(message.chat.id, 'Такой группы не существует. Введите номер группы')
            bot.register_next_step_handler(msg2, today_time)
    return today_time
def main():
    bot = telebot.TeleBot(TOKEN)
    bot.message_handler(commands=['start'])(send_welcome_fun(bot))
    bot.message_handler(content_types=['text'])(bot_message_fun(bot))
    bot.message_handler(content_types=['text'])(today_time_fun(bot))
    bot.polling(none_stop=True)
if name == '__main__':
    main()