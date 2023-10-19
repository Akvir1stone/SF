import telebot


bot = telebot.TeleBot('6394818946:AAHPLIUuOZ9YRhEDkxHm_XUDcYxBgwx6mhY')


@bot.message_handler(content_types=['photo'])
def react_to_meme(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme')


bot.stop_bot()
