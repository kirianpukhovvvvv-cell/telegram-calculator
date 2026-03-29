from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "Привет! Я калькулятор-бот. \n\n"
        "Что я умею:\n"
        "• 2 + 2\n"
        "• корень из 16\n"
        "• 100 USD в EUR\n"
        "• 5 м в см\n"
        "• пять умножить на три"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start — начать работу\n"
        "/help — показать эту справку\n\n"
        "Примеры математических выражений:\n"
        "2 + 2\n"
        "корень из 25\n"
        "пять умножить на шесть\n"
        "100 USD в EUR\n"
        "5 м в см"
    )
