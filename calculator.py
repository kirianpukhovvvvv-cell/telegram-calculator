from sympy import (
    sympify, sin, cos, tan, cot, sqrt, N, pi, E, exp, log, ln,
    factorial, binomial, I, re, im, Abs, sign, floor, ceiling,
    simplify, expand, Rational
)
from sympy.parsing.sympy_parser import parse_expr
from fractions import Fraction
import re

def calculate(expression):
    """
    Вычисляет математическое выражение с использованием sympy.
    Поддерживает: арифметику, тригонометрию, константы, функции, комплексные числа.
    Возвращает результат в удобном формате.
    """
    # Нормализуем ввод
    expression = expression.replace('tg', 'tan').replace('ctg', 'cot')
    expression = expression.replace('e', 'E')  # e → E (константа Эйлера)

    # Обработка факториалов: 5! → factorial(5)
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)

    # Обработка биномиальных коэффициентов: C(5,2) → binomial(5,2)
    expression = re.sub(r'C\((\d+),\s*(\d+)\)', r'binomial(\1,\2)', expression)

    # Обработка дробей: 1/2 → Rational(1,2) для точной арифметики
    expression = re.sub(r'(\d+)/(\d+)', r'Rational(\1,\2)', expression)

    try:
        # Парсим выражение с помощью sympy
        expr = parse_expr(expression, evaluate=False)

        # Упрощаем выражение перед вычислением
        simplified_expr = simplify(expr)

        # Вычисляем точное значение
        exact_result = sympify(simplified_expr)

        # Получаем десятичное представление
        decimal_result = N(exact_result)

        # Форматируем вывод в зависимости от типа результата
        if exact_result.is_real:
            # Для вещественных чисел пытаемся представить в виде дроби
            try:
                fraction_result = Fraction(decimal_result).limit_denominator(1000)
                if abs(fraction_result - decimal_result) < 1e-10:
                    return (
                f"Дробь: {fraction_result}\n"
                f"Десятичное: {decimal_result:.6f}\n"
                f"Точное: {exact_result}\n"
                f"Упрощённое: {simplified_expr}"
            )
            except (ValueError, TypeError):
                return (
                    f"Десятичное: {decimal_result:.6f}\n"
                    f"Точное: {exact_result}\n"
            f"Упрощённое: {simplified_expr}"
        )
        elif exact_result.has(I):
            # Для комплексных чисел
            real_part = N(re(exact_result))
            imag_part = N(im(exact_result))
            return (
                f"Комплексное число:\n"
                f"Действительная часть: {real_part:.6f}\n"
                f"Мнимая часть: {imag_part:.6f}\n"
                f"Точное: {exact_result}\n"
                f"Упрощённое: {simplified_expr}"
            )
        else:
            # Другие случаи
            return (
                f"Результат: {exact_result}\n"
                f"Десятичное: {decimal_result:.6f}\n"
                f"Упрощённое: {simplified_expr}"
            )
    except Exception as e:
        return f"Ошибка вычисления: {str(e)}"

# Тестирование функций калькулятора
if __name__ == "__main__":
    test_expressions = [
        "2 + 3",
        "10 / 4",
        "sin(pi/6)",
        "cos(pi/3)",
        "tan(pi/4)",
        "cot(pi/4)",
        "sqrt(16)",
        "(2 + 3) * 4",
        "1/2 + 1/3",  # Дробная арифметика
        "pi",
        "E",
        "exp(1)",
        "log(10)",
        "ln(E)",
        "5!",  # Факториал
        "C(5,2)",  # Биномиальный коэффициент
        "Abs(-5)",  # Модуль числа
        "sign(-3)",  # Знак числа
        "floor(3.7)",  # Округление вниз
        "ceiling(3.2)",  # Округление вверх
        "I**2",  # Комплексное число (i²)
        "expand((x + 1)**2)",  # Раскрытие скобок
        "simplify(x**2 + 2*x + 1)",  # Упрощение выражения
        "diff(x**3, x)",  # Производная
        "integrate(x**2, x)",  # Интеграл
        "limit(sin(x)/x, x, 0)",  # Предел
        "sqrt(2)**2",  # Проверка точности
        "2**10",  # Возведение в степень
        "3 * (4 + 5)",  # Скобки и умножение
        "log(1)",  # Логарифм единицы
        "sin(0)",  # Тригонометрия: sin(0)
        "cos(0)",  # Тригонометрия: cos(0)
    ]

    print("🧮 ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА\n")
    for i, expr in enumerate(test_expressions, 1):
        print(f"{i:2d}. {expr}")
        try:
            result = calculate(expr)
            print(f"    → {result}")
        except Exception as e:
            print(f"    ❌ Ошибка: {e}")
        print("-" * 60)
