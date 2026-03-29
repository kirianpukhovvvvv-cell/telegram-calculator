from sympy import sqrt, simplify, Rational
from sympy.parsing.sympy_parser import parse_expr

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

def calculate(expression):
    try:
        # Заменяем sqrt на sympy.sqrt для корректной обработки
        expression = expression.replace('sqrt', 'sqrt')

        # Парсим выражение с поддержкой корней и дробей
        expr = parse_expr(expression)


        # Упрощаем выражение (сокращаем дроби, упрощаем корни)
        simplified = simplify(expr)

        # Если результат — дробь, представляем в виде числитель/знаменатель
        if simplified.is_rational:
            return str(simplified)
        else:
            # Для иррациональных чисел — вычисляем численно с округлением
            numeric_result = float(simplified.evalf())
            return f"{simplified} ≈ {numeric_result:.6f}"

    except Exception as e:
        return f"Ошибка: {str(e)}"
