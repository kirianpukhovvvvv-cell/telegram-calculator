import re
from telegram import Update
from telegram.ext import ContextTypes
from utils.calculator import calculate, words_to_number
from utils.converter import convert_units

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Проверка на конвертацию единиц
    convert_match = re.match(r'(\d+(?:\.\d+)?|[а-яё\s]+)\s*([а-яё]+)\s+в\s+([а-яё]+)', text)
    if convert_match:
        value_str, from_unit, to_unit = convert_match.groups()
        try:
            # Если число задано словами, конвертируем
            if any(word in value_str for word in ['ноль', 'один', 'два', 'три', 'четыре', 'пять',
                                                   'шесть', 'семь', 'восемь', 'девять', 'десять']):
                value = words_to_number(value_str)
            else:
                value = float(value_str)
            response = convert_units(value, from_unit, to_unit)
        except ValueError:
            response = "Не удалось распознать число."
        await update.message.reply_text(response)
        return

    # Если не конвертация, пробуем вычислить как математическое выражение
    response = calculate(text)
    await update.message.reply_text(response)
