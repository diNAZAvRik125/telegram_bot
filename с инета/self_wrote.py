import telebot


bot = telebot.TeleBot('5287171926:AAEuer-VuJP-0l7EkouKpR9zDzu0jIC0j3Q')


@bot.message_handlers(commands=['start'])
def start(massage):
  bot.send_message(massage.chat.id,'<b>Привет! \n</b>'
                   'Это мой проект по Питон\n'
                   'Здесь можно найти собиснедников и погворить с ними о\n'
                   '-жизни 👀\n'
                   '-работе 💼\n'
                   'любви ❤️', parse_mode = 'html')
bot.polling(none_stop=True)