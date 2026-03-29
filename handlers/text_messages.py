from telegram import Update
from telegram.ext import ContextTypes
from utils.calculator import process_math_message
from utils.converter import convert_units, convert_currency

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик текстовых сообщений"""
    text = update.message.text

    # Проверяем математические выражения
    math_result = process_math_message(text)
    if math_result:
        await update.message.reply_text(math_result)
        return

    # Проверяем конвертацию единиц
    unit_result = convert_units(text)
    # Если результат не содержит сообщение о формате или неподдерживаемых единицах, значит, конвертация прошла успешно
    if "Формат:" not in unit_result and "Неподдерживаемые" not in unit_result:
        await update.message.reply_text(unit_result)
        return

    # Проверяем конвертацию валют
    currency_result = convert_currency(text)
    # Если результат не содержит сообщения об ошибке или формате, значит, конвертация прошла успешно
    if "Формат:" not in currency_result and "Ошибка" not in currency_result:
        await update.message.reply_text(currency_result)
        return

    # Если ни один обработчик не сработал, отправляем подсказку
    await update.message.reply_text(
        "Не понял команду. Используйте /help для справки."
    )
