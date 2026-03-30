import telebot
from config import TOKEN
from handlers import commands, text_messages

bot = telebot.TeleBot(TOKEN)

commands.register_handlers(bot)
text_messages.register_handlers(bot)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()