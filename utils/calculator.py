import math
import re

def russian_to_english(text):
    """
    Преобразует русские математические выражения в формат, понятный для вычисления.
    Поддерживает: +, -, *, /, √ (корень), числа словами.
    """
    replacements = {
        'плюс': '+',
        'минус': '-',
        'умножить на': '*',
        'разделить на': '/',
        'поделить на': '/',
        'делить на': '/',
        'корень из': 'sqrt(',
        'квадратный корень из': 'sqrt('
    }

    result = text.lower()
    for russian_term, english_symbol in replacements.items():
        result = result.replace(russian_term, english_symbol)

    # Добавляем закрывающие скобки для корней
    sqrt_count = result.count('sqrt(')
    result += ')' * sqrt_count

    # Заменяем русские числа на цифры
    words = result.split()
    processed_words = []

    from utils.converter import RUSSIAN_NUMBERS

    for word in words:
        # Проверяем, является ли слово числом на русском
        if word in RUSSIAN_NUMBERS:
            processed_words.append(str(RUSSIAN_NUMBERS[word]))
        else:
            # Оставляем как есть (операторы, скобки и т. д.)
            processed_words.append(word)

    final_expression = ' '.join(processed_words)
    return final_expression


def calculate_expression(expression):
    """
    Вычисляет математическое выражение после преобразования из русского формата.
    """
    try:
        # Преобразуем выражение
        converted_expr = russian_to_english(expression)
        # Заменяем sqrt на math.sqrt для корректного вычисления
        safe_expr = converted_expr.replace('sqrt', 'math.sqrt')
        # Вычисляем результат
        result = eval(safe_expr, {"__builtins__": {}, "math": math})
        return float(result)
    except Exception as e:
        raise ValueError(f"Ошибка вычисления: {str(e)}")

def is_mathematical_expression(text):
    """
    Проверяет, является ли текст математическим выражением.
    """
    # Регулярное выражение для поиска математических операторов
    math_pattern = r'[\+\-\*/\(\)\d\.]|sqrt|корень'
    return bool(re.search(math_pattern, text.lower()))

def process_math_message(text):
    """
    Основная функция обработки математических сообщений.
    Возвращает результат вычисления или None, если не математическое выражение.
    """
    if not is_mathematical_expression(text):
        return None

    try:
        result = calculate_expression(text)
        return f"Результат: {result}"
    except ValueError as e:
        return str(e)
