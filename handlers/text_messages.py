from telebot import TeleBot
from telebot.types import Message
from utils.calculator import calculate

def register_handlers(bot: TeleBot):
    @bot.message_handler(content_types=['text'])
    def handle_text(message: Message):
        text = message.text.strip()
        if text.startswith('/'):
            return  # Игнорируем неизвестные команды
        result = calculate(text)
        bot.send_message(message.chat.id, f"Результат: `{result}`")