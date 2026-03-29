import telebot
from utils.calculator import calculate

def register_handlers(bot):
    @bot.message_handler(func=lambda message: True)
    def handle_calculation(message):
        text = message.text.strip()

        # Проверка на математические функции
        if any(func in text for func in ['sqrt(', 'sin(', 'cos(', 'tan(', 'ctg(']):
            result = calculate(text)
            bot.reply_to(message, f"Результат: {result}")
            return

        # Базовые операции и дроби
        allowed_chars = set('0123456789+-*/. ')
        if all(c in allowed_chars for c in text) and any(op in text for op in '+-*/'):
            result = calculate(text)
            bot.reply_to(message, f"Результат: {result}")
        else:
            bot.reply_to(message, "Отправьте математическое выражение (например: 2+2, 1/2, sqrt(16), sin(30))")
