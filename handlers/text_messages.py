import telebot
from utils.calculator import calculate

def register_handlers(bot):
    @bot.message_handler(func=lambda message: True)
    def handle_calculation(message):
        text = message.text.strip()
        result = calculate(text)
        bot.reply_to(message, f"Результат: {result}")
