from sympy import sqrt, simplify, parse_expr
from utils.converter import russian_to_english, convert_units, convert_currency

def calculate(expression):
    # Перевод русских терминов и чисел
    expression = russian_to_english(expression)

    # Проверка на конвертацию
    if 'в' in expression and any(word in expression for word in ['метр', 'грамм', 'USD']):
        if any(curr in expression.upper() for curr in ['USD', 'EUR', 'RUB']):
            return convert_currency(expression)
        else:
            return convert_units(expression)

    # Обработка математических выражений
    try:
        expr = parse_expr(expression)
        simplified = simplify(expr)
        if simplified.is_rational:
            return str(simplified)
        else:
            numeric_result = float(simplified.evalf())
            return f"{simplified} ≈ {numeric_result:.6f}"
    except Exception as e:
        return f"Ошибка: {str(e)}"
