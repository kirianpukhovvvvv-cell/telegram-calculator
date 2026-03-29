import math
import re

def russian_to_english(text):
    """Преобразует русские математические выражения в формат, понятный для вычисления."""
    replacements = {
        'плюс': '+',
        'минус': '-',
        'умножить на': '*',
        'разделить на': '/',
        'поделить на': '/',
        'делить на': '/',
        'корень из': 'math.sqrt(',
        'квадратный корень из': 'math.sqrt('
    }

    result = text.lower()
    for russian_term, english_symbol in replacements.items():
        result = result.replace(russian_term, english_symbol)

    # Добавляем закрывающие скобки для корней
    sqrt_count = result.count('math.sqrt(')
    result += ')' * sqrt_count
    return result

def calculate_expression(expression):
    """Вычисляет математическое выражение после преобразования из русского формата."""
    try:
        converted_expr = russian_to_english(expression)
        result = eval(converted_expr, {"__builtins__": {}, "math": math})
        return float(result)
    except Exception as e:
        raise ValueError(f"Ошибка вычисления: {str(e)}")

def is_mathematical_expression(text):
    """Проверяет, является ли текст математическим выражением."""
    math_pattern = r'[\+\-\*/\(\)\d\.\s]|math\.sqrt|корень'
    return bool(re.search(math_pattern, text.lower()))

def process_math_message(text):
    """Основная функция обработки математических сообщений."""
    if not is_mathematical_expression(text):
        return None

    try:
        result = calculate_expression(text)
        return f"Результат: {result}"
    except ValueError as e:
        return str(e)
