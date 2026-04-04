from sympy import sympify, sin, cos, tan, cot, sqrt, N
from sympy.parsing.sympy_parser import parse_expr
from fractions import Fraction

def calculate(expression):
    """
    Вычисляет математическое выражение с использованием sympy.
    Поддерживает: +, -, *, /, sin, cos, tg, ctg, sqrt, дроби, скобки.
    Возвращает результат в виде дроби или десятичного числа.
    """
    # Нормализуем ввод: заменяем tg на tan, ctg на cot
    expression = expression.replace('tg', 'tan').replace('ctg', 'cot')

    try:
        # Парсим выражение с помощью sympy
        expr = parse_expr(expression)

        # Вычисляем точное значение
        exact_result = sympify(expr)

        # Получаем десятичное представление
        decimal_result = N(exact_result)

        # Пытаемся представить результат в виде дроби
        try:
            # Преобразуем десятичный результат в дробь
            fraction_result = Fraction(decimal_result).limit_denominator(1000)

            # Проверяем, насколько дробь близка к десятичному результату
            if abs(fraction_result - decimal_result) < 1e-10:
                return (
                    f"Дробь: {fraction_result}\n"
                    f"Десятичное: {decimal_result:.6f}\n"
                    f"Точное: {exact_result}"
                )
            else:
                return f"Десятичное: {decimal_result:.6f}\nТочное: {exact_result}"
        except:
            return f"Десятичное: {decimal_result:.6f}\nТочное: {exact_result}"

    except Exception as e:
        return f"Ошибка вычисления: {str(e)}"

# Тестирование функций калькулятора
if __name__ == "__main__":
    test_expressions = [
        "2 + 3",
        "10 / 4",
        "sin(0.5)",
        "sqrt(16)",
        "(2 + 3) * 4",
        "1/2 + 1/3",
        "tg(pi/4)",
        "cot(pi/4)"
    ]

    for expr in test_expressions:
        print(f"{expr} = {calculate(expr)}")
