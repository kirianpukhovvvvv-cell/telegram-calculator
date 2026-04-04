import math
from fractions import Fraction

def calculate(expression):
    """
    Вычисляет математическое выражение.
    Поддерживает: +, -, *, /, sin, cos, tg, ctg, sqrt, дроби, скобки.
    Возвращает результат в виде дроби или десятичного числа.
    """
    # Заменяем тригонометрические функции на их математические эквиваленты
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tg', 'math.tan')
    expression = expression.replace('ctg', '1/math.tan')
    expression = expression.replace('sqrt', 'math.sqrt')

    try:
        # Вычисляем выражение
        result = eval(expression, {"__builtins__": None}, {
            'math': math,
            'Fraction': Fraction,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        })

        # Пытаемся представить результат в виде дроби
        try:
            fraction_result = Fraction(result).limit_denominator(1000)
            if abs(fraction_result - result) < 1e-10:
                return f"Дробь: {fraction_result}\nДесятичное: {result:.6f}"
            else:
                return f"Десятичное: {result:.6f}"
        except:
            return f"Результат: {result:.6f}"

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
        "Fraction(1, 2) + Fraction(1, 3)"
    ]

    for expr in test_expressions:
        print(f"{expr} = {calculate(expr)}")
