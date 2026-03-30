from sympy import sqrt, simplify, Rational, evalf
from sympy.parsing.sympy_parser import parse_expr
from sympy.core.numbers import Rational as SymPyRational


def calculate(expression):
    try:
        # Заменяем текстовые обозначения корня на sympy.sqrt
        expression = expression.replace('корень из', 'sqrt(').replace('квадратный корень из', 'sqrt(')
        # Добавляем закрывающие скобки для каждого sqrt(
        sqrt_count = expression.count('sqrt(')
        expression += ')' * sqrt_count

        # Парсим выражение с поддержкой корней и дробей
        expr = parse_expr(expression)

        # Упрощаем выражение (сокращаем дроби, упрощаем корни)
        simplified = simplify(expr)

        # Проверяем, является ли результат рациональным числом (дробью)
        if isinstance(simplified, SymPyRational):
            return str(simplified)
        else:
            # Для иррациональных или сложных чисел — вычисляем численно с округлением
            numeric_result = simplified.evalf()
            # Проверяем, что результат — число
            if numeric_result.is_number:
                return f"{simplified} ≈ {float(numeric_result):.6f}"
            else:
                # Если результат содержит символы (например, x), возвращаем упрощённое выражение
                return str(simplified)

    except Exception as e:
        return f"Ошибка вычисления: {str(e)}"
