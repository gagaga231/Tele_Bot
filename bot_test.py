import telebot
bot = telebot.TeleBot("", parse_mode = None)
@bot.message_handler(commands=['star', 'help'])
def send_message(message):
    bot.reply_to(message, "дароу")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.infinity_polling()
