from sympy import sqrt, simplify, Rational
from sympy.parsing.sympy_parser import parse_expr


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
