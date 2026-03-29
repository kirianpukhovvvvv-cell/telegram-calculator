from fractions import Fraction
import sympy as sp
import re

def calculate_expression(expression: str) -> str:
    """
    Вычисляет математическое выражение с поддержкой дробей, корней и тригонометрии.
    Возвращает результат в виде дроби и десятичной дроби.
    """
    try:
        # Заменяем tg на tan для совместимости
        expression = expression.replace('tg', 'tan').replace('ctg', '1/tan')

        # Парсим выражение с помощью sympy
        expr = sp.sympify(expression)

        # Вычисляем точное значение
        exact_result = sp.simplify(expr)

        # Получаем десятичное представление
        decimal_result = float(exact_result.evalf())

        # Форматируем результат
        if isinstance(exact_result, sp.Rational):
            fraction_result = str(exact_result)
            return f"Результат:\nДробь: {fraction_result}\nДесятичная: {decimal_result:.6f}"
        elif exact_result.has(sp.sqrt):
            # Если результат содержит корни
            fraction_str = str(exact_result)
            return f"Результат:\nВыражение: {fraction_str}\nДесятичная: {decimal_result:.6f}"
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
        '√': 'sqrt',
        'пи': 'pi'
    }

    for ru, en in replacements.items():
        expression = expression.replace(ru, en)

    return expression
