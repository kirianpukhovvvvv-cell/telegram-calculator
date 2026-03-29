from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers.commands import start_command, help_command
from handlers.text_messages import handle_text_message
import sys
import psutil

def is_bot_already_running():
    """Проверяет, запущен ли уже экземпляр бота."""
    current_process = psutil.Process()
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['pid'] == current_process.pid:
                continue
            cmdline = proc.info.get('cmdline', [])
            if cmdline and any('bot.py' in arg for arg in cmdline):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

def main():
    if is_bot_already_running():
        print("Ошибка: экземпляр бота уже запущен! Завершаю работу.")
        sys.exit(1)

    # Остальной код запуска бота
    from config import BOT_TOKEN
    from telegram.ext import Application

    application = Application.builder().token(BOT_TOKEN).build()

    from handlers.commands import start_command, help_command
    from handlers.text_messages import handle_text_message

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))

    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()

def main():
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))

    # Добавляем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
