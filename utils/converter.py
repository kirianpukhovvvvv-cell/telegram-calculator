import requests
import re

# Таблицы конвертации
LENGTH_CONVERSIONS = {
    'м': 1, 'метр': 1,
    'см': 0.01, 'сантиметр': 0.01,
    'мм': 0.001, 'миллиметр': 0.001,
    'км': 1000, 'километр': 1000
}

WEIGHT_CONVERSIONS = {
    'кг': 1, 'килограмм': 1,
    'г': 0.001, 'грамм': 0.001,
    'т': 1000, 'тонна': 1000,
    'мг': 0.000001, 'миллиграмм': 0.000001
}

CURRENCY_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def convert_units(expression):
    """Конвертация физических величин"""
    pattern = r'(\d+(?:\.\d+)?)\s*(\w+)\s+в\s+(\w+)'
    match = re.search(pattern, expression, re.IGNORECASE)

    if not match:
        return "Формат: [число] [единица1] в [единица2]"

    value, unit1, unit2 = match.groups()
    value = float(value)

    # Определяем тип величины
    if unit1 in LENGTH_CONVERSIONS and unit2 in LENGTH_CONVERSIONS:
        base_value = value * LENGTH_CONVERSIONS[unit1]
        result = base_value / LENGTH_CONVERSIONS[unit2]
        return f"{value} {unit1} = {result} {unit2}"

    elif unit1 in WEIGHT_CONVERSIONS and unit2 in WEIGHT_CONVERSIONS:
        base_value = value * WEIGHT_CONVERSIONS[unit1]
        result = base_value / WEIGHT_CONVERSIONS[unit2]
        return f"{value} {unit1} = {result} {unit2}"

    else:
        return "Неподдерживаемые единицы измерения"

def get_exchange_rate(from_curr, to_curr):
    """Получение курса валют"""
    try:
        response = requests.get(CURRENCY_URL)
        data = response.json()

        if from_curr == 'USD':
            rate = data['rates'][to_curr]
        else:
            usd_rate = data['rates'][from_curr]
            rate = data['rates'][to_curr] / usd_rate

        return rate
    except Exception:
        return None

def convert_currency(expression):
    """Конвертация валют"""
    pattern = r'(\d+(?:\.\d+)?)\s*(\w{3})\s+в\s+(\w{3})'
    match = re.search(pattern, expression, re.IGNORECASE)

    if not match:
        return "Формат: [сумма] [код1] в [код2] (например: 100 USD в EUR)"

    amount, curr1, curr2 = match.groups()
    amount = float(amount)

    rate = get_exchange_rate(curr1.upper(), curr2.upper())
    if rate is None:
        return "Ошибка получения курса валют"
    result = amount * rate
    return f"{amount} {curr1.upper()} = {result:.2f} {curr2.upper()}"

def russian_to_english(text):
    """Перевод русских математических терминов в английские"""
    replacements = {
        'плюс': '+', 'минус': '-', 'умножить': '*', 'разделить': '/',
        'корень': 'sqrt', 'синус': 'sin', 'косинус': 'cos',
        'тангенс': 'tan', 'котангенс': 'ctg',
        'поделить': '/'
    }
    for russian, english in replacements.items():
        text = text.replace(russian, english)
    return text
