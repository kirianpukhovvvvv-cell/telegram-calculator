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
    # Обработка начального знака
    expression = expression.strip()
    if expression.startswith('+'):
        expression = expression[1:]
    elif expression.startswith('-'):
        expression = '0' + expression
    
    # Нормализация ввода
    expression = expression.replace('tg', 'tan').replace('ctg', 'cot')
    expression = expression.replace('e', 'E')  # e → E (константа Эйлера)

    # Обработка специальных функций
    expression = re.sub(r'(\d+)!', r'factorial(\1)', expression)
    expression = re.sub(r'C\((\d+),\s*(\d+)\)', r'binomial(\1,\2)', expression)
    expression = re.sub(r'(\d+)/(\d+)', r'Rational(\1,\2)', expression)

    try:
        # Парсинг и обработка выражения
        expr = parse_expr(expression, evaluate=False)
        simplified_expr = simplify(expr)
        exact_result = sympify(simplified_expr)
        decimal_result = N(exact_result)

        # Форматирование результата
        if exact_result.is_real:
            try:
                fraction_result = Fraction(decimal_result).limit_denominator(1000)
                if abs(fraction_result - decimal_result) < 1e-10:
                    return (
                        f"Дробь: {fraction_result}\n"
                        f"Десятичное: {decimal_result:.6f}\n"
                        f"Точное: {exact_result}\n"
                        f"Упрощённое: {simplified_expr}"
                    )
                else:
                    return (
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
            return (
                f"Результат: {exact_result}\n"
                f"Десятичное: {decimal_result:.6f}\n"
                f"Упрощённое: {simplified_expr}"
            )
    except Exception:
        return "❌ Произошла ошибка при вычислении. Проверьте правильность выражения."

# Тестирование функций калькулятора
if __name__ == "__main__":
    test_expressions = [
        "2 + 3",
        "+5 + 3",  # Тест на плюс в начале
        "-7 + 2",  # Тест на минус в начале
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
        "100 +",  # Некорректный ввод
        "5! + 3",  # Факториал с плюсом
        "C(3,2) + 1",  # Биномиальный коэффициент
        "sqrt(-1)",  # Комплексное число
        "2 + 2i",  # Комплексное число
        "2 + 2j",  # Комплексное число
        "2 + 2k",  # Некорректный ввод
        "2 + 2 *",  # Неполный ввод
        "2 + 2 / 0",  # Деление на ноль
        "2 + 2 / 1",  # Корректное деление
        "2 + 2 / 2",  # Корректное деление
        "2 + 2 / 3",  # Корректное деление
        "2 + 2 / 4",  # Корректное деление
        "2 + 2 / 5",  # Корректное деление
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

if __name__ == "__main__":
    # Запуск тестирования при прямом запуске файла
    test_expressions()
