import logging
import sys
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from calculator import calculate
from config import BOT_TOKEN
from telegram.error import Conflict

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Проверка единственного экземпляра бота
def check_single_instance():
    pid = str(os.getpid())
    pidfile = "/tmp/bot.pid"
    
    if os.path.exists(pidfile):
        with open(pidfile, 'r') as f:
            old_pid = f.read().strip()
            try:
                os.kill(int(old_pid), 0)
                logger.error(f"Уже запущен экземпляр бота с PID {old_pid}")
                sys.exit(1)
            except OSError:
                pass
    with open(pidfile, 'w') as f:
        f.write(pid)
    
    def remove_pid():
        os.remove(pidfile)
    
    import atexit
    atexit.register(remove_pid)

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

Просто отправьте математическое выражение!

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
"""
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик входящих сообщений с математическими выражениями"""
    user_input = update.message.text
    logger.info(f"Получено выражение от пользователя {update.effective_user.id}: {user_input}")

    try:
        # Вычисляем результат
        result = calculate(user_input)

        # Отправляем результат пользователю
        await update.message.reply_text(f"🧮 Результат:\n{result}")
    except Exception as e:
        logger.error(f"Ошибка при обработке выражения '{user_input}': {e}")
        await update.message.reply_text("❌ Ошибка вычисления. Проверьте правильность выражения.")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик ошибок"""
    logger.error(f"Ошибка бота: {context.error}")
    if isinstance(context.error, Conflict):
        logger.critical("Конфликт: уже запущен другой экземпляр бота!")
        sys.exit(1)
    elif isinstance(context.error, Exception):
        await update.message.reply_text("Произошла внутренняя ошибка. Попробуйте позже.")

def main():
    """Основная функция запуска бота"""
    try:
        # Проверяем единственный экземпляр бота
        check_single_instance()

        # Создаём приложение
        application = Application.builder().token(BOT_TOKEN).build()

        # Добавляем обработчики команд
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", start))  # Добавляем команду help

        # Добавляем обработчик сообщений
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        # Добавляем обработчик ошибок
        application.add_error_handler(error_handler)

        # Запускаем бота
        print("Бот запущен...")
        application.run_polling(
            poll_interval=1.0  # Интервал опроса
        )

    except Conflict as e:
        logger.critical(f"Конфликт: другой экземпляр бота уже запущен. Ошибка: {e}")
        print("Ошибка: уже запущен другой экземпляр бота. Завершите его перед запуском нового.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Критическая ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Бот остановлен вручную")
        sys.exit(0)
