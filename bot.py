import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
from calculator import calculate_expression, validate_and_format_input
import config

# Хранилище состояния режима (в памяти)
creator_mode_enabled = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8291462397:AAE94xlijZUL45k03wfnWlzXBOKUItNB2cQ"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text

    # Проверяем, включена ли связь с создателем и является ли пользователь создателем
    if creator_mode_enabled and user_id == config.CREATOR_ID:
        # Создатель отправляет сообщение — пересылаем его обратно как подтверждение
        await update.message.reply_text(
            f"✅ Режим связи с создателем активен. Ваше сообщение: {user_message}"
        )
        return

    # Обычная обработка математических выражений для всех пользователей
    formatted_expr = validate_and_format_input(user_message)
    result = calculate_expression(formatted_expr)
    await update.message.reply_text(result)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

async def secret_mode_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Секретная команда для включения/выключения режима связи с создателем."""
    user_id = update.effective_user.id

    if user_id != config.CREATOR_ID:
        await update.message.reply_text("❌ У вас нет доступа к этой команде.")
        return

    global creator_mode_enabled
    creator_mode_enabled = not creator_mode_enabled  # переключаем состояние

    status = "включён" if creator_mode_enabled else "выключен"
    await update.message.reply_text(f"🔄 Режим связи с создателем {status}.")

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    # Добавляем обработчик секретной команды
    application.add_handler(CommandHandler(config.SECRET_COMMAND.lstrip('/'), secret_mode_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен и готов к работе!")
    application.run_polling()

if __name__ == "__main__":
    main()
