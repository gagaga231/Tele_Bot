import telebot
bot = telebot.TeleBot("988777574:AAH8_92VYMFCtSyOc43S23aGgra_H7Vncag", parse_mode = None)
@bot.message_handler(commands=['star', 'help'])
def send_message(message):
    bot.reply_to(message, "дароу")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.infinity_polling()
