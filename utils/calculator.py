import math
from fractions import Fraction

def calculate(expression):
    try:
        # Обработка дробей
        expression = expression.replace(' ', '')
        if '/' in expression and not any(op in expression for op in ['sqrt', 'sin', 'cos', 'tan', 'ctg']):
            parts = expression.split('/')
            if len(parts) == 2:
                return str(Fraction(parts[0]) / Fraction(parts[1]))

        # Математические функции
        if 'sqrt(' in expression:
            num = float(expression.replace('sqrt(', '').rstrip(')'))
            return str(math.sqrt(num))

        if 'sin(' in expression:
            num = float(expression.replace('sin(', '').rstrip(')'))
            return str(round(math.sin(math.radians(num)), 6))

        if 'cos(' in expression:
            num = float(expression.replace('cos(', '').rstrip(')'))
            return str(round(math.cos(math.radians(num)), 6))

        if 'tan(' in expression:
            num = float(expression.replace('tan(', '').rstrip(')'))
            return str(round(math.tan(math.radians(num)), 6))

        if 'ctg(' in expression:
            num = float(expression.replace('ctg(', '').rstrip(')'))
            tan_val = math.tan(math.radians(num))
            if tan_val == 0:
                return "Ошибка: ctg(0) не определён"
            return str(round(1 / tan_val, 6))

        # Базовые операции
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Ошибка: {str(e)}"
