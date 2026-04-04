from telebot import TeleBot
from telebot.types import Message

def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def start_command(message: Message):
        bot.reply_to(message, "Привет! Я калькулятор-бот. Напиши выражение (например, 2+2).")

    @bot.message_handler(commands=['help'])
    def help_command(message: Message):
        help_text = """
Доступные команды:
/start – Начать работу с ботом
/help – Показать это сообщение
Просто напиши математическое выражение (2+2, 5*3 и т. д.)
"""
        bot.send_message(message.chat.id, help_text)
