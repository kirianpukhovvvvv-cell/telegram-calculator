import logging
import sys
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from calculator import calculate
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    welcome_text = """
🤖 Добро пожаловать в бот‑калькулятор!

🔢 **Арифметические операции:**
• Сложение: `+`
• Вычитание: `-`
• Умножение: `*`
• Деление: `/`
• Возведение в степень: `**`
• Остаток от деления: `%`

📐 **Тригонометрические функции:**
• `sin(x)`, `cos(x)`, `tan(x)`/`tg(x)`, `cot(x)`/`ctg(x)`
• Аргументы в радианах

🧮 **Функции и константы:**
• Квадратный корень: `sqrt(x)`
• Экспонента: `exp(x)`
• Логарифмы: `log(x)` (натуральный), `ln(x)`
• Факториал: `5!`
• Биномиальный коэффициент: `C(5,2)`
• Модуль: `Abs(x)`
• Знак числа: `sign(x)`
• Округление: `floor(x)`, `ceiling(x)`

🌠 **Константы:**
• Число π: `pi`
• Число Эйлера: `e` или `E`
• Мнимая единица: `I`

🧩 **Дополнительные возможности:**
• Дроби: `1/2`, `3/4`
• Скобки: `(2 + 3) * 4`
• Символьное упрощение: `simplify(x**2 + 2*x + 1)`
• Раскрытие скобок: `expand((x + 1)**2)`

**Примеры:**
`2 + 3`
`sin(pi/6)`
`sqrt(16)`
`1/2 + 1/3`
`(2 + 3) * 4`
`tg(pi/4)`
`5!`
`C(5,2)`
`Abs(-5)`
`I**2`
`expand((x + 1)**2)`

Просто отправьте математическое выражение!
    """
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик входящих сообщений с математическими выражениями"""
    user_input = update.message.text
    logger.info(f"Получено выражение от пользователя {update.effective_user.id}: {user_input}")

    # Вычисляем результат
    result = calculate(user_input)

    # Отправляем результат пользователю
    await update.message.reply_text(f"🧮 Результат:\n{result}")

def main():
    """Основная функция запуска бота"""
    try:
        # Создаём приложение
        application = Application.builder().token(BOT_TOKEN).build()

        # Добавляем обработчики
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Запускаем бота
        print("Бот запущен...")
        application.run_polling()

    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        if "Conflict" in str(e):
            print("Ошибка: уже запущен другой экземпляр бота. Завершите его перед запуском нового.")
        sys.exit(1)

if __name__ == "__main__":
    main()
