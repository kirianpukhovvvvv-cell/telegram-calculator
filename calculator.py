from fractions import Fraction
import sympy as sp
import math
import re

def calculate_expression(expression: str) -> str:
    """
    Вычисляет математическое выражение с поддержкой дробей, корней и тригонометрии.
    Возвращает результат в виде дроби и десятичной дроби.
    """
    try:
        # Заменяем tg на tan для совместимости
        expression = expression.replace('tg', 'tan')

        # Парсим выражение с помощью sympy
        expr = sp.sympify(expression)

        # Вычисляем точное значение (дробь/корень)
        exact_result = sp.simplify(expr)

        # Получаем десятичное представление
        decimal_result = float(exact_result.evalf())

        # Форматируем результат
        fraction_result = None
        if isinstance(exact_result, sp.Rational):
            fraction_result = str(exact_result)
        elif isinstance(exact_result, (sp.Add, sp.Mul, sp.Pow)):
            # Если результат содержит корни или дроби
            fraction_str = str(exact_result)
            if '/' in fraction_str or 'sqrt' in fraction_str:
                fraction_result = fraction_str

        # Формируем ответ
        if fraction_result:
            return f"Результат:\nДробь: {fraction_result}\nДесятичная: {decimal_result:.6f}"
        else:
            return f"Результат: {decimal_result:.6f}"

    except Exception as e:
        return f"Ошибка вычисления: {str(e)}"

def validate_and_format_input(expression: str) -> str:
    """Валидирует и форматирует ввод пользователя."""
    # Удаляем лишние пробелы
    expression = re.sub(r'\s+', ' ', expression.strip())

    # Заменяем русские обозначения на английские
    replacements = {
        'синус': 'sin',
        'косинус': 'cos',
        'тангенс': 'tan',
        'котангенс': '1/tan',
        'корень': 'sqrt',
        '√': 'sqrt'
    }

    for ru, en in replacements.items():
        expression = expression.replace(ru, en)

    return expression
