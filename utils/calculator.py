import math
import re
from num2words import num2words

# Словарь русских математических терминов
MATH_TERMS = {
    'плюс': '+', 'минус': '-', 'умножить': '*', 'разделить': '/',
    'корень': 'sqrt', 'синус': 'sin', 'косинус': 'cos',
    'тангенс': 'tan', 'котангенс': 'ctg'
}

# Словарь чисел словами
NUMBER_WORDS = {
    'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
    'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9,
    'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
    'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
    'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
    'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50,
    'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90,
    'сто': 100, 'двести': 200, 'триста': 300, 'четыреста': 400,
    'пятьсот': 500, 'шестьсот': 600, 'семьсот': 700, 'восемьсот': 800,
    'девятьсот': 900, 'тысяча': 1000, 'миллион': 1_000_000,
    'миллиард': 1_000_000_000, 'триллион': 1_000_000_000_000
}

def words_to_number(text: str) -> float:
    """Конвертирует русские слова в число."""
    # Простая реализация — в реальном проекте нужна более сложная логика
    words = text.lower().split()
    result = 0
    current = 0

    for word in words:
        if word in NUMBER_WORDS:
            num = NUMBER_WORDS[word]
            if num >= 1000:
                current *= num
                result += current
                current = 0
            else:
                current += num
    return result + current

def parse_russian_math(expression: str) -> str:
    """Парсит математическое выражение на русском языке."""
    expression = expression.lower()

    # Заменяем русские термины на математические символы
    for ru_term, math_term in MATH_TERMS.items():
        expression = expression.replace(ru_term, math_term)

    # Конвертируем числа словами в цифры
    words_pattern = r'\b(?:ноль|один|два|три|четыре|пять|шесть|семь|восемь|девять|десять|одиннадцать|двенадцать|тринадцать|четырнадцать|пятнадцать|шестнадцать|семнадцать|восемнадцать|девятнадцать|двадцать|тридцать|сорок|пятьдесят|шестьдесят|семьдесят|восемьдесят|девяносто|сто|двести|триста|четыреста|пятьсот|шестьсот|семьсот|восемьсот|девятьсот|тысяча|миллион|миллиард|триллион)\b'
    matches = re.findall(words_pattern, expression)
    for match in matches:
        num = NUMBER_WORDS.get(match, 0)
        expression = expression.replace(match, str(num))

    return expression

def calculate(expression: str) -> str:
    """Вычисляет математическое выражение с поддержкой русского языка."""
    try:
        # Парсим русское выражение
        parsed_expr = parse_russian_math(expression)

        # Выполняем вычисления
        if 'sqrt' in parsed_expr:
            parsed_expr = parsed_expr.replace('sqrt', 'math.sqrt')
        if 'sin' in parsed_expr:
            parsed_expr = parsed_expr.replace('sin', 'math.sin')
        if 'cos' in parsed_
