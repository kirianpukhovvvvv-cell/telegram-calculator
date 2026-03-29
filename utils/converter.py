# Конвертация единиц измерения
CONVERSION_RATES = {
    # Длина (в метрах)
    'м': 1, 'метр': 1, 'метры': 1,
    'см': 0.01, 'сантиметр': 0.01, 'сантиметры': 0.01,
    'мм': 0.001, 'миллиметр': 0.001, 'миллиметры': 0.001,
    'км': 1000, 'километр': 1000, 'километры': 1000,

    # Вес (в килограммах)
    'кг': 1, 'килограмм': 1, 'килограммы': 1,
    'г': 0.001, 'грамм': 0.001, 'граммы': 0.001,
    'т': 1000, 'тонна': 1000, 'тонны': 1000,
}

def convert_units(value: float, from_unit: str, to_unit: str) -> str:
    """Конвертирует единицы измерения."""
    from_unit = from_unit.lower().strip()
    to_unit = to_unit.lower().strip()

    if from_unit not in CONVERSION_RATES or to_unit not in CONVERSION_RATES:
        return "Неподдерживаемая единица измерения."

    # Конвертируем в базовые единицы (метры/килограммы)
    base_value = value * CONVERSION_RATES[from_unit]
    # Конвертируем из базовых единиц в целевые
    result = base_value / CONVERSION_RATES[to_unit]

    return f"{value} {from_unit} = {result} {to_unit}"
