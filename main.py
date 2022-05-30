import telebot
from telebot import types
import data_base


bot = telebot.TeleBot('5327302561:AAHjQZlfukSKDIEl72zNUQJifiabcvk_Wyc')


@bot.message_handler(commands=['start', 'help'])
def start(message):
  markup = types.ReplyKeyboardMarkup()
  next = types.KeyboardButton('next')
  markup.add(next)
  bot.send_message(message.chat.id,'<b>Привет! \n</b>'
                   'Это мой проект по Питон\n'
                   'Здесь можно найти собиснедников и погворить с ними о\n'
                   '-жизни 👀\n'
                   '-работе 💼\n'
                   'любви ❤️', parse_mode = 'html', reply_markup=markup)


@bot.message_handler(commands=['next'])
async def registration(message):
    bot.send_message(message.chat.id, '<b>придется зарегестрироваться \n</b>', parse_mode='html')
    markup = types.ReplyKeyboardMarkup()
    name = types.KeyboardButton('Имя')
    prichina = types.KeyboardButton('Причина')
    markup.add(name, start)
    bot.send_message(message.chat.id, 'КРЯ', reply_markup=markup)
    data = [2]
    if message == 'Имя':
        data[0] = message
        bot.send_message(message.chat.id, 'Теперь ввидите причину')
        data[1] = message
    else:
        data[1] = message
        bot.send_message(message.chat.id, 'Теперь ввидите имя')
        data[0] = message
    menu(message)


@bot.message_handler(commands=['отредактировать анкету'])
def update_blank(message):
    markup = types.ReplyKeyboardMarkup()
    name = types.KeyboardButton('Имя')
    prichina = types.KeyboardButton('Причина')
    cancellation = types.KeyboardButton('Отмена')
    markup.add(name, start, cancellation)
    bot.send_message(message.chat.id, 'КРЯ', reply_markup=markup)
    data = [2]
    if message == 'Имя':
        data[0] = message
        bot.send_message(message.chat.id, 'Теперь ввидите причину')
        data[1] = message
    elif message == 'Причина':
        data[1] = message
        bot.send_message(message.chat.id, 'Теперь ввидите имя')
        data[0] = message
    else:
        markup = types.ReplyKeyboardMarkup()
        next = types.KeyboardButton('next')
        markup.add(next)
        bot.send_message(message.chat.id, 'КРЯ', reply_markup=markup)


@bot.message_handler(commands=['удалить анкету'])
def update_blank(message):
    data_base.delete_user(message.from_user.id)


@bot.message_handler(commands=['найти собеседника'])
def find(message):
    markup = types.ReplyKeyboardMarkup()
    next_user = types.KeyboardButton('next_user')
    back = types.KeyboardButton('back')
    markup.add(next, back)
    row = data_base.next_user(data_base.get_info_user(message.from_user.id)[2])
    bot.send_message(message.chat.id, row, reply_markup=markup)


@bot.message_handler(commands=['back'])
def menu(message):
    markup = types.ReplyKeyboardMarkup()
    update = types.KeyboardButton('отредактировать анкету')
    find = types.KeyboardButton('найти собеседника')
    delete = types.KeyboardButton('удалить анкету')
    markup.add(update,find,delete)
    bot.send_message(message.chat.id, 'Меню', reply_markup=markup)


bot.polling(none_stop=True)