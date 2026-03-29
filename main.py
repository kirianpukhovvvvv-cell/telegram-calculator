import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from calculator import calculate_expression, validate_and_format_input

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = "8291462397:AAE94xlijZUL45k03wfnWlzXBOKUItNB2cQ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает текстовые сообщения с математическими выражениями."""
    user_message = update.message.text

    # Валидируем и форматируем ввод
    formatted_expr = validate_and_format_input(user_message)

    # Вычисляем результат
    result = calculate_expression(formatted_expr)

    # Отправляем ответ пользователю
    await update.message.reply_text(result)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает команду /start."""
    welcome_text = (
        "🤖 Привет! Я математический калькулятор.\n\n"
        "Я умею:\n"
        "• Стандартные операции: +, -, *, /\n"
        "• Тригонометрию: sin, cos, tan, ctg\n"
        "• Квадратные корни: sqrt() или √\n"
        "• Дроби: 1/2, 3/4 и т. д.\n"
        "• Комбинированные выражения\n\n"
        "Примеры:\n"
        "`sin(pi/4)` → 0.707\n"
        "`sqrt(2)/2` → дробь и десятичная\n"
        "`1/2 + 1/3` → 5/6 и 0.833\n\n"
        "Просто отправь мне математическое выражение!"
    )
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатывает команду /help."""
    help_text = (
        "📖 **Справка по калькулятору**\n\n"

        "**Операции:**\n"
        "+ — сложение\n"
        "- — вычитание\n"
        "* — умножение\n"
        "/ — деление\n\n"

        "**Функции:**\n"
        "sin(x) — синус\n"
        "cos(x) — косинус\n"
        "tan(x) — тангенс\n"
        "1/tan(x) или ctg(x) — котангенс\n"
        "sqrt(x) или √x — квадратный корень\n\n"

        "**Примеры выражений:**\n"
        "`2 + 3 * 4`\n"
        "`sin(pi/6)`\n"
        "`sqrt(8)/2`\n"
        "`1/3 + 1/6`\n"
        "`tan(pi/4) + sqrt(4)`\n\n"

        "Результат выводится в виде дроби (если возможно) и десятичной дроби."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

def main():
    """Основная функция запуска бота."""
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен и готов к работе!")
    application.run_polling()

if __name__ == "__main__":
    main()
