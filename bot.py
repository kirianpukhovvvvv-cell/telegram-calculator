import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from calculator import calculate
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    welcome_text = """
🤖 Добро пожаловать в бот‑калькулятор!

Доступные операции:
• Арифметика: +, -, *, /
• Тригонометрия: sin, cos, tg, ctg
• Квадратный корень: sqrt
• Дроби: Fraction(числитель, знаменатель)
• Скобки: ( )

Примеры:
2 + 3
sin(0.5)
sqrt(16)
Fraction(1,2) + Fraction(1,3)
(2 + 3) * 4

Просто отправьте математическое выражение!
    """
    await update.message.reply_text(welcome_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик входящих сообщений с математическими выражениями"""
    user_input = update.message.text

    # Вычисляем результат
    result = calculate(user_input)

    # Отправляем результат пользователю
    await update.message.reply_text(f"🧮 Результат:\n{result}")

def main():
    """Основная функция запуска бота"""
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
