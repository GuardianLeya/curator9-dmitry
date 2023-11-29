import telebot

bot = telebot.TeleBot('6579098656:AAHSWGoa4uT35WMBqLGhpnsKqz4cv-rvUww')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщеньице')


@bot.message_handler(commands=['pay'])
def main(message):
    bot.send_message(message.chat.id, 'С вас списано миллион долларов')


@bot.message_handler(commands=['матан'])
def main(message):
    bot.send_message(message.chat.id, 'передайте андрею баканчеву, что он лучший')


@bot.message_handler(commands=['тик ток'])
def main(message):
    bot.send_message(message.chat.id, 'какой тик ток, иди уроки делай')


@bot.message_handler(commands=['подвал'])
def main(message):
    bot.send_message(message.chat.id, 'тебя скелет поцеловал')


@bot.message_handler(commands=['фантазия'])
def main(message):
    bot.send_message(message.chat.id, 'фантазия кончилась')


bot.infinity_polling()
