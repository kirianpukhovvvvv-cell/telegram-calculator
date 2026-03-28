def calculate(expression: str) -> str:
    """Вычисляет математическое выражение."""
    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )
        if isinstance(result, float):
            result = round(result, 6)
        return str(result)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"
    except (SyntaxError, NameError, TypeError, ValueError):
        return "Ошибка: некорректное выражение."
    except Exception as e:
        return f"Неожиданная ошибка: {e}"