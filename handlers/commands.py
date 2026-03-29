from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я умный калькулятор с поддержкой русского языка.\n\n"
        "Что я умею:\n"
        "• Считать: `два плюс три умножить на десять`\n"
        "• Функции: `синус тридцать`, `корень сто`\n"
        "• Конвертировать: `два метра в сантиметры`\n\n"
        "Используй `/help` для подробной справки.",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 **Помощь по калькулятору**\n\n"

        "**Математические операции:**\n"
        "`плюс`, `минус`, `умножить`, `разделить` или `+`, `-`, `*`, `/`\n\n"

        "**Функции:**\n"
        "`корень N` (или `sqrt(N)`) — квадратный корень\n"
        "`синус N`, `косинус N`, `тангенс N`, `котангенс N` — тригонометрические функции (N в градусах)\n\n"

        "**Числа словами:**\n"
        "Поддерживаются числа от `ноль` до `секстиллион`\n"
        "Примеры: `двадцать пять`, `три миллиона`\n\n"

        "**Конвертация:**\n"
        "`[число] [единица1] в [единица2]`\n"
        "Примеры:\n"
        "`два метра в сантиметры`\n"
        "`полтора килограмма в граммы`\n\n"

        "Используй `/convert` для запуска конвертера."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def convert_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Конвертер активен. Поддерживаемые единицы:\n\n"
        "**Длина:** м, см, мм, км\n"
        "**Вес:** кг, г, т\n\n"
        "**Примеры:**\n"
        "`2 метра в сантиметры` → `2 м = 200 см`\n"
        "`1.5 кг в граммы` → `1.5 кг = 1500 г`",
        parse_mode='Markdown'
    )
