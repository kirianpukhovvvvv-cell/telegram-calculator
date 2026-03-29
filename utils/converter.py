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

# Словарь чисел русскими словами (полный)
RUSSIAN_NUMBERS = {
    # Единицы
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
    'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
    # Десятки
    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
    'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
    'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
    'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
    'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90,
    # Сотни
    'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
    'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
    'девятьсот': 900,
    # Тысячи и миллионы
    'тысяча': 1000, 'тысячи': 1000, 'тысяч': 1000,
    'миллион': 1_000_000, 'миллиона': 1_000_000, 'миллионов': 1_000_000,
    'миллиард': 1_000_000_000, 'миллиарда': 1_000_000_000, 'миллиардов': 1_000_000_000,
    'триллион': 1_000_000_000_000, 'триллиона': 1_000_000_000_000, 'триллионов': 1_000_000_000_000,
}

def words_to_number(text):
    """Преобразует текст с русскими числами в числовое значение"""
    words = text.lower().split()
    result = 0
    current = 0

    for word in words:
        if word in RUSSIAN_NUMBERS:
            value = RUSSIAN_NUMBERS[word]
            if value >= 1000:  # Масштабные единицы (тысяча, миллион и т. д.)
                if current == 0:
                    current = 1
                result += current * value
                current = 0
            else:
                current += value
    result += current
    return result

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
        response = requests.get(CURRENCY_APIURL)
        data = response.json()

        if from_curr == to_curr:
            return 1.0

        # Если валюта не USD, сначала переводим в USD, затем в целевую
        if from_curr != 'USD':
            usd_rate = data['rates'].get(from_curr.upper())
            if usd_rate is None:
                return None
            amount_in_usd = 1 / usd_rate
        else:
            amount_in_usd = 1.0

        target_rate = data['rates'].get(to_curr.upper())
        if target_rate is None:
            return None

        return amount_in_usd * target_rate
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

    rate = get_exchange_rate(curr1, curr2)
    if rate is None:
        return "Ошибка получения курса валют"
    result = amount * rate
    return f"{amount} {curr1.upper()} = {result:.2f} {curr2.upper()}"
